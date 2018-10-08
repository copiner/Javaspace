#GUI:Graphical User Interface
import easygui
#easygui.msgbox("hi")

#import easygui as gu
import sys
while 1:
    easygui.msgbox("welcome...")
    msg = "what do you like..."
    title = "interactive"
    choices = ['A','B','C','D']
    choice = easygui.choicebox(msg, title, choices)
    easygui.msgbox('you choice : ' + str(choice), 'ido')

    msg = "again"
    title = 'choice please'

    if easygui.ccbox(msg, title):
        pass
    else:
        sys.exit(0)

