import time
import pyautogui
import pywinauto
from pywinauto import Application

# Inicializace seznamů
browser_windows = {}

# Seznam podporovaných prohlížečů
browsers = ["Opera", "Brave", "Microsoft Edge", "Google Chrome", "Mozilla Firefox"]
address_field_names = {
    "Microsoft Edge": "Adresní a vyhledávací řádek",
    "Brave": "Adresní a vyhledávací řádek",
    "Google Chrome": "Adresní a vyhledávací řádek",
    "Mozilla Firefox": "Adresní a vyhledávací řádek",
    "Opera": "Adresové pole",
}

# Získání otevřených oken prohlížečů
for window in pyautogui.getAllWindows():
    for browser in browsers:
        if browser in window.title:
            if browser not in browser_windows:
                browser_windows[browser] = []
            browser_windows[browser].append(window.title)



# Výpis do konzole a zápis do souboru
with open('soubor1.txt', 'w', encoding='utf-8') as file:
    for browser, windows in browser_windows.items():
        print(f"=== {browser} ===")
        file.write(f"=== {browser} ===\n")
        for win_title in windows:
            print(f"[{win_title}]")
            file.write(f"[{win_title}]\n")
            app = Application(backend='uia')
            try:
                app.connect(title=win_title)
                dlg = app.top_window()
                dlg.click_input()
                
                wrapper_list = dlg.descendants(control_type="TabItem")
                tab_urls = []
                for wrapper in wrapper_list:
                    try:
                        url = dlg.child_window(title=address_field_names[browser], control_type="Edit").get_value()
                        tab_urls.append(url)
                        print(url)
                    except:
                        pass
                    pywinauto.keyboard.send_keys('^w')  # Zavření záložky
                    time.sleep(0.5)
                
                for url in tab_urls:
                    file.write(url + '\n')
                if tab_urls:
                    file.write('-' * len(tab_urls[-1]) + '\n')
                
                # Zavření poslední záložky a celého okna
                dlg.close()
                time.sleep(1)
            except:
                print("(Nelze připojit k oknu)")
                file.write("(Nelze připojit k oknu)\n")
        print('\n')
        file.write('\n')
