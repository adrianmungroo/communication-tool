import streamlit as st
import pandas as pd
import plotly.express as px
import os
from styles import load_css
import base64
from device_detection import detect_device

# Set page config
st.set_page_config(
    page_title="Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"  # Start with sidebar collapsed
)

# Load custom CSS with page name for specific styling
load_css(page_name="Defining_Atlanta")

# Import shared components
from shared_components import create_sidebar

# Store current page in session state for sidebar to access
st.session_state['current_page'] = __file__

# Create the sidebar with the current page name
create_sidebar(os.path.basename(__file__))

# Display device information in a small, unobtrusive way
device_info = detect_device()
st.markdown(f"<div style='text-align: right; color: #666; font-size: 0.8rem; margin-bottom: 10px;'>You're viewing this page on a {device_info['device_type']} device running {device_info['os']}.</div>", unsafe_allow_html=True)

######################## PAGE CONTENT ########################

# Load the required images
energydef_path = os.path.join(os.getcwd(), "assets", "energyshed_define.png")
supply_path = os.path.join(os.getcwd(), "assets", "supply_area.png")
demand_path = os.path.join(os.getcwd(), "assets", "demand_area.png")
how_it_is_changing_path = os.path.join(os.getcwd(), "assets", "defining_atlanta_how_changing.png")
looking_forward_path = os.path.join(os.getcwd(), "assets", "defining_atlanta_looking_forward.png")
grid_structure_path = os.path.join(os.getcwd(), "assets", "grid_structure.png")

# Read the image files as bytes and convert to base64
with open(energydef_path, "rb") as f:
    energydef_bytes = f.read()
energydef_base64 = base64.b64encode(energydef_bytes).decode()

with open(supply_path, "rb") as f:
    supply_bytes = f.read()
supply_base64 = base64.b64encode(supply_bytes).decode()

with open(demand_path, "rb") as f:
    demand_bytes = f.read()
demand_base64 = base64.b64encode(demand_bytes).decode()

with open(how_it_is_changing_path, "rb") as f:
    how_it_is_changing_bytes = f.read()
how_it_is_changing_base64 = base64.b64encode(how_it_is_changing_bytes).decode()

with open(looking_forward_path, "rb") as f:
    looking_forward_bytes = f.read()
looking_forward_base64 = base64.b64encode(looking_forward_bytes).decode()

with open(grid_structure_path, "rb") as f:
    grid_structure_bytes = f.read()
grid_structure_base64 = base64.b64encode(grid_structure_bytes).decode()

# Create two columns for the main content
col1, col2 = st.columns([1, 2])

with col1:
    # Left column - Defining Atlanta's Energyshed
    st.markdown("""
    <h1 style="color: #1E5C8E; margin-bottom: 1.5rem;">Defining Atlanta's <br> Energyshed</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            For Atlanta, understanding the city's 
            <span style="color: #1E5C8E; font-weight: bold;">energyshed</span> means mapping the diverse 
            sources of electricity that power our 
            homes, businesses, and transit—whether 
            from rooftop solar, distant power plants, or 
            wind farms across the region.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the energyshed definition image
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{energydef_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
             alt="Energyshed Definition">
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Right column - Supply and Demand
    st.markdown("""
    <h1 style="color: #1E5C8E; margin-bottom: 1.5rem;">Supply and Demand <br> of Energy</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Much like highly developed urban areas, metropolitan Atlanta is a consumption “island”, and its energy demand is met by its Energyshed supply network that stretches far beyond Atlanta borders, encompassing power plants, transmission lines, and fuel sources from across multiple states. The city's energy resilience, pricing, and environmental footprint should be understood in this broader context. 
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for the supply and demand images
    img_col1, img_col2 = st.columns([1.5, 1])
    
    with img_col1:
        # Supply area image
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{supply_base64}" 
                 style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
                 alt="Supply Area">
            <p style="text-align: center; margin-top: 10px; font-weight: bold;">Balancing Authority of Energy Supply and Demand</p>
        </div>
        """, unsafe_allow_html=True)
    
    with img_col2:
        # Demand area image
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{demand_base64}" 
                 style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
                 alt="Demand Area">
            <p style="text-align: center; margin-top: 10px; font-weight: bold;">High demand metro Atlanta area</p>
        </div>
        """, unsafe_allow_html=True)

# Add a divider
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# Grid Structure Section
image_col, text_col = st.columns([2, 1])

with image_col:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{grid_structure_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
             alt="Grid Structure">
    </div>
    """, unsafe_allow_html=True)

with text_col:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">Power Grid Structure 
</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            The electricity grid flows from high-voltage generation & transmission lines to your home outlet via massive spiderweb distribution lines, with later segments experiencing more power losses than previous. Substation customers (e.g., Electric Membership Corporations) and primary customers (e.g., large factories) maintain their own distribution equipment and handle technical requirements on their own. Meanwhile, secondary customers like homes and small buildings, which can exist within an EMC's service area, receive complete end-to-end service (upkeep and repairs) from utilities, explaining why different customer types have different pricing models based on their infrastructure responsibilities.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Add a divider
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# How It's Changing section
# Use columns for responsive layout - will stack on mobile automatically
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{how_it_is_changing_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
             alt="How It's Changing">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">How It's Changing</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            The metropolitan area stands at a pivotal moment in its energy evolution. The growing population and urban development are creating more complex energy needs, while emerging technologies are simultaneously transforming both energy demand and supply patterns. The rapid expansion of energy-intensive data centers, aging grid infrastructure requiring modernization, and the challenge of retrofitting existing commercial and residential buildings for greater efficiency are reshaping our energy landscape. Meanwhile, peak demand management and building electrification present both challenges and opportunities for a more resilient system.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Add a divider before the 3-column format content
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# Load the required images for the 3-row format
efficiency_path = os.path.join(os.getcwd(), "assets", "defining_energy_efficiency.png")
local_gen_path = os.path.join(os.getcwd(), "assets", "defining_local_gen_storage.png")
grid_path = os.path.join(os.getcwd(), "assets", "defining_grid.png")

# Read the image files as bytes and convert to base64
with open(efficiency_path, "rb") as f:
    efficiency_bytes = f.read()
efficiency_base64 = base64.b64encode(efficiency_bytes).decode()

with open(local_gen_path, "rb") as f:
    local_gen_bytes = f.read()
local_gen_base64 = base64.b64encode(local_gen_bytes).decode()

with open(grid_path, "rb") as f:
    grid_bytes = f.read()
grid_base64 = base64.b64encode(grid_bytes).decode()

# Create three columns for the content sections
col1, col2, col3 = st.columns(3)

# First column - Energy Efficiency
with col1:
    st.markdown("""
    <h3 style="text-align: center; color: #1E5C8E; margin-bottom: 1rem;">What Energy Efficiency <br> Measures are There?</h3>
    """, unsafe_allow_html=True)
    
    # Display the energy efficiency image
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{efficiency_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Energy Efficiency Measures">
    </div>
    """, unsafe_allow_html=True)
    
    # Energy efficiency text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Energy efficiency improvements are vital for a more resilient and affordable energy use as demand increases. Heat pumps provide efficient heating and cooling, reducing energy use by up to 50%. Building envelope improvements—better insulation, air sealing, and high-performance windows—minimize waste and improve comfort.
        </p>
        <div style="text-align: center; margin-top: 15px;">
            <a href="https://www.energy.gov/energysaver/energy-saver" style="color: #1E5C8E; font-weight: bold;">CLICK for more info</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Second column - Local Generation and Storage
with col2:
    st.markdown("""
    <h3 style="text-align: center; color: #1E5C8E; margin-bottom: 1rem;">Local Generation <br> and Storage</h3>
    """, unsafe_allow_html=True)
    
    # Display the local generation image
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{local_gen_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Local Generation and Storage">
    </div>
    """, unsafe_allow_html=True)
    
    # Local generation text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Distributed energy resources are changing Atlanta's electricity landscape. Rooftop solar enables on-site clean energy production, while battery storage systems preserve excess generation for evening use or outages. Electric vehicles double as grid resources through bidirectional charging capabilities.
        </p>
        <div style="text-align: center; margin-top: 15px;">
            <a href="https://www.energy.gov/eere/solar/articles/solar-plus-storage-101" style="color: #1E5C8E; font-weight: bold;">CLICK for more info</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Third column - Impacts to Electric Grid
with col3:
    st.markdown("""
    <h3 style="text-align: center; color: #1E5C8E; margin-bottom: 1rem;">Impacts to our <br> Electric Grid</h3>
    """, unsafe_allow_html=True)
    
    # Display the grid image
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{grid_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Electric Grid Impacts">
    </div>
    """, unsafe_allow_html=True)
    
    # Grid impacts text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Atlanta's grid faces new demands from growing data centers and changing energy flows. Rather than one-way delivery from large power plants, our grid must now manage two-way power flows from distributed solar, batteries, and electric vehicles.
        </p>
        <div style="text-align: center; margin-top: 15px;">
            <a href="https://www.energy.gov/smart-grid" style="color: #1E5C8E; font-weight: bold;">CLICK for more info</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add a divider before the Looking Forward section
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# Looking Forward section header
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(f"""
    <div style="text-align: center; margin-top: 2rem;">
        <img src="data:image/png;base64,{looking_forward_base64}" 
             style="width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
             alt="Looking Forward">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <h2 style="color: #1E5C8E; margin-bottom: 0.75rem;">Looking Forward</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            This tool helps visualize how energy is moved through space, who produces it, who consumes it, and how local decisions shape our shared energy future. 
            <br><br>
            Users can explore how different energy strategies—from building retrofits to distributed solar deployment to grid modernization—can impact Atlanta's energy future.
        </p>
    </div>
    """, unsafe_allow_html=True)
