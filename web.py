import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a to-do item", 
              placeholder="Type a to-do", on_change=add_todo, 
              key="new_todo")