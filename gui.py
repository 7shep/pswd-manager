import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.
file = open("Passwords.txt", "r")
pswd = file.readlines()
split = pswd[0] + pswd[1] + "\n"


layout = [[sg.Text('Enter the Software, Username and Password')],
            [sg.Text('Software       '), sg.InputText()],
            [sg.Text('Username     '), sg.InputText()],
            [sg.Text('Password      '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button("Passwords")]]

passwordLayout = [[sg.Text('Passwords.')],
                  [sg.Text(split)],
                  [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Password Manager', layout)
# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Ok':
        file = open("Passwords.txt", "a")
        file.write("Software: " + values[0] + ":|" + " Username: " + values[1] + ":|" + " Password: " + values[2] + "\n")
        # prints the software, username and password into a txt file.
        file.close()
    if event == "Passwords":
        print("Test")
        window = sg.Window('Passwords', passwordLayout)
window.close()
