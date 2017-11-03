# -*- coding: utf-8 -*-
#!/usr/bin/python3


# Program: Grim Banshee rev 1.0
# Language:  Python 2.7
# Author: import JJAG as Butch
# Email: unity_zero_unity@protonmail.com
# Date: October 8, 2017
# License:  ?

# Dependecies (example Fedora Linux)
# sudo dnf install tkinter
# sudo dnf install python-xlib
# sudo pip install --upgrade pip
# sudo pip install pyautogui
# sudo dnf install xsel
# sudo dnf install xclip
# sudo pip install pyperclip

# To start Grim_Banshee:
# change directory (cd) to Grim_Banshee file,
# then type "python Grim_Banshee.py" into terminal





import pyautogui
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
import os
import random
import time as timed_
import pyperclip



T = [[]]
Task = [[]]
message = [[]]
time = [[]]
conditional = ['always','always','always','always','always','always','always','always','always','always']

flag = 0
pos = (0,0)
Do_flag = True
annotate = ''

i = 0

keys = ['enter','esc','\\n','shift','alt','ctrl','tab','backspace','delete','pageup','pagedown','home','end','up','down','left','right','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','volumemute','volumedown','volumeup','pause','capslock','numlock','scrolllock','insert','printscreen','winleft','winright','command','a','A','b','B','c','C','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','`','~','1','!','2','@','3','#','4','$','5','%','6','^','7','&','8','*','9','(','0',')','-','_','=','+','[','{',']','}',"\\",'|',';',':',"'","\"",',','<','.','>','/','?']

specials = ['enter','esc','\\n','shift','alt','ctrl','tab','backspace','delete','pageup','pagedown','home','end','up','down','left','right','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','command','volumemute','volumedown','volumeup','pause','capslock','numlock','scrolllock','insert','printscreen','winleft','winright']

letters = ['a','A','b','B','c','C','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','`','~','1','!','2','@','3','#','4','$','5','%','6','^','7','&','8','*','9','(','0',')','-','_','=','+','[','{',']','}',"\\",'|',';',':',"'","\"",',','<','.','>','/','?']




def Clear():
    
    try:
        ring = int(clr.get())
        ring = ring -1
        count = 0
        for o in time[ring]:
            count += float(o)
        
        tmp = nice_time(str(float(run_var.get()) - float(count)))
        run_var.set(tmp)
        
        root.update_idletasks()
        T[ring] = []
        Task[ring] = []
        message[ring] = []
        time[ring] = []
        
    except:
        val = letter_check()
        #user musn't enter text into spinbox
        
       
        

def Clearall():
    
    global T, Task, message, time
    
    
    conditional = ['always','always','always','always','always','always','always','always','always','always']
    
    
    for p,o in enumerate(Task):
        for q,r in enumerate(o):
            if r == 'kd':
                pyautogui.keyUp(message[p][q])
    
    pos = pyautogui.position()
    pyautogui.mouseUp(pos[0],pos[1],button='left')
    pyautogui.mouseUp(pos[0],pos[1],button='right')
    
    T = [[]]
    Task = [[]]
    message = [[]]
    time = [[]]
    
    run_var.set("0.000")
    try:
        root.update_idletasks()
    except:
        pass
        #in case of program close in Train while loop
    

