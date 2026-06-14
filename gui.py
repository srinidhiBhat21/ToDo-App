import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

todos = functions.get_todos()

list_box = sg.Listbox(
    values=todos,
    key="todos",
    enable_events=True,
    size=[45, 10]
)

window = sg.Window(
    "My To-Do App",
    layout=[
        [label],
        [input_box, add_button],
        [list_box]
    ],
    font=("Helvetica", 20)
)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Add":
        todo = values["todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)

        window["todos"].update(values=todos)
        window["todo"].update(value="")

window.close()