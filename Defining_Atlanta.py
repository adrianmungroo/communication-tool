import streamlit as st
import pandas as pd
import plotly.express as px
import os
from styles import load_css

# Set page config
st.set_page_config(
    page_title="Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"  # Always show sidebar by default
)

# Load custom CSS with page name for specific styling
load_css(page_name="Defining_Atlanta")

# Set up the background image
img_path = os.path.join(os.getcwd(), "assets", "atlanta.jpg")

# Read the image file as bytes
with open(img_path, "rb") as f:
    img_bytes = f.read()

# Apply background image using CSS with base64 encoding
import base64
img_base64 = base64.b64encode(img_bytes).decode()


# Custom sidebar navigation
with st.sidebar:
        
    # Get current page name
    current_page = os.path.basename(__file__)
    
    # Navigation links with icons
    if current_page == "Defining_Atlanta.py":
        st.markdown('<a href="." class="nav-link active" target="_self"><span class="nav-icon">🏠</span> Defining Atlanta</a>', unsafe_allow_html=True)
    else:
        st.markdown('<a href="." class="nav-link" target="_self"><span class="nav-icon">🏠</span> Defining Atlanta</a>', unsafe_allow_html=True)
        
    if "1_Energy_Efficiency.py" in os.listdir("pages"):
        st.markdown('<a href="Energy_Efficiency" class="nav-link" target="_self"><span class="nav-icon">🔋</span> Energy Efficiency</a>', unsafe_allow_html=True)
        
    if "2_Local_Generation.py" in os.listdir("pages"):
        st.markdown('<a href="Local_Generation" class="nav-link" target="_self"><span class="nav-icon">☀️</span> Local Generation and Storage</a>', unsafe_allow_html=True)
        
    if "3_Energy_Grid.py" in os.listdir("pages"):
        st.markdown('<a href="Energy_Grid" class="nav-link" target="_self"><span class="nav-icon">🔌</span> Our Energy Grid</a>', unsafe_allow_html=True)
        
    if "4_Looking_Future.py" in os.listdir("pages"):
        st.markdown('<a href="Looking_Future" class="nav-link" target="_self"><span class="nav-icon">🔮</span> Looking to the Future</a>', unsafe_allow_html=True)
    
    # Additional sidebar information
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### About", unsafe_allow_html=True)
    st.info("This dashboard provides insights into Atlanta's energy ecosystem and explores strategies for a sustainable future.")
    
    # Optional: Add contact or help information
    with st.expander("Need Help?"):
        st.write("Learn more at: https://energyshed.research.gatech.edu/")

######################## PAGE CONTENT ########################

# Create two columns - one for text content and one for the image
col1, col2 = st.columns([1, 1])

with col1:
    # All text content in the first column
    st.header("Defining Atlanta Energyshed")
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        The capital of Georgia and centerpiece of a metropolitan area exceeding 6 million 
        residents, Atlanta represents a critical energy ecosystem with distinctive 
        characteristics shaped by its climate, geography, and economic profile. With 
        hot, humid summers driving substantial cooling demand and a dispersed urban 
        footprint requiring extensive transportation networks, Atlanta's 
        energy consumption patterns present unique challenges and opportunities for 
        innovation.
    </div>
    """, unsafe_allow_html=True)
    
    st.header("How It's Changing")
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        Our metropolitan area stands at a pivotal moment in its energy evolution. 
        The growing population and urban development are creating more complex 
        energy needs, while emerging technologies are simultaneously transforming 
        both energy demand and supply patterns. The rapid expansion of energy-
        intensive data centers, aging grid infrastructure requiring modernization, 
        and the challenge of retrofitting existing commercial and residential 
        buildings for greater efficiency are reshaping our energy landscape.
    </div>
    """, unsafe_allow_html=True)

    st.header("Looking Forward")
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px;">
        This tool allows users to explore how different energy strategies—from 
        building retrofits to distributed solar deployment to grid modernization—can 
        impact Atlanta's energy future. By providing data-driven analysis of various 
        scenarios, we aim to empower policymakers, businesses, community 
        organizations, and residents to make informed decisions that enhance 
        energy affordability, improve resilience, and create mutual benefits for 
        utilities, consumers, and communities throughout the Atlanta region.
    </div>
    """, unsafe_allow_html=True)
with col2:
    # Display the Atlanta image in the second column
    # Use HTML to control the image display with styling
    st.markdown(f"""
    <div style="height: 100%; display: flex; justify-content: center; align-items: center;">
        <img src="data:image/jpg;base64,{img_base64}" 
             style="width: 100%; height: 100%; object-fit: cover; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
             alt="Atlanta Skyline">
    </div>
    """, unsafe_allow_html=True)

# Add a divider before the 3-row format content
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# First row - Energy Efficiency Measures
st.markdown("""
<div style="display: flex; margin-bottom: 2rem; background-color: #f0f8ff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <div style="flex: 1; padding: 20px; display: flex; align-items: center; justify-content: center;">
        <!-- Placeholder for left image -->
        <div style="width: 100%; height: 200px; background-color: #dceaf9; border-radius: 5px; display: flex; align-items: center; justify-content: center;">
            <span style="color: #1E88E5; font-size: 3rem;">🏠</span>
        </div>
    </div>
    <div style="flex: 2; padding: 20px;">
        <div style="color: #1E88E5; margin-bottom: 1rem; text-align: center; font-size: 1.5rem; font-weight: bold;">What Energy Efficiency Measures are There?</div>
        <p style="color: #333; line-height: 1.6;">
            Energy efficiency improvements are vital for a more resilient and affordable energy use as demand increases. Heat pumps provide efficient heating and cooling, reducing energy use by up to 50%. Building envelope improvements—better insulation, air sealing, and high-performance windows—minimize waste and improve comfort. Smart thermostats, LED lighting, and efficient appliances further reduce electricity demand while cutting utility bills and easing grid strain during peak periods.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Second row - Local Generation and Storage
