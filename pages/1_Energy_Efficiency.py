import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# Add parent directory to path to import styles
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from styles import load_css

# Set page config
st.set_page_config(
    page_title="Energy Efficiency | Atlanta Energyshed",
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
    
    if current_page == "1_Energy_Efficiency.py":
        st.markdown('<a href="Energy_Efficiency" class="nav-link active" target="_self"><span class="nav-icon">🔋</span> Energy Efficiency</a>', unsafe_allow_html=True)
    else:
        st.markdown('<a href="Energy_Efficiency" class="nav-link" target="_self"><span class="nav-icon">🔋</span> Energy Efficiency</a>', unsafe_allow_html=True)
    
    if os.path.exists(os.path.join(os.path.dirname(__file__), "2_Local_Generation.py")):
        st.markdown('<a href="Local_Generation" class="nav-link" target="_self"><span class="nav-icon">☀️</span> Local Generation and Storage</a>', unsafe_allow_html=True)
    
    if os.path.exists(os.path.join(os.path.dirname(__file__), "3_Energy_Grid.py")):
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

# Load the required images
from PIL import Image

# First part images
ee_seasonal_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ee_seasonal.png")
ee_emissions_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ee_emissions.png")

# Second part images
ee_pie_typical_home_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ee_pie_typical_home.jpg")
ee_pie_contribution_savings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ee_pie_contribution_savings.png")
ee_pie_contribution_stress_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ee_pie_contribution_stress.png")
ee_pie_stress_reduction_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ee_pie_stress_reduction.png")

# Load the images using PIL
ee_seasonal_img = Image.open(ee_seasonal_path)
ee_emissions_img = Image.open(ee_emissions_path)
ee_pie_typical_home_img = Image.open(ee_pie_typical_home_path)
ee_pie_contribution_savings_img = Image.open(ee_pie_contribution_savings_path)
ee_pie_contribution_stress_img = Image.open(ee_pie_contribution_stress_path)
ee_pie_stress_reduction_img = Image.open(ee_pie_stress_reduction_path)

# Create three columns for the main content
col1, col2, col3 = st.columns([1, 1, 1])

# First column - Energy Efficiency
with col1:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 1.5rem;">Energy Efficiency</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Energy efficiency is defined as the ratio of useful heat output to energy input. In Atlanta, about 65% of homes use natural gas for space and water heating, 25% rely on electric resistance heating, and fewer than 10% use heat pumps. Traditional gas systems operate at 70-90% efficiency, and electric resistance heating at ~95%, but heat pumps achieve 250-400% efficiency by moving heat rather than generating it.
        </p>
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6; margin-top: 10px;">
            Replacing older systems with heat pumps, combined with envelope upgrades like insulation and air sealing, can reduce a home's Energy Use Intensity (EUI) from ~70 to ~50 kBtu/ft²/year — a 30% improvement. Heat pump water heaters also cut emissions by over 26%, offering a scalable path to cost-effective, low-carbon housing.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Second column - Heat Pumps and Housing Envelope
with col2:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 1.5rem;">What are Heat Pumps?</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Heat pumps use electricity to move heat rather than generate it, bringing warmth indoors during winter and cooling during summer. In Atlanta's hot-humid climate, they offer an efficient all-electric alternative to natural gas systems. While traditional heating systems deliver less than 1 unit of heat per unit of fuel, heat pumps provide 2.5 to 4 units of heat per unit of electricity, leading to 30% lower energy use annually as shown in the graph.
        </p>
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6; margin-top: 10px;">
            Though the upfront cost is higher, the running cost is comparable to natural gas, with lower emissions and greater seasonal efficiency.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-top: 1.5rem; margin-bottom: 1.5rem;">What do we mean by Housing Envelope?</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            The home envelope is the physical barrier formed by walls, roof, windows, doors, and foundation that controls heat, air, and moisture flow. It plays a critical role in energy efficiency by reducing energy loss and maintaining indoor comfort. In Atlanta homes, poor insulation and air leakage alone account for over 50% of elevated Energy Use Intensity (EUI).
        </p>
    </div>
    """, unsafe_allow_html=True)

# Third column - Images
with col3:
    # Add some spacing to align with the text
    st.markdown("<div style='margin-top: 4.5rem;'></div>", unsafe_allow_html=True)
    
    # Display the seasonal usage graph using Streamlit's native image display
    st.image(ee_seasonal_img, use_column_width=True, caption="")
    
    # Add some spacing between images
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    
    # Display the emissions image using Streamlit's native image display
    st.image(ee_emissions_img, use_column_width=True, caption="")

# Add a divider before the second part
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# SECOND PART - First row with 3 columns

# First row - 3 columns
col1_row1, col2_row1, col3_row1 = st.columns([1, 1, 1])

# Column 1 - Typical Home Energy Use
with col1_row1:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 1.5rem;">Typical Home Energy <br>Use</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Atlanta homes primarily consume energy for heating/cooling (40%), followed by water heating, electronics, and lighting. Inefficiencies in HVAC systems, insulation, and windows contribute to high Energy Use Intensity (EUI) ~70 kBtu/ft²/year in older homes.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Column 2 - Improvements & Smart Technologies
with col2_row1:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 1.5rem;">Improvements & Smart Technologies</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            Upgrades like solar PV (30%), heat pumps (20%), and window insulation (20%) significantly reduce energy demand. Smart thermostats, EV smart charging, and IoT-based occupancy lighting (each ~10%) further optimize usage, collectively achieving up to 30% EUI reduction.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Column 3 - Contribution of Smart & Sustainable Technologies pie chart
with col3_row1:
    # Add some spacing to align with the text
    st.markdown("<div style='margin-top: 4.5rem;'></div>", unsafe_allow_html=True)
    
    # Display the contribution savings pie chart
    st.image(ee_pie_contribution_savings_img, use_column_width=True, caption="")

# Second row - 2 columns
col1_row2, col2_row2 = st.columns([1, 2])

# Column 1 - Typical Home Energy Use pie chart
with col1_row2:
    # Display the typical home energy use pie chart
    st.image(ee_pie_typical_home_img, use_column_width=True, caption="")
    st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #666;'>Source: EIA, NREL, ENERGY STAR, and Georgia Power data estimates</p>", unsafe_allow_html=True)

# Column 2 - Grid Stress Reduction with 2 sub-columns for charts
with col2_row2:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 1.5rem;">Grid Stress Reduction</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 0.95rem; color: #2c3e50; line-height: 1.6;">
            During peak summer demand, Atlanta homes can draw 5-10 kW each, stressing the grid. Smart scheduling, envelope upgrades, and load-shifting via EVs and heat pumps can lower this peak by up to 30%, enhancing grid stability and resilience.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create 2 sub-columns for the pie charts
    subcol1, subcol2 = st.columns(2)
    
    with subcol1:
        # Display the contributors to grid stress pie chart
        st.image(ee_pie_contribution_stress_img, use_column_width=True, caption="")
    
    with subcol2:
        # Display the grid stress reduction pie chart
        st.image(ee_pie_stress_reduction_img, use_column_width=True, caption="")
