# app/main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, get_top_regions, plot_boxplot

# Set page config for better appearance
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Title and description
st.title("Solar Potential Across Benin, Sierra Leone, and Togo")
st.markdown("Explore solar radiation metrics (GHI) across countries with interactive visualizations.")

# Load data
try:
    combined = load_data()
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

# Sidebar for country selection
st.sidebar.header("Filter Options")
all_countries = combined['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=all_countries,
    default=all_countries,
    help="Choose one or more countries to compare."
)

# Main content
if selected_countries:
    # GHI Boxplot
    st.subheader("GHI Distribution by Country")
    fig = plot_boxplot(combined, metric='GHI', countries=selected_countries)
    st.pyplot(fig)
    
    # Top Regions Table
    st.subheader("Top Countries by Average GHI")
    top_regions = get_top_regions(combined, metric='GHI', n=3)
    st.table(top_regions.style.format({"GHI": "{:.2f}"}))
else:
    st.warning("Please select at least one country to visualize.")

# Footer
st.markdown("---")
st.markdown("Developed for Kifiya AI Mastery Bootcamp | Data Source: Cleaned Solar Radiation CSVs")