def Help():
    print("")
    print("Overview:")
    print("Grim Banshee automates a sequence of mouse and/or keyboard commands. It stores the sequences in 10 possible memory locations that you can toggle during training.  After or during training, if you click Do, Do All, or Repeat, the tasks trained so far will be automatically performed for you.  Your progress is automatically saved after every training.")
    print(" ")
    print("Advanced:")
    print("When the Do button is clicked, only the tasks in memory #X are done.  For the Do case, those tasks will be done 1 time.  For a repeated Do case (when reps is greater than 0), those tasks will be repeated  any number of times as set in the reps box.  The Do All button has more options.  The default case is when the random and rigid checkboxes are unchecked.  In the default case, tasks will be preformed starting in memory #1 until complete, and then tasks in memory #2 will be done, and so on.  Also, a text comparison conditionality can be configured to determine whether to proceed to the next memory.  If 'always' is selected, there is no condition; it always advances.  If 'same' is selected, then it advances only if the text in the two text boxes (top and bottom) are the same.  If 'diff' is selected, then it advances only if the text in the two text boxes are different.  If you click Do All when 'random' is check-marked, then the memories will be invoked in random memory order:  example:  2 could come before 1.  But all tasks within the memory are executed in order.  If a Do All 'rigid' case is done, then the tasks will be done in order of the saved settings in either your GB_save.txt file or your custom named file (in either case you have to Load or Load As them first).  That means all tasks will have a memory #1.  To accomplish this when training, you can use a tilda (~) command to switch memories.  Then do a tisk ` command to exit the second memory to return to training the first memory.  Do All can be repeated as similar to Do by increasing the number in the reps box.") 
    print("")
    
    print("Example basic process flow:")
    print("Step 1. After you click Train, click on the terminal and enter a command.")
    print("Step 2. If applicable, move the mouse to a screen location where the command is to be done.  Hint:  You can use Alt-Tab to focus back to the terminal.")
    print("Step 3. Press the Enter key (focus must be on terminal).")
    print("Step 4. That completes one command in the training sequence.")  
    print("Step 5+ Repeat as you like; make sure new commands are typed into the terminal.")
    print("Step next to last.  Press the ` key and Enter to stop training.")  
    print("Step last. Now click the Do button to run your command sequence.")
    
      
    print("")
    print("Buttons:")
    print("Clear = clear memory for training in memory #X.  Otherwise, new commands will be appended to end of existing training.")
    print("Clearall = clear all training memory and liberate all keyboard and mouse buttons")
    print("Train = store a sequence of key commands in memory #X")
    print("Do = execute sequence of key commands in memory #X")
    print("Do All = execute all memory sequences in order")
    print("Rand = apply random ordering to Do All process")  
    print("Rigid = when Load or Load As is clicked, the next Do All will perform the tasks in the order indicated in the loaded file as if all memories are 1.")
    print("#X = which memory to clear, train, or do.  Use menu (e.g. 1).")
    print("Save and Save As = saves a text file with all training.  Avoid using | in your 't' commands because that is delimiter. Progress is automatically saved to GB_Save.txt.")
    print("Load and Load As = loads a text file with training settings.")
    print("")
    print("For Do All, use top and bottom text boxes for text comparison as follows:")
    print("Always = always execute the next Training (e.g. 2 after 1.)")
    print("Diff = only execute the next training if two text boxes are different")
    print("Same = only execute the next training if two text boxes are same")
    print("")
    
    print("Key mappings for 'k', 'kd', 'ku', and 'hk' commands:")
    for o in specials:
        print(o + ", "),
    print("")
    print("")
    
    
    print("Rigid Training:")
    print("Utilize ~ and ` during training to toggle between memories as follows.")
    print("Step 1. Select a memory location by toggling the memory menu box (call this first).")
    print("Step 2. After you click Train, click on the terminal.")
    print("Step 2+ Enter commands into the first memory as you like.")
    print("Step 3. Select a new memory location with the training memory menu (call this second).")
    print("Step 4. Click on the terminal to bring it to focus.")
    print("Step 5. Type a ~ command and press Enter.  You may now enter commands to the second memory.")
    print("Step 6. When you are finished adding training commands to the second memory location, enter a ` command and press enter.")
    print("Step 7. This returns you to the first training, where you can continue training or exit with another ` command.")
    print("Tip:  During any training which requires that you wait for another application to process, you may want to use the ` command to exit out of training before starting that application.  This avoids Grim Banshee crashing.  In general, use ` or ~ before toggling new memory rings or time box.")
    
    print("")
    
    print("Command mapping:")
    print("L or l = left click")
    print("R or r = right click")
    print("D or d = double left click")
    print("b = delete previous command")
    print("h = hold left mouse button and drag mouse to position, then copy to OS clipboard.")
    print("c = highlight, copy, and save in top text box")
    print("v = paste from top text box to mouse position")
    print("cc = highlight, copy, and save in bottom text box")
    print("vv = paste from bottom text box to mouse position")
    print("su = scroll up")
    print("sd = scroll down")
    print("lhd = left click and hold down")
    print("lhu = left unclick")
    print("rhd = right click and hold down")
    print("rhu = right unclick")
    print("t = type in text (enter on next prompt)")
    print("k = press any single keyboard key")
    print("kd = press and hold single key")
    print("ku = lift up single key")
    print("hk = hotkey combination")
    print("` = done training in memory #X")
    print("~ = start a new training mode without needing to finish old one.  Change memory before pressing Enter.")
    print("Enter button = associate mouse position with key command preceding.")
    print("help = mini-help (just commands)")
    print("")


