"""
ARCANOVA AI - Master Storytelling & Voice Application
Strict Obsidian Black & Soft Beige Palette (Zero White), 3-Input Control Panel (Pocket, Genre, Topic),
Instant < 30s Execution, Complete Stories Under 600 Words, and 4+ Minute Voice Narration.
"""

import os
import sys
import time
import random
from pathlib import Path
import importlib.metadata

# Patch importlib.metadata.version for Streamlit PyInstaller executable compatibility
_orig_version = importlib.metadata.version
def _patched_version(distribution_name):
    try:
        return _orig_version(distribution_name)
    except importlib.metadata.PackageNotFoundError:
        if distribution_name.lower() == "streamlit":
            return "1.38.0"
        return "1.0.0"

importlib.metadata.version = _patched_version

import streamlit as st

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from src.config import EMOJIS
from src.styles import inject_custom_styles
from src.audience_pockets import AUDIENCE_POCKETS
from src.llm_engine import llm_engine
from src.tts_engine import tts_engine

# Motivational Quotes
MOTIVATIONAL_QUOTES = [
    "\"The future belongs to those who believe in the beauty of their dreams.\" -- Eleanor Roosevelt",
    "\"It always seems impossible until it's done.\" -- Nelson Mandela",
    "\"Do not go where the path may lead, go instead where there is no path and leave a trail.\" -- Ralph Waldo Emerson",
    "\"You do not rise to the level of your goals. You fall to the level of your systems.\" -- James Clear",
    "\"How wonderful it is that nobody need wait a single moment before starting to improve the world.\" -- Anne Frank",
    "\"Words are, in my not-so-humble opinion, our most inexhaustible source of magic.\" -- J.K. Rowling"
]

GENRE_OPTIONS = [
    "🏰 Magic & Wizarding Fantasy (J.K. Rowling Style)",
    "🦚 Divine Saga & Mythological Lore (Radha & Krishna)",
    "📖 Introspective Courage & Memoir (Anne Frank Style)",
    "🔥 Modern Romance & Drama (Ana Huang Style)",
    "⚡ Atomic Habits & Mastery (James Clear Style)",
    "🏛️ Dark Noir & Sovereign Lore (Adults)",
    "🌌 Sci-Fi & Cyber-Tech Legends",
    "🌟 Family Triumph & Motivational"
]

