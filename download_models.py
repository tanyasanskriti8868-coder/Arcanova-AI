"""
ARCANOVA AI - Model Downloader CLI Script
Downloads Qwen 2.5 3B LLM and Kokoro TTS 82M models directly to local disk cache.
No Hugging Face gated API keys required!
"""

import os
import sys
from pathlib import Path

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
CACHE_DIR = BASE_DIR / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def download_qwen_model():
    print("==================================================")
    print("📥 Downloading Qwen 2.5 3B Instruct model locally...")
    print("==================================================")
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        model_id = "Qwen/Qwen2.5-3B-Instruct"
        print(f"Fetching tokenizer for {model_id}...")
        AutoTokenizer.from_pretrained(model_id, cache_dir=str(CACHE_DIR), trust_remote_code=True)
        print(f"Fetching model weights for {model_id}...")
        AutoModelForCausalLM.from_pretrained(model_id, cache_dir=str(CACHE_DIR), trust_remote_code=True)
        print("✅ Qwen 2.5 3B model downloaded and cached successfully!")
    except Exception as e:
        print(f"⚠️ Notice downloading Qwen model: {e}")
        print("ARCANOVA fallback neural engine will handle story generation.")

def download_kokoro_model():
    print("\n==================================================")
    print("🔊 Downloading Kokoro TTS (82M) weights locally...")
    print("==================================================")
    try:
        from huggingface_hub import hf_hub_download
        onnx_path = hf_hub_download(
            repo_id="hexgrad/Kokoro-82M",
            filename="kokoro-v1_0.onnx",
            local_dir=str(CACHE_DIR)
        )
        voices_path = hf_hub_download(
            repo_id="hexgrad/Kokoro-82M",
            filename="voices.bin",
            local_dir=str(CACHE_DIR)
        )
        print("✅ Kokoro-82M TTS model downloaded and cached successfully!")
    except Exception as e:
        print(f"⚠️ Notice downloading Kokoro TTS model: {e}")
        print("ARCANOVA audio engine fallback will handle voice generation.")

if __name__ == "__main__":
    download_qwen_model()
    download_kokoro_model()
    print("\n🎉 All model download steps completed!")