def Help_l():

    print("Key mapping:")
    print("L or l = left click")
    print("R or r = right click")
    print("D or d = double left click")
    print("b = delete previous command")
    print("w = wait the amount of time in the task time box (use this as a last resort -- instead use m or l with longer time.")
    print("h = highlight from previous mouse position and copy to OS clipboard")
    print("c = highlight, copy, and save in top text box")
    print("v = paste from top text box to mouse position")
    print("cc = highlight, copy, and save in bottom text box")
    print("vv = paste from bottom text box to mouse position")
    print("p = move to position and paste")
    print("m = move to position")
    print("su = scroll up")
    print("sd = scroll down")
    print("lhd = left click and hold down")
    print("lhu = left unclick")
    print("rhd = right click and hold down")
    print("rhu = right unclick")
    print("t = type in text (enter on next prompt)")
    print("k = press any single keyboard key")
    print("kd = press and hold single key")
    print("ku = lift up single key")
    print("hk = hotkey combination")
    print("` = done training in memory #X")
    print("~ = start a new training mode without needing to finish old one.  Change memory before pressing Enter.")
    print("Enter button = associate mouse position with key command preceding.")
    print("")


def nice_time(tmp):
    
    if len(tmp.split('.')) > 1:
        if len(tmp) == 3:
            tmp = tmp + '00'
        elif len(tmp) == 4:
            tmp = tmp + '0'
    
    return tmp


def letter_check():
    letter_fault = 0
    
    try:
        float(time_.get())
        float(clr.get())
        float(cascade.get())
        float(falss.get())
    except:
        letter_fault = 1
        
        clr.delete(0,"end")
        clr.insert(0,'1')
        
        cascade.delete(0,"end")
        cascade.insert(0,'1')
        
        falls.delete(0,"end")
        falls.insert(0,'1')
        
        time_.delete(0,"end")
        time_.insert(0,'0.250')
        print("Only enter numbers into spinboxes!")
    
    return letter_fault


def convert_for_lazy(msg):
    if msg == 'ctrl':
        msg = 'ctrlleft'
    elif msg == 'alt':
        msg = 'altleft'
    elif msg == 'shift':
        msg = 'shiftleft'
        
    return msg


def add_to(var):
    global flag, pos
    ring = int(cascade.get())
    ring = ring -1
    
    msg = ''
    
    if var == "t":
        let = 0
        while let == 0:
            try:
                print("Text: "),
                msg = raw_input()
                let = 1
            except:
                print("Invalid input.")
                let = 0
    
    elif var == "k" or var == 'ku' or var == 'kd':
        let = 0
        while let == 0:
            
            print("Key: "),
            msg = raw_input()
            if msg in keys:
                let = 1
            else:
                print("Invalid input. Type any regular key or one of these special keys:")
                for o in specials:
                    print(o + ", "),
                print("")
                let = 0
    
    
    elif var == "hk":
        let = 0
        while let == 0:
            
            print("Key|Key|Key: "),
            msg = raw_input()
            parse = msg.split('|')
            
            let = 1
            if len(parse) > 5:
                print("Sorry, only 5 hotkey sequence supported. Exiting to Train.")
            
            else:
                
                for o in parse:
                    
                    if o in keys:
                        pass
                    else:
                        let = 0
                if let == 0:
                    print("Invalid input. Here are keys:")
                    for o in specials:
                        print(o + ", "),
                    print("")
    
    elif var == "#":
        print("Note: "),
        msg = raw_input()
        
        
    
    
    
    try:
        
        if flag == 1:
            T[ring].append(pos)
        elif flag == 0:
            T[ring].append(pyautogui.position())
        
        Task[ring].append(var)
        time[ring].append(time_.get())
        
        message[ring].append(msg)
    
    except:
        
        T.append([])
        Task.append([])
        time.append([])
        message.append([])
        
        if flag == 1:
            T[ring].append(pos)
        elif flag == 0:
            T[ring].append(pyautogui.position())
        Task[ring].append(var)
        time[ring].append(time_.get())
        message[ring].append(msg)
        #avoid allocating memory unless via grim banshee input
        

    tmp = nice_time(str(float(run_var.get()) + float(time_.get())))
     
    run_var.set(tmp)
    root.update_idletasks()



