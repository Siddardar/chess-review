import PySimpleGUI as psg

psg.theme('DarkAmber')
layout = [[(psg.Graph((870, 870), (0, 0), (870, 870), key='Graph'))]]
window = psg.Window('Car Dashboard', layout, finalize=True)
window['Graph'].draw_image(filename='./frame.png', location=(0, 870))
window['Graph'].draw_image(filename='./board.png', location=(35, 835))
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break

window.close()
