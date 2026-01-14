import streamlit as st

st.title("Добрый день!")

first_name = st.text_input("Set first name: ")
last_name = st.text_input("Set last name: ")

if first_name == "" and last_name == '':
    message = "Привет!"
else:
    message = f"Привет, {first_name} {last_name}"

st.write(message)

if "show_text" not in st.session_state:
    st.session_state.show_text = False

def show_handler():
    st.session_state.show_text = not st.session_state.show_text

st.button("**Кликни, чтобы получить текст!**", on_click=show_handler)

if st.session_state.show_text:
    st.write("Спрятанное сообщение")