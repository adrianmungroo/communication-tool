import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys
import base64
from PIL import Image

# Add parent directory to path to import styles
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from styles import load_css

# Set page config
st.set_page_config(
    page_title="Grid Under Pressure | Atlanta Energyshed",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"  # Start with sidebar collapsed
)

# Load custom CSS
load_css()

# Import shared components
from shared_components import create_sidebar, show_wip_warning

# Store current page in session state for sidebar to access
st.session_state['current_page'] = __file__

# Create the sidebar with the current page name
create_sidebar(os.path.basename(__file__))

######################## PAGE CONTENT ########################

# Image Paths
gup_icon1_path = r"assets/gup_icon1.png"
gup_icon2_path = r"assets/gup_icon2.png"
gup_icon3_path = r"assets/gup_icon3.png"
gup_affordable_path = r"assets/gup_affordable.png"
gup_cost_time_path = r"assets/gup_cost_time.png"
gup_demand_path = r"assets/gup_demand.png"
gup_reduced_cost_path = r"assets/gup_reduced_cost.png"
gup_high_cost_path = r"assets/gup_high_cost.png"

# Load the images as bytes and convert to base64
with open(gup_icon1_path, "rb") as f:
    gup_icon1_bytes = f.read()
    gup_icon1_base64 = base64.b64encode(gup_icon1_bytes).decode()

with open(gup_icon2_path, "rb") as f:
    gup_icon2_bytes = f.read()
    gup_icon2_base64 = base64.b64encode(gup_icon2_bytes).decode()   

with open(gup_icon3_path, "rb") as f:
    gup_icon3_bytes = f.read()
    gup_icon3_base64 = base64.b64encode(gup_icon3_bytes).decode()

with open(gup_affordable_path, "rb") as f:
    gup_affordable_bytes = f.read()
    gup_affordable_base64 = base64.b64encode(gup_affordable_bytes).decode()

with open(gup_cost_time_path, "rb") as f:
    gup_cost_time_bytes = f.read()
    gup_cost_time_base64 = base64.b64encode(gup_cost_time_bytes).decode()

with open(gup_demand_path, "rb") as f:
    gup_demand_bytes = f.read()
    gup_demand_base64 = base64.b64encode(gup_demand_bytes).decode()

with open(gup_reduced_cost_path, "rb") as f:
    gup_reduced_cost_bytes = f.read()
    gup_reduced_cost_base64 = base64.b64encode(gup_reduced_cost_bytes).decode()

with open(gup_high_cost_path, "rb") as f:
    gup_high_cost_bytes = f.read()
    gup_high_cost_base64 = base64.b64encode(gup_high_cost_bytes).decode()

# Title
st.markdown("""
    <h1 style="font-size: 2.5rem; color: #1E5C8E; margin-bottom: 1rem;">Grid Under Pressure</h1>
    """, unsafe_allow_html=True)

# Main description text in a styled container
st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Atlanta's electrical grid stands at a critical juncture, facing mounting pressure from multiple directions. The traditional 
            model of centralized power distribution is giving way to a complex network balancing increased demand with diverse energy 
            sources.
            <br><br>
            This transformation demands thoughtful planning and targeted investments to ensure reliability while enabling the region's 
            clean energy transition and economic growth.
        </p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<h2 style="color: #1E5C8E; margin-bottom: 0.1rem;">Increased Demand</h2>
""", unsafe_allow_html=True)

_, icons, text, _ = st.columns([1,1,7,1])

with icons:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_icon1_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Increased Demand Icon">
    </div>
    """, unsafe_allow_html=True)

with text:
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Data centers require enormous electricity and exceptional reliability, essentially functioning as small towns on the grid. The increasing EV adoption in Atlanta also contributes to grid stress. Meanwhile, residential and commercial growth further strains the system. 
        </p>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("""
<h2 style="color: #1E5C8E; margin-bottom: 0.1rem;">Irregular Demand</h2>
""", unsafe_allow_html=True)

_, icons, text, _ = st.columns([1,1,7,1])

with icons:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_icon2_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Irregular Demand Icon">
    </div>
    """, unsafe_allow_html=True)

with text:
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Grid management grows increasingly complex as energy sources diversify. Unlike traditional power plants, distributed solar produces variable output based on weather and time of day. Electric vehicles create unpredictable demand spikes, while battery systems can both consume and supply power. This variability demands advanced forecasting, control systems, and market structures to maintain stability while optimizing distributed resource use.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<h2 style="color: #1E5C8E; margin-bottom: 0.1rem;">Infrastructural Difficulties</h2>
""", unsafe_allow_html=True)

