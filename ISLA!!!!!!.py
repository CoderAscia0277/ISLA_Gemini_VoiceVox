#!/usr/bin/env python
# coding: utf-8

# In[25]:


import google.generativeai as genai
import requests
import json
import pygame.mixer
import time
from io import BytesIO

class Gemini:
    apikey ="" genai.configure(api_key=apikey)
    def ISLA(prompt):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    
class voiceVox:  
    response = " "
    def __init__(self,text):
        self. url_head = "https://api.tts.quest/v3/voicevox/synthesis?"
            
        self.response = text
            
    def play(self):
        print("Calling play function")
        url_data = "error"
        response = requests.get(self.URL)
        if response.status_code == 200:
            print('Request success')
            data = json.loads(response.text)
            response_success = data["success"]
            if response_success: 
                url_data = data["mp3StreamingUrl"]
            else:
                print('Request Failed')
        return url_data
     
    def audio_start(self):
        print("Calling Audio Start Func")
        url_play = self.play()
        audio_data = requests.get(url_play)
        pygame.mixer.init()
       # DisplayText = True
        if audio_data.status_code == 200:
        # Load the MP3 data into Pygame mixer
            mp3_data = BytesIO(audio_data.content)
            pygame.mixer.music.load(mp3_data)
        # Play the loaded MP3 file
            print("Audio is about to run")
            time.sleep(1.25)
            pygame.mixer.music.play()
        # Keep the program running until the music finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    def convertTextToVoice(self):
        print("Calling Start function")
        speaker_num = 47
        self.URL = f"""https://api.tts.quest/v3/voicevox/synthesis?text={self.response}&speaker={speaker_num}"""
        self.audio_start()
        
    @classmethod
    def newInput(cls,text):
        return cls(text)


# In[38]:


text = input()
prompt = f"""query:{text}, no.tokens:35, response_language:Japanese"""
bot = Gemini.ISLA(prompt)
IslaBot = voiceVox.newInput(bot)
print(bot)
voiceVox.convertTextToVoice(IslaBot)


# In[ ]:




