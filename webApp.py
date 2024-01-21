import streamlit as web  # module for webapp interface
import functions

todos = functions.get_todos('todos.txt')


def add_todo():

    todo = web.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos('todos.txt', todos)


web.title("My To-Do App")  # this generates the App with the given title
web.subheader("This a web interface ")
web.write("Salam, this is my WebApp. Alhamduli'lah!!")
# All these function in order on writing on web interface

for index, todo in enumerate(todos):
    checkbox = web.checkbox(todo, key=todo)  # .checkbox() generates check boxes
    if checkbox:
        todos.pop(index)
        functions.write_todos('todos.txt', todos)
        del web.session_state[todo]
        web.experimental_rerun()


web.text_input(label="", placeholder="Add new todo...",
               on_change=add_todo, key='new_todo')
