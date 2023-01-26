import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from PIL import ImageGrab, Image
import cv2
import io
import numpy as np
import pytesseract
from gtts import gTTS
import playsound

#INPUT LIBRARIES
import pyautogui
import tkinter
import keyboard
import time
import speech_recognition as sr
#from pocketsphinx import LiveSpeech
import sounddevice as sd
import wavio
from scipy.io.wavfile import write
import soundfile


def touch_place():
 screen.blit(bg,(0,0))
 pygame.display.update()
 for event in pygame.event.get():
  if event.type ==pygame.MOUSEBUTTONDOWN:
   xi,yi=pygame.mouse.get_pos()
   input_location.append([xi,yi])

#mouse area detection for the text
def area():
 running=True
 while running:
  screen.blit(bg,(0,0))
  pygame.display.update()
  for event in pygame.event.get():
   if event.type ==pygame.MOUSEBUTTONDOWN:
    xb,yb=pygame.mouse.get_pos()
    beginning_pos.append([xb,yb])
   if event.type == pygame.MOUSEBUTTONUP:
    xe,ye=pygame.mouse.get_pos()
    final_pos.append([xe,ye])
    running = False

def text_function():
 print(beginning_pos,final_pos)
 #location info for image to text conversion

 xb,yb=(np.array(beginning_pos[0])*n)[0],(np.array(beginning_pos[0])*n)[1]
 xe,ye=(np.array(final_pos[0])*n)[0],(np.array(final_pos[0])*n)[1]

 print(xb,yb,xe,ye)
 #image to use for text conversion
 
 img_for_text = screenshot.crop((xb, yb,xe, ye))
 #generated text
 text = pytesseract.image_to_string(img_for_text, lang="eng")
 print(text)
 return text

#audio from the text
def sound_function():
 audio=gTTS(text=text_function(),lang="en",slow=False)
 audio.save("audio.mp3")
 #playing the audio
 playsound.playsound("audio.mp3",True)


def record_function():
 #voice recording
 record=sd.rec(int(duration*fps),samplerate=fps,channels=2)
 sd.wait()
 write("voice.wav",fps,record)
 #analyze the voice
 data, samplerate = soundfile.read('voice.wav')
 soundfile.write('new.wav', data, samplerate, subtype='PCM_16')


def speech_recognize():
 rec=sr.Recognizer()
 #generate the text
 with sr.AudioFile("new.wav") as source:
  audio=rec.record(source)
  time.sleep(1)
  text=rec.recognize_google(audio)
  #input_text.append(text)
  return text

#input location of the text
def touch_function():
 loc=np.array(input_location[0])
 pyautogui.click(loc[0]*n,loc[1]*n)
 #type the text
 pyautogui.typewrite(speech_recognize())
 #PRESS ENTER AND SEND
 pyautogui.press("enter")


#pygame initialization
pygame.init()

fps=44100
duration=5 #maybe more
n=2 #image resizing factor
#position info collect


try:
 while True:
  input_text=[]
  input_location=[]

  beginning_pos=[]
  final_pos=[]

 #take screenshot
  time.sleep(10) #change that from terminal also add to the gui
  screenshot=ImageGrab.grab()
  pic=screenshot.size

  #resize image
  img = screenshot.resize((pic[0]//n,pic[1]//n), Image.Resampling.LANCZOS)
  #save the image
  img.save("image.png", 'PNG') 

  #pygame screen, same size with the cropped image
  screen=pygame.display.set_mode((pic[0]//n,pic[1]//n))

  #show as a background image
  bg = pygame.image.load("./image.png")

  #AREA
  area()
  #beginning_pos,final_pos=area()
  
  #printing actual mouse locations 
  #print("actual beginning",np.array(beginning_pos[0])*n,"and end",np.array(final_pos[0])*n)

  #AI SOUND
  sound_function()

  #RECORD
  record_function()

  #SPEECH RECOGNITION
  speech_recognize()

  #TOUCH PLACE
  touch_place()

  #TOUCH 
  touch_function()
except KeyboardInterrupt:
 print("KEY PRESSED QUITTING")



