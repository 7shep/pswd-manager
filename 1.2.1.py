import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

#Opens Passwords.txt
f = open("Passwords.txt", "r")
# Reads all the lines in the file
data = f.readlines()
f.close()

# For the replacing text
rep = str(data)

# For replacing text, do it in parts so that it doesn't repeat the passwords 3x over.
partOne = rep.replace(']', '')
partTwo = partOne.replace('[', '')
partThree = partTwo.replace('n', '')

layout = [[sg.Text('Enter the Software, Username and Password')],
            [sg.Text('Software       '), sg.InputText()],
            [sg.Text('Username     '), sg.InputText()],
            [sg.Text('Password      '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button("Passwords")]]

passwordLayout = [[sg.Text('Passwords.')],
                  [sg.Text(partThree)],
                  [sg.Button('Ok'), sg.Button('Cancel')]]

pswdUpdate = [[sg.Text("Passwords Updated.")]]

# Create the Window
window = sg.Window('Password Manager', layout)
# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":   # if user closes window or clicks cancel
        break
    if event == 'Ok':
        file = open("Passwords.txt", "a")
        file.write("Software: " + values[0] + " Username: " + values[1] + " Password: " + values[2] + "\n")
        # prints the software, username and password into a txt file.
        file.close()
        window = sg.Window("Passwords Updated!", pswdUpdate)

    if event == "Passwords":
        window = sg.Window('Passwords', passwordLayout)
window.close()
