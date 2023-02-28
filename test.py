import PySimpleGUI as sg
from fentoboardimage import fenToImage, loadPiecesFolder
from PIL import Image

boardImage = fenToImage(
    fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    squarelength=100,
    pieceSet=loadPiecesFolder("./pieces"),
    darkColor="#D18B47",
    lightColor="#FFCE9E"
)


frame = Image.open("./frame.png")
frame.paste(boardImage, (35, 35))
im = frame.rotate(180)
img = frame.save("board.png", 'PNG')


sg.theme('DarkAmber')
layout = [
    [sg.Push(), sg.Text("Blah", justification='center'), sg.Push()],
    [sg.Image('./board.png', key="-BOARD-")]]


window = sg.Window('Game Review', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'End Analysis':
        break


window.close()