def Train():
    global flag, pos
    pos = pyautogui.position()
    
    install = 1
    while install != '`':
        
        
        try:
            
            annotate = ''
            
            txt_old = txt.get()
            txt2_old = txt2.get()
            
            ring = int(cascade.get())
            
            print('Enter # ' + str(ring) + ': '),
            install = raw_input() 
            
            if install == "L" or install == 'l':
                add_to('l')
            
            elif install == "R" or install == 'r':
                add_to('r')
            
            elif install == "D" or install == 'd':
                add_to('d')
                
            elif install == 'w':
                add_to('w')
                
            elif install == 'b':
                try:
                    ind = ring - 1
                    T[ind] = T[ind][:len(T[ind])-1]
                    Task[ind] = Task[ind][:len(Task[ind])-1]
                    message[ind] = message[ind][:len(message[ind])-1]
                    time[ind] = time[ind][:len(time[ind])-1]
                except:
                    print("nothing to delete")
                
            
            elif install == "h":
                flag = 1
                add_to('lhd') 
                flag = 0
                add_to('m')
                add_to('lhu') 
                add_to('h')
            
            
            elif install == "c":
                flag = 1
                add_to('lhd') 
                flag = 0
                add_to('m')
                add_to('lhu') 
                add_to('c')
            
            
            elif install == "v":
                add_to('l')
                add_to('v')
                
                
            elif install == "cc":
                flag = 1
                add_to('lhd') 
                flag = 0
                add_to('m')
                add_to('lhu') 
                add_to('cc')
            
            
            elif install == "vv":
                add_to('l')
                add_to('vv')
                
                
            elif install == "p":
                add_to('l')
                add_to('p')
            
                
            elif install == "m":
                add_to('m')
                
            elif install == "su":
                add_to('su')    
                
            elif install == "sd":
                add_to('sd')  
                
            elif install == "lhd":
                add_to('lhd')  
                
            elif install == "rhd":
                add_to('rhd')    
            
            elif install == "lhu":
                add_to('lhu')  
                
            elif install == "rhu":
                add_to('rhu')
                
            elif install == "t":
                add_to('t')   
                
            elif install == "k":
                add_to('k')
                
            elif install == "kd":
                add_to('kd')    
                        
            elif install == "ku":
                add_to('ku')
                
            elif install == "hk":
                add_to('hk')
            
            elif install == "help":
                Help()
                
            elif install == "#":
               add_to("#")
                
                
                
            elif install == "~":
                Train()
                
            pos = pyautogui.position()
        
        
        except:
            
            
            letter_fault = letter_check()
            if letter_fault == 0:
            
                print("Don't start a new Train until finished first one (type '`' to finish).   Advanced:  Tilda fail? You must change Train memory before typing ~.  Starting all over...")
                Clearall()
            
            install = '`'
            #handle malformed recurssions and/or while loop exits
        
    
    
    try: 
        ring = int(cascade.get()) - 1
        conditional[ring] = diff_var.get()
        Save()
    except:
        Clearall()
        print("Unclean exit.  Starting all over.")        
        #clean when program is still allocated but original grim banshee has died
    

