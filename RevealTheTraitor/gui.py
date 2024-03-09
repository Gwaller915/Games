import PySimpleGUI as sg

# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("The King needs help! Some one in his court is plotting to assassinate him!", size=(80,6))], [sg.Button("OK")]]

# Create the window
window = sg.Window("Message from the King", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()