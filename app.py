import streamlit as st
from rembg import remove
from PIL import Image
from moviepy.editor import ImageClip

st.set_page_config(page_title="AI Image Tool", page_icon="✨", layout="centered")

st.title("✨ AI Web App: Background Remover & Image to Video")

uploaded_file = st.file_uploader("📂 Upload an image", type=["jpg","jpeg","png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # --- REMOVE BACKGROUND ---
    st.subheader("🔹 Remove Background")
    result = remove(image)
    st.image(result, caption="Background Removed", use_column_width=True)

    # --- CHANGE BACKGROUND ---
    st.subheader("🔹 Change Background")
    bg_choice = st.color_picker("Pick a background color", "#00ff00")
    bg = Image.new("RGB", result.size, bg_choice)
    final = Image.alpha_composite(bg.convert("RGBA"), result)
    st.image(final, caption="Background Changed", use_column_width=True)

    # --- IMAGE TO VIDEO ---
    st.subheader("🔹 Image to Video")
    duration = st.slider("Select video duration (seconds)", 2, 10, 5)
    clip = ImageClip(final).set_duration(duration)
    clip.write_videofile("output.mp4", fps=24, codec="libx264")
    st.video("output.mp4")