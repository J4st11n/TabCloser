import time
import string
import pyautogui
import pywinauto
from pywinauto import Application
 
#inicializace řad
BrowserWindows     = []
ApplicationWindows = []

#hledání stringů
BrowserNameEdge    = "Microsoft​ Edge"
BrowserNameOpera   = "Opera"
BrowserNameBrave   = "Brave"
BrowserName		   = ["Brave", "Opera", "Microsoft Edge","Microsoft\u200b Edge"]

#hledání aktivních oken které jsou prohlížeči
for x in pyautogui.getAllWindows():
    if(x.title.find(BrowserName[0]) > 0):        
        BrowserWindows.append(str(x.title))
    if(x.title.find(BrowserName[1]) > 0):
        BrowserWindows.append(str(x.title))
    if(x.title.find(BrowserName[2]) > 0):        
        BrowserWindows.append(str(x.title))
    if(x.title.find(BrowserName[3]) > 0):        
        BrowserWindows.append(str(x.title))
    else:
        ApplicationWindows.append(x.title)


for browser in BrowserWindows:
    
    #hledání pouze opera prohlížečů
    if(((browser.find("Opera")>=1))):
        
        #BrowserTitle bude array která se bude doplňovat do app.connect
        BrowserTitle = browser
        app = Application(backend='uia')
        app.connect(title=BrowserTitle)
        app.top_window().maximize()

        #vypisování url
        element_name = "Adresové pole"
        dlg = app.top_window()
        dlg.click_input()
        #url = dlg.child_window(title=element_name, control_type="Edit").get_value()
        #print(url)
        #změna záložky pro vypsání více url
        wrapper_list = dlg.descendants(control_type="TabItem")

        with open('soubor1.txt', 'a', encoding='utf-8') as file:
            for wrapper in wrapper_list:
                urlSize = 0
                #print(wrapper.window_text())
                try:
                    url = dlg.child_window(title=element_name, control_type="Edit").get_value()
                    print(url)
                    try:
                        file.write(str(url) + '\n')
                    except:
                        file.write(str(url.encode('utf-8')) + '\n')
                    urlSize = len(url)
                except:
                    pass
                for xc in range(urlSize):
                    file.write("-")
                file.write('\n')
                file.write('\n')
                file.close()
                break
            pywinauto.keyboard.send_keys('^w')