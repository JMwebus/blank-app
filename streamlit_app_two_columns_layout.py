# Streamlit App Two-Columns Layout


import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Custom Streamlit App",
    page_icon="📊",
    layout="wide"
)

# Custom header
st.markdown(
    """
    <style>
    .header {
        font-size: 32px;
        color: #4CAF50;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="header">
        <img src="https://via.placeholder.com/150" width="150" />
        <h1>Custom Streamlit Title</h1>
        <p>Your custom subtitle or tagline here</p>
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)

# Create two columns with specified width ratio
left_column, right_column = st.columns([0.3, 0.7])

# Content for the left column
with left_column:
    st.header("Left Column")
    st.write("This is the left column, taking up 30% of the width.")
    st.image("https://via.placeholder.com/100", caption="Sample Image")

# Content for the right column
with right_column:
    st.header("Right Column")
    st.write("This is the right column, taking up 70% of the width.")
    st.write("You can add more content here, such as charts, tables, or text.")
