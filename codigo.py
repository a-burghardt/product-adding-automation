import pyautogui
import time


#pyautogui.click
#pyautogui.write
#pyautogui.hotkey
#pyautogui.press


pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)

pyautogui.click(x=1876, y=364)
pyautogui.write("arthurb@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234567890")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

import pandas

table = pandas.read_csv("produtos.csv")
print(table)

for line in table.index:
    pyautogui.click(x=1880, y=249)

    codigo = table.loc[line, "codigo"]


    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "obs"]))

    obs = table.loc[line, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))


    pyautogui.press("tab")
    pyautogui.press("enter")