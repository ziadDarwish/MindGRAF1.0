import PySimpleGUI as sg
import pathlib
import wff as wff
from PIL import Image
sg.ChangeLookAndFeel('Dark') # change style

WIN_W = 90
WIN_H = 10

WIN_W2 = 90
WIN_H2 = 25

file = None

w = wff.wff()

menu_layout = [['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', 'Save As', '---', 'Exit']]]

layout = [[sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]
,[sg.Multiline(font=('Consolas', 12), size=(WIN_W2, WIN_H2), key='Console')]]

window = sg.Window('Mind-GRAF 1.0', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window['_BODY_'].expand(expand_x=True, expand_y=True)
window['Console'].expand(expand_x=True, expand_y=True)
def new_file():
    '''Reset body and info bar, and clear filename variable'''
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    file = None
    return file

def checkSyntax(cmd ,successMessage):
    try:
        print(cmd)
        t=w.prettyParse(cmd,"")
        window['Console'].update(value=successMessage)
        print("OK")
    except:
        window['Console'].update(value="SYNTAX ERROR. USE COMMAND 'help' FOR FURTHER HELP. OR TRY AGAIN")

 
i = 0

while True:
    event, values = window.read(timeout_key=1)
    print(event)
    if event in('Exit', None):
        break
    if event == 'Return:36':
        i=i+1
        if "showContexts" in values['_BODY_']:
            checkSyntax(values['_BODY_'],"SHOWING CONTEXT")
            
        if "setContext" in values['_BODY_']:
            checkSyntax(values['_BODY_'],"SETTING CONTEXT")
    
        if "removeContext" in values['_BODY_']:
            checkSyntax(values['_BODY_'],"REMOVING CONTEXT")

        if "addToContext" in values['_BODY_']:
            checkSyntax(values['_BODY_'],"ADDING CONTEXT")

        if "setContext" in values['_BODY_']:
            checkSyntax(values['_BODY_'],"SETTING CONTEXT")

        if "showHypothesis" in values['_BODY_']:
            checkSyntax(values['_BODY_'],"SHOWING HYPOTHESIS")
        
        # else:
        #     window['Console'].update(value="MIND-GRAF CANNOT RECOGNIZE YOUR INPUT!")
        
        
               

# def open_file():
#     '''Open file and update the infobar'''
#     filename = sg.popup_get_file('Open', no_window=True)
#     if filename:
#         file = pathlib.Path(filename)
#         window['_BODY_'].update(value=file.read_text())
#         window['_INFO_'].update(value=file.absolute())
#         return file

# def save_file(file):
#     '''Save file instantly if already open; otherwise use `save-as` popup'''
#     if file:
#         file.write_text(values.get('_BODY_'))
#     else:
#         save_file_as()

# def save_file_as():
#     '''Save new file or save existing file with another name'''
#     filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
#     if filename:
#         file = pathlib.Path(filename)
#         file.write_text(values.get('_BODY_'))
#         window['_INFO_'].update(value=file.absolute())
#         return file
