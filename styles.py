import streamlit as st
import os

def load_css(page_name=None):
    """
    Function to load custom CSS styles for the Atlanta Energyshed Dashboard
    
    Args:
        page_name: Optional name of the current page to apply specific styling
    """
    st.markdown('''
    <style>
        .sidebar .sidebar-content {
            background-color: #f5f5f5;
        }
        .sidebar-nav {
            padding: 10px;
        }
        .nav-link {
            padding: 15px 10px;
            text-decoration: none;
            border-radius: 5px;
            display: block;
            transition: background-color 0.3s;
            margin-bottom: 8px;
            font-weight: 500;
        }
        .nav-link:hover {
            background-color: #e0e0e0;
        }
        .nav-link.active {
            background-color: #1E88E5;
            color: white;
        }
        .sidebar-header {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #e0e0e0;
        }
        .nav-icon {
            margin-right: 10px;
        }
        /* Custom styling for headers */
        h1, h2, h3 {
            color: #1E88E5 !important;
            text-align: center !important;
            font-weight: 600 !important;
            margin-bottom: 1.5rem !important;
        }
        /* Add a subtle underline to headers */
        h1::after, h2::after, h3::after {
            content: "";
            display: block;
            width: 100px;
            height: 2px;
            background-color: #1E88E5;
            margin: 0.5rem auto;
        }
        /* Hide default sidebar navigation */
        [data-testid="stSidebarNav"] {display: none !important;}
        
        /* Remove header anchor links */
        .header-anchor {
            display: none !important;
        }
        
        /* Remove hover effect and pointer cursor from headers */
        h1, h2, h3, h4, h5, h6 {
            pointer-events: none !important;
        }
        
        /* Hide Streamlit's default anchor links for headers */
        .st-emotion-cache-ztfqz8 a {
            display: none !important;
        }
    </style>
    ''', unsafe_allow_html=True)