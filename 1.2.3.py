import PySimpleGUI as sg 

sg.theme('DarkPurple4')   # Add a touch of color
# All the stuff inside your window.

#Opens Passwords.txt
f = open("Passwords.txt", "r")
# Reads all the lines in the file
data = f.readlines()
f.close()

# For the replacing text
rep = str(data)

# For replacing text, do it in parts so that it doesn't repeat the passwords 3x over.
#Replaces "]" with nothing
partOne = rep.replace(']', '')
#Replaces "[" with nothing
partTwo = partOne.replace('[', '')
#Replaces "|" with a new line
partThree = partTwo.replace("|", '\n \n')

#Layout for the starting screen
layout = [[sg.Text('Enter the Software, Username and Password')],
            [sg.Text('Software       '), sg.InputText()],
            [sg.Text('Username     '), sg.InputText()],
            [sg.Text('Password      '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button("Passwords")]]

#Layout for the password screen
passwordLayout = [[sg.Text('Passwords:')],
                  [sg.Text(partThree)],
                  [sg.Button('Ok'), sg.Button('Go Back')]]

#Layout for the password updated screen
pswdUpdate = [[sg.Text("Passwords Updated. (note: the most recent password wont show up until you restart the application)")],
             [sg.Button('Go Back'), sg.Button('Cancel')], [sg.Button('Passwords')]]

# Create the Window
window = sg.Window('Password Manager', layout)
# Event Loop to process "events" and get the "values" of the inputs

#:)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":   # if user closes window or clicks cancel
        break
    if event == 'Ok':
        file = open("Passwords.txt", "a")
        file.write("Software: " + values[0] + " Username: " + values[1] + " Password: " + values[2] + "|")
        # prints the software, username and password into a txt file.
        file.close()
        window = sg.Window("Passwords Updated!", pswdUpdate)

    if event == "Passwords":
        window = sg.Window('Passwords', passwordLayout)
        if event == "Go Back":
            break
window.close()