"""
ARCANOVA AI - Standalone Executable Launcher
Launches the Streamlit server programmatically and automatically opens the user's web browser.
"""

import os
import sys
import time
import threading
import webbrowser
from pathlib import Path
import importlib.metadata

# Fix importlib.metadata.PackageNotFoundError for Streamlit in PyInstaller frozen bundles
_orig_version = importlib.metadata.version
def _patched_version(distribution_name):
    try:
        return _orig_version(distribution_name)
    except importlib.metadata.PackageNotFoundError:
        if distribution_name.lower() == "streamlit":
            return "1.51.0"
        return "1.0.0"

importlib.metadata.version = _patched_version

import streamlit.web.cli as stcli

def open_browser():
    """Wait for server to start and automatically open the default web browser."""
    time.sleep(2.0)
    try:
        webbrowser.open("http://localhost:8501")
    except Exception:
        pass

if __name__ == "__main__":
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    # Path resolution for frozen or standalone execution
    if getattr(sys, 'frozen', False):
        bundle_dir = Path(sys._MEIPASS)
    else:
        bundle_dir = Path(__file__).resolve().parent
    
    app_path = bundle_dir / "app.py"
    if not app_path.exists():
        app_path = Path(__file__).resolve().parent / "app.py"

    # Launch browser in a background thread
    threading.Thread(target=open_browser, daemon=True).start()

    sys.argv = [
        "streamlit",
        "run",
        str(app_path),
        "--global.developmentMode=false",
        "--server.headless=true",
        "--server.port=8501",
        "--browser.gatherUsageStats=false",
    ]
    sys.exit(stcli.main())
