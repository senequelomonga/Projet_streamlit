import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
from PIL import Image
import re
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Streamlit project",
    #page_icon=smiley_logo,
    layout="wide",
    initial_sidebar_state="expanded",)
    
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
tab1, tab2, tab3 = st.tabs(["📈Insights","📝Glossaire","📃summary"])

with tab1:
    st.header("📈 Insight")
    col1, col2, col3, col4 = st.columns(4)
    col1.info("**Nombre d'employeurs**")
    col2.info("**Masse salariale nette**")
    col3.info("**Nombre total d'heures**")
    col4.info("**Age moyen d'employés**")
    col1.metric("Nombre d'employeurs", data["nombre_d_employeurs"].sum())
    col2.metric("Masse_salariale_nette", data["masse_salariale_nette"].sum())
    col3.metric(
        "Nombre total d'heures déclarées", round(data["nombre_d_heures_declarees"].sum(),2)
    )
    col4.metric("Average Age:", value = round(data["age_moyen_categ_x_dep"].mean(),2))
    

    
     ############ cleaning liste region
    region_liste = [
        elem for elem in data["region"].unique() if "_non classé ailleurs_" not in elem
        ]
    #################### fin list region
    #print(region_liste)

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
                
    # Afficher la carte par region 

    data['longitude'] = data['geo_point_2d'].str.split(',', expand=True)[0]
    data['latitude'] = data['geo_point_2d'].str.split(',', expand=True)[1]
    ##data['latitude'] = data['latitude'].astype(float)

    longitude = data[data["region"]==selection_region]["longitude"].values
    latitude = data[data["region"]==selection_region]["latitude"].values


    m = folium.Map(location=[longitude[0] , latitude[0]], zoom_start= 9)
    #folium.Marker(
    st_data = st_folium(m, width=725)
    
    #Nuage de points interactif
    st.subheader("Nuage de points")
    numeric_cols = data.select_dtypes(include=["float", "int"]).columns.tolist()


    with st.empty():
        var_x = st.selectbox("Choisissez la variable en abscisse", numeric_cols, key='var_x')

    with st.empty():
        var_y = st.selectbox("Choisissez la variable en ordonnée", numeric_cols, key='var_y')
    with st.empty():
        categorical_cols=data.select_dtypes(include=["float", "int"]).columns.tolist()
        var_col= st.selectbox("variable pour colorier les points",categorical_cols)
    # Créer le nuage de points
    fig0 = px.scatter(
        data_frame=data,
        x=var_x,
        y=var_y,
        color=var_col,
        title=f"{var_x} VS {var_y}"
    )

    # Afficher le nuage de points
    st.plotly_chart(fig0)



    # Créer le diagramme à barres interactif avec Plotly Express
    total = data['masse_salariale_nette'].sum()
    data['masse salariale'] = total

    # Créer l'histogramme interactif avec Plotly Express
    fig1 = px.histogram(
        data_frame=data,
        x='type_d_emploi',
        y='masse salariale',
        nbins=10,
        title="Repartition de la masse salariale par type d'emploi",
        labels={'type_d_emploi': 'type_d_emploi', 'masse salariale': 'masse salariale'},
        template='plotly_white'
    )

    # Afficher l'histogramme interactif avec Streamlit
    st.plotly_chart(fig1)



    # Calculer les pourcentages
    total = data['nombre_d_employeurs'].sum()
    data['pourcentage'] = (data['nombre_d_employeurs'] / total) * 100

    # Créer l'histogramme interactif avec Plotly Express
    fig2 = px.histogram(
        data_frame=data,
        x='type_d_emploi',
        y='pourcentage',
        nbins=10,
        title="Pourcentage d'employeur par type d'emploi",
        labels={'type_d_emploi': 'type_d_emploi', 'pourcentage': 'Pourcentage'},
        template='plotly_white'
    )







    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['nombre_d_heures_declarees', 'masse_salariale_nette'])

    st.line_chart(chart_data)
    

with tab2:
    st.header("📝 Glossaire")
    st.write("test")
    st.info(
            """
            Données sur les particuliers employeurs en 2018 issues des dispositifs Cesu et Pajemploi.
            Année 2018.

            Source : Acoss-Urssaf, CnCesu, Centre Pajemploi

            Les données sont ventilées par catégorie d'emploi (type d'emploi x dispositif déclaratif) :
            
            1. **CESU_HGED :** Hors garde d'enfant - CESU). 
            2. **PAJE_GED** Garde d'enfant à domicile - PAJE.
            3. **PAJE_AM** Assistantes maternelles - PAJE.
            """,
        )

with tab3:
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

    txt = st.text_area('Traitement du Dataset', '''Lors du traitement d'un dataset contenant des valeurs manquantes, il est important de suivre quelques étapes clés pour les gérer de manière appropriée. Voici un résumé des étapes courantes dans le traitement des valeurs manquantes dans un dataset :

    1. Identification des valeurs manquantes 
    2. Analyse de la nature des valeurs manquantes 
    3. Évaluation de l'impact des valeurs manquantes 
    4. Suppression des valeurs manquantes 
    5. Imputation des valeurs manquantes 
    6. Création d'indicateurs de valeurs manquantes 
    7. Validation du dataset traité 
    Il convient de noter que le traitement des valeurs manquantes peut varier en fonction du contexte et des exigences spécifiques du projet. Il est essentiel d'adapter ces étapes en fonction de votre propre dataset et de l'objectif de votre analyse ou modèle.
    ''')
    st.write('Dataset:', (txt))
 

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
       
       # Lien Linkedin 
        lien = "https://www.linkedin.com/in/s%C3%A9n%C3%A8que-lomonga-146448a2/"  
        
        st.sidebar.markdown(
    f"""
    <p style='text-align: center;'><a href="{lien}" target="_blank">🚹Mon profil Linkedin</a></p>
    """,
    unsafe_allow_html=True
        )
        
        # Lien Github
        lien = "https://github.com/senequelomonga"  
        
        st.sidebar.markdown(
    f"""
    <p style='text-align: center;'><a href="{lien}" target="_blank">🚹Mon profil Github</a></p>
    """,
    unsafe_allow_html=True
        )

        st.info(
            "Données sur les particuliers employeurs en 2020 issues des dispositifs Cesu, Pajemploi et DNS.Année 2020."
        )
        st.markdown("""---""")
        cover_image = Image.open("3286556.jpg")
        st.sidebar.image(cover_image, use_column_width=True)

##faire black à la fin du projet


########Diagramme à barres interactif
#fig = px.bar(
#   data_frame=data, y=data["code_categorie_d_emploi"].unique(),
#   x="masse_salariale_nette", title="Évolution de la masse salariale par catégorie d'emplois"
#)
#st.plotly_chart(fig)





