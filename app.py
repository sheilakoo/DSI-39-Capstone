# Import libraries
from pathlib import Path
import streamlit as st
from urllib.request import urlopen
import pandas as pd
import numpy as np
import requests
import pickle 
import mediapipe as mp
import cv2
#import tempfile
#from sklearn.linear_model import LogisticRegression, RidgeClassifier


# This code is different for each deployed app.
CURRENT_THEME = "dark"
IS_DARK_THEME = True
EXPANDER_TEXT = """
    This is Streamlit's default *Dark* theme. You can enable it in the app menu
    (☰ -> Settings -> Theme) or by copying the following code to
    `.streamlit/config.toml`:

    ```python
    [theme]
    primaryColor="#02ffff"
    backgroundColor="#191919"
    secondaryBackgroundColor="#505050"
    textColor="#ffffff"
    font="monospace"
    ```
    """

### --- WEB LAYOUT --- ###
# Configure webpage
st.set_page_config(
    page_title='Ride Ride Revolution',
    page_icon='🚲',
    layout='wide',
    initial_sidebar_state='expanded',
    )

# Load the image
#image = st.image("/Users/sheilakoo/Desktop/GA - Data Science Immersive/Capstone/images/page_title.png")
st.markdown("""
    <h1 style='text-align: center; font-size: 70px;'>RIDE RIDE REVOLUTION</h1>
""", unsafe_allow_html=True)

### --- TOP NAVIGATION BAR --- ###
selected = option_menu(
    menu_title = None,
    options = ['About', 'Instructions', 'Play'],
    icons = ['eject', 'stop', 'play'],
    menu_icon = '🚲',
    default_index = 0,
    orientation = 'horizontal',
    styles={
        'nav-link-selected': {'background-color': '#02ffff'},
        }
)

### --- ABOUT --- ###
if selected == 'About':
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Ride Ride Revolution')
        st.markdown("<p style='text-align: justify;'>Welcome to Ride Ride Revolution, the thrilling spin experience designed to bring the joy of indoor cycling to everyone. Whether you're a seasoned spin enthusiast or a complete beginner, this game is your passport to a world of fun, fitness, and rhythm. Let's dive into what makes Ride Ride Revolution a game-changer in the world of indoor cycling.</p>", unsafe_allow_html=True)
        st.markdown("")
        st.subheader('Why Spin?')
        st.markdown("""
                    <p style='text-align: justify;'>Indoor cycling, often referred to as "spin" is a dynamic and invigorating way to get fit. This low-impact exercise offers numerous benefits for your body and mind:
                    <u1>
                    <li>Cardiovascular Health: Spin is a fantastic way to boost your heart health, improve circulation, and enhance your endurance.</li>
                    <li>Weight Management: Burn calories and shed those extra pounds in a fun and engaging way.</li>
                    <li>Stress Relief: Unplug from the daily grind, enjoy the music, and feel the stress melt away as you ride.</li>
                    </u1>
                    </p>
    """, unsafe_allow_html=True)
        st.markdown("")
        st.subheader('Why Ride Ride Revolution?')
        st.markdown("""
                    <p style='text-align: justify;'>Ride Ride Revolution is a game that combines the fun of indoor cycling with the excitement of a video game. The game is simple: pedal to the beat and avoid obstacles to score points. The more you play, the more you'll want to play. Here's why:
                    <u1>
                    <li> Fun While Exercising: The game is designed to be fun and engaging, with a variety of different levels and music to keep you entertained.</li>
                    <li> Learn At Your Own Pace: New to spin? We got your back. With Ride Ride Revolution, you can spin at your own pace and gradually build your confidence.</li>
                    <li> Real-Time Feedback: Get instant feedback on your choreography and rhythm. "Ride Ride Revolution" is like having a personal spin instructor guiding you.</li>
                    </u1>
                    </p>               
    """, unsafe_allow_html=True)
        st.markdown("")
        st.subheader('Have Fun!')
        st.markdown("""
                    <p style='text-align: justify;'>We believe that everyone can enjoy the benefits of spin in a supportive and friendly environment. Our mission is to empower you, boost your confidence, and encourage you to embrace a healthier lifestyle.
                    With "Ride Ride Revolution," you're always in control and there's no limit to what you can achieve on your spin bike. Let's revolutionize your ride!</p>
                    """, unsafe_allow_html=True)
    with col2:
        # Set size of the video
        _, container, _ = st.columns([8, 12, 8])
        container.video(data="/Users/sheilakoo/Desktop/GA - Data Science Immersive/Capstone/videos/physical.mp4")

### --- INSTRUCTIONS --- ###
if selected == 'Instructions':
    st.write("hello")

### --- PLAY --- ###
if selected == 'Play':
    #cap = cv2.VideoCapture('videos/iwitw.mp4')
    cap = cv2.VideoCapture(0)

    frame_placehoder = st.empty()
    
    stop_button_pressed = st.button("Stop")

    while cap.isOpened() and not stop_button_pressed:

        ret, frame = cap.read()

        if not ret:
            st.write("this video capture has ended")
            break


        # press q key to terminate webcam capture mode
        #if cv2.waitKey(10) & 0xFF == ord('q'):
        #    break

#cap.release()
#cv2.destroyAllWindows()
#cv2.waitKey(1)
#cap.release()
