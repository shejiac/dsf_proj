import json

# Read notebook
with open('DSF_draft.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find cells with duplicate content signatures
print("=== DUPLICATE CONTENT DETECTION ===\n")

# Look for cells mentioning DS1, DS2, DS3 assessments
ds_mentions = {}
for i, cell in enumerate(nb['cells']):
    content = ''
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
    elif cell['cell_type'] == 'code':
        content = ''.join(cell['source'])
    
    # Track DS mentions
    if 'DS1' in content or 'SPY OHLCV' in content:
        if 'DS1' not in ds_mentions:
            ds_mentions['DS1'] = []
        ds_mentions['DS1'].append((i, cell['cell_type'], len(content)))
    if 'DS2' in content or 'LOBSTER' in content:
        if 'DS2' not in ds_mentions:
            ds_mentions['DS2'] = []
        ds_mentions['DS2'].append((i, cell['cell_type'], len(content)))
    if 'DS3' in content or 'FRED' in content:
        if 'DS3' not in ds_mentions:
            ds_mentions['DS3'] = []
        ds_mentions['DS3'].append((i, cell['cell_type'], len(content)))

print("DS1 mentions (cell_index, type, content_length):")
for ds in sorted(ds_mentions.keys()):
    cells = ds_mentions[ds]
    print(f"\n{ds}:")
    for cell_idx, cell_type, length in cells:
        print(f"  Cell {cell_idx}: {cell_type} ({length} chars)")

print(f"\n=== TOTAL CELLS: {len(nb['cells'])} ===")

# Show first few sections
print("\n=== CELL STRUCTURE (first 100 cells) ===")
for i in range(min(100, len(nb['cells']))):
    cell = nb['cells'][i]
    ctype = cell['cell_type']
    if ctype == 'markdown':
        src = ''.join(cell['source'])[:50].replace('\n', ' ')
        print(f"{i:3d}: MD | {src}...")
    else:
        src = ''.join(cell['source'])[:50].replace('\n', ' ')
        print(f"{i:3d}: PY | {src}...")
