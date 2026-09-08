"""
ARCANOVA AI - Portable Offline Package Creator
Bundles the compiled executable, offline Kokoro-82M voice weights, and neural assets
into a single ready-to-share ZIP file for any Windows laptop!
"""

import os
import sys
import shutil
import zipfile
from pathlib import Path

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
DIST_DIR = BASE_DIR / "dist" / "ARCANOVA_AI"
OUTPUT_ZIP = BASE_DIR / "ARCANOVA_AI_Offline_Portable.zip"

def create_offline_package():
    print("==================================================")
    print("📦 Creating 100% Offline Portable Software Package...")
    print("==================================================")

    if not DIST_DIR.exists():
        print(f"❌ Error: Compiled folder not found at {DIST_DIR}")
        print("Please run `python build_exe.py` first.")
        return

    import streamlit
    streamlit_static = Path(streamlit.__file__).parent / "static"

    # Ensure streamlit static files exist in both possible search paths
    target_static_1 = DIST_DIR / "_internal" / "streamlit" / "static"
    target_static_2 = DIST_DIR / "streamlit" / "static"
    target_static_1.mkdir(parents=True, exist_ok=True)
    target_static_2.mkdir(parents=True, exist_ok=True)

    if streamlit_static.exists():
        print(f"Ensuring Streamlit static assets in distribution...")
        shutil.copytree(streamlit_static, target_static_1, dirs_exist_ok=True)
        shutil.copytree(streamlit_static, target_static_2, dirs_exist_ok=True)

    # Ensure cache folder exists inside dist bundle
    bundle_cache = DIST_DIR / "cache"
    bundle_cache.mkdir(parents=True, exist_ok=True)

    # Copy local Kokoro voice weights if available in local cache
    local_cache = BASE_DIR / "cache"
    if local_cache.exists():
        for file_name in os.listdir(local_cache):
            src_file = local_cache / file_name
            if src_file.is_file() and (file_name.endswith(".onnx") or file_name.endswith(".bin") or file_name.endswith(".wav")):
                dst_file = bundle_cache / file_name
                print(f"Copying offline asset: {file_name}...")
                shutil.copy2(src_file, dst_file)

    # Create README_PORTABLE.txt inside bundle
    readme_text = """==================================================
ARCANOVA AI - Portable Offline Edition
==================================================

How to run on any Windows PC:
1. Double-click `ARCANOVA_AI.exe` inside this folder.
2. The application will automatically open in your web browser.
3. 100% Offline execution -- no internet connection or Python required!

Enjoy creating stories and voice narrations!
"""
    with open(DIST_DIR / "README_PORTABLE.txt", "w", encoding="utf-8") as f:
        f.write(readme_text)

    # Compress into a single zip file
    print(f"\nCompressing entire bundle into: {OUTPUT_ZIP.name}...")
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(DIST_DIR):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(DIST_DIR.parent)
                zipf.write(file_path, arcname)

    print("\n==================================================")
    print(f"🎉 SUCCESS! Portable offline package created:")
    print(f"📁 {OUTPUT_ZIP}")
    print("==================================================")

if __name__ == "__main__":
    create_offline_package()
