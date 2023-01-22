import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    to_do = st.session_state["new_todo"] + '\n'
    todos.append(to_do)
    functions.write_todos(todos)


st.title("This Is Todo App")
st.subheader("This app is intended to boost productivity in a mysterious way")
st.write("Type to add a new todo or check the checkboxes to complete todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="label", placeholder="Add a new todo...",
              label_visibility='collapsed',
              on_change=add_todo, key="new_todo")
