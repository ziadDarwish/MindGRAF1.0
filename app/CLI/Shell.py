import PySimpleGUI as sg
import pathlib
import wff as wff

sg.ChangeLookAndFeel('Dark') # change style

WIN_W = 90
WIN_H = 10

WIN_W2 = 90
WIN_H2 = 25

file = None

w = wff.wff()

layout = [[sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]
,[sg.Multiline(font=('Consolas', 12), size=(WIN_W2, WIN_H2), key='Console')]]

window = sg.Window('Mind-GRAF 1.0', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window['_BODY_'].expand(expand_x=True, expand_y=True)
window['Console'].expand(expand_x=True, expand_y=True)


def checkSyntax(cmd ,successMessage):
    try:
        print(cmd)
        t=w.prettyParse(cmd,"")
        window['Console'].update(value=successMessage)
        print("OK")
    except:
        window['Console'].update(value="SYNTAX ERROR. USE COMMAND 'help' FOR FURTHER HELP. OR TRY AGAIN")


while True:
    event, values = window.read(timeout_key=1)
    print(event)
    
    if event in('Exit', None):
        break
    if event == '\r':
        try:
            tree = w.prettyParse(values['_BODY_'],"")
            
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

            if "?" in values['_BODY_']:
                window['Console'].update(value="Query")
            if "definenode" in tree:
                window['Console'].update(value="Drawing Node")
            if "removenode" in tree:
                window['Console'].update(value="Removing Node")
            if "definerelation" in tree:
                window['Console'].update(value="Relation Defined")
            if "saveprop" in tree:
                window['Console'].update(value="Proposition Saved")
            if "forward" in tree:
                window['Console'].update(value="Tracing Using Forward Chaining")
            if "backward" in tree:
                window['Console'].update(value="Tracing Using Backward Chaining")      
        except:
             window['Console'].update(value="SYNTAX ERROR. USE COMMAND 'help' FOR FURTHER HELP. OR TRY AGAIN")
                

        # else:
        #     window['Console'].update(value="MIND-GRAF CANNOT RECOGNIZE YOUR INPUT!")
        
  