# Page Configuration
st.set_page_config(
    page_title="ARCANOVA AI | Sovereign Narrative & Voice Engine",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Strict Black & Beige CSS
inject_custom_styles()

def main():
    # Sidebar Dashboard - Strict Black & Beige
    with st.sidebar:
        st.markdown(f"## {EMOJIS['SETTINGS']} System Dashboard")
        st.caption("⚡ **Generation Speed**: Instant (< 10s Total)")
        st.caption("🎙️ **Voice Narration**: 4+ Minutes Continuous Audio")
        st.caption("🎨 **Palette**: Obsidian Black | Soft Beige (Zero White)")
        st.markdown("---")
        st.markdown("### 👑 ARCANOVA AI v5.0")
        st.info("Full Narrative & Voice Engine Active.")

    # Main Royal Header
    st.markdown("""
    <div style='text-align: center; padding: 10px 0 15px 0;'>
        <h1 style='font-size: 3.8rem; margin-bottom: 5px; color: #F4EAD4;'>ARCANOVA AI</h1>
        <p style='font-size: 1.35rem; color: #E6D7C3; font-style: italic; font-family: "Cormorant Garamond", serif;'>
            The Sovereign Storytelling & 4+ Minute Voice Narration Suite
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Dynamic Motivational Quote Banner
    selected_quote = random.choice(MOTIVATIONAL_QUOTES)
    st.markdown(f"""
    <div class="motivational-banner">
        {selected_quote}
    </div>
    """, unsafe_allow_html=True)

    # Clean 2-Column Split: Inputs on LEFT Panel (5/12), Showcase on RIGHT Panel (7/12)
    left_panel, right_panel = st.columns([5, 7])

    with left_panel:
        st.markdown(f"""
        <div class="royal-card">
            <h2>{EMOJIS['POCKETS']} Story Control Panel</h2>
            <p style="color: #D4C3AC; font-size: 0.95rem;">Select your audience pocket, choose a literary genre, and enter your premise.</p>
        </div>
        """, unsafe_allow_html=True)

        # INPUT 1: Section Pocket
        st.markdown(f"### 1. {EMOJIS['POCKETS']} Audience Pocket")
        pocket_options = list(AUDIENCE_POCKETS.keys())
        audience_choice = st.radio(
            "Select Section Pocket",
            options=pocket_options,
            format_func=lambda x: AUDIENCE_POCKETS[x]["title"],
            index=1,
            horizontal=False
        )
        pocket_info = AUDIENCE_POCKETS[audience_choice]
        st.markdown(f"<span class='pocket-badge-royal'>{pocket_info['badge']}</span>", unsafe_allow_html=True)

        # INPUT 2: Specific Literary Genre Selection
        st.markdown(f"### 2. {EMOJIS['SETTINGS']} Literary Genre & Style")
        selected_genre = st.selectbox(
            "Select Story Genre:",
            options=GENRE_OPTIONS,
            index=0 if audience_choice == "Kids" else (2 if audience_choice == "Students" else 5)
        )

        # INPUT 3: Story Topic Input (Soft Beige Box, Pure Black Text & Placeholder)
        st.markdown(f"### 3. {EMOJIS['STORY']} Story Topic & Characters")
        prompt_input = st.text_area(
            "Topic input:",
            value="",
            placeholder="What topic do you want to listen to today? E.g., Radha & Krishna, Harry Potter, or a student overcoming challenges...",
            height=130
        )

        # Fail-Safe Primary Action Button
        st.markdown("<br>", unsafe_allow_html=True)
        generate_clicked = st.button(f"{EMOJIS['GENERATE']} Generate Story & Narration (One-Touch)")

    with right_panel:
        st.markdown(f"""
        <div class="royal-card">
            <h2>{EMOJIS['STORY']} Narrative & Voice Showcase</h2>
            <p style="color: #D4C3AC; font-size: 0.95rem;">Your generated story and 4+ minute audio narration will render here.</p>
        </div>
        """, unsafe_allow_html=True)

        # Real-time 0% to 100% Progress Generation Engine
        if generate_clicked:
            topic = prompt_input.strip() if prompt_input.strip() else pocket_info["default_prompt"]

            progress_container = st.empty()
            status_text = st.empty()
            progress_bar = progress_container.progress(0)

            start_time = time.time()

            # 0% - 35%: Story Generation
            status_text.markdown(f"<p style='color:#F4EAD4;'>📖 <b>[35%] Weaving narrative for: '{topic}'...</b></p>", unsafe_allow_html=True)
            progress_bar.progress(35)

            res = llm_engine.generate_story(
                audience_key=audience_choice,
                genre=selected_genre,
                prompt_input=topic
            )

            # 35% - 85%: Voice Narration Synthesis
            status_text.markdown("<p style='color:#F4EAD4;'>🎙️ <b>[75%] Synthesizing 4+ minute voice narration track...</b></p>", unsafe_allow_html=True)
            progress_bar.progress(75)

            audio_file = tts_engine.generate_narration(
                text=res["full_text"],
                tone_name="Warm & Soothing" if audience_choice == "Adults" else "Energetic & Heroic",
                voice_id="af_heart"
            )

            # 100%: Finished!
            progress_bar.progress(100)
            status_text.markdown("<p style='color:#F4EAD4;'>✨ <b>[100%] Story & 4+ Minute Voice Narration generated successfully!</b></p>", unsafe_allow_html=True)
            time.sleep(0.3)

            progress_container.empty()
            status_text.empty()

            elapsed = round(time.time() - start_time, 2)

            st.session_state["current_result"] = res
            st.session_state["audio_file"] = audio_file
            st.session_state["elapsed"] = elapsed
            st.session_state["genre_used"] = selected_genre

        # Display Current Generated Story & Audio Result
        res = st.session_state.get("current_result")
        audio_file = st.session_state.get("audio_file")
        elapsed = st.session_state.get("elapsed", 0)
        genre_used = st.session_state.get("genre_used", "")

        if res:
            word_count = len(res['story'].split())
            st.success(f"✨ Royal Story & 4+ Minute Narration generated in **{elapsed} seconds**! (Total: **{word_count} words**)")

            # Display Clean Multi-Paragraph Story
            st.markdown(f"""
            <div class="story-display-royal">
                <div style="font-size: 1.1rem; color: #E6D7C3; margin-bottom: 12px; font-weight: 600;">
                    👑 {genre_used}
                </div>
                {res['story'].replace('\n', '<br><br>')}
                <div class="warm-closing-royal">
                    {res['warm_closing']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Display Interactive Audio Player
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"### {EMOJIS['NARRATION']} Voice Narration Player (4+ Minutes)")

            if audio_file and os.path.exists(audio_file):
                with open(audio_file, "rb") as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/wav")

                col_dl1, col_dl2 = st.columns(2)
                with col_dl1:
                    st.download_button(
                        label="⬇️ Download Audio (WAV - 4+ Mins)",
                        data=audio_bytes,
                        file_name=f"ARCANOVA_Narration_{audience_choice}.wav",
                        mime="audio/wav"
                    )
                with col_dl2:
                    st.download_button(
                        label="📄 Download Story Text (TXT)",
                        data=f"{res['story']}\n\n{res['warm_closing']}",
                        file_name=f"ARCANOVA_Story_{audience_choice}.txt",
                        mime="text/plain"
                    )

    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 40px 0 10px 0; color: #D4C3AC; font-size: 0.9rem;'>
        ARCANOVA AI &copy; 2026 | Built with Streamlit, Sovereign Story Engine & Windows Voice Synthesis
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
