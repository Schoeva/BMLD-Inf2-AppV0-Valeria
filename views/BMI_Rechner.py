import streamlit as st
from functions.BMI_Rechner import bmi_rechner, bmi_kategorie

st.title("BMI Rechner")

with st.form("BMI_form"):
    gewicht = st.number_input("Geben Sie Ihr Gewicht in kg ein:")
    groesse = st.number_input("Geben Sie Ihre Körpergröße in m ein:")

    button = st.form_submit_button("Berechnen")

if button:
    bmi = bmi_rechner(gewicht, groesse)
    kategorie = bmi_kategorie(bmi)
    st.write(f"Ihr BMI ist: {bmi}")
    st.write(f"Kategorie: {kategorie}")
    st.balloons()