def Do():
    
    global i
    store = run_var.get()
    value = ''
    
    if i == 0:
        ring = int(falls.get()) 
        ring = ring - 1
    else:
        ring = i
    
    
    for p,o in enumerate(T[ring]):
        
        
        
        if Task[ring][p] in ['w','b',"#"]:
            pass
        else:
            pyautogui.moveTo(o[0],o[1],duration = float(time[ring][p]))
        
        if Task[ring][p] == 'l':
            pyautogui.click(o[0],o[1])
            
        elif Task[ring][p] == 'r':
            pyautogui.rightClick()   
            
        elif Task[ring][p] == 'd':
            pyautogui.doubleClick()
            
        elif Task[ring][p] == 'w':
            timed_.sleep(float(time_.get()))
            
        elif Task[ring][p] == 'h':
            pyautogui.hotkey('ctrlleft','c')
            
        elif Task[ring][p] == 'm':
            pass
            
        elif Task[ring][p] == 'c':
            pyautogui.hotkey('ctrlleft','c')
            txt.set(pyperclip.paste())
            
        elif Task[ring][p] == 'cc':
            pyautogui.hotkey('ctrlleft','c')
            txt2.set(pyperclip.paste())  
            
        elif Task[ring][p] == 'v':
            pyperclip.copy(txt.get())
            pyautogui.hotkey('ctrlleft','v')
            
        elif Task[ring][p] == 'vv':
            pyperclip.copy(txt2.get())
            pyautogui.hotkey('ctrlleft','v')
        
        elif Task[ring][p] == 'p':
            pyautogui.hotkey('ctrlleft','v')
        
        elif Task[ring][p] == 'su':
            pyautogui.scroll(1)
        
        elif Task[ring][p] == 'sd':
            pyautogui.scroll(-1)
        
        elif Task[ring][p] == 'lhd':
            pyautogui.mouseDown(o[0],o[1],button='left')
            
        elif Task[ring][p] == 'lhd':
            pyautogui.mouseDown(o[0],o[1],button='right') 
            
        elif Task[ring][p] == 'lhu':
            pyautogui.mouseUp(o[0],o[1],button='left')
            
        elif Task[ring][p] == 'lhu':
            pyautogui.mouseUp(o[0],o[1],button='right') 
            
        elif Task[ring][p] == 't':
            pyautogui.typewrite(message[ring][p]) 
            
        elif Task[ring][p] == 'k':
            msg = convert_for_lazy(message[ring][p])
            pyautogui.press(msg)
                
        elif Task[ring][p] == 'ku':
            msg = convert_for_lazy(message[ring][p])
            pyautogui.keyUp(msg) 
            
        elif Task[ring][p] == 'kd':
            msg = convert_for_lazy(message[ring][p])
            pyautogui.keyDown(msg) 
            
        elif Task[ring][p] == 'help':
            Help_l()    
        
        elif Task[ring][p] == 'hk':
            parse = message[ring][p].split('|')
            
            new = []
            for j in parse:
                new.append(convert_for_lazy(j))
            
        
            
            if len(new) == 0:
                pass
            elif len(new) == 1:
                pyautogui.hotkey(new[0])
            elif len(new) == 2:
                pyautogui.hotkey(new[0],new[1])
            elif len(new) == 3:
                pyautogui.hotkey(new[0],new[1],new[2])
            elif len(new) == 4:
                pyautogui.hotkey(new[0],new[1],new[2],new[3])  
            elif len(new) == 5:
                pyautogui.hotkey(new[0],new[1],new[2],new[3],new[4])          
                
    
    
        
        tmp = nice_time(str(float(run_var.get()) - float(time[ring][p])))
        run_var.set(tmp)
        root.update_idletasks()
    
    if i != 1:
        run_var.set(store)
        root.update_idletasks()


def Do_all():
    global i
    
    
    i = 1
    store = run_var.get()
    
    list = [0,1,2,3,4,5,6,7,8,9]
    
    if rand_var.get() == 1:
        rlist = random.sample(list,10)
        list = rlist
  
    
    
    
    for index,o in enumerate(list):
        proc = 0
        if conditional[index] == 'same':
            if txt.get() == txt2.get():
                proc = 1
        elif conditional[index] == 'diff':
            if txt.get() != txt2.get():
                proc = 1
        elif conditional[index] == 'always':
            proc = 1
        
        
        
        if proc == 1:
            
            if init == 1:
                i = o
                try:
                    Do()
                except:
                    pass
                    #unallacated memory
    
    i = 0
    

    run_var.set(store)
    root.update_idletasks()
    

def Repeat():
    global i 
    
    num_reps = int(reps.get())
    mem = int(falls.get())
    
    for o in range(num_reps+1):
        i = mem-1
        Do()


def RepAll():
    global i 
    
    num_reps = int(reps.get())
    mem = int(falls.get())
    
    for o in range(num_reps+1):
        Do_all()



