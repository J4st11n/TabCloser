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
BrowserName		   = ["Opera", "Brave", "Microsoft Edge","Microsoft\u200b Edge"]

address_field_names = {
    "Microsoft Edge": "Adresní a vyhledávací řádek",
    "Brave": "Adresní a vyhledávací řádek",
    "Avast Browser": "Adresní řádek",
    "Opera GX": "Adresové pole",
    "Google Chrome": "Adresní a vyhledávací řádek",
    "Mozilla Firefox": "Adresní a vyhledávací řádek"
}

element_name = ["Adresové pole", "Adresní a vyhledávací řádek", "Adresní a vyhledávací řádek"]

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
        #element_name[0] = "Adresové pole"
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
                    url = dlg.child_window(title=element_name[0], control_type="Edit").get_value()
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
         
        