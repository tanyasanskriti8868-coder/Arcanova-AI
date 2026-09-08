# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [('C:\\Users\\DELL\\anaconda3\\Lib\\site-packages\\streamlit\\static', 'streamlit/static'), ('C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\arcanova-ai\\src', 'src'), ('C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\arcanova-ai\\app.py', '.')]
datas += collect_data_files('streamlit')
datas += copy_metadata('streamlit')


a = Analysis(
    ['C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\arcanova-ai\\run_app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['streamlit.runtime.scriptrunner.magic_funcs', 'streamlit.runtime.scriptrunner.script_run_context', 'streamlit.runtime.scriptrunner.script_runner', 'win32com.client', 'pythoncom', 'soundfile'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['torch', 'torchvision', 'torchaudio', 'transformers', 'scipy', 'matplotlib', 'pandas', 'IPython', 'notebook', 'jupyter', 'PyQt5', 'PySide6', 'PyQt6', 'PySide2', 'cv2'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ARCANOVA_AI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ARCANOVA_AI',
)
