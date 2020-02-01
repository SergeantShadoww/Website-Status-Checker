import requests
import PySimpleGUI as sg

def win():
    global page
    try:

        sg.theme('DarkAmber')  

        layout = [  [sg.Text('Website Status Checker')],
                    [sg.Text('Enter website to check status off.'), sg.InputText()],
                    [sg.Button('Check'), sg.Button('Exit')] ]

        window = sg.Window('Window Title', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):   # if user closes window or clicks cancel
                break
            page = values[0]
            if not page.startswith('https://') or page.startswith('http://'):
                sg.Popup('Please enter website including http || https!')
            else: 
                print('Calling checker...')
                main()
    except Exception as e:
        print(e)

def main():
    try:
        ww = requests.get(page)
    except Exception as e:
        print(e)
        sg.Popup('\nWebsite is down or your request was blocked.')
    #Add more status codes if you want, these are just the codes I thought off.
    if ww.status_code == 404:
        x = "Page could not be found, 404."
    elif ww.status_code == 200:
        x = "Page was found, 200."
    elif ww.status_code == 503:
        x = "Service unavailbale, 503."
    else:
        x = ww.status_code
    sg.Popup("Result:",x)

    #Logging section.
    f = open('logs.txt', 'a')
    f.write(page+":"+" "+str(ww.status_code))
    f.close()

win()
