import os
import subprocess
import sys
from pathlib import Path

def convert_ui_files():
    """
    Convert all .ui files in forms_ui directory to .py files in forms_py directory
    """
    # Get the base directory
    base_dir = Path(__file__).parent.parent

    ui_dir = base_dir / "forms_ui"
    py_dir = base_dir / "forms_py"

    # Ensure the Python forms directory exists
    if not py_dir.exists():
        py_dir.mkdir(parents=True)

    # Get all .ui files
    ui_files = list(ui_dir.glob("*.ui"))

    if not ui_files:
        print("No UI files found in forms_ui directory.")
        return

    print(f"Found {len(ui_files)} UI files to convert.")

    # Convert each file
    for ui_file in ui_files:
        py_file = py_dir / f"ui_{ui_file.stem}.py"

        # Command to convert UI to Python
        cmd = ["pyuic5", str(ui_file), "-o", str(py_file)]

        try:
            print(f"Converting {ui_file.name} to {py_file.name}...")
            subprocess.run(cmd, check=True)
            print(f"Successfully converted {ui_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {ui_file.name}: {e}")
        except FileNotFoundError:
            print("Error: pyuic5 not found. Make sure PyQt5 is installed and pyuic5 is in your PATH.")
            print("You can install it with: pip install PyQt5")
            sys.exit(1)

    print("\nConversion complete!")
    print(f"Converted {len(ui_files)} UI files to Python files in {py_dir}")

if __name__ == "__main__":
    convert_ui_files()