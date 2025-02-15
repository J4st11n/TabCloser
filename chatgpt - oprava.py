import time
import pyautogui
import pywinauto
from pywinauto import Application

# Inicializace seznamů
BrowserWindows = []

# Hledání prohlížeče Opera
BrowserName = "Opera"
element_name = "Adresové pole"

# Funkce pro kontrolu, zda okno stále existuje
def is_window_open(window_title):
    for w in pyautogui.getAllWindows():
        if BrowserName in w.title:
            return True
    return False

# Najdi aktivní okna prohlížeče
for x in pyautogui.getAllWindows():
    if BrowserName in x.title:
        BrowserWindows.append(str(x.title))

for browser in BrowserWindows:
    # Připojení k oknu prohlížeče
    app = Application(backend='uia')
    app.connect(title=browser)
    dlg = app.top_window()
    
    with open('soubor1.txt', 'a', encoding='utf-8') as file:
        while is_window_open(browser):  # Dokud je okno stále otevřené
            try:
                url = dlg.child_window(title=element_name, control_type="Edit").get_value()
                if url:
                    print(url)
                    file.write(url + '\n')
                    file.write('-' * len(url) + '\n\n')
            except:
                pass
            
            file.flush()  # Ujisti se, že se data zapíší do souboru
            pywinauto.keyboard.send_keys('^w')  # Zavři aktuální záložku
            time.sleep(1)  # Malé zpoždění pro stabilitu
