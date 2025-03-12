import streamlit as st
import os
import base64

# Define the path to the image folder
image_folder = os.path.join(os.getcwd(), "images")

# Define the list of units and map them to local .jpg image file paths in the /images folder
unit_images = {
    "Crawler": "crawler.jpg",
    "Fang": "fang.jpg",
    "Hound": "hound.jpg",
    "Marksman": "marksman.jpg",
    "Arclight": "arclight.jpg",
    "Wasp": "wasp.jpg",
    "Mustang": "mustang.jpg",
    "Sledgehammer": "sledgehammer.jpg",
    "Steelballs": "steelball.jpg",
    "Stormcaller": "stormcaller.jpg",
    "Phoenix": "phoenix.jpg",
    "Phantom Ray": "phantom_ray.jpg",
    "Tarantula": "tarantula.jpg",
    "Sabertooth": "sabertooth.jpg",
    "Rhino": "rhino.jpg",
    "Hacker": "hacker.jpg",
    "Wraith": "wraith.jpg",
    "Scorpion": "scorpion.jpg",
    "Vulcan": "vulcan.jpg",
    "Fortress": "fortress.jpg",
    "Melting Point": "melting_point.jpg",
    "Sandworm": "sandworm.jpg",
    "Raiden": "raiden.jpg",
    "Overlord": "overlord.jpg",
    "War Factory": "war_factory.jpg",
    "Fire Badger": "fire_badger.jpg",
    "Typhoon": "typhoon.jpg",
    "Farseer": "farseer.jpg",
}