def Save():
    
    
    with open("GB_Save.txt", "w") as text_file:
        for p,o in enumerate(T):
            
            for q,r in enumerate(o):
                text_file.write(str(p+1) + '|' + str(Task[p][q]) + '|' + str(r) + '|' + time[p][q] + '|' + message[p][q] + '\n')
                
    
    


def SaveAs():
    
    f = asksaveasfilename()
    
        
    with open(f, "w") as text_file:
        for p,o in enumerate(T):
            
            
            for q,r in enumerate(o):
                text_file.write(str(p+1) + '|' + str(Task[p][q]) + '|' + str(r) + '|' + time[p][q] + '|' + message[p][q])
                text_file.write('\n')
 


def Load():
    
    Clearall()
    tmp = 0.0
    
    
    
    with open("GB_Save.txt",'r') as text_file:
    
        for p,o in enumerate(text_file):
            
            if len(o) > 1 and o[0] != "#": 
                
                try:
                    
                    tmpsplit = o.split("|")
                    m = ''
                    m2 = ''
                    m3 = ''
                    m4 = ''
                    m5 = ''
                    
                    if len(tmpsplit) == 5:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4].split('\n')[0]
                        
                    elif len(tmpsplit) == 6:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5].split('\n')[0]
                        
                    elif len(tmpsplit) == 7:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5]
                        m3 = tmpsplit[6].split('\n')[0]
                        
                    elif len(tmpsplit) == 8:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5]
                        m3 = tmpsplit[6]
                        m4 = tmpsplit[7].split('\n')[0]
                        
                    elif len(tmpsplit) == 9:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5]
                        m3 = tmpsplit[6]
                        m4 = tmpsplit[7]
                        m5 = tmpsplit[8].split('\n')[0]
                    
                    
                    if m2 != '':
                        m = m + '|' + m2 
                    elif m3 != '':
                        m = m + '|' + m3
                    elif m4 != '':
                        m = m + + '|' + m4
                    elif m5 != '':
                        m = m + '|' + m5
                    
                    
                    if int(rigid_var.get()) == 1:
                        aa = 0
                        
                    else:
                        aa=int(a)-1
                    
                    
                    try:
                        Task[aa].append(b)
                    except:
                        
                        T.append([])
                        Task.append([])
                        time.append([])
                        message.append([])
                        Task[aa].append(b)
                    d = c.split("(")
                    e = d[1].split(")")
                    f = e[0].split(",")
                    g = (int(f[0]),int(f[1]))
                    T[aa].append(g)
                    time[aa].append(t)
                    message[aa].append(str(m))
                    
                    tmp = float(tmp) + float(t)
                except:
                    print("Invalid file format.")
            
            else:
                pass
            
    
    
    tmp = nice_time(str(tmp))    
     
    run_var.set(tmp)
    root.update_idletasks()
    
    

def LoadAs():
    
    Clearall()
    tmp = 0.0
    
    root.update_idletasks()
    
    file = askopenfilename()
    text_file = open(file, "r") 
    for p,o in enumerate(text_file): 
        
        if len(o) > 0 and o[0] != "#": 
            
                try:
                    
                    tmpsplit = o.split("|")
                    
                    if len(tmpsplit) == 5:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4].split('\n')[0]
                        
                    elif len(tmpsplit) == 6:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5].split('\n')[0]
                        
                    elif len(tmpsplit) == 7:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5]
                        m3 = tmpsplit[6].split('\n')[0]
                        
                    elif len(tmpsplit) == 8:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5]
                        m3 = tmpsplit[6]
                        m4 = tmpsplit[7].split('\n')[0]
                        
                    elif len(tmpsplit) == 9:
                        a = tmpsplit[0]
                        b = tmpsplit[1] 
                        c = tmpsplit[2]
                        t = tmpsplit[3]
                        m = tmpsplit[4]
                        m2 = tmpsplit[5]
                        m3 = tmpsplit[6]
                        m4 = tmpsplit[7]
                        m5 = tmpsplit[8].split('\n')[0]
                    
                    
                    if m2 != '':
                        m = m + '|' + m2 
                    elif m3 != '':
                        m = m + '|' + m3
                    elif m4 != '':
                        m = m + + '|' + m4
                    elif m5 != '':
                        m = m + '|' + m5
                    
                    
                    if int(rigid_var.get()) == 1:
                        aa = 0
                        
                    else:
                        aa=int(a)-1
                    
                    
                    try:
                        Task[aa].append(b)
                    except:
                        
                        T.append([])
                        Task.append([])
                        time.append([])
                        message.append([])
                        Task[aa].append(b)
                    d = c.split("(")
                    e = d[1].split(")")
                    f = e[0].split(",")
                    g = (int(f[0]),int(f[1]))
                    T[aa].append(g)
                    time[aa].append(t)
                    message[aa].append(str(m))
                    
                    tmp = float(tmp) + float(t)
                except:
                    print("Invalid file format.")
                
        else:
            pass
        
    tmp = nice_time(str(tmp))    
     
    run_var.set(tmp)
    root.update_idletasks()
    






