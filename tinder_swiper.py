import speech_recognition as sr
import keyboard
import time
import pyautogui
import webbrowser
import PySimpleGUI as sg
import cv2
sg.theme('DarkAmber')   # Add a touch of color
url = 'https://tinder.com/app/recs'
webbrowser.open_new_tab(url)
cords_like,cords_more,cords_no = None,None,None
while(cords_like == None or cords_no == None or cords_more == None):
    cords_like = pyautogui.locateCenterOnScreen('like.png', confidence=0.8)
    cords_no = pyautogui.locateCenterOnScreen('dislike.png', confidence=0.8)
    cords_more = pyautogui.locateCenterOnScreen('info.png', confidence=0.8)
cords_more = (cords_more.x, cords_more.y - 300)
print('coords found')
r = sr.Recognizer()
# All the stuff inside your window.
layout = [  [sg.Image(size = (100,100),key = 'mic')],
            [sg.Text('Text:'), sg.Text(key = 'text')],
            [sg.Text('Result:')] ,
            [sg.Image(key = 'result')],
            [sg.Button('Ready')] ]

# Create the Window
window = sg.Window('Window Title', layout, size = (600,600), resizable = True, keep_on_top = True)
while True:
    event, values = window.read()
    if event == 'Ready': # if user closes window or clicks cancel
        window['Ready'].update(visible = False)
        break
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout = 100)
    if event == sg.WIN_CLOSED: # if user closes window
        break
    with sr.Microphone() as source:
        window['mic'].update('mic_on.png')
        window.read(timeout = 1)
        audio = r.listen(source, phrase_time_limit =  3)  
    window['mic'].update('mic_off.png')
    window.read(timeout = 1)
    try: 
        text = r.recognize_google(audio)
        window['text'].update(text)
        if ('left' in text.lower()):
            pyautogui.moveTo(cords_no)
            pyautogui.click(cords_no)
            window['result'].update('dislike.png')
        elif('right' in text.lower()):
            pyautogui.moveTo(cords_like)
            pyautogui.click(cords_like)
            window['result'].update('like.png')
        elif('more' in text.lower()): 
            pyautogui.moveTo(cords_more)
            pyautogui.click(cords_more)
    except sr.UnknownValueError:
        pyautogui.moveTo(cords_more)
        pyautogui.click(cords_more)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
window.close()
# obtain audio from the microphone

    