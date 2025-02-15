import time
import pyautogui
import pywinauto
import pygetwindow as gw
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from comtypes import COMError

# Název prohlížeče a prvku adresního řádku
BrowserName = "Opera"
element_name = "Adresové pole"

# Funkce pro kontrolu, zda je okno stále otevřené
def is_window_open():
    return any(BrowserName in w for w in gw.getAllTitles())  # Opraveno volání metody

# Najdi aktivní okno prohlížeče Opera
browser_window = None
for window in gw.getWindowsWithTitle(BrowserName):
    if BrowserName in window.title:
        browser_window = window
        break

# Pokud nebylo okno nalezeno, ukonči skript
if not browser_window:
    print("Okno prohlížeče Opera nebylo nalezeno.")
    exit()

# Kliknutí na okno prohlížeče (střed okna)
x, y, width, height = browser_window.left, browser_window.top, browser_window.width, browser_window.height
pyautogui.click(x + width // 2, y + height // 2)  # Kliknutí doprostřed okna
time.sleep(0.5)  # Počkej, než se okno zaměří

# Připojení k oknu prohlížeče
app = Application(backend='uia')
app.connect(title=browser_window.title)
dlg = app.top_window()

with open('soubor1.txt', 'a', encoding='utf-8') as file:
    while is_window_open():  # Dokud je okno otevřené
        try:
            url = dlg.child_window(title=element_name, control_type="Edit").get_value()
            if url:
                print(url)
                file.write(url + '\n')
                file.write('-' * len(url) + '\n\n')
        except (ElementNotFoundError, COMError) as e:
            print(f"Chyba při získávání URL: {e}")
            break

        file.flush()  # Ujisti se, že se data zapíší do souboru

        # Zavření aktuální záložky
        try:
            pyautogui.click(x + width - 50, y + 20)  # Kliknutí na zavírací tlačítko záložky
            time.sleep(1)  # Krátká pauza pro stabilitu
        except COMError as e:
            print(f"Chyba při zavírání záložky: {e}")
            pass  # Ignoruj chybu a pokračuj

    # Po zpracování všech záložek přidej závěrečnou zprávu
    file.write("Všechny záložky byly úspěšně uloženy a zavřeny.\n")
    print("Všechny záložky byly úspěšně uloženy a zavřeny.")