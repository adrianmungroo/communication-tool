import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys
from PIL import Image

# Add parent directory to path to import styles
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from styles import load_css

# Set page config
st.set_page_config(
    page_title="Grid Under Pressure | Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"  # Always show sidebar by default
)

# Load custom CSS
load_css()

# Custom sidebar navigation
with st.sidebar:
    # Get current page name
    current_page = os.path.basename(__file__)
    
    # Navigation links with icons
    st.markdown('<a href="." class="nav-link" target="_self"><span class="nav-icon">🏠</span> Defining Atlanta</a>', unsafe_allow_html=True)
    
    if os.path.exists(os.path.join(os.path.dirname(__file__), "1_Energy_Efficiency.py")):
        st.markdown('<a href="Energy_Efficiency" class="nav-link" target="_self"><span class="nav-icon">🔋</span> Energy Efficiency</a>', unsafe_allow_html=True)
    
    if os.path.exists(os.path.join(os.path.dirname(__file__), "2_Local_Generation.py")):
        st.markdown('<a href="Local_Generation" class="nav-link" target="_self"><span class="nav-icon">☀️</span> Local Generation and Storage</a>', unsafe_allow_html=True)
    
    if current_page == "3_Energy_Grid.py":
        st.markdown('<a href="Energy_Grid" class="nav-link active" target="_self"><span class="nav-icon">🔌</span> Grid Under Pressure</a>', unsafe_allow_html=True)
    else:
        st.markdown('<a href="Energy_Grid" class="nav-link" target="_self"><span class="nav-icon">🔌</span> Grid Under Pressure</a>', unsafe_allow_html=True)
    
    if os.path.exists(os.path.join(os.path.dirname(__file__), "4_Looking_Future.py")):
        st.markdown('<a href="Looking_Future" class="nav-link" target="_self"><span class="nav-icon">🔮</span> Looking to the Future</a>', unsafe_allow_html=True)
    
    # Additional sidebar information
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### About", unsafe_allow_html=True)
    st.info("This dashboard provides insights into Atlanta's energy ecosystem and explores strategies for a sustainable future.")
    
    # Optional: Add contact or help information
    with st.expander("Need Help?"):
        st.write("Learn more at: https://energyshed.research.gatech.edu/")

######################## PAGE CONTENT ########################

# Create a placeholder image for the grid visualization
def create_placeholder_image():
    # Create a blank image with a light background
    img = Image.new('RGB', (600, 400), color=(240, 248, 255))
    return img

# Create the placeholder image
grid_placeholder = create_placeholder_image()

# Create three columns for the main content
col1, col2, col3 = st.columns([1, 2, 3])

# First column - Grid Under Pressure
with col1:
    st.markdown("""
    <h1 style="color: #1E5C8E; margin-bottom: 1.5rem;">Grid Under Pressure</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Atlanta's electrical grid stands at a critical juncture, facing mounting pressure from multiple directions. 
            The traditional model of centralized power distribution is giving way to a complex network balancing increased demand with 
            diverse energy sources. This transformation demands thoughtful planning and targeted investments to ensure reliability 
            while enabling the region's clean energy transition and economic growth.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Second column - Challenges with icons
with col2:
    # Increased Demand section with icon
    st.markdown("""
    <div style="text-align: center;">
        <h3 style="color: #1E5C8E; margin-bottom: 1rem;">Increased Demand 🏢</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Data centers require enormous electricity and exceptional reliability, essentially functioning as 
            small towns on the grid. Meanwhile, residential and commercial growth further strains the system.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Irregular Demand section with icon    
    st.markdown("""
    <div style="text-align: center;">
        <h3 style="color: #1E5C8E; margin-bottom: 1rem;">Irregular Demand 📈</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Grid management grows increasingly complex as energy sources diversify. Unlike traditional power 
            plants, distributed solar produces variable output based on weather and time of day. Electric vehicles 
            create unpredictable demand spikes, while battery systems can both consume and supply power.
        </p>
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6; margin-top: 10px;">
            This variability demands advanced forecasting, control systems, and market structures to maintain 
            stability while optimizing distributed resource use.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Infrastructural Difficulties section with icon    
    st.markdown("""
    <div style="text-align: center;">
        <h3 style="color: #1E5C8E; margin-bottom: 1rem;">Infrastructural Difficulties 🔌</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Atlanta's aging infrastructure wasn't designed for today's bidirectional power flows, creating voltage 
            regulation issues and thermal overloads. Substations, transformers, and control systems need significant 
            upgrades to safely accommodate distributed energy.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Third column - Grid visualization placeholder
with col3:
    # Add some spacing to align with the text
    st.markdown("<div style='margin-top: 4.5rem;'></div>", unsafe_allow_html=True)
    
    # Display the placeholder image
    st.markdown("""
    <div style="text-align: center;">
        <h3 style="color: #1E5C8E; margin-bottom: 1rem;">Slider for scenarios 🔍</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the placeholder image
    st.image(grid_placeholder, use_column_width=True, caption="")
    
    # Add a note about the placeholder
    st.markdown("""
    <div style="text-align: center; font-style: italic; color: #666; font-size: 0.8rem;">
        Interactive grid visualization placeholder
    </div>
    """, unsafe_allow_html=True)
