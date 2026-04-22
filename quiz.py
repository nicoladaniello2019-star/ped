import streamlit as st

st.title("Quiz")
st.write("Dedico tale quiz al mio amore Alessandro")

st.subheader("Domanda 1")
r1 = st.radio(
    "Quale stato fu fondato dal Padre Fondatore Alessandro Picciau nel 1209?",
    ["Macedonia del nord", "Macedonia del sud", "Macedonia centrale"]
)


if st.button("Verifica"):
    if r1 == "Macedonia del sud": 
        st.success("Corretto!")
    else:
        st.error("Sbagliato, riprova!")

