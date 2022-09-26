import base64
import streamlit as st
import utils

class Home():

    def __init__(self, background, font):
        bg_ext = background.split('.')[-1]
        _, image_col, _ = st.columns([1, 1, 1])
        with image_col:
            st.image("assets/logo_text.png", width = 300)
        self.font = font
        st.markdown(
            f"""<style>
                        .reportview-container {{
                            background: url(data:image/{bg_ext};base64,{base64.b64encode(open(background, "rb").read()).decode()})
                            }}
                            background-position: center;
                            background-repeat: no-repeat;
                            background-size: cover;
                            }}
                        </style>""",
            unsafe_allow_html = True
        )
    def render_details(self):
        st.markdown(
            f"<h3 style='text-align: center; color:#00FF00;'>Simple Data Visualization tool developed using streamlit</h3>",
            unsafe_allow_html = True)
        st.markdown(
            f"<h4 style='text-align: center; color:#ff0000;'>{utils.description_text}</h4>",
            unsafe_allow_html = True)
        st.text("")
        _, video_cont, _ = st.columns([0.25, 1, 1])
        video_cont.markdown("""
        """, unsafe_allow_html = True)
        st.markdown(
            f"<h2 style='text-align: center; color:#00FF00;'> It Currently supported for csv files only.</h2>",
            unsafe_allow_html = True)
           
        st.markdown(
            f"<div align = 'center'><h3 style='text-align: center;'>Developed with ❤ by <a href = ''><i>Anupam Mohanty</i></a></h3></div>",
            unsafe_allow_html = True)


    def fire(self):
        self.render_details()

def app():
    app = Home("assets/cyan_bg.jpg", "#00FFFF")
    app.fire()
    