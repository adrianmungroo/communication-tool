import streamlit as st
import os
from streamlit_javascript import st_javascript

def show_wip_warning():
    """
    Display a warning popup indicating that the page is a work in progress.
    This should be called on all pages except the main Defining Atlanta page.
    """
    st.warning(
        "⚠️ **Work in Progress** ⚠️\n\n"
        "#### This page is currently under development and not yet complete. "
    )

def create_sidebar(current_page=None):
    """
    Creates a consistent sidebar for the Energyshed application.
    This function should be called from all pages to ensure a consistent navigation experience.
    
    Args:
        current_page (str, optional): The filename of the current page (e.g., 'Defining_Atlanta.py').
                                     If None, will attempt to determine from session state.
    
    Returns:
        None
    """
    # Try to detect if user is on desktop or mobile
    try:
        # Get the user agent string from the browser
        ua_string = st_javascript("window.navigator.userAgent;", key="sidebar_ua_detector")
        
        # Simple check for mobile devices (this is a basic approach)
        is_mobile = False
        if ua_string and isinstance(ua_string, str):
            mobile_keywords = ['Android', 'iPhone', 'iPad', 'Mobile', 'Tablet']
            is_mobile = any(keyword in ua_string for keyword in mobile_keywords)
        
        # For desktop users, expand the sidebar by default
        if not is_mobile and 'sidebar_state' not in st.session_state:
            # Use JavaScript to expand the sidebar for desktop users
            st_javascript("""
                if (!window.frameElement) {
                    const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
                    if (sidebar) {
                        const sidebarContent = sidebar.querySelector('[data-testid="stSidebarContent"]');
                        if (sidebarContent && sidebarContent.style.width === '0px') {
                            const expanderButton = sidebar.querySelector('button[kind="secondary"]');
                            if (expanderButton) {
                                expanderButton.click();
                            }
                        }
                    }
                }
            """, key="sidebar_expander")
            # Mark that we've set the sidebar state
            st.session_state['sidebar_state'] = 'expanded'
    except Exception as e:
        # If there's any error, just continue without changing sidebar state
        pass
    
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
