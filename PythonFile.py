import JarvisAI
import re
import pprint
import random

jar_assis = JarvisAI.JarvisAssistant()



def t2s(text):
    jar_assis.text2speech(text)

s="Hello I am Jarvis. I am here to help you , Tell me ur Name:"
print(s)
t2s(s)
res_of_mic_input= jar_assis.mic_input()
name=res_of_mic_input.split(' ')[-1]
s=" Hey "+name+" How can i help you?"
print(s)
t2s(s)

while True:
    res_of_mic_input= jar_assis.mic_input()



    if re.search('weather|temperature', res_of_mic_input):
        city = res_of_mic_input.split(' ')[-1]
        weather_res = jar_assis.weather(city=city)
        print(weather_res)
        t2s(weather_res)
    

    if re.search('open', res_of_mic_input):
        domain = res_of_mic_input.split(' ')[-1]
        open_result = jar_assis.website_opener(domain)
        print(open_result)
    
    if re.search('launch', res_of_mic_input):
        dict_app = {
            'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            'teamviewer': 'C:\Program Files (x86)\TeamViewer\TeamViewer.exe',
            'vs code' : 'D:\Microsoft VS Code\Code.exe',
            'calculator' : 'C:\Windows\system32\calc.exe',
            'notepad' : 'C:\Windows\system32\notepad.exe',
        }

        app = res_of_mic_input.split(' ')[-1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            print('Application path not found')
        else:
            t2s('Launching: ' + app)
            jar_assis.launch_any_app(path_of_app=path)
    
    if re.search('news', res_of_mic_input):
        news_res = jar_assis.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me read first 2 of them")
        t2s(news_res[0])
        t2s(news_res[1])

    

    if re.search('date', res_of_mic_input):
        date = jar_assis.tell_me_date()
        print(date)
        print(t2s(date))

    if re.search('time', res_of_mic_input):
        time = jar_assis.tell_me_time()
        print(time)
        t2s(time)

    
    if re.search('hi|hello', res_of_mic_input):
        l=["Hi","Hello","Namaste","Namaskar"]
        sp=random.choice(l)+" "+name+" Tell me how can i help you?"
        print(sp)
        t2s(sp)

    if re.search('how are you', res_of_mic_input):
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print(f"I am {response}")
        t2s(f"I am {response}")

    if re.search('your name|who are you', res_of_mic_input):
        print("My name is Jarvis, I am your personal assistant")
        t2s("My name is Jarvis, I am your personal assistant")
    

    if re.search('tell me about|who is|what is', res_of_mic_input):
        topic = res_of_mic_input.split()
        wiki_res = jar_assis.tell_me(topic)
        print(wiki_res)
        t2s(wiki_res)

    if re.search('what can you do', res_of_mic_input):
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "tell me": "Example: 'tell me about India'",
            "weather": "Example: 'what weather/temperature in Mumbai?'",
            "news": "Example: 'news for today' ",
        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
        I can open websites for you, launch application and more. See the list of commands-"""
        print(ans)
        pprint.pprint(li_commands)
        t2s(ans)

    if re.search('bye', res_of_mic_input):
        exiting = jar_assis.shutdown()
