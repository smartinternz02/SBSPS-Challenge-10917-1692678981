import pickle as pk
import requests
import streamlit as st
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_chat import message as st_message

#css
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.json()

hide_st_style = """
                <style>
                #MainMenu { visibility : hidden;}
                footer { visibility : hidden;}
                header { visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style , unsafe_allow_html = True)


# use local css
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
Placement_Predict_Model = pk.load(open('C:/Users/J RISHI KRISHNA/study/vs/WS/streamlit/Diabetics prediction/savedmodels/model_saved.sav','rb'))

selected = option_menu(
        menu_title ="",
        options =["Placement"],
        icons = ["house"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal")

if selected == "Placement":
    with st.container():
        def add_bg_from_url():
            st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
            unsafe_allow_html=True)
        add_bg_from_url()
    st.title("Placement Prediction using ML&DL")
    col1, col2, col3, col4, col5, col6, col7, = st.columns(7)
    with col1:
        index = st.text_input('Serial no')
    with col1:
        gender = st.text_input('Gender')
    with col2:
        ssc_p = st.text_input('SSC_%')
    with col3:
        hsc_p = st.text_input('Inter_%')
    with col4:
        hsc_s = st.text_input('Specilaisation')
    with col4:
        degree_p = st.text_input('Degree %')
    with col5:
        degree_t = st.text_input('Degree Stream')
    with col5:
        workex = st.text_input('workex 0 or 1')
    with col6:
        etest_p = st.text_input('employee_test%')
    with col2:
        specialisation = st.text_input('specialization')
    with col3:
        mba_p = st.text_input('mba %')
    with col6:
        status = st.text_input('position')
    with col7:
        salary = st.text_input('estimatedsalary')
    with col7:
        gender = st.text_input("emptest%")


    placement_prediction = ''

    if st.button('status'):
        Placement_Prediction = Placement_Predict_Model.predict([[index, gender, ssc_p, hsc_p, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p, status, salary, gender]])

        if(Placement_Prediction[0] == 12):
            placement_prediction = 'Person is placed'
        else:
            placement_prediction = 'person is not placed'

    st.success(placement_prediction)

    st.write("-----")
    st.subheader("Note")
    st.write(" specialization 1= Arts,2=commerce,3=science,4=others")
    st.write("salary should be out of 10 , convert the estimated value out of 10")
    st.write("Position = 1 = placed , 0 = mot placed")
    



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                              
