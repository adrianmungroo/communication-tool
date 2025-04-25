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
    page_title="Energy Efficiency | Atlanta Energyshed",
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
show_wip_warning()

######################## PAGE CONTENT ########################

# Load the required images
from PIL import Image

# Image Paths
ee_house_path = r"assets\ee_house.png"
ee_envelope_eui_path = r"assets\ee_envelope_eui.png"
ee_seasonal_energy_use_path = r"assets\ee_seasonal_energy_use.png"
ee_annual_energy_use_path = r"assets\ee_annual_energy_use.png"
ee_what_if_path = r"assets\ee_what_if.png"
ee_savings_path = r"assets\ee_savings.png"

# Load the images as bytes and convert to base64
with open(ee_house_path, "rb") as f:
    ee_house_bytes = f.read()
    ee_house_base64 = base64.b64encode(ee_house_bytes).decode()

with open(ee_envelope_eui_path, "rb") as f:
    ee_envelope_eui_bytes = f.read()
    ee_envelope_eui_base64 = base64.b64encode(ee_envelope_eui_bytes).decode()   

with open(ee_seasonal_energy_use_path, "rb") as f:
    ee_seasonal_energy_use_bytes = f.read()
    ee_seasonal_energy_use_base64 = base64.b64encode(ee_seasonal_energy_use_bytes).decode()

with open(ee_annual_energy_use_path, "rb") as f:
    ee_annual_energy_use_bytes = f.read()
    ee_annual_energy_use_base64 = base64.b64encode(ee_annual_energy_use_bytes).decode()

with open(ee_what_if_path, "rb") as f:
    ee_what_if_bytes = f.read()
    ee_what_if_base64 = base64.b64encode(ee_what_if_bytes).decode()

with open(ee_savings_path, "rb") as f:
    ee_savings_bytes = f.read()
    ee_savings_base64 = base64.b64encode(ee_savings_bytes).decode()

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
        <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">Energy Efficiency</h2>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Energy efficiency means doing the same tasks while using less energy. In Atlanta homes, this includes simple actions like switching to LED bulbs, upgrading to energy-efficient appliances, and using smart thermostats. Many older homes lose energy through poor insulation and outdated systems, but these can be improved. Adding insulation, sealing leaks, and installing heat pumps can make homes significantly more efficient. These upgrades lower utility bills, ease demand on the power grid, and cut greenhouse gas (GHG) emissions, aligning with Atlanta’s sustainability goals.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{ee_house_base64}" 
             style="width: 60%; height: auto; border-radius: 10px;" 
             alt="Energy efficient home with sustainable features">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">What do we mean by Housing Envelope?</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            The housing envelope is the outer structure of your home i.e. walls, roof, windows, floor, and foundation. It controls how much heat, air and moisture enters or escapes your house. When the envelope is poorly insulated or have leakage, it leads to higher energy bills and discomfort.
            <br><br>
            Fixing the envelope by adding insulation, sealing leaks, and upgrading windows can reduce EUI by 20-30% in Atlanta houses:
            <ul style="margin-top: 10px; margin-bottom: 5px; padding-left: 25px;">
                <li>Pre-1980: 70 kBtu/ft²/year, with upgrades: 45 kBtu/ft²/year</li>
                <li>1980-2020: 55 kBtu/ft²/year, with upgrades: 38 kBtu/ft²/year</li> 
                <li>2020-Now: 28 kBtu/ft²/year, with upgrades: 24 kBtu/ft²/year (Limited savings potential)</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{ee_envelope_eui_base64}" 
             style="width: 90%; height: auto; border-radius: 10px;" 
             alt="Housing envelope energy usage intensity (EUI) comparison by construction era">
    </div>
    """, unsafe_allow_html=True)

# Add a divider
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">What are Heat Pumps?</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Heat pumps transfer heat instead of generating it. In the winter, they bring heat inside from the air outside, and in the summer, they remove heat from your home.
            <br><br>
            Compared to gas furnaces and resistive electric heaters, heat pumps are 2.5 to 4 times more efficient. In Atlanta’s mild winters, they work especially well year-round. Replacing older systems with heat pumps can reduce heating energy use by up to 70%.Line graph shows monthly energy consumption for a typical 2020-era Atlanta home with and without heat pump.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{ee_seasonal_energy_use_base64}" 
             style="width: 90%; height: auto; border-radius: 10px;" 
             alt="Seasonal energy consumption comparison with and without heat pump">
    </div>
    """, unsafe_allow_html=True)

# Add a divider
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">Why Efficiency Upgrades Matter?</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Older homes waste energy through poor insulation, air leaks, and outdated systems. Upgrading the building envelope and switching to efficient heat pumps can nearly cut energy use in half and significantly reduce carbon emissions.
            <br><br>
            A bar chart compares annual energy use and shows how emissions drop with upgrades.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{ee_annual_energy_use_base64}" 
             style="width: 70%; height: auto; border-radius: 10px;" 
             alt="Annual energy usage and emissions reduction with efficiency upgrades">
    </div>
    """, unsafe_allow_html=True)

# Add a divider
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 3]) 

with col1:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">Here's what we personally gain</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Efficiency upgrades also deliver big savings. Better insulation, smarter heating, and efficient appliances reduce electricity and gas use lowering bills by hundreds of dollars each year.
            <br><br>
            A bar chart shows household energy and cost savings by home type. 
            <br><br>
            Both all-electric and gas-heated homes benefit, especially older ones. These improvements make homes healthier, more comfortable, and more affordable.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
    <img src="data:image/png;base64,{ee_what_if_base64}" 
             style="width: 50%; height: auto; border-radius: 10px;" 
             alt="What-if analysis of energy efficiency improvements">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px; margin-top: 15px;">
        <img src="data:image/png;base64,{ee_savings_base64}" 
             style="width: 90%; height: auto; border-radius: 10px;" 
             alt="Household energy and cost savings by home type">
    </div>
    """, unsafe_allow_html=True)    
    
    