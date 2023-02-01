from colorama import init

init()
import os
import time
import keyboard
import pyautogui
import win32api
import win32con
import sys
import json
import psutil

os.system('mode con: cols=57 lines=30')
os.system('cls')
os.system('title Kendo Switcher')

toolbar_width = 20


def get_mouse_position():
    x, y = win32api.GetCursorPos()
    return x, y


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
           
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

if checkIfProcessRunning('javaw.exe'):
    print('Minecraft process found!')
    time.sleep(2)
    os.system('cls')
else:
    print('Minecraft process not found!')
    print('Please run Minecraft before running this script.')
    input('Press enter to exit...')
    exit()


# setup toolbar

logo = """\033[1;31m                      
     +--^----------,--------,-----,--------^-,
    | |||||||||   `--------'     |          O
    `+---------------------------^----------|
    `\_,---------,---------,--------------'
         / XXXXXX /'|       /' by \033[1;31m@jean
        / XXXXXX /  `\    /'
       / XXXXXX /`-------'
      / XXXXXX /
     / XXXXXX /
    (________(                
     `------'   \033[0m"""
print(logo)
sys.stdout.write("                 [%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) 

for i in range(toolbar_width):
    time.sleep(0.1) 
 
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")



os.system('cls')


def crear_cfgs():
 print('Ponte encima del slot del casco y presiona A')
 while True:
    if keyboard.is_pressed('a'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["casco_slot"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)

        break
# print('                   \033[1;37mEnter \033[1;31mmacro \033[1;37mkey: \033[0m', end="")

# macro_key = input()
 print('Ponte encima del slot de la pechera y presiona B')
 while True:
    if keyboard.is_pressed('b'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["pechera_slot"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break
 print('Ponte encima del slot de los pantalones y presiona C')
 while True:
    if keyboard.is_pressed('c'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["pantalones_slot"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break
 print('Ponte encima del slot de los zapatos y presiona D')
 while True:
    if keyboard.is_pressed('d'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["zapatos_slot"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break


 print('Ponte encima del casco puesto y presiona M')
 while True:
    if keyboard.is_pressed('m'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["casco_inv"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break
 print('Ponte encima de la pechera puesta y presiona F')
 while True:
    if keyboard.is_pressed('f'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["pechera_inv"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break
 print('Ponte encima de los pantalones puestos y presiona G')
 while True:
    if keyboard.is_pressed('g'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["pantalones_inv"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break
 print('Ponte encima de los zapatos puestos y presiona H')
 while True:
    if keyboard.is_pressed('h'):
        with open("cfg.json", "r") as f:
         data = json.load(f)
        data["zapatos_inv"] = get_mouse_position()
        with open("cfg.json", "w") as f:
         json.dump(data, f, indent=4)
        break
 os.system('cls')


logo = """\033[1;31m
     +--^----------,--------,-----,--------^-,
    | |||||||||   `--------'     |          O
    `+---------------------------^----------|
    `\_,---------,---------,--------------'
         / XXXXXX /'|       /' by \033[1;31m@jean
        / XXXXXX /  `\    /'
       / XXXXXX /`-------'
      / XXXXXX /
     / XXXXXX /
    (________(                
     `------' 

\033[1;31m                      kendo\033[1;37m.exe


                    \033[1;31m1. \033[1;37mMacro
                    \033[1;31m2. \033[1;37mCrear cfgs




"""

print(logo)
select = input("                    \033[1;31m> \033[1;37m")
if select == "2":
    crear_cfgs()
else:
    pass




print('                   \033[1;37mEnter \033[1;31mmacro \033[1;37mkey: \033[0m', end="")

macro_key = input()

os.system('cls')
print(logo)

print(f'                   \033[1;31mmacro \033[1;37mkey set to: \033[1;41m \033[1;37m{macro_key} \033[0m')
print('                   \033[1;31mMacro \033[1;37mStatus \033[1;42mOn')


def press_key(key):
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

def Macro():
   
    
    with open("cfg.json", "r") as f:
        data = json.load(f)
        global casco_slot
        casco_slot = data["casco_slot"]
        global pechera_slot
        pechera_slot = data["pechera_slot"]
        global pantalones_slot
        pantalones_slot = data["pantalones_slot"]
        global zapatos_slot
        zapatos_slot = data["zapatos_slot"]
        global casco_inv
        casco_inv = data["casco_inv"]
        global pechera_inv
        pechera_inv = data["pechera_inv"]
        global pantalones_inv
        pantalones_inv = data["pantalones_inv"]
        global zapatos_inv
        zapatos_inv = data["zapatos_inv"]
    

    pyautogui.hotkey('e')
    time.sleep(0.2)
    win32api.SetCursorPos((casco_slot))
    time.sleep(0.034)
    press_key(ord('1'))
    time.sleep(0.034)
    win32api.SetCursorPos((pechera_slot))
    time.sleep(0.034)
    press_key(ord('2'))
    time.sleep(0.034)
    win32api.SetCursorPos((pantalones_slot))
    time.sleep(0.034)
    press_key(ord('3'))
    time.sleep(0.034)
    win32api.SetCursorPos((zapatos_slot))
    time.sleep(0.034)
    press_key(ord('4'))
    time.sleep(0.034)

    win32api.SetCursorPos((casco_inv))
    time.sleep(0.034)
    press_key(ord('1'))
    time.sleep(0.034)
    win32api.SetCursorPos((pechera_inv))
    time.sleep(0.034)
    press_key(ord('2'))
    time.sleep(0.034)
    win32api.SetCursorPos((pantalones_inv))
    time.sleep(0.034)
    press_key(ord('3'))
    time.sleep(0.034)
    win32api.SetCursorPos((zapatos_inv))
    time.sleep(0.034)
    press_key(ord('4'))
    time.sleep(0.034)

    win32api.SetCursorPos((casco_slot))
    time.sleep(0.034)
    press_key(ord('1'))
    time.sleep(0.034)
    win32api.SetCursorPos((pechera_slot))
    time.sleep(0.034)
    press_key(ord('2'))
    time.sleep(0.034)
    win32api.SetCursorPos((pantalones_slot))
    time.sleep(0.034)
    press_key(ord('3'))
    time.sleep(0.034)
    win32api.SetCursorPos((zapatos_slot))
    time.sleep(0.034)
    press_key(ord('4'))
    time.sleep(0.034)
    pyautogui.hotkey('e')

def run_macro_on_keypress():
    while True:
        if keyboard.is_pressed(macro_key):
            Macro()
       

run_macro_on_keypress()