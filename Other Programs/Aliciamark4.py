
print("Loading...")
import msvcrt,os,sys,time

try:
    import requests
    time.sleep(1)
except Exception as error_0:
    print(error_0)
    time.sleep(1)
    print('Installing requests')
    os.system('pip install requests')
    time.sleep(3)

try:
    import threading
    time.sleep(1)
except Exception as error_1:
    print(error_1)
    time.sleep(1)
    print('Installing threading')
    os.system('pip install threading')
    time.sleep(3)

try:
    import pyttsx3
    time.sleep(1)
except Exception as error_2:
    print(error_2)
    time.sleep(1)
    print('Installing pyttsx3')
    os.system('pip install pyttsx3')
    time.sleep(3)
   
try:
    import pyautogui
    time.sleep(1)
except Exception as error_3:
    print(error_3)
    time.sleep(1)
    print('Installing pyautogui')
    os.system('pip install pyautogui')
    time.sleep(3)
   

try:
    import openai
    time.sleep(1)
except Exception as error_5:
    print(error_5)
    time.sleep(1)
    print('Installing openai')
    os.system('pip install openai')
    time.sleep(3)
   
try:
    import webbrowser
except Exception as error_6:
    print(error_6)
    print('Installing webbrowser')
    os.system('pip install webbrowser')
    time.sleep(3)

try:
    import tkinter
except Exception as error_7:
    print(error_7)
    print('Installing tkinter')
    os.system('pip install tkinter')
    time.sleep(3)

import requests,threading
import pyttsx3,pyautogui
import openai,webbrowser
import tkinter as tk
from PIL import ImageTk, Image
   

engine = pyttsx3.init()

import datetime

from cmath import pi, sin
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
b=1
c=1
z=0
# variable x is for person identification
x=0
os.system('color B')

def thumbnail():
    os.system('cls')
    print('Connection Initiated')
    print('\n\n\n')
    print('                                          /$$$$$$\ \$$$$$$$$$$\                      /$$$$$$$$$$//                      ')
    time.sleep(0.02)
    print('                                         /$$$$$$$$\ \$$$$$$$$$$\                    /$$$$$$$$$$//                       ') 
    time.sleep(0.02)
    print('                                        /$$$$/\$$$$\       \$$$$\                  /$$$$//                              ')
    time.sleep(0.02)
    print('                                       /$$$$// \$$$$\       \$$$$\                /$$$$//                               ')
    time.sleep(0.02)
    print('         /~~~~~~~~~~~~~~~~~~~~~~~~~~~~/$$$$//~~~\$$$$\~~~~~~~\$$$$\~~~~~~~~~~~~~~/$$$$//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//')
    time.sleep(0.02)
    print('        /    //~~~~~~~~~~~~~~~~~~~~~~/$$$$//~~~~~\$$$$\~~~~~~~\$$$$\~~~~~~~~~~~~/$$$$//~~~~~~~~~~/ /~~~~~~~~~~~~~~~~~// ')
    time.sleep(0.02)
    print('       /    //                      /$$$$//       \$$$$\       \$$$$\          /$$$$//          / /                 //  ')
    time.sleep(0.02)
    print('      /    //       /--------------/$$$$//---------\$$$$\-------\$$$$\--------/$$$$//----------/ /                 //   ')
    time.sleep(0.02)
    print('     /    //       / /------------/$$$$//-----------\$$$$\-------\$$$$\------/$$$$//------------/                 //    ')
    time.sleep(0.02)
    print('    /    //       / /            /$$$$//             \$$$$\       \$$$$\    /$$$$//                              //     ')
    time.sleep(0.02)
    print('   /    ~~~~~~~~~/ /~~~~~~~~~~~~/$$$$//~~~~~~~~~~~~~~~\$$$$\~~~~~~~\$$$$\~~/$$$$//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//      ')
    time.sleep(0.02)
    print('  /    ~~~~~~~~~~~~~~~~~~~~~~~~/$$$$//~~~~~~~~~~~~~~~~~\$$$$\~~~~~~~\$$$$\/$$$$//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//       ')
    time.sleep(0.02)
    print(' /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$//                   \$$$$$$$$$$\ \$$$$$$$$//                                        ')
    time.sleep(0.02)
    print('/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$//                     \$$$$$$$$$$\ \$$$$$$//                                         ')
    time.sleep(0.02)
thumbnail()

