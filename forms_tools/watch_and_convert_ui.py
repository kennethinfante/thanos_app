import os
import subprocess
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class UIFileHandler(FileSystemEventHandler):
    def __init__(self, ui_dir, py_dir):
        self.ui_dir = ui_dir
        self.py_dir = py_dir

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.ui'):
            ui_file = Path(event.src_path)
            py_file = self.py_dir / f"{ui_file.stem}.py"

            print(f"UI file changed: {ui_file.name}")
            self.convert_ui_file(ui_file, py_file)

    def convert_ui_file(self, ui_file, py_file):
        cmd = ["pyuic5", str(ui_file), "-o", str(py_file)]

        try:
            print(f"Converting {ui_file.name} to {py_file.name}...")
            subprocess.run(cmd, check=True)
            print(f"Successfully converted {ui_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {ui_file.name}: {e}")

def watch_ui_directory():
    base_dir = Path(__file__).parent
    ui_dir = base_dir / "forms_ui"
    py_dir = base_dir / "forms_py"

    # Ensure the Python forms directory exists
    if not py_dir.exists():
        py_dir.mkdir(parents=True)

    # First, convert all existing UI files
    ui_files = list(ui_dir.glob("*.ui"))
    handler = UIFileHandler(ui_dir, py_dir)

    for ui_file in ui_files:
        py_file = py_dir / f"{ui_file.stem}.py"
        handler.convert_ui_file(ui_file, py_file)

    # Then start watching for changes
    observer = Observer()
    observer.schedule(handler, str(ui_dir), recursive=False)
    observer.start()

    print(f"\nWatching for changes in {ui_dir}...")
    print("Press Ctrl+C to stop")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    watch_ui_directory()