import PySimpleGUI as sg
import qrcode 
layout = [
    [sg.Input(key='data')],
    [sg.Button('GENERATE'),sg.Button('CLOSE')],
    [sg.Image(key='output')]

]
window = sg.Window('QRCODE',layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
       break
    elif event == 'GENERATE':
        qc = qrcode.make(values['data'])
        qc.save('qr_code.png')
        window['output'].update('qr_code.png')
window.close()



# a = qrcode.make('https://www.youtube.com/watch?v=41Nck7hRrEA&t=3s')
# a.save('qrcode.png')