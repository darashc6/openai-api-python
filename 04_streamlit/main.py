import streamlit as st
import pandas as pd
import numpy as np
import random
import time

"""
# My first app
"""
st.text("Simple text -> st.text()")
st.text("Hello World!")

st.text("An example of writing a dataframe -> Using pd.DataFrame() inside st.write()")
st.write(
    pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
)

st.text("Another example of writing a dataframe -> Using st.dataframe()")
st.text("This example uses Panda's DataFrame, as well the 'column_config' property to define the column layout.", )
st.dataframe(
    pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.sh", "https://extras.sh", "https://issues.sh"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)]
        }
    ),
    column_config={
        "name": "App Name",
        "url": st.column_config.LinkColumn("App URL"),
        "stars": st.column_config.NumberColumn("GitHub Stars", help="Number of stars on GitHub", format="%d ⭐"),
        "views_history": st.column_config.LineChartColumn("Views History", y_min=0, y_max=5000)
    },
    hide_index=True
)

st.text("Drawing a Line Chart -> st.line_chart()")
st.line_chart(
    pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
)

st.text("Plot a data point of a map")

show_map = st.checkbox("Show map?", key="checkbox_map", on_change=lambda: print(f"Checkbox value selected: {st.session_state.checkbox_map}"))

if show_map:
    st.map(pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    ))

st.text("Using Streamlit's inbuild widgets")

show_widgets = st.checkbox("Show widgets?", key="my_checkbox", on_change=lambda: print(f"Checkbox value selected: {st.session_state.my_checkbox}"))

def streamlit_text_input():
    # https://docs.streamlit.io/library/api-reference/widgets/st.text_input

    st.text_input(
        "Your name: ", 
        key="input_name",
        placeholder="Enter your name",
        help="Example of a Streamlit TextInput widget",
        on_change=lambda: print(f"Input Value: {st.session_state.input_name}")
    )

def streamlit_number_input():
    # https://docs.streamlit.io/library/api-reference/widgets/st.number_input

    st.number_input(
        "Enter a Number:",
        step=1,
        key='input_number',
        min_value=1,
        max_value=50,
        help="Example of a Streamlit NumberInput widget",
        on_change=lambda: print(f"Number Input Value: {st.session_state.input_number}")
    )

def streamlit_button():
    # https://docs.streamlit.io/library/api-reference/widgets/st.button

    st.button(
        "Click here", 
        key="my_button", 
        help="Example of a Streamlit Button widget",
        type="secondary",
        on_click=lambda: print("Button clicked")
    )

def streamlit_checkbox():
    # https://docs.streamlit.io/library/api-reference/widgets/st.checkbox

    st.checkbox(
        "I agree to the terms and conditions",
        key="terms_checkbox",
        help="Example of a Streamlit CheckBox widget",
        on_change=lambda: print(f"Agree to terms and conditions? {st.session_state.terms_checkbox}")
    )

def streamlit_radio():
    # https://docs.streamlit.io/library/api-reference/widgets/st.radio

    st.radio(
        "Your favorite color",
        ["Red", "Blue", "Green"],
        key="radio_favcolor",
        help="Example of a Streamlit Radio widget",
        captions=["Color Red", "Color Blue", "Color Green"],
        horizontal=True,
        on_change=lambda: print(f"Your favourite color: {st.session_state.radio_favcolor}")
    )

def streamlit_selectbox():
    # https://docs.streamlit.io/library/api-reference/widgets/st.selectbox

    st.selectbox(
        "Your favourite city", 
        ["Paris", "London", "Madrid", "Berlin"], 
        key="selectbox_favcity", 
        help="Example of a Streamlit SelectBox widget",
        on_change=lambda: print(f"Your favourite city is: {st.session_state.selectbox_favcity}")
    )

def streamlit_slider():
    st.slider(
        "Slider", 
        min_value=0, 
        max_value=100, 
        value=0,
        key="my_slider", 
        on_change=lambda: print(f"Slider value selected: {st.session_state.my_slider}"))

def streamlit_file_uploader():
    # https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader

    st.file_uploader(
        "Upload a file:",
        key="file_uploaded",
        type=["png", "jpg"],
        help="Example of a Streamlit FileUploader widget",
        on_change=lambda: print(f"File uploaded: {st.session_state.file_uploaded}")
    )

if show_widgets:
    streamlit_text_input()
    streamlit_number_input()
    streamlit_button()
    streamlit_checkbox()
    streamlit_radio()
    streamlit_selectbox()
    streamlit_slider()
    streamlit_file_uploader()


# Adding a sidebar -> st.sidebar() or using 'with'
with st.sidebar:
    st.selectbox(
        "Select an option",
        ["US", "UK", "DE", "FR"]
    )

    st.slider(
        "Temperature"
    )


# Columns
# First column -> 20% of space
# Second column -> 50% of space
# Third column -> 30% of space
col1, col2, col3 = st.columns([0.2, 0.5, 0.3], gap="medium")

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

# Expanders
with st.expander("See explanation for Columns"):
    st.write("The first column takes 20% of the available width.")
    st.write("The second column takes 50% of the available width.")
    st.write("The thrid column takes 30% of the available width.")

# Progress bar and spinners
with st.spinner("Wait for it..."):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress_bar.progress(i + 1)
    st.success("Done!")
