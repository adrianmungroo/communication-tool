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
    page_title="Local Generation and Storage | Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"  # Always show sidebar by default
)

# Load custom CSS
load_css()


# Import the sidebar module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from sidebar import create_sidebar

# Store current page in session state for sidebar to access
st.session_state['current_page'] = __file__

# Create the sidebar with the current page name
create_sidebar(os.path.basename(__file__))

######################## PAGE CONTENT ########################

st.markdown("""
<div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    Distributed energy resources (DERs) are transforming how Atlanta generates, stores, and manages electricity. 
    These technologies enable local energy production, reducing transmission losses and increasing grid resilience.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Solar Potential")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        Atlanta receives approximately 5.2 hours of peak sunlight daily on average, making solar PV systems viable throughout the metropolitan area. 
        Rooftop solar potential is estimated at 4,800 MW across the region, with additional opportunities for ground-mounted systems, 
        solar parking canopies, and community solar gardens.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for solar growth
    years = list(range(2015, 2026))
    solar_capacity = [10, 25, 50, 90, 150, 240, 350, 500, 700, 950, 1200]
    
    solar_data = pd.DataFrame({
        'Year': years,
        'Installed Capacity (MW)': solar_capacity
    })
    
    fig = px.line(solar_data, x='Year', y='Installed Capacity (MW)', 
                 title='Solar PV Growth in Atlanta Metro',
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    st.header("Battery Storage")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        Battery energy storage systems are increasingly being deployed alongside solar installations and at strategic grid locations. 
        These systems provide multiple benefits: peak shaving, backup power during outages, and the ability to time-shift 
        renewable generation to periods of high demand.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for battery deployments
    storage_data = pd.DataFrame({
        'Application': ['Residential', 'Commercial', 'Utility', 'Microgrid'],
        'Installed Capacity (MWh)': [45, 120, 250, 85]
    })
    
    fig = px.pie(storage_data, values='Installed Capacity (MWh)', names='Application', 
                title='Battery Storage Deployment by Sector',
                color_discrete_sequence=px.colors.sequential.Plasma_r)
    st.plotly_chart(fig, use_container_width=True)
