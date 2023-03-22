import openai

import speech_recognition as sr

import pyttsx3
engine = pyttsx3.init()

listener = sr.Recognizer()
openai.api_key ="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"

while True:
    
    with sr.Microphone() as source:
        print("speak now...")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        
        model = "text-davinci-003"
        
#        user = input("enter your question here:")
        
#        if "exit" in user:
        if "exit" in data:    
            break
    
        completion = openai.Completion.create(model= "text-davinci-003",
#          prompt = user,
          prompt = data,
          max_tokens = 1024,
          temperature = 0.5,
          n = 1,
          stop = None)
        response = completion.choices[0].text
        choice = int(input("PRESS '1' TO PRINT RESPONSE OR PRESS '2' TO LISTEN RESPONSE: "))
        
        if choice == 1:
            print(response)
        
        else:
            print(response)
            engine.say(response)
            engine.runAndWait()
            
        repeat = input("Do you want to ask more questions:")  
        if repeat in ["NO","no","No","nO"]:
            break