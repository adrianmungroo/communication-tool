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
        st.markdown('<a href="Energy_Grid" class="nav-link" target="_self"><span class="nav-icon">🔌</span> Grid Under Pressure</a>', unsafe_allow_html=True)
        
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

# Load the required images
energydef_path = os.path.join(os.getcwd(), "assets", "energyshed_define.png")
supply_path = os.path.join(os.getcwd(), "assets", "supply_area.png")
demand_path = os.path.join(os.getcwd(), "assets", "demand_area.png")

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

# Create two columns for the main content
col1, col2 = st.columns([1, 2])

with col1:
    # Left column - Defining Atlanta's Energyshed
    st.markdown("""
    <h1 style="color: #1E5C8E; margin-bottom: 1.5rem;">Defining Atlanta's Energyshed</h1>
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
             style="width: 90%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
             alt="Energyshed Definition">
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Right column - Supply and Demand
    st.markdown("""
    <h1 style="color: #1E5C8E; margin-bottom: 1.5rem;">Supply and Demand</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Much like how distant streams and various sources affect water use, Atlanta's 
            energyshed supply network stretches far beyond Atlanta borders, 
            encompassing power plants, transmission lines, and fuel sources from across 
            multiple states, creating a complex web of interdependencies that impact the 
            city's energy resilience, pricing, and environmental footprint.
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
                 style="width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
                 alt="Supply Area">
            <p style="text-align: center; margin-top: 10px; font-weight: bold;">Supply</p>
        </div>
        """, unsafe_allow_html=True)
    
    with img_col2:
        # Demand area image
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{demand_base64}" 
                 style="width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" 
                 alt="Demand Area">
            <p style="text-align: center; margin-top: 10px; font-weight: bold;">Demand</p>
        </div>
        """, unsafe_allow_html=True)

# Add a divider before the second part
st.markdown("<hr style='margin: 3rem 0; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)

# How It's Changing section
st.markdown("""
<h1 style="text-align: center; color: #1E5C8E; margin-bottom: 1.5rem;">How It's Changing</h1>

<div style="background-color: rgba(240, 248, 255, 0.8); padding: 25px; border-radius: 5px; margin-bottom: 2.5rem;">
    <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6; text-align: justify;">
        Our metropolitan area stands at a pivotal moment in its energy evolution. The growing population and urban development 
        are creating more complex energy needs, while emerging technologies are simultaneously transforming both energy 
        demand and supply patterns. The rapid expansion of energy-intensive data centers, aging grid infrastructure requiring 
        modernization, and the challenge of retrofitting existing commercial and residential buildings for greater efficiency are 
        reshaping our energy landscape. Meanwhile, peak demand management and building electrification present both 
        challenges and opportunities for a more resilient system.
    </p>
</div>

<h1 style="text-align: center; color: #1E5C8E; margin-bottom: 1.5rem;">Looking Forward</h1>

<div style="background-color: rgba(240, 248, 255, 0.8); padding: 25px; border-radius: 5px; margin-bottom: 1rem;">
    <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6; text-align: justify;">
        This tool helps visualize how energy is moved through space, who produces it, who consumes it, and how local decisions 
        shape our shared energy future. <br><br>
        Users can explore how different energy strategies—from building retrofits to distributed solar deployment to grid 
        modernization—can impact Atlanta's energy future.
    </p>
</div>
""", unsafe_allow_html=True)

# Add a divider before the 3-row format content
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
             style="width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Energy Efficiency Measures">
    </div>
    """, unsafe_allow_html=True)
    
    # Energy efficiency text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 0.9rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Energy efficiency improvements are vital for a more resilient and affordable energy use as demand increases. Heat pumps provide efficient heating and cooling, reducing energy use by up to 50%. Building envelope improvements—better insulation, air sealing, and high-performance windows—minimize waste and improve comfort.
        </p>
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
             style="width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Local Generation and Storage">
    </div>
    """, unsafe_allow_html=True)
    
    # Local generation text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 0.9rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Distributed energy resources are changing Atlanta's electricity landscape. Rooftop solar enables on-site clean energy production, while battery storage systems preserve excess generation for evening use or outages. Electric vehicles double as grid resources through bidirectional charging capabilities.
        </p>
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
             style="width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Electric Grid Impacts">
    </div>
    """, unsafe_allow_html=True)
    
    # Grid impacts text
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px;">
        <p style="font-size: 0.9rem; color: #2c3e50; line-height: 1.5; margin: 0;">
            Atlanta's grid faces new demands from growing data centers and changing energy flows. Rather than one-way delivery from large power plants, our grid must now manage two-way power flows from distributed solar, batteries, and electric vehicles.
        </p>
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
