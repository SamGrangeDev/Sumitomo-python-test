import streamlit as st
import streamlit.components.v1 as components

# Function to fetch the map content from OneDrive
def load_map():
    # Use the direct link to the HTML file on OneDrive
    onedrive_html_link = "https://1drv.ms/u/s!AkhLpUUo4922blUR47UzRCYKNUI?embed=1"
    
    # Alternatively, if the HTML file is small, you could fetch the file content directly
    # Here we're assuming you already modified the local HTML file to use cloud links
    with open('local_path_to_modified_map.html', 'r', encoding='utf-8') as file:
        map_html = file.read()
    return map_html

# Streamlit app code
st.title("QGIS2web Map Embedded")

# Display the map
map_html = load_map()
components.html(map_html, height=600, width=800)
