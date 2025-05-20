import streamlit as st
import os

def show_wip_warning():
    """
    Display a warning popup indicating that the page is a work in progress.
    """
    # Apply custom CSS for larger font sizes
    st.markdown(
        """
        <style>
        .warning-message {
            font-size: 35px;
            font-weight: bold;
            color: #333;
            text-align: center;
            background-color: hsl(54, 100%, 60%);
            padding: 20px;
            border-radius: 50px;
            margin-bottom: 20px;
        }
        </style>
        <div class="warning-message">⚠️ Work in Progress ⚠️ <br> This page is under development.</div>
        """, 
        unsafe_allow_html=True
    )

def create_sidebar(current_page=None):
    """
    Creates a consistent sidebar for the Atlanta Energyshed application.
    This function should be called from all pages to ensure a consistent navigation experience.
    
    Args:
        current_page (str, optional): The filename of the current page (e.g., 'Defining_Atlanta.py').
                                     If None, will attempt to determine from session state.
    
    Returns:
        None
    """
    with st.sidebar:
        # If current_page is not provided, try to get it from session state or other means
        if current_page is None:
            current_page = os.path.basename(st.session_state.get('current_page', ''))
        
        # Navigation links with icons
        # Home page
        if current_page == "Defining_Atlanta.py":
            st.markdown('<a href="." class="nav-link active" target="_self"><span class="nav-icon">🏠</span> Defining Energyshed</a>', unsafe_allow_html=True)
        else:
            st.markdown('<a href="." class="nav-link" target="_self"><span class="nav-icon">🏠</span> Defining Energyshed</a>', unsafe_allow_html=True)
        
        # Always show Energy Efficiency page
        if current_page == "1_Energy_Efficiency.py":
            st.markdown('<a href="Energy_Efficiency" class="nav-link active" target="_self"><span class="nav-icon">🔋</span> Energy Efficiency</a>', unsafe_allow_html=True)
        else:
            st.markdown('<a href="Energy_Efficiency" class="nav-link" target="_self"><span class="nav-icon">🔋</span> Energy Efficiency</a>', unsafe_allow_html=True)
        
        # Always show Local Generation page
        if current_page == "2_Local_Generation.py":
            st.markdown('<a href="Local_Generation" class="nav-link active" target="_self"><span class="nav-icon">☀️</span> Local Generation and Storage</a>', unsafe_allow_html=True)
        else:
            st.markdown('<a href="Local_Generation" class="nav-link" target="_self"><span class="nav-icon">☀️</span> Local Generation and Storage</a>', unsafe_allow_html=True)
        
        # Always show Energy Grid page
        if current_page == "3_Energy_Grid.py":
            st.markdown('<a href="Energy_Grid" class="nav-link active" target="_self"><span class="nav-icon">🔌</span> Grid Under Pressure</a>', unsafe_allow_html=True)
        else:
            st.markdown('<a href="Energy_Grid" class="nav-link" target="_self"><span class="nav-icon">🔌</span> Grid Under Pressure</a>', unsafe_allow_html=True)
        
        # Always show Looking Future page
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
