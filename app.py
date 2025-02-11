import streamlit as st # type: ignore

st.set_page_config(page_title="Eyad Nation", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi, I am Eyad :wave:")
    st.title("An Electronics Engineer in the making")
    st.write("I am passionate about money")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I want????")
        st.write("##")
        st.write(
            """
            My biggest desires in life include:
            - 2018 Camaro ZL1 1LE Matte Black with Tiny Red Accents
            - US Green Card
            - Black Tabby Maine-Coon
            - Teacup Chihuahua


            """
        )

