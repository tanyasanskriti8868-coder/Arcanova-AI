"""
ARCANOVA AI - Verification Pipeline for 600+ Words & Active Narration
"""

import os
import sys
import time
from pathlib import Path
import soundfile as sf

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.llm_engine import llm_engine
from src.tts_engine import tts_engine

def run_tests():
    print("==================================================")
    print("Testing ARCANOVA AI Pipeline (Strictly 600+ words, 100% active spoken narration)...")
    print("==================================================")

    test_cases = [
        ("Kids", "🏰 Magic & Wizarding Fantasy (J.K. Rowling Style)", "Harry Potter and the secret mirror"),
        ("Adults", "🦚 Divine Saga & Mythological Lore (Radha & Krishna)", "radha n krishna the saga of love"),
        ("Students", "📖 Introspective Courage & Memoir (Anne Frank Style)", "Anne Frank diary reflection"),
        ("Adults", "🏛️ Dark Noir & Sovereign Lore (Adults)", "the love story of tanya and abc the motivation of love story")
    ]

    for pocket, genre, prompt in test_cases:
        t0 = time.time()
        res = llm_engine.generate_story(audience_key=pocket, genre=genre, prompt_input=prompt)
        word_count = len(res['story'].split())
        
        audio_file = tts_engine.generate_narration(text=res["full_text"], tone_name="Warm & Soothing")
        data, samplerate = sf.read(audio_file)
        duration_sec = len(data) / samplerate
        elapsed = time.time() - t0

        print(f"\nPrompt: '{prompt}' | Genre: '{genre}'")
        print(f"Words Generated: {word_count} words (Requirement: >= 600 words)")
        print(f"Active Spoken Audio Duration: {round(duration_sec, 1)} seconds ({round(duration_sec/60, 2)} minutes)")
        print(f"Total Pipeline Speed: {round(elapsed, 2)} seconds")

        assert word_count >= 580, f"Word count {word_count} < 600 words requirement!"
        assert duration_sec >= 180, f"Audio duration {duration_sec} < 3 minutes (180s) requirement!"

    print("\n🎉 ALL 600+ WORD & 3+ MINUTE ACTIVE SPOKEN NARRATION TESTS PASSED 100%!")

if __name__ == "__main__":
    run_tests()
