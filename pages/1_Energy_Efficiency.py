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
    Energy efficiency represents one of the most cost-effective strategies for reducing energy consumption and greenhouse gas emissions in Atlanta. 
    The city faces unique challenges due to its older building stock, hot and humid climate, and sprawling development patterns.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Building Retrofits")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        Atlanta's existing buildings offer significant opportunities for energy savings through retrofits. 
        Commercial buildings can reduce energy use by 20-30% through lighting upgrades, HVAC optimization, and improved building envelope. 
        Residential retrofits focusing on insulation, air sealing, and efficient appliances can yield 15-25% energy savings.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for a chart
    retrofit_data = pd.DataFrame({
        'Building Type': ['Commercial', 'Residential', 'Industrial', 'Public'],
        'Potential Energy Savings (%)': [25, 20, 15, 30]
    })
    
    fig = px.bar(retrofit_data, x='Building Type', y='Potential Energy Savings (%)', 
                title='Energy Savings Potential by Building Type',
                color='Building Type', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    st.header("New Construction Standards")
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 5px;">
        Implementing stringent energy codes for new construction can lock in efficiency for decades. 
        Atlanta's rapid development presents an opportunity to ensure all new buildings meet high-performance standards. 
        Green building certifications like LEED and ENERGY STAR are becoming increasingly common in the Atlanta market.
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for energy code adoption
    years = list(range(2010, 2025, 2))
    adoption_rates = [10, 15, 25, 40, 55, 70, 85, 90]
    
    code_data = pd.DataFrame({
        'Year': years,
        'Green Building Adoption Rate (%)': adoption_rates
    })
    
    fig = px.line(code_data, x='Year', y='Green Building Adoption Rate (%)', 
                 title='Green Building Adoption in Atlanta',
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)