init = 0

root = Tk()
root.title("Grim Banshee")


menubar = Menu(root)
menubar.add_command(label="Save",command=Save)
menubar.add_command(label="SaveAs",command=SaveAs)
menubar.add_command(label="Load",command=Load)
menubar.add_command(label="LoadAs",command=LoadAs)
menubar.add_command(label="Help",command=Help)

root.config(menu=menubar)



txt = StringVar()
Txt = Entry(root,width=30,textvariable=txt)
Txt.pack()


frame = Frame(root)

a = Button(frame,text="Clear",command=Clear)
a.pack(side=LEFT)

w = Label(frame, text=" ")
w.pack(side=LEFT)

clr = Spinbox(frame,from_=1, to = 10,width=2)
clr.pack(side=LEFT)

x = Label(frame, text=" ")
x.pack(side=LEFT)

z = Button(frame,text="ClearAll",command=Clearall)
z.pack(side=LEFT)


y = Label(frame, text="              ")
y.pack(side=LEFT)


frame.pack()





frame = Frame(root)

b = Button(frame,text="Train",command=Train)
b.pack(side=LEFT)

w = Label(frame, text=" ")
w.pack(side=LEFT)

cascade = Spinbox(frame,from_=1, to = 10,width=2)
cascade.pack(side=LEFT)


x = Label(frame, text=" ")
x.pack(side=LEFT)

diff_var = StringVar(frame)
diff_var.set("always")

difference = OptionMenu(frame,diff_var,"always","diff","same")
difference.config(width=7)
difference.pack(side=LEFT)



y = Label(frame, text="        ")
y.pack(side=LEFT)

frame.pack()



frame = Frame(root)

falls = Spinbox(frame,from_=1, to = 10,width=2)
c = Button(frame,text="Do",command=Repeat)
c.pack(side=LEFT)


falls.pack(side=LEFT)


rand_var = IntVar()
rigid_var = IntVar()
run_var = StringVar()
run_var.set("0.000")
h = Button(frame,text="Do All",command=RepAll)
h.pack(side=LEFT)

h = Checkbutton(frame,text="rand",variable=rand_var)
h.pack(side=LEFT)

rigid = Checkbutton(frame,text='rigid',variable=rigid_var)
rigid.pack(side=LEFT)


frame.pack()




frame = Frame(root)

#mem_box = Spinbox(frame,from_=1, to = 10,width=2)
reps = Spinbox(frame,from_=0, to = 1000,width=3)


u = Label(frame, text="number of repeats: ")
u.pack(side=LEFT)

reps.pack(side=LEFT)

u = Label(frame, text=" ")
u.pack(side=LEFT)


frame.pack()



frame = Frame(root)

tsk = Label(frame,text="task time (s): ")
tsk.pack(side=LEFT)

time_ = Spinbox(frame,from_=0.001, to = 1000,increment=0.001, width = 5)
time_.pack(side=LEFT)
time_.delete(0,"end")
time_.insert(0,'0.250')

u = Label(frame, text=" ")
u.pack(side=LEFT)

tt = Label(frame,text="total (s): ")
tt.pack(side=LEFT)

runtime = Label(frame,textvariable=run_var)
runtime.pack(side=LEFT)

frame.pack()





txt2 = StringVar()
Txt2 = Entry(root,width=30,textvariable=txt2)
Txt2.pack()




init = 1

root.mainloop()


Clearall()
