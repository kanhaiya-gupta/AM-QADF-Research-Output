#!/usr/bin/env python3
"""
Convert Mermaid diagrams from Methodology.md to PNG images.
Extracts all Mermaid code blocks and converts them using mmdc (Mermaid CLI).

Requirements:
    npm install -g @mermaid-js/mermaid-cli
    Or: npm install -g @mermaid-js/mermaid-cli

Usage:
    python convert_mermaid_to_images.py
    python convert_mermaid_to_images.py --file Methodology.md --output ../flowchart_images
"""

import subprocess
import re
import os
import argparse
from pathlib import Path
from typing import List, Tuple


def extract_all_mermaid_from_markdown(markdown_file: Path) -> List[Tuple[str, str]]:
    """
    Extract all Mermaid code blocks from markdown file.
    
    Returns:
        List of tuples: (diagram_name, mermaid_code)
    """
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    diagrams = []
    in_mermaid_block = False
    mermaid_lines = []
    mermaid_start_line = 0
    
    for line_num, line in enumerate(lines):
        # Check for start of mermaid block
        if line.strip() == '```mermaid':
            in_mermaid_block = True
            mermaid_lines = []
            mermaid_start_line = line_num
            continue
        
        # Check for end of mermaid block
        if in_mermaid_block and line.strip() == '```':
            mermaid_code = ''.join(mermaid_lines).strip()
            if mermaid_code:
                # Find headings before this block (closest and parent)
                diagram_name = None
                headings_found = []  # List of (level, text) tuples
                
                # Look backwards from the mermaid block start
                for i in range(mermaid_start_line - 1, -1, -1):
                    heading_match = re.match(r'^(#{2,})\s+(.+)$', lines[i])
                    if heading_match:
                        heading_level = len(heading_match.group(1))
                        heading_text = heading_match.group(2).strip()
                        headings_found.append((heading_level, heading_text))
                        # Collect up to 3 headings for context
                        if len(headings_found) >= 3:
                            break
                
                # Build diagram name from heading context
                if headings_found:
                    # Get the closest heading (first in list)
                    closest_level, closest_text = headings_found[0]
                    
                    # If closest heading is generic (like "Selection Decision Tree"),
                    # use parent heading instead for better uniqueness
                    if closest_level >= 4 and ('selection' in closest_text.lower() and 'decision' in closest_text.lower()):
                        # Look for a more specific parent heading (level 2 or 3)
                        for level, text in headings_found[1:]:
                            if level <= 3:  # Use level 2 or 3 as parent
                                # Use parent heading as base name
                                diagram_name = re.sub(r'[^\w\s-]', '', text)
                                diagram_name = re.sub(r'[-\s]+', '_', diagram_name).lower()
                                # Add "decision_tree" suffix for clarity
                                if 'decision' not in diagram_name:
                                    diagram_name = f"{diagram_name}_decision_tree"
                                break
                    
                    # If no parent context needed or found, use closest heading
                    if not diagram_name:
                        diagram_name = re.sub(r'[^\w\s-]', '', closest_text)
                        diagram_name = re.sub(r'[-\s]+', '_', diagram_name).lower()
                
                # If no heading found, try to extract from mermaid code
                if not diagram_name:
                    # Check for specific diagram types based on content
                    if 'Grid Type Selection' in mermaid_code or ('grid' in mermaid_code.lower() and 'selection' in mermaid_code.lower()):
                        diagram_name = "grid_type_selection_decision_tree"
                    elif 'Interpolation Method Selection' in mermaid_code or ('interpolation' in mermaid_code.lower() and 'method' in mermaid_code.lower() and 'selection' in mermaid_code.lower()):
                        diagram_name = "interpolation_method_selection_decision_tree"
                    elif 'Multi-Source Data Input' in mermaid_code or ('hatching' in mermaid_code.lower() and 'laser' in mermaid_code.lower() and 'ct' in mermaid_code.lower()):
                        diagram_name = "signal_mapping_process_overview"
                    elif re.search(r'flowchart\s+(LR|TB|TD|RL)', mermaid_code):
                        diagram_type = re.search(r'flowchart\s+(LR|TB|TD|RL)', mermaid_code).group(1).lower()
                        diagram_name = f"flowchart_{diagram_type}_{len(diagrams) + 1}"
                    elif re.search(r'graph\s+\w+', mermaid_code):
                        diagram_name = f"graph_{len(diagrams) + 1}"
                    else:
                        diagram_name = f"diagram_{len(diagrams) + 1}"
                
                # Ensure uniqueness by adding index if needed
                base_name = diagram_name
                counter = 1
                while any(name == diagram_name for name, _ in diagrams):
                    diagram_name = f"{base_name}_{counter}"
                    counter += 1
                
                diagrams.append((diagram_name, mermaid_code))
            
            in_mermaid_block = False
            mermaid_lines = []
            continue
        
        # Collect mermaid code lines
        if in_mermaid_block:
            mermaid_lines.append(line)
    
    return diagrams


