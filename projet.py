"""
Dashboard Streamlit
"""
import pandas as pd
import streamlit as st
import numpy as np

#st.cache_data
def load():
    """
    This fu#nctions aimns to load data
    Returns:
        data as dataframe
    """
    df= pd.read_csv("C:/Users/seneq/OneDrive/Documents/projet-écol/particuliers-employeurs-en-2020.csv", sep=";")
    return df


from streamlit_image_comparison import image_comparison

#set page config
st.header("Image-Comparison Example")

# render image-comparison
image_comparison(
    img1="3286556.jpg",
    img2="7955.jpg",
)

st.title("Employeur particulier en 2020")
st.subheader("Sénèque LOMONGA")
data= load()
st.write(data.head())
st.write("Dataset") 


col10, col11, col12 = st.columns(3)
col10.metric("nombre_d_employeurs", "3255993")
col11.metric("masse_salariale_nette", "8174049289.95")
col12.metric("nombre total d'heures déclarées","1 504 003 185")

from PIL import Image

image = Image.open("Logo_psb_colored-removebg-preview.png")

col1, col2, col3 = st.columns(3)

st.sidebar.image(image)
st.sidebar.header("Sénèque LOMONGA")
st.sidebar.subheader("Business Intelligence")
st.sidebar.markdown("Données sur les particuliers employeurs en 2020 issues des dispositifs Cesu, Pajemploi et DNS.Année 2020.")
st.sidebar.title("Vous pouvez filtrer la donnée")
st.sidebar.radio("Choisir les types de données",["Employeur","Employé"])