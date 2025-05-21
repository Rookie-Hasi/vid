import streamlit as st
from yt_dlp import YoutubeDL
import traceback
import os

# Page configuration
st.set_page_config(page_title="viddl.online - Video Downloader", layout="centered")

# Header
st.title("📥 Universal Video Downloader")
st.markdown("Download videos from **TikTok, Facebook, Instagram, Twitter, and YouTube** easily with viddl.online.")
st.markdown("---")

# How to use instructions
with st.expander("❓ How to Download Videos?"):
    st.markdown("""
    1. Select the platform (TikTok, Facebook, Instagram, Twitter, YouTube).
    2. Paste the video URL in the input box.
    3. Click the **Download** button.
    4. Wait for the video to download.
    5. Click the download button to save the video to your device.
    
    **Note:** Only individual videos are supported; playlists or multiple videos at once are not supported.
    """)

# Platform selection
platform = st.selectbox("Select Platform", ["TikTok", "Facebook", "Instagram", "Twitter", "YouTube"])
url = st.text_input(f"Enter {platform} video URL")

# Download button
if st.button("Download"):
    if not url:
        st.warning("Please enter a video URL.")
    else:
        try:
            st.info("⏳ Downloading video...")

            output_dir = "downloads"
            os.makedirs(output_dir, exist_ok=True)

            ydl_opts = {
                'outtmpl': os.path.join(output_dir, '%(title).40s.%(ext)s'),
                'format': 'mp4',
                'noplaylist': True,
                'quiet': True,
                'no_warnings': True,
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            st.success("✅ Download complete!")

            with open(filename, "rb") as f:
                st.download_button(
                    label="📥 Click here to download video",
                    data=f,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )

        except Exception as e:
            st.error("❌ Download failed!")
            st.code(traceback.format_exc())

# Footer
st.markdown("---")
st.markdown("### 🔒 Disclaimer")
st.markdown("This tool is for educational and personal use only. Please respect content ownership and copyright rules when downloading videos.")

st.markdown("### 👨‍💻 About")
st.markdown("Created by [viddl.online](https://viddl.online) — bringing you fast, secure video downloads.")