def mermaid_to_png(input_file: Path, output_file: Path, scale: int = 3, background: str = "white"):
    """
    Convert Mermaid file to PNG using mmdc.
    
    Args:
        input_file: Path to .mmd file
        output_file: Path to output .png file
        scale: Scale factor for resolution (default: 3)
        background: Background color (default: "white")
    """
    try:
        subprocess.run([
            "mmdc",
            "-i", str(input_file),
            "-o", str(output_file),
            "-s", str(scale),
            "--backgroundColor", background
        ], check=True, capture_output=True, text=True)
        print(f"  ✓ Converted {input_file.name} → {output_file.name}")
        return True
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        print(f"  ✗ Error converting {input_file.name}: {error_msg}")
        return False
    except FileNotFoundError:
        print(f"  ✗ Error: 'mmdc' command not found. Please install @mermaid-js/mermaid-cli:")
        print(f"    npm install -g @mermaid-js/mermaid-cli")
        return False


def process_mermaid_diagrams(md_file: Path, output_dir: Path, scale: int = 3, background: str = "white"):
    """
    Process all Mermaid diagrams from markdown file.
    
    Args:
        md_file: Path to markdown file
        output_dir: Directory to save .mmd and .png files
        scale: Scale factor for PNG resolution
        background: Background color for PNG
    """
    if not md_file.exists():
        print(f"✗ Error: {md_file} not found!")
        return
    
    print(f"\n📄 Processing: {md_file.name}")
    print("=" * 60)
    
    # Extract all Mermaid diagrams
    diagrams = extract_all_mermaid_from_markdown(md_file)
    
    if not diagrams:
        print("⚠ No Mermaid diagrams found in the file.")
        return
    
    print(f"✓ Found {len(diagrams)} Mermaid diagram(s)\n")
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each diagram
    success_count = 0
    for i, (diagram_name, mermaid_code) in enumerate(diagrams, 1):
        print(f"[{i}/{len(diagrams)}] Processing: {diagram_name}")
        
        # Create filenames
        mmd_file = output_dir / f"{diagram_name}.mmd"
        png_file = output_dir / f"{diagram_name}.png"
        
        # Save Mermaid code to .mmd file
        try:
            with open(mmd_file, 'w', encoding='utf-8') as f:
                f.write(mermaid_code)
            print(f"  ✓ Saved Mermaid code to {mmd_file.name}")
        except Exception as e:
            print(f"  ✗ Error saving {mmd_file.name}: {e}")
            continue
        
        # Convert to PNG
        if mermaid_to_png(mmd_file, png_file, scale=scale, background=background):
            success_count += 1
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"✓ Successfully processed {success_count}/{len(diagrams)} diagram(s)")
    print(f"📁 Output directory: {output_dir.absolute()}")
    print("=" * 60)


def check_mermaid_cli():
    """Check if Mermaid CLI is available."""
    try:
        result = subprocess.run(
            ["mmdc", "--version"], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip() or result.stderr.strip()
            print(f"✓ Mermaid CLI found: {version}")
            return True
        else:
            return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Convert Mermaid diagrams from markdown files to PNG images"
    )
    parser.add_argument(
        "--file",
        type=str,
        default="Methodology.md",
        help="Input markdown file (default: Methodology.md)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="../flowchart_images",
        help="Output directory for images (default: ../flowchart_images)"
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=3,
        help="Scale factor for PNG resolution (1-5, default: 3)"
    )
    parser.add_argument(
        "--background",
        type=str,
        default="white",
        help="Background color (default: white)"
    )
    
    args = parser.parse_args()
    
    # Get script directory
    script_dir = Path(__file__).parent
    
    # Define input and output paths
    md_file = script_dir / args.file
    output_dir = script_dir / args.output
    
    print("=" * 60)
    print("Mermaid to PNG Converter")
    print("=" * 60)
    print(f"Input:  {md_file}")
    print(f"Output: {output_dir}")
    print()
    
    # Check if mmdc is available
    if not check_mermaid_cli():
        print("⚠ Warning: Mermaid CLI (mmdc) not found!")
        print("  Install with: npm install -g @mermaid-js/mermaid-cli")
        print("  Or visit: https://github.com/mermaid-js/mermaid-cli")
        print()
        print("  Alternative: Use online Mermaid editor at https://mermaid.live")
        return
    
    # Process diagrams
    process_mermaid_diagrams(
        md_file=md_file,
        output_dir=output_dir,
        scale=args.scale,
        background=args.background
    )


if __name__ == "__main__":
    main()

