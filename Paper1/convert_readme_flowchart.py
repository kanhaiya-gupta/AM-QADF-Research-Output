#!/usr/bin/env python3
"""
Convert Mermaid flowcharts from README.md and deployment_flowchart.md to PNG images.

Requirements:
    npm install -g @mermaid-js/mermaid-cli

Usage:
    python convert_readme_flowchart.py
    python convert_readme_flowchart.py --file deployment_flowchart.md
    python convert_readme_flowchart.py --all
"""

import subprocess
import re
import os
import argparse
from pathlib import Path


def extract_mermaid_from_markdown(markdown_file: Path) -> str:
    """Extract the Mermaid flowchart from a markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find mermaid code block
    pattern = r'```mermaid\n(.*?)```'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    else:
        raise ValueError(f"No Mermaid diagram found in {markdown_file.name}")


def mermaid_to_png(input_file: Path, output_file: Path, scale: int = 5, background: str = "white"):
    """Convert Mermaid file to PNG using mmdc."""
    try:
        subprocess.run([
            "mmdc",
            "-i", str(input_file),
            "-o", str(output_file),
            "-s", str(scale),
            "--backgroundColor", background
        ], check=True, capture_output=True, text=True)
        print(f"✓ Converted {input_file.name} → {output_file.name}")
        return True
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        print(f"✗ Error converting {input_file.name}: {error_msg}")
        return False
    except FileNotFoundError:
        print(f"✗ Error: 'mmdc' command not found. Please install @mermaid-js/mermaid-cli:")
        print(f"  npm install -g @mermaid-js/mermaid-cli")
        return False


def check_mermaid_cli():
    """Check if Mermaid CLI is available."""
    try:
        result = subprocess.run(
            ["mmdc", "--version"], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def process_file(markdown_file: Path, output_dir: Path, output_name: str, scale: int = 5, background: str = "white"):
    """Process a single markdown file and convert its Mermaid diagram."""
    # Extract mermaid code
    try:
        print(f"📄 Extracting Mermaid diagram from {markdown_file.name}...")
        mermaid_code = extract_mermaid_from_markdown(markdown_file)
        print("✓ Found Mermaid diagram\n")
    except ValueError as e:
        print(f"✗ Error: {e}")
        return False
    
    # Create filenames
    mmd_file = output_dir / f"{output_name}.mmd"
    png_file = output_dir / f"{output_name}.png"
    
    # Save Mermaid code to .mmd file
    try:
        with open(mmd_file, 'w', encoding='utf-8') as f:
            f.write(mermaid_code)
        print(f"✓ Saved Mermaid code to {mmd_file.name}")
    except Exception as e:
        print(f"✗ Error saving {mmd_file.name}: {e}")
        return False
    
    # Convert to PNG
    print(f"🖼️  Converting to PNG (scale: {scale}x for high quality)...")
    if mermaid_to_png(mmd_file, png_file, scale=scale, background=background):
        print(f"✓ Success! Output: {png_file.name}\n")
        return True
    else:
        print(f"✗ Conversion failed\n")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Convert Mermaid flowcharts from markdown files to PNG images"
    )
    parser.add_argument(
        "--file",
        type=str,
        choices=["readme", "deployment", "all"],
        default="readme",
        help="Which flowchart to convert: 'readme', 'deployment', or 'all' (default: readme)"
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=6,
        help="Scale factor for PNG resolution (1-5, default: 5 for high quality)"
    )
    parser.add_argument(
        "--background",
        type=str,
        default="white",
        help="Background color (default: white)"
    )
    
    args = parser.parse_args()
    
    # Get paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    output_dir = script_dir / "flowchart_images"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("Convert Mermaid Flowcharts to PNG")
    print("=" * 60)
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
    
    success_count = 0
    total_count = 0
    
    # Process files based on argument
    files_to_process = []
    
    if args.file in ["readme", "all"]:
        readme_file = repo_root / "README.md"
        if readme_file.exists():
            files_to_process.append((readme_file, "framework_overview_flowchart"))
        else:
            print(f"⚠ Warning: {readme_file} not found")
    
    if args.file in ["deployment", "all"]:
        deployment_file = script_dir / "deployment_flowchart.md"
        if deployment_file.exists():
            files_to_process.append((deployment_file, "deployment_architecture_flowchart"))
        else:
            print(f"⚠ Warning: {deployment_file} not found")
    
    if not files_to_process:
        print("✗ No files to process!")
        return
    
    print(f"📋 Processing {len(files_to_process)} file(s)\n")
    
    # Process each file
    for markdown_file, output_name in files_to_process:
        total_count += 1
        print(f"[{total_count}/{len(files_to_process)}] Processing: {markdown_file.name}")
        print("-" * 60)
        if process_file(markdown_file, output_dir, output_name, scale=args.scale, background=args.background):
            success_count += 1
        print()
    
    # Summary
    print("=" * 60)
    print(f"✓ Successfully processed {success_count}/{total_count} file(s)")
    print(f"📁 Output directory: {output_dir.absolute()}")
    print("=" * 60)


if __name__ == "__main__":
    main()
