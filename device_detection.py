import streamlit as st
from user_agents import parse

def detect_device():
    """
    Detect if the user is on a mobile device or PC.
    
    Returns:
        dict: A dictionary with device information including:
            - is_mobile (bool): True if the device is mobile, False otherwise
            - device_type (str): 'mobile', 'tablet', or 'desktop'
            - browser (str): Browser name
            - os (str): Operating system name
    """
    # Get the user agent from the request headers
    try:
        # Access the request object through streamlit's experimental server features
        # This is wrapped in a try/except because it depends on internal Streamlit APIs
        # that might change in future versions
        user_agent_string = st.get_option("client.toolbarMode")
        if not user_agent_string or user_agent_string == "":
            # If we can't get the user agent directly, use a fallback approach
            # This is less reliable but better than nothing
            user_agent_string = st.experimental_get_query_params().get('ua', [''])[0]
    except:
        # If all else fails, we'll have to use a default
        user_agent_string = ""
    
    # Parse the user agent string
    user_agent = parse(user_agent_string)
    
    # Determine device type
    if user_agent.is_mobile:
        device_type = "mobile"
    elif user_agent.is_tablet:
        device_type = "tablet"
    else:
        device_type = "desktop"
    
    # Return device information
    return {
        "is_mobile": user_agent.is_mobile,
        "device_type": device_type,
        "browser": user_agent.browser.family,
        "os": user_agent.os.family
    }

def get_device_specific_styles():
    """
    Returns CSS styles based on the detected device type.
    
    Returns:
        str: CSS styles as a string
    """
    device_info = detect_device()
    
    # Base styles that apply to all devices
    base_styles = """
    .common-style {
        padding: 10px;
    }
    """
    
    # Mobile-specific styles
    if device_info["is_mobile"]:
        return base_styles + """
        .device-specific {
            font-size: 0.9rem;
            padding: 5px;
        }
        .image-container img {
            width: 100% !important;
        }
        """
    # Desktop-specific styles
    else:
        return base_styles + """
        .device-specific {
            font-size: 1.1rem;
            padding: 15px;
        }
        """

def display_device_info():
    """
    Display device information in the Streamlit app.
    Useful for debugging or informing users.
    """
    device_info = detect_device()
    
    st.write("### Device Information")
    st.write(f"Device Type: {device_info['device_type']}")
    st.write(f"Browser: {device_info['browser']}")
    st.write(f"Operating System: {device_info['os']}")
