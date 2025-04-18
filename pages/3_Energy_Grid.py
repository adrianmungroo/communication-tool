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
    page_title="Our Energy Grid | Atlanta Energyshed",
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
        st.markdown('<a href="Energy_Grid" class="nav-link active" target="_self"><span class="nav-icon">🔌</span> Our Energy Grid</a>', unsafe_allow_html=True)
    else:
        st.markdown('<a href="Energy_Grid" class="nav-link" target="_self"><span class="nav-icon">🔌</span> Our Energy Grid</a>', unsafe_allow_html=True)
    
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

st.markdown("""
<div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    Atlanta's electricity grid is undergoing a significant transformation as it adapts to changing demand patterns, 
    integrates renewable energy, and improves resilience against extreme weather events and other disruptions.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Grid Modernization")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        The region's utilities are investing in advanced metering infrastructure, distribution automation, and smart grid technologies. 
        These investments enable more precise monitoring and control of electricity flows, faster outage detection and restoration, 
        and better integration of distributed energy resources.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for grid investments
    investment_data = pd.DataFrame({
        'Category': ['Smart Meters', 'Distribution Automation', 'Substation Upgrades', 'Transmission Enhancements', 'Cybersecurity'],
        'Investment ($ Millions)': [120, 85, 65, 95, 40]
    })
    
    fig = px.bar(investment_data, x='Category', y='Investment ($ Millions)', 
                title='Grid Modernization Investments',
                color='Category', color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    st.header("Reliability Metrics")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        Grid reliability is measured using standard industry metrics such as SAIDI (System Average Interruption Duration Index) 
        and SAIFI (System Average Interruption Frequency Index). Atlanta's utilities have been working to improve these metrics 
        through targeted infrastructure investments and vegetation management.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for reliability metrics
    years = list(range(2015, 2025))
    saidi_values = [120, 115, 105, 100, 90, 85, 80, 75, 72, 70]
    saifi_values = [1.5, 1.4, 1.3, 1.25, 1.2, 1.15, 1.1, 1.05, 1.0, 0.95]
    
    reliability_data = pd.DataFrame({
        'Year': years + years,
        'Value': saidi_values + saifi_values,
        'Metric': ['SAIDI'] * 10 + ['SAIFI'] * 10
    })
    
    fig = px.line(reliability_data, x='Year', y='Value', color='Metric',
                 title='Grid Reliability Improvements',
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)