# Matrix key
# S = 6 # unit wins, >95% HP left
# A = 5 # unit wins, 60-95% HP left
# B = 4 # unit wins, 10-60% HP left
# C = 3 # unit wins, <10% HP left
# / = 2 mirror match
# D = 1 # unit lose, Opponent 10-50% HP left
# E = 0 # unit lose, Opponent >50% HP left
# Load unit matrix and overrides into Pandas DataFrames
unit_matrix_data = {
    # Add the matrix data for counters here as columns
    "Crawler": [
        2, # Crawler
        4, # Fang
        1, # Hound
        5, # Marksman
        0, # Arclight
        0, # Wasp
        5, # Mustang
        1, # Sledgehammer
        5, # Steelballs
        5, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        4, # Sabertooth
        1, # Rhino
        5, # Hacker
        0, # Wraith
        3, # Scorpion
        0, # Vulcan
        5, # Fortress
        5, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        0, # Fire Badger
        1, # Typhoon
        1, # Farseer
    ],
    "Fang": [
        1, # Crawler
        2, # Fang
        1, # Hound
        5, # Marksman
        0, # Arclight
        4, # Wasp
        1, # Mustang
        0, # Sledgehammer
        3, # Steelballs
        0, # Stormcaller
        5, # Phoenix
        4, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        1, # Rhino
        5, # Hacker
        0, # Wraith
        0, # Scorpion
        0, # Vulcan
        3, # Fortress
        4, # Melting Point
        1, # Sandworm
        4, # Raiden
        4, # Overlord
        1, # War Factory
        0, # Fire Badger
        0, # Typhoon
        1, # Farseer
    ],
    "Hound": [
        5, # Crawler
        5, # Fang
        2, # Hound
        1, # Marksman
        1, # Arclight
        0, # Wasp
        3, # Mustang
        1, # Sledgehammer
        1, # Steelballs
        4, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        3, # Sabertooth
        1, # Rhino
        1, # Hacker
        0, # Wraith
        1, # Scorpion
        1, # Vulcan
        1, # Fortress
        3, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        1, # Fire Badger
        1, # Typhoon
        1, # Farseer
    ],
    "Marksman": [
        1, # Crawler
        1, # Fang
        4, # Hound
        2, # Marksman
        6, # Arclight
        1, # Wasp
        1, # Mustang
        1, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        5, # Phoenix
        1, # Phantom Ray
        4, # Tarantula
        1, # Sabertooth
        1, # Rhino
        6, # Hacker
        5, # Wraith
        3, # Scorpion
        4, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        1, # Raiden
        5, # Overlord
        1, # War Factory
        5, # Fire Badger
        3, # Typhoon
        1, # Farseer
    ],
    "Arclight": [
        6, # Crawler
        6, # Fang
        4, # Hound
        0, # Marksman
        2, # Arclight
        0, # Wasp
        6, # Mustang
        1, # Sledgehammer
        1, # Steelballs
        0, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        0, # Rhino
        0, # Hacker
        0, # Wraith
        0, # Scorpion
        1, # Vulcan
        0, # Fortress
        0, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        0, # War Factory
        1, # Fire Badger
        1, # Typhoon
        1, # Farseer
    ],
    "Wasp": [
        6, # Crawler
        1, # Fang
        6, # Hound
        3, # Marksman
        6, # Arclight
        2, # Wasp
        1, # Mustang
        6, # Sledgehammer
        6, # Steelballs
        6, # Stormcaller
        4, # Phoenix
        1, # Phantom Ray
        6, # Tarantula
        6, # Sabertooth
        5, # Rhino
        6, # Hacker
        0, # Wraith
        5, # Scorpion
        5, # Vulcan
        5, # Fortress
        4, # Melting Point
        6, # Sandworm
        4, # Raiden
        4, # Overlord
        5, # War Factory
        6, # Fire Badger
        1, # Typhoon
        1, # Farseer
    ],
    "Mustang": [
        1, # Crawler
        4, # Fang
        1, # Hound
        4, # Marksman
        0, # Arclight
        4, # Wasp
        2, # Mustang
        0, # Sledgehammer
        0, # Steelballs
        3, # Stormcaller
        5, # Phoenix
        3, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        1, # Rhino
        4, # Hacker
        1, # Wraith
        1, # Scorpion
        0, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        4, # Raiden
        4, # Overlord
        1, # War Factory
        1, # Fire Badger
        1, # Typhoon
        1, # Farseer
    ],
    "Sledgehammer": [
        5, # Crawler
        6, # Fang
        4, # Hound
        3, # Marksman
        5, # Arclight
        0, # Wasp
        6, # Mustang
        2, # Sledgehammer
        1, # Steelballs
        4, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        1, # Rhino
        4, # Hacker
        0, # Wraith
        0, # Scorpion
        1, # Vulcan
        0, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        0, # War Factory
        1, # Fire Badger
        4, # Typhoon
        1, # Farseer
    ],
    "Steelballs": [
        1, # Crawler
        1, # Fang
        4, # Hound
        4, # Marksman
        5, # Arclight
        0, # Wasp
        5, # Mustang
        4, # Sledgehammer
        2, # Steelballs
        5, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        4, # Tarantula
        1, # Sabertooth
        5, # Rhino
        0, # Hacker
        0, # Wraith
        1, # Scorpion
        4, # Vulcan
        3, # Fortress
        4, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        4, # Fire Badger
        5, # Typhoon
        3, # Farseer
    ],
    "Stormcaller": [
        1, # Crawler
        6, # Fang
        1, # Hound
        4, # Marksman
        6, # Arclight
        0, # Wasp
        3, # Mustang
        1, # Sledgehammer
        1, # Steelballs
        2, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        4, # Tarantula
        4, # Sabertooth
        0, # Rhino
        6, # Hacker
        0, # Wraith
        6, # Scorpion
        5, # Vulcan
        4, # Fortress
        5, # Melting Point
        0, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        1, # Fire Badger
        5, # Typhoon
        1, # Farseer
    ],
    "Phoenix": [
        6, # Crawler
        0, # Fang
        6, # Hound
        1, # Marksman
        6, # Arclight
        1, # Wasp
        1, # Mustang
        6, # Sledgehammer
        5, # Steelballs
        6, # Stormcaller
        2, # Phoenix
        1, # Phantom Ray
        6, # Tarantula
        6, # Sabertooth
        6, # Rhino
        6, # Hacker
        5, # Wraith
        6, # Scorpion
        6, # Vulcan
        6, # Fortress
        1, # Melting Point
        6, # Sandworm
        1, # Raiden
        4, # Overlord
        5, # War Factory
        6, # Fire Badger
        4, # Typhoon
        1, # Farseer
    ],
    "Phantom Ray": [
        5, # Crawler
        1, # Fang
        6, # Hound
        3, # Marksman
        6, # Arclight
        3, # Wasp
        1, # Mustang
        6, # Sledgehammer
        6, # Steelballs
        6, # Stormcaller
        3, # Phoenix
        2, # Phantom Ray
        6, # Tarantula
        6, # Sabertooth
        6, # Rhino
        6, # Hacker
        5, # Wraith
        6, # Scorpion
        6, # Vulcan
        6, # Fortress
        1, # Melting Point
        6, # Sandworm
        1, # Raiden
        3, # Overlord
        5, # War Factory
        6, # Fire Badger
        4, # Typhoon
        1, # Farseer
    ],
    "Tarantula": [
        5, # Crawler
        5, # Fang
        4, # Hound
        1, # Marksman
        4, # Arclight
        0, # Wasp
        4, # Mustang
        4, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        2, # Tarantula
        1, # Sabertooth
        1, # Rhino
        3, # Hacker
        0, # Wraith
        1, # Scorpion
        4, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        4, # Fire Badger
        5, # Typhoon
        1, # Farseer
    ],
    "Sabertooth": [
        1, # Crawler
        3, # Fang
        1, # Hound
        3, # Marksman
        5, # Arclight
        0, # Wasp
        4, # Mustang
        4, # Sledgehammer
        5, # Steelballs
        1, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        5, # Tarantula
        2, # Sabertooth
        4, # Rhino
        5, # Hacker
        0, # Wraith
        4, # Scorpion
        5, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        5, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "Rhino": [
        3, # Crawler
        3, # Fang
        4, # Hound
        3, # Marksman
        6, # Arclight
        0, # Wasp
        4, # Mustang
        4, # Sledgehammer
        1, # Steelballs
        6, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        4, # Tarantula
        1, # Sabertooth
        2, # Rhino
        5, # Hacker
        0, # Wraith
        5, # Scorpion
        5, # Vulcan
        1, # Fortress
        0, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        0, # War Factory
        5, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "Hacker": [
        1, # Crawler
        0, # Fang
        3, # Hound
        0, # Marksman
        6, # Arclight
        0, # Wasp
        1, # Mustang
        1, # Sledgehammer
        6, # Steelballs
        0, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        1, # Rhino
        2, # Hacker
        0, # Wraith
        1, # Scorpion
        1, # Vulcan
        0, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        0, # War Factory
        5, # Fire Badger
        5, # Typhoon
        1, # Farseer
    ],
    "Wraith": [
        6, # Crawler
        4, # Fang
        6, # Hound
        1, # Marksman
        6, # Arclight
        6, # Wasp
        4, # Mustang
        5, # Sledgehammer
        5, # Steelballs
        6, # Stormcaller
        1, # Phoenix
        1, # Phantom Ray
        5, # Tarantula
        5, # Sabertooth
        5, # Rhino
        6, # Hacker
        2, # Wraith
        5, # Scorpion
        5, # Vulcan
        5, # Fortress
        0, # Melting Point
        5, # Sandworm
        1, # Raiden
        1, # Overlord
        5, # War Factory
        6, # Fire Badger
        1, # Typhoon
        1, # Farseer
    ],
    "Scorpion": [
        1, # Crawler
        6, # Fang
        5, # Hound
        1, # Marksman
        5, # Arclight
        0, # Wasp
        5, # Mustang
        5, # Sledgehammer
        6, # Steelballs
        1, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        4, # Tarantula
        1, # Sabertooth
        1, # Rhino
        5, # Hacker
        0, # Wraith
        2, # Scorpion
        6, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        6, # Fire Badger
        6, # Typhoon
        4, # Farseer
    ],
    "Vulcan": [
        6, # Crawler
        6, # Fang
        5, # Hound
        1, # Marksman
        4, # Arclight
        0, # Wasp
        6, # Mustang
        4, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        1, # Rhino
        3, # Hacker
        0, # Wraith
        1, # Scorpion
        2, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        5, # Fire Badger
        4, # Typhoon
        1, # Farseer
    ],
    "Fortress": [
        1, # Crawler
        1, # Fang
        3, # Hound
        4, # Marksman
        6, # Arclight
        0, # Wasp
        3, # Mustang
        5, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        5, # Tarantula
        3, # Sabertooth
        5, # Rhino
        6, # Hacker
        0, # Wraith
        4, # Scorpion
        5, # Vulcan
        2, # Fortress
        0, # Melting Point
        1, # Sandworm
        1, # Raiden
        0, # Overlord
        1, # War Factory
        6, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "Melting Point": [
        1, # Crawler
        1, # Fang
        1, # Hound
        3, # Marksman
        5, # Arclight
        1, # Wasp
        3, # Mustang
        4, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        4, # Phoenix
        4, # Phantom Ray
        5, # Tarantula
        4, # Sabertooth
        6, # Rhino
        6, # Hacker
        6, # Wraith
        5, # Scorpion
        6, # Vulcan
        6, # Fortress
        2, # Melting Point
        4, # Sandworm
        5, # Raiden
        4, # Overlord
        4, # War Factory
        5, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "Sandworm": [
        4, # Crawler
        4, # Fang
        4, # Hound
        6, # Marksman
        6, # Arclight
        0, # Wasp
        4, # Mustang
        5, # Sledgehammer
        1, # Steelballs
        6, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        4, # Tarantula
        4, # Sabertooth
        3, # Rhino
        5, # Hacker
        0, # Wraith
        4, # Scorpion
        5, # Vulcan
        3, # Fortress
        1, # Melting Point
        2, # Sandworm
        0, # Raiden
        0, # Overlord
        1, # War Factory
        6, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "Raiden": [
        6, # Crawler
        1, # Fang
        6, # Hound
        3, # Marksman
        6, # Arclight
        1, # Wasp
        1, # Mustang
        6, # Sledgehammer
        6, # Steelballs
        6, # Stormcaller
        5, # Phoenix
        5, # Phantom Ray
        6, # Tarantula
        6, # Sabertooth
        6, # Rhino
        6, # Hacker
        6, # Wraith
        6, # Scorpion
        6, # Vulcan
        6, # Fortress
        1, # Melting Point
        4, # Sandworm
        2, # Raiden
        1, # Overlord
        6, # War Factory
        6, # Fire Badger
        5, # Typhoon
        4, # Farseer
    ],
    "Overlord": [
        6, # Crawler
        1, # Fang
        6, # Hound
        1, # Marksman
        6, # Arclight
        1, # Wasp
        1, # Mustang
        6, # Sledgehammer
        6, # Steelballs
        6, # Stormcaller
        1, # Phoenix
        1, # Phantom Ray
        6, # Tarantula
        6, # Sabertooth
        6, # Rhino
        6, # Hacker
        6, # Wraith
        6, # Scorpion
        6, # Vulcan
        6, # Fortress
        1, # Melting Point
        6, # Sandworm
        4, # Raiden
        2, # Overlord
        6, # War Factory
        6, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "War Factory": [
        4, # Crawler
        5, # Fang
        5, # Hound
        5, # Marksman
        6, # Arclight
        0, # Wasp
        5, # Mustang
        6, # Sledgehammer
        5, # Steelballs
        4, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        6, # Tarantula
        5, # Sabertooth
        5, # Rhino
        1, # Hacker
        0, # Wraith
        5, # Scorpion
        6, # Vulcan
        4, # Fortress
        1, # Melting Point
        5, # Sandworm
        0, # Raiden
        0, # Overlord
        2, # War Factory
        6, # Fire Badger
        5, # Typhoon
        5, # Farseer
    ],
    "Fire Badger": [
        6, # Crawler
        6, # Fang
        4, # Hound
        1, # Marksman
        4, # Arclight
        0, # Wasp
        5, # Mustang
        3, # Sledgehammer
        1, # Steelballs
        5, # Stormcaller
        0, # Phoenix
        0, # Phantom Ray
        1, # Tarantula
        1, # Sabertooth
        1, # Rhino
        1, # Hacker
        0, # Wraith
        0, # Scorpion
        1, # Vulcan
        0, # Fortress
        1, # Melting Point
        1, # Sandworm
        0, # Raiden
        0, # Overlord
        0, # War Factory
        2, # Fire Badger
        4, # Typhoon
        1, # Farseer
    ],
    "Typhoon": [
        5, # Crawler
        6, # Fang
        4, # Hound
        1, # Marksman
        3, # Arclight
        6, # Wasp
        4, # Mustang
        1, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        1, # Phoenix
        1, # Phantom Ray
        4, # Tarantula
        1, # Sabertooth
        0, # Rhino
        1, # Hacker
        3, # Wraith
        0, # Scorpion
        1, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        1, # Raiden
        1, # Overlord
        1, # War Factory
        1, # Fire Badger
        0, # Typhoon
        1, # Farseer
    ],
    "Farseer": [
        3, # Crawler
        5, # Fang
        5, # Hound
        1, # Marksman
        5, # Arclight
        5, # Wasp
        4, # Mustang
        4, # Sledgehammer
        1, # Steelballs
        1, # Stormcaller
        3, # Phoenix
        3, # Phantom Ray
        3, # Tarantula
        1, # Sabertooth
        1, # Rhino
        4, # Hacker
        5, # Wraith
        1, # Scorpion
        4, # Vulcan
        1, # Fortress
        1, # Melting Point
        1, # Sandworm
        1, # Raiden
        1, # Overlord
        1, # War Factory
        4, # Fire Badger
        3, # Typhoon
        2, # Farseer
    ],
}


UNITS = list(unit_matrix_data.keys())

st.set_page_config(layout="wide", page_title="Mechabellum Unit Counters")

# Sidebar configuration
cols_per_row = st.sidebar.slider(
    "Select the number of columns per row:", min_value=2, max_value=24, value=13, step=1
)
cols_per_row_output = st.sidebar.slider(
    "Select the number of columns per row for output:",
    min_value=5,
    max_value=24,
    value=16,
    step=1,
)
show_sliders = st.sidebar.checkbox("Show Weight Sliders")

# Initialize session state
if "selected_units" not in st.session_state:
    st.session_state.selected_units = []
if "weights" not in st.session_state:
    st.session_state.weights = {unit: 1 for unit in unit_images.keys()}


# Helper function to convert image to base64
def get_image_as_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Display unit selection grid
def display_unit_selection_grid(unit_list, cols_per_row, show_sliders):
    num_units = len(unit_list)
    for i in range(0, num_units, cols_per_row):
        cols = st.columns(cols_per_row)
        for j, unit in enumerate(unit_list[i : i + cols_per_row]):
            with cols[j]:
                if st.checkbox(
                    f" ",
                    key=f"checkbox:{unit}",
                    value=(unit in st.session_state.selected_units),
                ):
                    if unit not in st.session_state.selected_units:
                        st.session_state.selected_units.append(unit)
                else:
                    if unit in st.session_state.selected_units:
                        st.session_state.selected_units.remove(unit)

                border_style = (
                    "border: 3px solid black;"
                    if unit in st.session_state.selected_units
                    else "border: 3px solid transparent;"
                )
                img_path = os.path.join(image_folder, unit_images[unit])
                img_base64 = get_image_as_base64(img_path)

                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <img src="data:image/jpeg;base64,{img_base64}" style="width:100%; {border_style} border-radius: 10px;">
                        <p>{unit}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if show_sliders and unit in st.session_state.selected_units:
                    st.session_state.weights[unit] = st.slider(
                        f" ",
                        key=f"slider:{unit}",
                        min_value=1,
                        max_value=5,
                        value=st.session_state.weights[unit],
                    )


# Function to calculate the counter score
def get_counter_score(selected_units, unit_matrix_data, weights):
    scores = {unit: 0 for unit in UNITS}
    div = {unit: 0 for unit in UNITS}

    for selected in selected_units:
        for unit, counters in unit_matrix_data.items():
            index = UNITS.index(selected)
            scores[unit] += counters[index] * weights[selected]
            div[unit] += weights[selected]

    if selected_units:
        scores = {k: scores[k] / div[k] if scores[k] > 0 else 0 for k in scores.keys()}
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


# Function to classify units into tiers based on score
def classify_by_tier(best_counters):
    tier_bins = {
        "S Tier (6 points)": [],
        "A Tier (5 points)": [],
        "B Tier (4 points)": [],
        "C Tier (3 points)": [],
        "D/E/F Tier (0-2 points)": [],
    }

    for unit, score in best_counters:
        if score == 6:
            tier_bins["S Tier (6 points)"].append(unit)
        elif score == 5:
            tier_bins["A Tier (5 points)"].append(unit)
        elif score == 4:
            tier_bins["B Tier (4 points)"].append(unit)
        elif score == 3:
            tier_bins["C Tier (3 points)"].append(unit)
        else:
            tier_bins["D/E/F Tier (0-2 points)"].append(unit)

    return tier_bins


# Display the best counter units in matrix format
def display_best_counters(tiered_counters, cols_per_row_output):
    st.write("Best Counter Units by Tier:")
    for tier, units in tiered_counters.items():
        st.markdown(f"**{tier}**")
        if units:
            cols = st.columns(cols_per_row_output)
            for idx, unit in enumerate(units):
                base_unit = unit.split(":")[0].strip() if ":" in unit else unit
                img_path = os.path.join(image_folder, unit_images[base_unit])
                img_base64 = get_image_as_base64(img_path)

                with cols[idx % cols_per_row_output]:
                    st.markdown(
                        f"""
                        <div style="text-align: center;">
                            <img src="data:image/jpeg;base64,{img_base64}" style="width:100%; border-radius: 10px;">
                            <p><b>{unit.split(":")[1].strip() if ":" in unit else ""}</b></p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


# Main execution
unit_list = list(unit_images.keys())
display_unit_selection_grid(unit_list, cols_per_row, show_sliders)

selected_units = st.session_state.selected_units
raw_weights = st.session_state.weights
total_weight = sum(raw_weights.values())
weights = {
    unit: (raw_weights[unit] / total_weight) if unit in raw_weights else 0
    for unit in UNITS
}

best_counters = get_counter_score(selected_units, unit_matrix_data, weights)
tiered_counters = classify_by_tier(best_counters)
display_best_counters(tiered_counters, cols_per_row_output)
