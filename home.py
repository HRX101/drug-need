import streamlit as st 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
import pickle as pc
st.set_page_config(page_title='Drug Need', layout = 'wide', page_icon = 'logo.png', initial_sidebar_state = 'auto')
st.title("Welcome to drug needer")
st.write("Enter your following details")
age=st.text_input("Enter your Age")
if age!="":
    age=int(age)
sex = st.selectbox(
    'Choose your Gender',
    ('Male','Female'))
if sex=='Male':
    sex=1
else:
    sex=0
bp = st.radio('How your BP?', ["High", "Normal", "Low"])
if bp=="High":
    bp=2 
elif bp=="Normal":
    bp=1 
else:
    bp=0 
ch=st.radio("Cholesterol level",["High","Normal"])
if ch=="High":
    ch=1 
else:
    ch=0 
    
np1=st.text_input("Enter sodium level[ex: 42.012]")
if np1!="":
    np1=float(np1)
Button=st.button("submit")

with open('logistic.pkl', 'rb') as file:
      
    # Call load method to deserialze
    model= pc.load(file)
scaler = pc.load(open('lb.pkl', 'rb'))
if Button and np!="" and age!="":
    features=np.array([age,sex,bp,ch,np1])
    features=features.reshape(1,features.shape[0])
    print(features)
    st.write("You need this "+scaler.inverse_transform(model.predict(features)))
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .main {background-color: #f8f9d2;
            background-color: #f8f9d2;
background-image: linear-gradient(315deg, #f8f9d2 0%, #e8dbfc 74%);

            
            
            }
            h1{color:black;}
            p{color:black;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


