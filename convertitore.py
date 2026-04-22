import streamlit as st

st.title("Convertitore test")
km = st.number_input("Inserisci i chilometri:")
miglia = km * 0.621371
st.write(f"{km} km sono equivalenti a {miglia:.2f} miglia.")
