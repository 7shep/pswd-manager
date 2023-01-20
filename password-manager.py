import PySimpleGUI as sg
import sqlite3

master_password = "0"

sg.theme('DarkPurple4')   # Add a touch of color

try:
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    # Create the passwords table if it doesn't already exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, software TEXT, username TEXT, password TEXT)""")
except sqlite3.Error as e:
    sg.popup("Error connecting to the database:", e)    
    exit()

try:
    cursor.execute("SELECT * FROM passwords")
    data = cursor.fetchall()
except sqlite3.Error as e:
    sg.popup("Error reading from the database:", e)
    exit()

# Create the passwords table if it doesn't already exist
cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, software TEXT, username TEXT, password TEXT)""")


data = [(x[0], x[1].strip("'"), x[2].strip("'"), x[3].strip("'")) for x in data]
partThree = '\n \n'.join(['Software: {}  Username: {}  Password: {}'.format(x[1],x[2],x[3]) for x in data])

# Layout for the starting screen
layout = [[sg.Text('Enter the Software, Username and Password', font=("Helvetica", 20))],
            [sg.Text('Software       ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14))],
            [sg.Text('Username     ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14))],
            [sg.Text('Password      ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14))],
            [sg.Button('Ok', button_color=("white", "green"), font=("Helvetica", 14)), 
             sg.Button('Cancel', button_color=("white", "red"), font=("Helvetica", 14)), 
             sg.Button("Passwords", button_color=("white", "blue"), font=("Helvetica", 14))]]

# Layout for the password screen
passwordLayout = [[sg.Text('Passwords:', font=("Helvetica", 20))],
                  [sg.Text(partThree, font=("Helvetica", 14))],
                  [sg.Button('Ok', button_color=("white", "green"), font=("Helvetica", 14)), 
                   sg.Button('Go Back', button_color=("white", "blue"), font=("Helvetica", 14))]]

# Layout for the password updated screen
pswdUpdate = [[sg.Text("Passwords Updated.", font=("Helvetica", 20))],
             [sg.Button('Go Back', button_color=("white", "blue"), font=("Helvetica", 14)), 
              sg.Button('Cancel', button_color=("white", "red"), font=("Helvetica", 14)), 
              sg.Button('Passwords', button_color=("white", "blue"), font=("Helvetica", 14))]]

master_layout = [[sg.Text('Enter the Master Password', font=("Helvetica", 20))],
            [sg.Text('Master Password       ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14), password_char='*')],
            [sg.Button('OK', button_color=("white", "green"), font=("Helvetica", 14))],
            [sg.Button('Cancel', button_color=("white", "red"), font=("Helvetica", 14))]
            ]
master_window = sg.Window('Master Password', master_layout)
event, values = master_window.read()
if event == 'OK':
    # Verify if the entered password is correct
    if values[0] != master_password:
        sg.popup('Incorrect Master Password')
        master_window.close()
        exit()
    else:
        master_window.close()
        # continue with the rest of the script

# Create the Window
window = sg.Window('Password Manager', layout)

try:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":   # if user closes window or clicks cancel
            break
        if event == 'Ok':
            cursor.execute("INSERT INTO passwords (software, username, password) VALUES (?, ?, ?)", (values[0], values[1], values[2]))
            conn.commit()
            window.Layout(pswdUpdate)  # Update the current window with the new layout
        if event == 'Go Back':
            window.close()
            layout = [[sg.Text('Enter the Software, Username and Password', font=("Helvetica", 20))],
            [sg.Text('Software       ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14))],
            [sg.Text('Username     ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14))],
            [sg.Text('Password      ', font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14))],
            [sg.Button('Ok', button_color=("white", "green"), font=("Helvetica", 14)), 
             sg.Button('Cancel', button_color=("white", "red"), font=("Helvetica", 14)), 
             sg.Button("Passwords", button_color=("white", "blue"), font=("Helvetica", 14))]]
            window = sg.Window('Password Manager', layout, default_element_size=(20, 1), auto_size_text=True, default_button_element_size=(14, 2))
        if event == 'Passwords':
            cursor.execute("SELECT * FROM passwords")
            data = cursor.fetchall()
            data = [(x[0], x[1].strip("'"), x[2].strip("'"), x[3].strip("'")) for x in data]
            partThree = '\n \n'.join(['Software: {}  Username: {}  Password: {}'.format(x[1],x[2],x[3]) for x in data])
            window = sg.Window('Passwords', [[sg.Text('Passwords:'),sg.Text(partThree)],
                      [sg.Button('Ok'), sg.Button('Go Back')]])
            if event == "Go Back":
                window.close()
                window = sg.Window('Password Manager', layout, default_element_size=(40, 1), auto_size_text=False, default_button_element_size=(8, 2))
except Exception as e:
    sg.popup("An error occurred: ", e)