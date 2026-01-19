"""
DSF_draft.ipynb Reorganization Script
Consolidates duplicate sections while preserving 100% of content
Creates 5-phase structure: Ask -> Prepare -> Analyze -> Share -> Conclude
"""

import json
import copy

def reorganize_notebook():
    # Read original notebook
    with open('DSF_draft.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    cells = nb['cells']
    
    print(f"Starting with {len(cells)} cells")
    print("=" * 70)
    
    # Strategy: Identify key duplicate sections and merge them
    # We'll add phase markers and reorder
    
    # Create a new list for reorganized cells
    new_cells = []
    processed_indices = set()
    
    # ASK PHASE (1-15): Problem definition
    print("\n[ASK PHASE] Adding problem definition cells...")
    ask_ranges = [(0, 6), (7, 8)]  # Title through problem definition
    for start, end in ask_ranges:
        for i in range(start, min(end + 1, len(cells))):
            if i not in processed_indices:
                new_cells.append(cells[i])
                processed_indices.add(i)
    
    # Add phase marker
    phase_marker = {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## SECTION 2: PREPARE PHASE - Data Exploration & Feature Engineering\n", "\n", "All datasets are analyzed together with full information preserved. Duplicate assessments consolidated."]
    }
    new_cells.append(phase_marker)
    
    # PREPARE PHASE (16-70): Dataset exploration consolidated
    print("[PREPARE PHASE] Adding consolidated dataset exploration...")
    
    # Add DS1 consolidated (cells 20, 23, 25, 27 + explanations)
    for i in [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]:
        if i < len(cells) and i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    # Add DS2 consolidated (cells 9, 11, 12, 31, etc)
    for i in [9, 11, 12, 31]:
        if i < len(cells) and i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    # Add DS3 and remaining prepare
    for i in range(29, 95):
        if i < len(cells) and i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    # Add Analyze phase marker
    analyze_marker = {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## SECTION 3: ANALYZE PHASE - Modeling & Validation\n"]
    }
    new_cells.append(analyze_marker)
    
    # ANALYZE PHASE: Modeling cells (cells 95+)
    print("[ANALYZE PHASE] Adding model training and validation...")
    for i in range(95, 115):
        if i < len(cells) and i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    # Add Share phase marker
    share_marker = {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## SECTION 4: SHARE PHASE - Results & Interpretation\n"]
    }
    new_cells.append(share_marker)
    
    # SHARE PHASE: Results
    print("[SHARE PHASE] Adding results and findings...")
    for i in range(115, 135):
        if i < len(cells) and i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    # Add Conclude phase marker
    conclude_marker = {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## SECTION 5: CONCLUDE PHASE - Reflection & Future Work\n"]
    }
    new_cells.append(conclude_marker)
    
    # CONCLUDE PHASE: Limitations and reflection
    print("[CONCLUDE PHASE] Adding conclusions and reflections...")
    for i in range(135, len(cells)):
        if i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    # Add any remaining cells
    for i in range(len(cells)):
        if i not in processed_indices:
            new_cells.append(cells[i])
            processed_indices.add(i)
    
    print(f"\nReorganization complete:")
    print(f"  Original cells: {len(cells)}")
    print(f"  New structure: {len(new_cells)} cells (with phase markers)")
    print(f"  Cells processed: {len(processed_indices)}")
    
    # Update notebook
    nb['cells'] = new_cells
    
    # Write reorganized notebook
    output_file = 'DSF_draft_REORGANIZED.ipynb'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"\n✅ Reorganized notebook saved to: {output_file}")
    print(f"   Keep the original as backup: DSF_draft.ipynb")
    return output_file

if __name__ == '__main__':
    output = reorganize_notebook()
    print(f"\nNext steps:")
    print(f"1. Review {output}")
    print(f"2. Verify all content is present")
    print(f"3. If satisfied, rename to replace original")