_, icons, text, _ = st.columns([1,1,7,1])

with icons:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_icon3_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Infrastructural Difficulties Icon">
    </div>
    """, unsafe_allow_html=True)

with text:
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            Our current infrastructure wasn't designed for bidirectional power flows, creating voltage regulation issues and thermal overloads. Substations, transformers, and control systems need significant upgrades to safely accommodate distributed energy.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Why Fuel Mix Affects Price
st.markdown("""
<h2 style="color: #1E5C8E; margin-bottom: 0.1rem;">Why Fuel Mix Affects Price</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
        Electricity generation costs depend on which types of power plants are running. When demand is low, cheap, steady baseload plants (like nuclear) meet most needs. As demand rises, mid-cost plants (like gas combined-cycle) are added. On very hot or cold days, expensive peaker plants (like gas turbines) are used to cover the highest demand — driving prices up. The more we rely on costly plants, the higher the overall electricity price for consumers later on.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

# image 1
with col1:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_demand_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Increased Demand">
    </div>
    """, unsafe_allow_html=True)
    
# image 2
with col2:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_cost_time_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Increased Demand">
    </div>
    """, unsafe_allow_html=True)

# Title
st.markdown("""
<h2 style="color: #1E5C8E; margin-bottom: 0.1rem;">Finding a mutually cost beneficial solution</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
        Despite the mounting challenges—surging demand, irregular usage patterns, and aging infrastructure—the path forward for Atlanta's electrical grid is not only navigable but promising. The very forces driving complexity in our energy system—modernization, distributed energy resources (DERs), and emerging technologies—also offer the blueprint for a more resilient, flexible, and sustainable grid.
        <br><br>
        By leveraging these technologies intelligently—through coordinated EV charging, demand flexibility, and grid-integrated DERs—Atlanta can transform potential strains into valuable resources. What's emerging is a <strong>mutually beneficial framework</strong>—where reliability and resilience are not sacrificed in the pursuit of sustainability but are instead strengthened by it. Through collaborative planning and targeted investments, Atlanta can lead the way in demonstrating how a city can modernize its grid while supporting economic growth, reducing emissions, and empowering communities.
    </p>
</div>
""", unsafe_allow_html=True)

###

st.markdown("""
<h2 style="color: #1E5C8E; margin-bottom: 0.1rem;">Impact of Datacenters and DERs in Fuel Mix and Price</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

with col1:
    # title
    st.markdown("""
    <h3 style="color: #1E5C8E; margin-bottom: 0.1rem;">Before / After Datacenters</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            This scenario shows just how much energy—and subsequent pressure on surrounding grid infrastructure—that datacenters require to function, and how the energy landscape, cost, and fuel mix changes as our grid attempts to handle this increased load
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # image 1
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_high_cost_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Increased Demand">
    </div>
    """, unsafe_allow_html=True)
    # small font caption under image in red text
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <p style="font-size: 1.5rem; color: #FF0000; line-height: 1.6;">
            <strong>HIGH COST RELATIVELY</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    # title
    st.markdown("""
    <h3 style="color: #1E5C8E; margin-bottom: 0.1rem;">Before / After DER Implementation</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            This scenario shows just how our system adjusts to increased DER usage. While DER decreased energy usage drastically during daylight hours, it also forces greater reliance on generation that can be quickly scaled up and down—coal and natural gas plants
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # image 1
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_reduced_cost_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Increased Demand">
    </div>
    """, unsafe_allow_html=True)
    # small font caption under image in red text
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <p style="font-size: 1.5rem; color: #FF0000; line-height: 1.6;">
            <strong>REDUCED COST</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # title
    st.markdown("""
    <h3 style="color: #1E5C8E; margin-bottom: 0.1rem;">Datacenters + DER</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(240, 248, 255, 0.8); padding: 20px; border-radius: 5px; margin-bottom: 20px;">
        <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6;">
            So what does it look like all together? This scenario shows how the demand changes and subsequently the cost and emissions when all these changes come all at once
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # image 1
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/png;base64,{gup_affordable_base64}" 
             style="width: 70%; height: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" 
             alt="Increased Demand">
    </div>
    """, unsafe_allow_html=True)
    # small font caption under image in red text
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <p style="font-size: 1.5rem; color: #FF0000; line-height: 1.6;">
            <strong>AFFORDABLE COST</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <p style="font-size: 0.8rem; color: #2c3e50; line-height: 1.6;">
        <strong>NOTE: Cost predictions are for demonstration purposed only for now rather than actual model output</strong>
    </p>
</div>
""", unsafe_allow_html=True)