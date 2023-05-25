import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Charger les données
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/seneq/OneDrive/Documents/projet-écol/particuliers-employeurs-en-2020.csv", sep=";")
    return df

# Titre de l'application
st.title("Employeur particulier en 2020")

# Charger les données
data = load_data()

# Afficher les premières lignes des données
st.write(data.head())
st.subheader("Dataset")

# Onglets
tab1, tab2, tab3,tab4 = st.tabs(["📈Insight Employeurs", "📊Insight Employés", "📝Glossaire","📃summary"])

with tab1:
    st.header("📈 Insight Employeurs")
    col1, col2, col3 = st.columns(3)
    col1.info("**Nombre d'employeurs**")
    col2.info("**Masse salariale nette**")
    col3.info("**Nombre total d'heures**")
    col1.metric("Nombre d'employeurs", data["nombre_d_employeurs"].sum())
    col2.metric("Masse_salariale_nette", data["masse_salariale_nette"].sum())
    col3.metric(
        "Nombre total d'heures déclarées", data["nombre_d_heures_declarees"].sum()
    )
    
     ############ cleaning liste region
    region_liste = [
        elem for elem in data["region"].unique() if "_non classé ailleurs_" not in elem
        ]
    #################### fin list region
    print(region_liste)

    ###### prepa slect box
    selection_region = st.selectbox("Séléctionner votre region", region_liste)
    ############

    ######bouton valider region
    button = st.button("valider votre region")

    if button:
            if selection_region == "Normandie":

             st.metric(
                    "Nombre d'employeur en Normandie",
                    value=data[data["region"] == "Normandie"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Normandie']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Occitanie":
                st.metric(
                    "Nombre d'employeur en Occitanie",
                    value=data[data["region"] == "Occitanie"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Occitanie']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Bretagne":
                st.metric(
                    "Nombre d'employeur en Bretagne",
                    value=data[data["region"] == "Bretagne"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Bretagne']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Centre-Val de Loire":
                st.metric(
                    "Nombre d'employeur en Centre-Val de Loire",
                    value=data[data["region"] == "Centre-Val de Loire"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Centre-Val de Loire']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Nouvelle-Aquitaine":
                st.metric(
                    "Nombre d'employeur en Nouvelle-Aquitaine",
                    value=data[data["region"] == "Nouvelle-Aquitaine"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Nouvelle-Aquitaine']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Provence-Alpes-Côte d'Azur":
                st.metric(
                    "Nombre d'employeur en Provence-Alpes-Côte d'Azur",
                    value=data[data["region"] == "Provence-Alpes-Côte d'Azur"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Provence-Alpes-Côte dAzur']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Auvergne-Rhône-Alpes":
                st.metric(
                    "Nombre d'employeur en Auvergne-Rhône-Alpes",
                    value=data[data["region"] == "Auvergne-Rhône-Alpes"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Auvergne-Rhône-Alpes']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Bourgogne-Franche-Comté":
                st.metric(
                    "Nombre d'employeur en Bourgogne-Franche-Comté",
                    value=data[data["region"] == "Bourgogne-Franche-Comté"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Bourgogne-Franche-Comté']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Pays de la Loire":
                st.metric(
                    "Nombre d'employeur en Pays de la Loire",
                    value=data[data["region"] == "Pays de la Loire"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Pays de la Loire']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Grand Est":
                st.metric(
                    "Nombre d'employeur en Grand Est",
                    value=data[data["region"] == "Grand Est"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Grand Est']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Hauts-de-France":
                st.metric(
                    "Nombre d'employeur en Hauts-de-France",
                    value=data[data["region"] == "Hauts-de-France"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Hauts-de-France']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Île-de-France":
                st.metric(
                    "Nombre d'employeur en Île-de-France",
                    value=data[data["region"] == "Île-de-France"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Île-de-France']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Corse":
                st.metric(
                    "Nombre d'employeur en Corse",
                    value=data[data["region"] == "Corse"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Corse']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Martinique":
                st.metric(
                    "Nombre d'employeur en Martinique",
                    value=data[data["region"] == "Martinique"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Martinique']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Guyane":
                st.metric(
                    "Nombre d'employeur en Guyane",
                    value=data[data["region"] == "Guyane"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Guyane']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "La Réunion":
                st.metric(
                    "Nombre d'employeur en La Réunion",
                    value=data[data["region"] == "Corse"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Corse']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )
            elif selection_region == "Guadeloupe":
                st.metric(
                    "Nombre d'employeur en La Guadeloupe",
                    value=data[data["region"] == "Guadeloupe"]["nombre_d_employeurs"].sum(),
                    delta=f"{round(((data[data['region']=='Guadeloupe']['nombre_d_employeurs'].sum() - data['nombre_d_employeurs'].mean())/data['nombre_d_employeurs'].sum())*100,2)}",
                )    
        # elif selection_region == 'Normandie':
        #     st.write(data[data['region']=='Normandie']['nombre_d_employeurs'].sum())
        # elif selection_region == 'Normandie':
        #     st.write(data[data['region']=='Normandie']['nombre_d_employeurs'].sum())
            else:
                st.write("Pas de region sélectionnée")

with tab2:
    st.header("📊 Insight Employés")
    st.write("test")

with tab3:
    st.header("📝 Glossaire")
    st.write("test")

with tab4:
    st.header("📃 Summary")
    st.info(data)
    st.write("Nombre de colonnes :", data.shape[1])
    st.write("Nombre de lignes :", data.shape[0])

    # Analyse des valeurs manquantes
    fig, ax = plt.subplots()
    missing_values = data.isnull().sum().sum()
    not_missing_values = data.notnull().sum().sum()
    ax.pie([missing_values, not_missing_values], labels=["Valeurs manquantes", "Valeurs non manquantes"],
           autopct="%1.1f%%", colors=["lightblue", "steelblue"])
    ax.set_aspect("equal")
    st.pyplot(fig)

    st.warning(f"Nombre total de valeurs manquantes : {missing_values}")

 

# main function
with st.sidebar:
        col1, col2, col3 = st.columns(3)
        col2.image("Logo_psb_colored-removebg-preview.png", use_column_width=True)
        st.markdown("""---""")
        st.markdown(
            """
                        <h4 style='text-align: center; color: black;'> Sénèque LOMONGA </h4>
                        """,
            unsafe_allow_html=True,
        )
        st.info(
            "Données sur les particuliers employeurs en 2020 issues des dispositifs Cesu, Pajemploi et DNS.Année 2020."
        )
        st.markdown("""---""")
        cover_image = Image.open("3286556.jpg")
        st.sidebar.image(cover_image, use_column_width=True)

##faire black à la fin du projet


   