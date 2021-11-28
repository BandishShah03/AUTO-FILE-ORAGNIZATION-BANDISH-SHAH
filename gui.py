import PySimpleGUI as f

f.theme('BlueMono')

layout = [[f.Text("")],[f.Text("Choose source folder: ", size = (20,1)),f.InputText(readonly = True), f.FolderBrowse()],[f.Text("Choose destination folder: ", size = (20,1)),f.InputText(readonly = True), f.FolderBrowse()], [f.Text("")],[f.Button("Submit", size = (8,1))]]

window = f.Window("Pyhton Project", layout, size = (600,200))

while True:
    event, v = window.read()

    if v[0] == '':
        print("Please enter a source path")
        continue

    if v[1] == '':
        print("Please enter a destination path")
        continue
    if event == f.WIN_CLOSED or event == "Exit":
        break

    elif event == "Submit":
        source = v[0]
        destination = v[1]
        break