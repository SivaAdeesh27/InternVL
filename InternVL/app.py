import streamlit as st

st.set_page_config(layout="wide")

hide_streamlit_style = """
<style>
    /* Hide the Streamlit header and menu */
    header {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    html, body, .fullScreenFrame, .fullScreenFrame iframe {
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
        border: none;
        display: block;
        overflow: hidden;
    }

    .fullScreenFrame {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 9999;
    }

    .main .block-container {
        padding: 0;
        margin: 0;
        height: 100vh;
    }

    /* Hide Streamlit header and footer */
    header, footer {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Embed the external Streamlit webpage
st.markdown(
    """
    <div class="fullScreenFrame">
        <iframe src="https://internvl.opengvlab.com/"></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

