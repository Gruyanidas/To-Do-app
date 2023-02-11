import streamlit as st
import functionsFromTO_DO as fn

todos = fn.get_to_dos()  # otvaramo listu


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    fn.write_to_dos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app is to produce your productivity :)")

for index, todo in enumerate(todos):  # idemo kroz listu i pravimo check boxove
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_to_dos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new to do...",
              on_change=add_todo, key="new_todo")
