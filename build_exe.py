"""
ARCANOVA AI - Standalone EXE Builder
Fast, optimized PyInstaller build for the standalone Windows desktop application.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent

def build_executable():
    print("==================================================")
    print("📦 Building ARCANOVA AI Standalone Windows Executable...")
    print("==================================================")
    
    import streamlit
    streamlit_static = Path(streamlit.__file__).parent / "static"
    print(f"Found Streamlit static assets at: {streamlit_static}")
    
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--name=ARCANOVA_AI",
        "--onedir",
        "--noconfirm",
        "--clean",
        "--collect-data=streamlit",
        "--copy-metadata=streamlit",
        "--hidden-import=streamlit.runtime.scriptrunner.magic_funcs",
        "--hidden-import=streamlit.runtime.scriptrunner.script_run_context",
        "--hidden-import=streamlit.runtime.scriptrunner.script_runner",
        "--hidden-import=win32com.client",
        "--hidden-import=pythoncom",
        "--hidden-import=soundfile",
        "--exclude-module=torch",
        "--exclude-module=torchvision",
        "--exclude-module=torchaudio",
        "--exclude-module=transformers",
        "--exclude-module=scipy",
        "--exclude-module=matplotlib",
        "--exclude-module=pandas",
        "--exclude-module=IPython",
        "--exclude-module=notebook",
        "--exclude-module=jupyter",
        "--exclude-module=PyQt5",
        "--exclude-module=PySide6",
        "--exclude-module=PyQt6",
        "--exclude-module=PySide2",
        "--exclude-module=cv2",
        f"--add-data={streamlit_static};streamlit/static",
        f"--add-data={BASE_DIR / 'src'};src",
        f"--add-data={BASE_DIR / 'app.py'};.",
        str(BASE_DIR / "run_app.py")
    ]
    
    try:
        subprocess.run(cmd, cwd=str(BASE_DIR), check=True)
        
        # Ensure static files exist in both internal and root
        dist_dir = BASE_DIR / "dist" / "ARCANOVA_AI"
        target_static_1 = dist_dir / "_internal" / "streamlit" / "static"
        target_static_2 = dist_dir / "streamlit" / "static"
        target_static_1.mkdir(parents=True, exist_ok=True)
        target_static_2.mkdir(parents=True, exist_ok=True)
        
        if streamlit_static.exists():
            shutil.copytree(streamlit_static, target_static_1, dirs_exist_ok=True)
            shutil.copytree(streamlit_static, target_static_2, dirs_exist_ok=True)
            
        print("\n==================================================")
        print("🎉 Executable built successfully inside 'dist/ARCANOVA_AI/'!")
        print("==================================================")
    except Exception as e:
        print(f"⚠️ PyInstaller Build process output: {e}")

if __name__ == "__main__":
    build_executable()
