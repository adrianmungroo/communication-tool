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
    page_title="Local Generation and Storage | Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"  # Start with sidebar collapsed
)

# Load custom CSS
load_css()


# Import shared components
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from shared_components import create_sidebar, show_wip_warning

# Store current page in session state for sidebar to access
st.session_state['current_page'] = __file__

# Create the sidebar with the current page name
create_sidebar(os.path.basename(__file__))

# Show work-in-progress warning
# show_wip_warning()

######################## PAGE CONTENT ########################

## LOAD Images

from PIL import Image

# Image Paths
lg_bat_path = r"assets/lg_bat.png"
lg_capacity_path = r"assets/lg_capacity.png"
lg_flexible_path = r"assets/lg_flexible.png"
lg_texas_path = r"assets/lg_texas.png"

# Load the images as bytes and convert to base64
with open(lg_bat_path, "rb") as f:
    lg_bat_bytes = f.read()
    lg_bat_base64 = base64.b64encode(lg_bat_bytes).decode()

with open(lg_capacity_path, "rb") as f:
    lg_capacity_bytes = f.read()
    lg_capacity_base64 = base64.b64encode(lg_capacity_bytes).decode()
    
with open(lg_flexible_path, "rb") as f:
    lg_flexible_bytes = f.read()
    lg_flexible_base64 = base64.b64encode(lg_flexible_bytes).decode()
    
with open(lg_texas_path, "rb") as f:
    lg_texas_bytes = f.read()
    lg_texas_base64 = base64.b64encode(lg_texas_bytes).decode()

## Actual page content begins

# title
st.markdown("""
<h4 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem; text-align: left; font-size: 3rem; margin-bottom: 1rem;">Local Generation & Storage</h4>
""", unsafe_allow_html=True)

left_col, middle_col, right_col = st.columns([1,2,2])

with left_col:
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.3rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            New technologies are transforming how Atlanta generates, stores, and manages electricity. These technologies enable local and distributed energy resources, reducing the dependency on the grid, increasing resiliency, and overall efficiency.
        </p>
    </div>
    """, unsafe_allow_html=True)

with middle_col:
    # title
    st.markdown("""
    <h2 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem;">Local Generation</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.2rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Atlanta receives approximately 5.2 hours of peak sunlight daily on average. 
            <br><br>
            Rooftop solar potential is estimated at 4,800 MW across the region, with additional opportunities for ground-mounted systems, solar parking canopies, and community solar gardens.
        </p>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    # title
    st.markdown("""
    <h2 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem;">Storage and EVs</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.0rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Battery energy storage systems are increasingly being deployed alongside solar installations and at strategic grid locations. These systems provide multiple benefits: peak shaving, backup power during outages, and the ability to time-shift renewable generation to periods of high demand.
            <br><br>
            Electric Vehicles (EVs) are increasingly becoming retrofitted with bi-directional charging, enabling the usage of their battery in cases of emergency as extra energy storage for homes and other building types.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
# break
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# title
st.markdown("""
<h2 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem;">Need & Growth Potential</h2>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([1,1])

with left_col:
    # text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.2rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Local generation and storage can help mitigate weather-related disruptions that may affect the power of millions of customers, more so in large metropolitan areas such as in Atlanta. Such disruptions are becoming more common due to climate change.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h4 style="color: #1E5C8E; padding-top: 1rem; margin-top: 0.5rem; text-align: center;">Development to Mitigate</h4>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.2rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Fortunately, Georgia has been investing in both energy battery storage and solar power generation systems for the last 5-10 years, in addition to technology developments such as bidirectional power flows, further increasing the flexibility of decentralized energy systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{lg_texas_base64}" 
             style="width: 60%; height: auto; border-radius: 10px;" 
             alt="Energy efficient home with sustainable features">
    </div>
    <p style="font-size: 1rem; color: #2c3e50; line-height: 1.5; margin: 0; text-align: center;">Texas Winter-related power outage Source: NPR</p>
    """, unsafe_allow_html=True)

left_img, right_img = st.columns([1,1])

with left_img:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{lg_bat_base64}" 
             style="width: 70%; height: auto; border-radius: 10px;" 
             alt="Energy efficient home with sustainable features">
    </div>
    <p style="font-size: 1rem; color: #2c3e50; line-height: 1.5; margin: 0; text-align: center;">Battery Storage Source: Georgia Power</p>
    """, unsafe_allow_html=True)

with right_img:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{lg_capacity_base64}" 
             style="width: 70%; height: auto; border-radius: 10px;" 
             alt="Energy efficient home with sustainable features">
    </div>
    <p style="font-size: 1rem; color: #2c3e50; line-height: 1.5; margin: 0; text-align: center;">Source: US Energy Information Administration</p>
    """, unsafe_allow_html=True)

# break
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)
    
# title
st.markdown("""
<h2 style="color: #1E5C8E; padding-top: 0rem; margin-top: 0.5rem;">Flexible Energy Management</h2>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{lg_flexible_base64}" 
             style="width: 90%; height: auto; border-radius: 10px;" 
             alt="Energy efficient home with sustainable features">
    </div>
    """, unsafe_allow_html=True)

    