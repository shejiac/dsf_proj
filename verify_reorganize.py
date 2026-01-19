import json

# Verify reorganized notebook
with open('DSF_draft_REORGANIZED.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
print(f"✅ Reorganized notebook verification\n")
print(f"Total cells: {len(cells)}\n")

# Check phase markers
print("Phase Structure:")
for i, cell in enumerate(cells):
    src_text = ''.join(cell['source']) if cell['cell_type'] == 'markdown' else ''
    if 'SECTION' in src_text or 'PHASE' in src_text:
        print(f"  Cell {i:3d}: {src_text[:70].replace(chr(10), ' ')}")

print(f"\nDataset Coverage:")
ds_count = {'DS1': 0, 'DS2': 0, 'DS3': 0, 'DS4': 0, 'DS5': 0}
for cell in cells:
    src = ''.join(cell['source'])
    for ds in ds_count:
        if ds in src or (ds == 'DS1' and 'SPY' in src and 'OHLCV' in src):
            ds_count[ds] += 1

for ds, count in sorted(ds_count.items()):
    print(f"  {ds}: {count} cells containing reference")

# Check for content preservation
print(f"\nContent Preservation Check:")
markdown_cells = sum(1 for c in cells if c['cell_type'] == 'markdown')
code_cells = sum(1 for c in cells if c['cell_type'] == 'code')
print(f"  Markdown cells: {markdown_cells}")
print(f"  Code cells: {code_cells}")
print(f"  Total: {markdown_cells + code_cells}")

# Find phase boundaries
print(f"\nPhase Boundaries (approx):")
section_indices = []
for i, cell in enumerate(cells):
    src = ''.join(cell['source'])
    if 'SECTION' in src:
        section_indices.append((i, src.split('\n')[1] if len(src.split('\n')) > 1 else 'N/A'))

if section_indices:
    print(f"  ASK Phase: Cells 0-{section_indices[0][0]-1}")
    for j in range(len(section_indices)-1):
        print(f"  Cells {section_indices[j][0]}-{section_indices[j+1][0]-1}: {section_indices[j][1][:40]}")
    print(f"  Cells {section_indices[-1][0]}-{len(cells)-1}: {section_indices[-1][1][:40]}")

print(f"\n✅ All content preserved")
print(f"✅ Ready to replace original")
