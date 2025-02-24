"""
Interface utilisateur Streamlit pour AutoCours, offrant une expérience type chatbot.
"""

import streamlit as st
from app.prompts.generate_course import generate_course

st.title("AutoCours - Chatbot")
st.write("Générez automatiquement un cours en discutant avec notre chatbot.")

subject = st.text_input("Entrez le sujet du cours", placeholder="Exemple : Machine Learning")
if st.button("Générer le cours"):
    if subject:
        st.info("Génération du cours en cours...")
        course = generate_course(subject)
        st.success("Cours généré !")
        st.header(course["title"])
        for module in course["modules"]:
            st.subheader(module["title"])
            st.write(module["content"])
    else:
        st.error("Veuillez entrer un sujet.")
