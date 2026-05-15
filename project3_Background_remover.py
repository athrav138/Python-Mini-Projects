import streamlit as st
from PIL import Image
from rembg import remove
import io

st.set_page_config(
    page_title="AI Background Remover",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ AI Background Remover")

if "output_img" not in st.session_state:
    st.session_state.output_img = None

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGBA")

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Remove Background"):

            with st.spinner("Removing background..."):

                input_bytes = io.BytesIO()
                img.save(input_bytes, format="PNG")

                output_bytes = remove(input_bytes.getvalue())

                output_image = Image.open(
                    io.BytesIO(output_bytes)
                )

                st.session_state.output_img = output_image

    with col2:
        if st.button("Clear / Upload New"):
            st.session_state.output_img = None
            st.rerun()

if st.session_state.output_img is not None:

    st.subheader("Background Removed")

    st.image(
        st.session_state.output_img,
        use_container_width=True
    )

    download_buffer = io.BytesIO()

    st.session_state.output_img.save(
        download_buffer,
        format="PNG"
    )

    st.download_button(
        label="Download Image",
        data=download_buffer.getvalue(),
        file_name="background_removed.png",
        mime="image/png"
    )
    

# Command to Run - py -m streamlit run project3_background_remover.py
