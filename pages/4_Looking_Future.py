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
    page_title="Looking to Future | Atlanta Energyshed",
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
    
    if os.path.exists(os.path.join(os.path.dirname(__file__), "3_Energy_Grid.py")):
        st.markdown('<a href="Energy_Grid" class="nav-link" target="_self"><span class="nav-icon">🔌</span> Grid Under Pressure</a>', unsafe_allow_html=True)
    
    if current_page == "4_Looking_Future.py":
        st.markdown('<a href="Looking_Future" class="nav-link active" target="_self"><span class="nav-icon">🔮</span> Looking to the Future</a>', unsafe_allow_html=True)
    else:
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
    Atlanta's energy future will be shaped by a combination of technological innovation, policy decisions, 
    market forces, and community priorities. This section explores potential scenarios and their implications for the region.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Decarbonization Pathways")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        Multiple pathways exist for reducing carbon emissions from Atlanta's energy system. 
        These include accelerated renewable energy deployment, electrification of buildings and transportation, 
        energy efficiency improvements, and potentially green hydrogen for hard-to-electrify sectors.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for emissions reduction
    years = list(range(2020, 2051, 5))
    baseline = [100, 95, 90, 85, 80, 75, 70]
    moderate = [100, 85, 70, 55, 40, 25, 15]
    aggressive = [100, 75, 50, 30, 15, 5, 0]
    
    emissions_data = pd.DataFrame({
        'Year': years * 3,
        'Emissions (% of 2020)': baseline + moderate + aggressive,
        'Scenario': ['Baseline'] * 7 + ['Moderate Action'] * 7 + ['Aggressive Action'] * 7
    })
    
    fig = px.line(emissions_data, x='Year', y='Emissions (% of 2020)', color='Scenario',
                 title='Carbon Emissions Reduction Scenarios',
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    st.header("Energy Equity")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        As Atlanta's energy system evolves, ensuring equitable access to clean energy and its benefits is crucial. 
        Energy burden—the percentage of household income spent on energy—varies significantly across the region, 
        with some neighborhoods spending over 10% of income on energy costs.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for energy burden
    neighborhoods = ['Downtown', 'Midtown', 'Buckhead', 'West End', 'East Atlanta', 'South Atlanta']
    energy_burden = [3.2, 2.8, 2.5, 8.5, 6.2, 9.8]
    
    burden_data = pd.DataFrame({
        'Neighborhood': neighborhoods,
        'Energy Burden (% of Income)': energy_burden
    })
    
    fig = px.bar(burden_data, x='Neighborhood', y='Energy Burden (% of Income)', 
                title='Energy Burden by Neighborhood',
                color='Energy Burden (% of Income)', 
                color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)
