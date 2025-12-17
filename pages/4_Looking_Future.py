import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys
import base64

# Add parent directory to path to import styles
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from styles import load_css

# Set page config
st.set_page_config(
    page_title="Looking to Future | Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"  # Start with sidebar collapsed
)

# Load custom CSS
load_css()

# Import shared components
from shared_components import create_sidebar, show_wip_warning

# Store current page in session state for sidebar to access
st.session_state['current_page'] = __file__

# Create the sidebar with the current page name
create_sidebar(os.path.basename(__file__))

# Show work-in-progress warning
# show_wip_warning()

######################## PAGE CONTENT ########################

# load images

from PIL import Image

# Image Paths
temp_agem = r"assets/temp_images/agem.png"
temp_ss1 = r"assets/temp_images/ss1.png"
temp_ss2 = r"assets/temp_images/ss2.png"


# Load the images as bytes and convert to base64
with open(temp_agem, "rb") as f:
    temp_agem_bytes = f.read()
    temp_agem_base64 = base64.b64encode(temp_agem_bytes).decode()

with open(temp_ss1, "rb") as f:
    temp_ss1_bytes = f.read()
    temp_ss1_base64 = base64.b64encode(temp_ss1_bytes).decode()

with open(temp_ss2, "rb") as f:
    temp_ss2_bytes = f.read()
    temp_ss2_base64 = base64.b64encode(temp_ss2_bytes).decode()

# actual page content

st.markdown("""
<h2 style="color: #1E5C8E; padding-top: 2rem; margin-top: 0.5rem;">Supply Stack <br> (Balancing authority: SOCO)</h2>
""", unsafe_allow_html=True)

# image
st.markdown(f"""
<div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
    <img src="data:image/png;base64,{temp_ss1_base64}" 
            style="width: 90%; height: auto; border-radius: 10px;" 
            alt="Energy efficient home with sustainable features">
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
    <img src="data:image/png;base64,{temp_ss2_base64}" 
            style="width: 90%; height: auto; border-radius: 10px;" 
            alt="Energy efficient home with sustainable features">
</div>
""", unsafe_allow_html=True)
    
# break
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# title
st.markdown("""
<h2 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem;">Grid Edge Model Expansion</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.2rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            The initial analyses have expanded to include all 11 counties within the Atlanta Metropolitan Area.
        </p>
    </div>
    """, unsafe_allow_html=True)

# images
st.markdown("""
<h4 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem; text-align: left; font-size: 3rem; margin-bottom: 1rem;">Residential Comparison: Baseline vs. Heatpump Retrofit</h4>
""", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
    <img src="https://i.imgur.com/qJpCqbP.gif" 
            style="width: 60%; height: auto; border-radius: 10px;" 
            alt="Energy efficient home with sustainable features">
</div>
""", unsafe_allow_html=True)

    
st.markdown("""
<h4 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem; text-align: left; font-size: 3rem; margin-bottom: 1rem;">Commercial Comparison: Baseline vs. Heatpump Retrofit</h4>
""", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
    <img src="https://i.imgur.com/3XtFCgq.gif" 
            style="width: 60%; height: auto; border-radius: 10px;" 
            alt="Energy efficient home with sustainable features">
</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
    <img src="https://i.imgur.com/7D9aWnT.gif" 
            style="width: 60%; height: auto; border-radius: 10px;" 
            alt="Energy efficient home with sustainable features">
</div>
""", unsafe_allow_html=True)