st.markdown("""
<div style="display: flex; margin-bottom: 2rem; background-color: #f0f8ff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <div style="flex: 2; padding: 20px;">
        <div style="color: #1E88E5; margin-bottom: 1rem; text-align: center; font-size: 1.5rem; font-weight: bold;">Local Generation and Storage</div>
        <p style="color: #333; line-height: 1.6;">
            Distributed energy resources are changing Atlanta's electricity landscape. Rooftop solar enables on-site clean energy production, while battery storage systems preserve excess generation for evening use or outages. Electric vehicles double as grid resources through bidirectional charging capabilities. These technologies create a more flexible energy system while allowing Atlantans to actively participate in the clean energy transition.
        </p>
    </div>
    <div style="flex: 1; padding: 20px; display: flex; align-items: center; justify-content: center;">
        <!-- Placeholder for right image -->
        <div style="width: 100%; height: 200px; background-color: #dceaf9; border-radius: 5px; display: flex; align-items: center; justify-content: center;">
            <span style="color: #1E88E5; font-size: 3rem;">☀️</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Third row - Impacts to our Electric Grid
st.markdown("""
<div style="display: flex; margin-bottom: 2rem; background-color: #f0f8ff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <div style="flex: 1; padding: 20px; display: flex; align-items: center; justify-content: center;">
        <!-- Placeholder for left image -->
        <div style="width: 100%; height: 200px; background-color: #dceaf9; border-radius: 5px; display: flex; align-items: center; justify-content: center;">
            <span style="color: #1E88E5; font-size: 3rem;">🔌</span>
        </div>
    </div>
    <div style="flex: 2; padding: 20px;">
        <div style="color: #1E88E5; margin-bottom: 1rem; text-align: center; font-size: 1.5rem; font-weight: bold;">Impacts to our Electric Grid</div>
        <p style="color: #333; line-height: 1.6;">
            Atlanta's grid faces new demands from growing data centers and changing energy flows. Rather than one-way delivery from large power plants, our grid must now manage two-way power flows from distributed solar, batteries, and electric vehicles. This transformation requires strategic planning and infrastructure investments to maintain reliability while supporting clean energy growth. Understanding these impacts helps develop solutions that balance decarbonization goals with reliable service for Atlanta's economy.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Add a divider before the Key Concepts section
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# Key Concepts section header
st.markdown("<h1 style='text-align: center; color: #1E5C8E; margin-bottom: 2rem;'>Key Concepts</h1>", unsafe_allow_html=True)

# Main concept banner
st.markdown("""
<div style="background-color: #F0F8FF; padding: 1rem; border-radius: 5px; margin-bottom: 2rem; text-align: center;">
    <div style="font-size: 1.5rem; color: #1E5C8E; line-height: 1.6;">
        Energy is not only about <span style="color: #d9534f; font-weight: bold; font-style: italic;">HOW MUCH</span> you use, but <span style="color: #d9534f; font-weight: bold; font-style: italic;">WHEN</span> you use it
    </div>
</div>
""", unsafe_allow_html=True)

# Create three columns for the content
left_col, middle_col, right_col = st.columns([1, 2, 1])

# Left column content
with left_col:
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 15px; border-radius: 5px; margin-bottom: 1rem;">
        <div style="color: #1E5C8E; font-size: 1.2rem;">
            Look at an example where we generate a large amount of solar energy => BUT we can only use some of it
        </div>
    </div>
    <div style="background-color: #F0F8FF; padding: 15px; border-radius: 5px; margin-bottom: 1rem;">
        <div style="color: #1E5C8E; font-size: 1.2rem;">
            We don't use energy at the same <span style="color: #d9534f;">rate</span> we generate it
        </div>
    </div>
    """, unsafe_allow_html=True)

# Middle column - Energy usage graph
with middle_col:
    # Load the energy usage graph image
    energy_graph_path = os.path.join(os.getcwd(), "assets", "energy_usage_graph.jpg")
    
    # Read the image file as bytes
    with open(energy_graph_path, "rb") as f:
        graph_bytes = f.read()
    
    # Convert to base64 for embedding in HTML
    graph_base64 = base64.b64encode(graph_bytes).decode()
    
    # Use custom HTML to display the image without fullscreen button
    st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpg;base64,{graph_base64}" 
             style="max-width: 100%; border-radius: 5px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Energy Usage Graph">
    </div>
    """, unsafe_allow_html=True)

# Right column content
with right_col:
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 15px; border-radius: 5px; margin-bottom: 1rem;">
        <div style="color: #1E5C8E; font-size: 1.2rem;">
            What are some solutions?
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 15px; border-radius: 5px; margin-bottom: 1rem;">
        <div style="color: #d9534f; font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem;">
            STORE IT
        </div>
        <div>
            A simple solution is batteries! Just store the energy and use it later. There are other types of storage, like using heat or potential energy.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 15px; border-radius: 5px; margin-bottom: 1rem;">
        <div style="color: #d9534f; font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem;">
            MIX IT
        </div>
        <div>
            Different energy sources have their own distinct energy profiles. Local generation, like solar or wind, are dependent on the environment, while fossil-fuel based generation can be ramped up and down based on need. Nuclear, on the other hand, is generally constant.
        </div>
    </div>
    """, unsafe_allow_html=True)