print("\n\n\nHi this is alice, show your ID to openAI module\nType the ID for user Verification ")
engine.say("Type the ID for user Verification")
engine.runAndWait()
#Protocol Encryption 
def cypherx():
    global lock
    b_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
    list7=list(b_key)
    list5=[]
    t_key='3ELtb'
    list4=list(t_key)

    for j_key in range(0,len(list4)):
        list5.append(list7.index(str(list4[j_key])))
    lock=''
    
    for l_key in range(0,len(list4)):
        
        lock=str(lock)+list7[list5[l_key]-7]
cypherx()
a = ""
y=''
while True:
    char = msvcrt.getch()
    if char == b'\r': # Enter key
        os.system('exit')
    elif char == b'\x08': # Backspace key
        a = a[:-1]
        print("\b \b", end='', flush=True)
    else:
        if a==lock:
            
            break
        else:

            a += char.decode("utf-8")
            print('*', end='', flush=True)
            
        
if a==lock:
    for color_delay in range(1,7):
        color_delay2='color 0'+str(color_delay)    
        os.system(color_delay2)
        time.sleep(0.02)
    os.system('color B')

    


    
    while c<=4:
        c=c+1
        time.sleep(0.01)    
        while b<=4:
            print('Imprint Checking/',end='')
            print(b*'*')
            b=b+1
            time.sleep(0.1)
            os.system('cls')
    print('_'*26)
    time.sleep(0.05)
    print('User Verified, WELCOME TO \\')
    time.sleep(0.05)
    print('PROJECT ALICE VERSION-3.8  \\'+'_'*92)
    time.sleep(0.02)
    print('-'*120)
    engine.say("User verified..")
    engine.runAndWait()
    l=0
    time.sleep(0.02)
    print('Hi,i can help you to boost your learning and create your Notes and Research Papers as fast as Possible Type print to see')
    time.sleep(0.02)
    print('Type `index` for all commands/ Type `install` for installing libraries/ Type `extra` for extras/ type `close` to exit')
    os.system('color b')
    os.system('title Project Aliciamark3.8')
    while z==0:
        variable_x=1
        print('To update the program type `update` or `website`________________________________________________________________________')
        time.sleep(0.02)
        print('To clear the screen type `cls` & `print` to see/                                                                        ')
        print('```````````````````````````````````````````````                          ')
        time.sleep(0.02)
        print('                                                                                           ')
        time.sleep(0.02)
        print('                                                                                              ')
        time.sleep(0.02)
        empty_que=''
        empty_ans=''
        def autosave():
            f = open("aliciadata.txt", "a")
            for null_void in range(2):
                f.write('\n')

            f.write('Question:-   ')
            f.write(empty_que)

            for null_void1 in range(2):
                f.write('\n')
                time.sleep(0.01)
            f.write('Answers:-')

            for null_void2 in range(2):
                f.write('\n')
                time.sleep(0.01)
            f.write(empty_ans)
            f.write('\n')
            f.write('----------------------------------------------------------------------------------------------')


            f.close()
            time.sleep(0.1)
            
                        
        
        alice_ai='ask me something'
        print('Ask me anything\n')
        while True:
            try:
                time.sleep(0.05)
                com=str(input('\n\Listening...'))
                abhii_input=com
            except Exception as input_error:
                print(input_error)
                time.sleep(1)


            #abhii_input=str(input('\nListening...'))
            if abhii_input=='close':
                time.sleep(0.1)
                print('closing...')
                os.system('color F')
                time.sleep(1)
                os.system('cls')
                os.system('title Command Prompt')
                z=1
                break


            elif com=='cls':
                os.system('cls')
            elif com=='install' or com=='pip':
                print('Installing Requests Module')
                os.system("pip install requests")
                time.sleep(1)
                os.system("color B")
                print("\nInstalling Text to speech\n\n")
                time.sleep(1)
                os.system("pip install pyttsx3")
                time.sleep(1)
                print("\nInstalling pywhatkit Api module\n\n")
                time.sleep(1)
                os.system("pip install pywhatkit")
                os.system("color 04")
                time.sleep(1)
                print("done.")
                time.sleep(1)
                print("\nInstalling pyautogui\n\n")
                time.sleep(1)
                os.system("pip install pyautogui")
                os.system("color b")
                time.sleep(1)
                print("\nInstalling webbrowser api\n\n")
                time.sleep(1)
                os.system("pip install webbrowser")
                os.system("color F")
                print("\nInstalling openai\n\n")
                time.sleep(1)
                os.system("pip install openai")
                os.system("color b")
                time.sleep(1)
            


            elif com=='screenshot' or com=='snap' or com=='movie':
                taker=input("movie or snap = ")
                if taker=="movie":
                    os.system("md movie")
                    frames=int(input("Type the frames for record"))
                    abhiii=int(input("Type the time delay between each frames"))

                    for newfileabhii in range(1,frames+1):
                        myScreenshot = pyautogui.screenshot()
                        new1=str(newfileabhii)
                        myScreenshot.save('movie\\'+str(newfileabhii)+'.png')
                        time.sleep(abhiii)
                    print("all frames was taken")
                    

                elif taker=="snap":
                    os.system("md screenshot")
                    timing=int(input("Type timer for taking screenshot = "))
                    time.sleep(timing)
                    myScreenshot = pyautogui.screenshot()
                    time.sleep(1)
                    myScreenshot.save(r'screenshot\\screenshot.png')
                    print("Done!")
                    os.startfile(r'screenshot')
                else:
                    print("Syntax error!")
            





            
            elif com=='green':
                os.system('color a')
            elif com=='cyan' or com=='blue':
                os.system('color b')
            elif com=='red':
                os.system('color 04')
            elif com=='white':
                os.system('color F')
        


            elif com=='default':

                time.sleep(0.1)
                os.system('cls')
                os.system('color b')
                os.system('title Project Alice')
    
            elif com=='reset':
              
                time.sleep(0.1)
                os.system('cls')
                os.system('color b')
                os.system('title Project Alice')

            elif com=='home':
           
                time.sleep(0.1)
                os.system('cls')
                os.system('color b')
                os.system('title Project Alice')
                
            

            

            elif com=='':
                print('say something')
    
            elif com=='what is your name':
                print('thinking...\n')
                time.sleep(0.1)
                
                if x==0:
                    naam=input('i am Alice. What is your name? ')
                    print('Nice to meet you',naam)
                    engine.say("Nice to meet you"+naam)
                    engine.runAndWait()
                    x=1
                    l=1
                else: print('Already told.')
                engine.say("Already told.")
                engine.runAndWait()
        
                
            
        
            elif com=='open':
                web=input('just type the website name only')
                os.system('start chrome ' +web)
                time.sleep(0.1)
            
            elif com=='open dir':
                dir=input('type the command')
                os.system('dir')
                time.sleep(2)
            
            elif com=='show me ip':
                dir=input('type the command')
                os.system('ipconfig')
                time.sleep(0.1)
            
            




                
            elif com=='call':
                os.system('call')
                time.sleep(0.1)
        
            elif com=='cd':
                os.system('cd')
                time.sleep(0.1)
        
            elif com=='cls':
                os.system('cls')
                time.sleep(0.1)
            
            elif com=='color':
                os.system('color')
                time.sleep(0.1)
        
            elif com=='date':
                os.system('date')
                time.sleep(0.1)
        
            elif com=='dir':
                os.system('dir')
                time.sleep(0.1)
        
            elif com=='echo':
                os.system('echo')
                time.sleep(0.1)
            
            elif com=='exit':
                os.system('exit')
                time.sleep(0.1)
        
            elif com=='find':
                os.system('find')
                time.sleep(0.1)
            
            elif com=='hostname':
                os.system('hostname')
                time.sleep(0.1)
            
            elif com=='pause':
                os.system('pause')
                time.sleep(0.1)
        
            elif com=='runas':
                os.system('runas')
                time.sleep(0.1)
            
            elif com=='sort':
                os.system('sort')
                time.sleep(0.1)
            
            elif com=='start':
                os.system('start')
                time.sleep(0.1)
            
            elif com=='taskkill':
                os.system('taskkill')
                time.sleep(0.1)
            
            elif com=='tasklist':
                os.system('tasklist')
                time.sleep(0.1)
            
            elif com=='time':
                os.system('time')
                time.sleep(0.1)
            
            elif com=='timeout':
                os.system('timeout')
                time.sleep(0.1)
        
            elif com=='title':
                ox=input('type the title name = ')
                os.system('title '+ox)
                time.sleep(0.1)
        
            elif com=='ver':
                os.system('ver')
                time.sleep(0.1)
        
            elif com=='w32tm':
                os.system('w32tm')
                time.sleep(0.1)
        
            elif com=='ftp':
                os.system('ftp')
                time.sleep(0.1)
                
            elif com=='ftype':
                os.system('ftype')
                time.sleep(0.1)
                
            elif com=='getmac':
                os.system('getmac')
                time.sleep(0.1)
            
            elif com=='mac':
                os.system('getmac')
                time.sleep(0.1)
                
            elif com=='ip':
                os.system('ipconfig')
                time.sleep(0.1)
                
            elif com=='ipconfig':
                os.system('ipconfig')
                time.sleep(0.1)
            
            elif com=='netsh':
                os.system('netsh')
                time.sleep(0.1)
            
            elif com=='netstat':
                os.system('netstat')
                time.sleep(0.1)
            
            elif com=='netinfo':
                os.system('netstat')
                time.sleep(0.1)
        
            elif com=='nslookup':
                os.system('nslookup')
                time.sleep(0.1)
                
            elif com=='pathping':
                os.system('pathping')
                time.sleep(0.1)
            
            elif com=='ping':
                os.system('ping')
                time.sleep(0.1)
            
            elif com=='route':
                os.system('route')
                time.sleep(0.1)
            
            elif com=='route print':
                os.system('route print')
                time.sleep(0.1)
            
            elif com=='systeminfo':
                os.system('systeminfo')
                time.sleep(0.1)
            
            elif com=='info':
                os.system('systeminfo')
                time.sleep(0.1)
                
            elif com=='telnet':
                os.system('telnet')
                time.sleep(0.1)
                
            elif com=='tftp':
                os.system('tftp')
                time.sleep(0.1)
                
            elif com=='attrib':
                os.system('attrib')
                time.sleep(0.1)
            
            elif com=='comp':
                os.system('comp')
                time.sleep(0.1)
            
            elif com=='compact':
                os.system('compact')
                time.sleep(0.1)
            
            elif com=='copy':
                os.system('copy')
                time.sleep(0.1)
            
            elif com=='xcopy':
                os.system('xcopy')
                time.sleep(0.1)
                
            elif com=='diskcomp':
                os.system('diskcomp')
                time.sleep(0.1)
            
            elif com=='diskcopy':
                os.system('diskcopy')
                time.sleep(0.1)
                
            elif com=='erase':
                os.system('erase')
                time.sleep(0.1)
            
            elif com=='del':
                os.system('del')
                time.sleep(0.1)
                
            elif com=='expand':
                os.system('expand')
                time.sleep(0.1)
            
            elif com=='fc':
                os.system('fc')
                time.sleep(0.1)
            
            elif com=='mkdir':
                os.system('mkdir')
                time.sleep(0.1)
            
            elif com=='move':
                os.system('move')
                time.sleep(0.1)
                
            elif com=='rename':
                os.system('rename')
                time.sleep(0.1)
            
            elif com=='replace':
                os.system('replace')
                time.sleep(0.1)
            
            elif com=='rmdir':
                os.system('rmdir')
                time.sleep(0.1)
            
            elif com=='rd':
                os.system('rd')
                time.sleep(0.1)
                
            elif com=='tree':
                os.system('tree')
                time.sleep(0.1)
                
            elif com=='type':
                os.system('type')
                time.sleep(0.1)
                
            elif com=='chkdsk':
                os.system('chkdsk')
                time.sleep(0.1)
                
            elif com=='chkntfs':
                os.system('chkntfs')
                time.sleep(0.1)
            
            elif com=='defrag':
                os.system('defrag')
                time.sleep(0.1)
            
            elif com=='diskpart':
                os.system('diskpart')
                time.sleep(0.1)
            
            elif com=='driverquery':
                os.system('driverquery')
                time.sleep(0.1)
            
            elif com=='label':
                os.system('label')
                time.sleep(0.1)
                
            elif com=='mode':
                os.system('mode')
                time.sleep(0.1)
            
            elif com=='mountvol':
                os.system('mountvol')
                time.sleep(0.1)
                
            elif com=='verify':
                os.system('verify')
                time.sleep(0.1)
        
            elif com=='vol':
                os.system('')
                time.sleep(0.1)
                
            elif com=='for':
                os.system('for')
                time.sleep(0.1)
            
            elif com=='gpresult':
                os.system('gpresult')
                time.sleep(0.1)
                
            elif com=='gpupdate':
                os.system('gpupdate')
                time.sleep(0.1)
            
            elif com=='perfmon':
                os.system('perfmon')
                time.sleep(0.1)
            
            elif com=='invert':
                os.system('color 70')
            elif com=='task':
                os.system('start taskmgr')

                
            elif com=='location':
                print(os.getcwd())
                
                k=os.getcwd()
                folder_path = r"{}"
                n=folder_path.format(k)
                os.startfile(n)
                time.sleep(0.1)
                

            elif com=='extra':
                print("There are some extra simple codes added for just for testing purpose\n")
                print("pip\nadmin\nwhatsapp\nreverse\ngame\nsnap\nscreenshot\nmovie\ncolor name\ngcd\nupdate\nwebsite\nlocation\nloop\nloop1\nloop2")
            
            elif com=='update':
                print("Download the latest alice version from google drive.")
                url1= 'https://drive.google.com/drive/folders/1lLKMS8VdnzT6uMNfa8ipiCUILTvOod6-'
                webbrowser.open_new_tab(url1)
                
            elif com=='website':
                print("Opening website")
                url2= 'https://abhi639679.wixsite.com/abhishek'
                webbrowser.open_new_tab(url2)
            
            elif com=='search':
                while True:
                    b12=str(input('Search in google = '))
                    n12='yt'
                    if n12 in b12:
                        m12='https://www.youtube.com/results?search_query='+b12[3:]
                        webbrowser.open_new_tab(m12)
                    elif b12=='close':
                        break
                    else:
                        x12='https://www.google.com/search?q='+b12
                        
                        webbrowser.open_new_tab(x12)







            elif com=='prompt':
                os.system('prompt')
                time.sleep(0.1)
            
            elif com=='disco':
                #color changer program
                ana=0
                bela=0
                speeder=float(input("type the frequency of lights(in milliseconds) = "))
                os.system("color b")
                while True:
                    os.system("color "+str(bela))
                    bela=bela+1
                    time.sleep(speeder)
                    if bela==10:
                        bela=1
                        while ana>=1:
                            os.system("color "+str(bela))
                            bela=bela-1
                            time.sleep(speeder)
            

                time.sleep(0.1)
            
            
            elif com=='i am abhi':
                thumbnail()
                
            
            elif com=='loop2':
                r=1
                s=0
                c=r
                while True:


                    while s==0:
                        print('---',r/10,'-----      -----',r,'-----------------')
                        r=r*10
                        time.sleep(0.01)
                        if r==10000000000:
                            s=1 
                    while s==1:

                        print('---',r/10,'-----     ------',r,'-----------------')
                        r=r/10
                        time.sleep(0.01)
                        if r==1:
                            s=0
                

            elif com=='loop1':
                a=10
                b=20
                c=25

                while a<=40:
                    print(c*' ',end='')
                    print(a*'*')
                    a=a+2
                    b=b+1
                    c=c-1
                    time.sleep(0.01)

                    if a==40:
                        while a>=3:
                            print(c*' ',end='')
                            print(a*'*')
                            a=a-2
                            b=b-1
                            c=c+1
                            time.sleep(0.01)
            
            elif com=='loop':
                abhii=10
                k=1
                while k<=abhii:
                    for a in range(1,abhii):
                            k=k+2
                            print(" "*10,"HH"," "*10,"##"," "*10,"HH",end="")
                            print("-"*a,"*"*a,"*"*k)
                            time.sleep(0.02)
                            if a==abhii-1:
                                        for b in range(1,abhii):
                                            a=a-1
                                            k=k-2
                                            print(" "*10,"HH"," "*10,"  "," "*10,"HH",end="")
                                            print("A"*a,"*"*a,"*"*k)
                                            
                                            time.sleep(0.02)

            
            #wifi password finder
            elif com=='wifi':
                os.system('netsh wlan show profile')
                wifi=input('type the wifi name from user profiles.(case Sensitive)')
                print('Check key content in security settings = wifi password')
                time.sleep(3)
                os.system('netsh wlan show profile '+wifi+' key=clear')

                time.sleep(0.1)
            elif com=='cmd':
                os.system('start cmd')
            
            #main admin codes run in cmd
            
            
            
            elif com=='admin':
                os.system('cls')
                os.system('color B')
                #Administrator executables projects. exception and handling
                
                def administrator():

                    # Create the window
                    window = tk.Tk()

                    # Set the window title
                    window.title("Administrator")

                    # Set the window dimensions
                    window.geometry("640x360")
                    window.resizable(False, False)


                    # Create a label widget
                    text = tk.Label(window, text="Query For The Developer")
                    text.pack()

                    # Create a text box widget
                    textbox = tk.Text(window, height=0, width=80)
                    textbox.place(x=20,y=0)
                    textbox.configure(bg="white")

                    textbox.pack()

                    img = Image.open("D:\JEE IIT\Homepage.jpg")
                    img = img.resize((640, 360))

                    # Create a PhotoImage object from the image
                    photo = ImageTk.PhotoImage(img)

                    label = tk.Label(image=photo, width=640, height=360)
                    label.image = photo  # keep a reference to the image to prevent garbage collection

                    # Add the Label widget to the window
                    label.pack()
                


                    def open_link():
                        webbrowser.open("https://abhi639679.wixsite.com/abhishek")

                    # Create a Button widget
                    button1 = tk.Button(window, text="SEND", command=open_link)

                    # Set the position of the button
                    button1.place(x=570, y=320)
                    # Add the Button widget to the window


                    # Display the window
                    window.mainloop()
                

                                            





                def sender(abhii,verma):
                    #for Sending message to telegram bot
                    #start-----------------------------------------------------------------------
                    time.sleep(0.1)
                    k=str(input("Type the message for Client: "))
                    TOKEN = abhii
                    CHAT_ID = verma
                    MESSAGE = k

                    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                    data = {'chat_id': CHAT_ID, 'text': MESSAGE}
                    response = requests.post(url, data=data)
                    #print(response.json())
                    try:
                        print('Message Sent')
                        print('_'*80,'\n\n')
                        time.sleep(0.1)
                        #end--------------------------------------------------------------------------
                    except:
                        print('Message Not Sent')
                        print('Message Sent')
                        print('_'*80,'\n\n')
                        time.sleep(0.1)



                def reciever(abhi1,verma1):
                    time.sleep(0.1)
                    #for Recieving Messages requests from telegram bot
                    #start-------------------------------------------------------------------------------
                    TOKEN = abhi1
                    CHAT_ID = verma1
                    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
                    response = requests.get(url)
                    data = response.json()
                    if 'result' in data:
                        for result in data['result']:
                            
                            MESSAGE = result['message']
                            CHAT_ID = MESSAGE['chat']['id']
                            text = MESSAGE['text']
                            # do something with the message
                        try:
                            print('Last Message Recieved:',text)
                        except:
                            print('Not yet any message recieved')
                        print('_'*80,'\n\n')
                        time.sleep(0.5)
                    else:
                        print("No new updates")
                        time.sleep(0.5)
                    #end------------------------------------------------------------------------------------

                def ftp(src,abhi2,verma2):
                    time.sleep(0.1)
                    TOKEN = abhi2
                    CHAT_ID = verma2
                    #for sending File to telegram bot from computer
                    #start--------------------------------------------------------------------

                    #for Sending file to telegram bot
                    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
                    file_path = src
                    print('Sending file...')

                    with open(file_path, "rb") as f:
                        response = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})

                    #print(response.status_code)
                    try:
                        print("Your File is Sended to the developer\n\n")
                        print('_'*80,'\n\n')
                    except:
                        print('Your File Not Sended')
                        print('_'*80,'\n\n')

                    #end--------------------------------------------------------------------------
                rule_book1=''
                rule_book2=''
                #encryption protocol1
                b_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
                list7_key=list(b_key)
                list5_key=[]
                t_key='Zuwn9wMwZK6UUW2mvUTOtK.Ynl'
                list4_key=list(t_key)

                for j_key in range(0,len(list4_key)):
                    list5_key.append(list7_key.index(str(list4_key[j_key])))
                keygen=''
                #print("\n\nYour Decrypted word is = ",end="")
                for l_key in range(0,len(list4_key)):
                    keygen=keygen+str(list7_key[list5_key[l_key]-7])
                keygen2=keygen+'fqKMae0iTtq0Ib1--xzE'

                #encryption protocol2
                b_key1=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
                list7_key1=list(b_key1)
                list5_key1=[]
                t_key1='wSnuKSKfKK'
                list4_key1=list(t_key1)

                for j_key1 in range(0,len(list4_key1)):
                    list5_key1.append(list7_key1.index(str(list4_key1[j_key1])))
                keygen1=''
                #print("\n\nYour Decrypted word is = ",end="")
                for l_key1 in range(0,len(list4_key1)):
                    keygen1=keygen1+str(list7_key1[list5_key1[l_key1]-7])
                keygen3=keygen1

                print('This Section is for Developer\n')
                url3= 'https://t.me/V_Alice_bot'

                print('Type (send) to send message\nType (get) for get message\nType (ftp) for File Transfer\nType (open) for open bot domain ')
                

                while True:
                    
                    abhii=str(input("\nabhishek:\metaserver\Listening..."))

                    if abhii=='send':
                        sender(keygen2,keygen3)
                    elif abhii=='get':
                        reciever(keygen2,keygen3)
                    elif abhii=='ftp':
                        k=os.getcwd()
                        folder_path = r"{}"
                        n=folder_path.format(k)
                        os.startfile(n)
                        time.sleep(0.5)
                        src=str(input("Paste the file location here:"))
                        ftp(src,keygen2,keygen3)
                    elif abhii=='open':
                        webbrowser.open_new_tab(url3)
                        

                        print('\n')
                        my_thread = threading.Thread(target=administrator,args=())
                        my_thread.start()
                        

                    elif abhii=='close'or'exit':
                        os.system('cls')
                        os.system('color b')
                        os.system('color b')
                        break
                    else:
                        print("wrong input")
                        os.system('color b')


            
            elif com=='control panel':
                os.system('ncpa.cpl')
                time.sleep(0.1)
            
            elif com=='ncpa.cpl':
                os.system('ncpa.cpl')
                time.sleep(0.1)
                
            elif com=='network properties':
                os.system('ncpa.cpl')
                time.sleep(0.1)
            
            elif com=='adapter settings':
                os.system('ncpa.cpl')
                time.sleep(0.1)
            
            elif com=='network':
                os.system('wmic nic get name, index')
                time.sleep(0.1)
                
            elif com=='dns':
                os.system('nslookup')
                time.sleep(0.1)
            
            elif com=='dns lookup':
                os.system('nslookup')
                time.sleep(0.1)
                
            
            elif com=='tracert':
                ser=input('Type the dns IP etc 8.8.8.8 OR website name')
                os.system('tracert '+ser)
                time.sleep(0.1)
            
            elif com=='arp':
                os.system('arp')
                time.sleep(0.1)
            
            elif com=='arp -a':
                os.system('arp -a')
                time.sleep(0.1)
            
            elif com=='speak':
                engine.say(alice_ai)
                engine.runAndWait()
            elif com=='history' or com=='print':
                os.system('cls')
                os.system('color F')
                os.system('type aliciadata.txt')
                time.sleep(1)
                for a_text in range(30):
                    print('|')
                    time.sleep(0.02)
                os.system('color B')
                print('Scroll-Up ^')
                
                
                





            elif com=='shutdown':
                dir=input('yes/no')
                if dir=='yes':
                    os.system('shutdown/s')
                    print('shutting down the system')
                else: time.sleep(0.1)
            
            elif com=='index':
                pyautogui.press('f11')
                time.sleep(0.1)
                
                print('_'*26)
                time.sleep(0.03)
                print('DEVELOPER: ABHISHEK VERMA \\')
                time.sleep(0.03)
                print('PROJECT ALICE VERSION-3.6  \\'+'_'*128)
                time.sleep(0.03)
                print('````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
                time.sleep(0.01)
                print('attrib      = display file attributes',end='')

                time.sleep(0.01)
                print('                         pause       = pauses the execution of a batch file and shows a message')
                
                print('call        = calls a batch file from another one',end='')
                time.sleep(0.01)
                print('             pause       = pauses the execution of a batch file and shows a message')
                

                print('cd          = change directory',end='')
                time.sleep(0.01)
                print('                                runas       = start a program as another user')
                
                
                print('cls         = clear screen',end='')
                time.sleep(0.01)
                print('                                    rmdir / rd  = delete directory')
                

                print('cmd         = start command prompt',end='')
                time.sleep(0.01)
                print('                            replace     = replace files')
                

                print('copy/xcopy  = copy files',end='')
                time.sleep(0.01)
                print('                                      rename      = rename files')
                

                print('compact     = display/change file compression',end='')
                time.sleep(0.01)
                print('                 reg         = add/read/import/export registry entries')
            
                print('comp        = compare file contents',end='')
                time.sleep(0.01)
                print('                           route       = display network routing table, add static routes/type route print for print')
            

                print('chkntfs     = display/change volume check at startup',end='')
                time.sleep(0.01)
                print('          shutdown    = shutdown the computer')
                

                print('chkdsk      = check volumes',end='')
                time.sleep(0.01)
                print('                                   sort        = sort the screen output')
                

                            

                print('driverquery = display installed devices and their properties',end='')
                time.sleep(0.01)
                print('  systeminfo  = displays computer-specific properties and configurations')
                

                print('diskpart    = volume management',end='')
                time.sleep(0.01)
                print('                               tracert     = trace routes similar to patchping')
                

                print('defrag      = defragment media',end='')
                time.sleep(0.01)
                print('                                taskkill    = terminate a process or a application')
                

                print('diskcopy    = copy floppy disc to another one',end='')
                time.sleep(0.01)
                print('                 tasklist    = display applications and related task')
            

                print('diskcomp    = compare content of two floppy disks',end='')
                time.sleep(0.01)
                print('             time        = display/edit the system time')
                

                print('dir         = list directory content',end='')
                time.sleep(0.01)
                print('                          timeout     = wait any time')
            

                print('echo        = text output',end='')
                time.sleep(0.01)
                print('                                     title       = set title for prompt')
                

                print('expand      = extract files',end='')
                time.sleep(0.01)
                print('                                   type        = display content of text files')
                

                print('erase / del = delete one or more files',end='')
                time.sleep(0.01)
                print('                        tree        = display folder structure graphically')
                

                print('exit        = exits the command prompt or a batch file',end='')
                time.sleep(0.01)
                print('        tftp        = transfer files to a TFTP server')
                

                print('find        = find files',end='')
                time.sleep(0.01)
                print('                                      telnet      = establish Telnet connection')
                

                print('format      = format volumes',end='')
                time.sleep(0.01)
                print('                                  ver         = display operating system version')
                

                print('ftp         = transfer files to a FTP server',end='')
                time.sleep(0.01)
                print('                  verify      = monitoring whether volumes are written correctly')
                

                print('fc          = copare files and display the differences',end='')
                time.sleep(0.01)
                print('        vol         = show volume description and serial numbers of the HDDs')
                

                print('ftype       = display file type and mapping',end='')
                time.sleep(0.01)
                print('                   w32tm       = setting time synchronisation/time server/time zone')
                

                print('for         = for loop',end='')
                time.sleep(0.01)
                print('                                        move        = move/rename files')
            

                print('gpresult    = display group policies',end='')
                time.sleep(0.01)
                print('                          mkdir       = create a new directory')
            

                print('getmac      = display MAC address',end='')
                time.sleep(0.01)
                print('                             netsh       = configure/control/display network components')
                
                print('gpupdate    = update group policies',end='')
                time.sleep(0.01)
                print('                           netstat     = display TCP/IP connections and status')
                
                print('hostname    = display host name',end='')
                time.sleep(0.01)
                print('                               nslookup    = query the DNS')
                

                print('ipconfig    = display IP network settings',end='')
                time.sleep(0.01)
                print('                     pathping    = test the connection to a specific IP address')
            

                print('label       = change volume name',end='')
                time.sleep(0.01)
                print('                              ping        = pings the network')
            


                print('mountvol    = assign/delete drive mountpoints',end='')
                time.sleep(0.01)
                print('                 perfmon     = start performance monitor')
            

                print('mode        = configure interfaces/devices',end='')
                time.sleep(0.01)
                print('                    prompt      = change command prompt')
                
                print('ncpa.cpl    = To open adapter properties',end='')
                time.sleep(0.01)
                print('                      network     = show all network adapters')
                
                print('nslookup    = for Dns Lookup & server IP check',end='')
                time.sleep(0.01)
                print('                wifi        = for checking wifi passwords')

                print('tracert     = tracing the IP and Ping of website ',end='')
                time.sleep(0.01)
                print('             arp /arp -a = it will show you the table ARP Poisioning')
                print('_______________________________________________________________________________________________________________________')
            
                

            
                
            else:

                try:
                    
                
                    print('thinking...\n\n')
                    
                    

                    os.environ["OPENAI_API_KEY"] = "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"
                    openai.api_key = os.getenv("OPENAI_API_KEY")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt="Q:"+abhii_input+"\nA:",
                        temperature=1,
                        max_tokens=2000,
                        top_p=1,
                        frequency_penalty=0.0,
                        presence_penalty=0.0,
                        stop=["A:"]
                    )
                    alice_ai=response['choices'][0]['text']
                    empty_ans=alice_ai
                    empty_que=abhii_input


                    #print('\n\n',variable_x)

                    text_lines=alice_ai.splitlines()
                    os.system('color b')
                    
                    for variable1 in range(0,len(text_lines)):
                        print(text_lines[variable1])
                        time.sleep(0.02)
                    autosave()


                    #engine.say(alice_ai)
                    #engine.runAndWait()
                    print('\n_______________________________________________________________________________________________________________________')
                    print('                                                                                                     \REQUEST-ENDS-HERE\\')
                except:

                    os.system('color 04')
                    print('Connection distrupted due to data packets lost. check your internet connection and try again.')
                    time.sleep(0.1)
                    
                    
                
            
            
    
else: 
    os.system('color 04')
    os.system('cls') 
    if z==0:
        
        print('Unauthorised access!')
        engine.say(" Unauthorised access!")
        engine.runAndWait()
        
        
        time.sleep(1)
        os.system('cls')
        print('\nClosing the program')
        os.system('color F')
        os.system('exit')
        
    else:
        print('Closing the program')
        
        os.system('exit')


os.system('color 04')
time.sleep(0.05)
os.system('color F')
os.system('cls')
        