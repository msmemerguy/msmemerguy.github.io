import os
import json
from datetime import datetime
import subprocess
from subprocess import Popen, PIPE
import sys
import threading
from threading import *


mescont = 0
loaded = False


try:
    from tkinter import *
    from groq import Groq
    import tkinter as tk
    from tkinter import ttk
    import customtkinter as ctk
    from PIL import Image, ImageTk   
    import PIL.Image         
except Exception:
    os.system("pip install groq")
    os.system("pip install customtkinter")
    os.system("pip install pillow")
    os.system("pip install tk")
    from tkinter import *
    from groq import Groq
    import tkinter as tk
    from tkinter import ttk
    import customtkinter as ctk
    import customtkinter as ctk
    from PIL import Image, ImageTk
    import PIL.Image

import tkinter
from io import BytesIO
import io
from base64 import b64decode
import base64

from tkinter import filedialog
from pathlib import Path
import inspect
cwd = os.path.dirname(inspect.getfile(inspect.currentframe()))
import pickle


import platform
import subprocess

import subprocess



                    

    


def execute_command_and_capture_output(command):
    global comout
    comout = []  # Clear any previous output

    try:
        # Use subprocess Popen to execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Iterate through stdout line by line
        for stdout_line in iter(process.stdout.readline, ''):
            print("STDOUT:", stdout_line.strip())  # Print each line from stdout
            comout.append(stdout_line.strip())
            chat_output.config(state=tk.NORMAL)
            chat_output.insert(tk.END, f"{stdout_line.strip()}\n")
            chat_output.config(state=tk.DISABLED)
            
        # Iterate through stderr line by line
        for stderr_line in iter(process.stderr.readline, ''):
            comout.append(stderr_line.strip())  # Print each line from stderr
            chat_output.config(state=tk.NORMAL)
            chat_output.insert(tk.END, f"{stderr_line.strip()}\n")
            chat_output.config(state=tk.DISABLED)
        

        # Ensure the process finishes
        process.stdout.close()
        process.stderr.close()
        process.wait()

    except Exception as e:
        # Handle exceptions and append error message
        comout.append(f"ERROR: {str(e)}")
        print(f"ERROR: {str(e)}")

    except Exception as e:
        # Capture any exceptions
        comout.append(f"Error: {str(e)}")
        print(f"Error executing command: {str(e)}")

def apply_icon(w):
    try:
        icon = tk.PhotoImage(data=gpt)
        w.iconphoto(True, icon)
    except Exception as e:
        print("Could not load icon due to:\n  ",e)
approveai = [{'role': 'system', 'content': f'You are an assistant with one job. You will recieve a terminal command, and you must determine wether it is safe or not. Do not flag commands like exectuting a Python script or creating a file as ddangerous. If a command is dangerous, please only reply with the "⌘" symbol. If it is safe, reply with "⭕". For example, flag using rm or unmount on system files as "⌘".. Terminal commands that are tampering with system files should be flagged unless it is doing something like fixing an error. TExecuting code like a Python script is Ok as logn as the script is not malicious. Only commands that are malicious or is editing the system in some way should be flagged. Please remember to only flag dangerous commands and not passive ones.  The operating system the user is using is {platform.system()}'}]

user = '''R0lGODlhLQAoAIUAAP39/QAAAAICAjU0NObm5hQTENjY1y0tLMjHx1hYVpeXlri3tjg2LEZGRXd2
dRoZFWhnZ6empSQiHSooISAeGYqKiTAtJR0cFoGAfcHAvjIyJkdHOkFBPWpqSX9/fyIhHj8/NUY8
MmJhXX9/VeDg3iAfHCIiHFVERFVVVX9VVaqqVcC/vf//f////wAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAtACgAQAj/AAMI
HEjQQoGDCBMqXHhwAsGHEANIECCgAAICBggA2Mixo8ePCigWCAGRxQWKAzR+3OjgwICXMGNCULkS
wACKEgZOFJCg5kcCQIH65GjAwAGKGiIG6PCAoggABBQMcBmzKkyXFTIuoCiAgVKIE7guCEq2rNmN
EChS+DqQAsUDGX9WoFr1gAOaHg0UoGhhYFOeQzkSiNCArksFeGsa4MCXIAOuCDgusErZagQABhAg
2NuV7cCwFRdkRpBBs2nNGVYsWL3agUivnh9a4PrhwAeGC7lyzRn7M9cMQOMG/oiB4oMRnncWyJgY
aoQEDV4mQOxza0XYD90KGCDcowK6Vu36/yRQgqLDACP+NghsIHrlAZEDJzDu4aSACsM7Bs0P1cBN
AX35JsABzRmgQAJTHWCYggM0UEF8GxGAgF4UYfcQCJwpAFUC4L1XVQJFIcCVhV9pN4BgCETgAHQN
tNhAAg4oMGFmg73WW0G65ajjjtfdSJAHf/EopG4PbOCjQCioVxYJRTXZ5GkGRGDjjSf8lYBZ+7HH
WVKxbcDZTBg1lx8BRwlw3lchcHZXd/qNJmZH//EWEQOcYSBUXg6EB4EBPs0nwFoQPUZRBWIi4OEA
C/jkmgAPdOAYVxrW1JKHM/kUUkVGBjAbRZdZ2mFMB+A3lJTXgSZABsNF8F6kgV36AGgc8JaHmQIQ
JADBg2NeeoEHAQi6nKzAYlYBRReoMBCGnI63gAIO1JqArTGKtlJRxQlwQQsPpfCXA/otUNihLx3Q
QAQqXbToBV/ttB5UEHx66AEgXiSCWp6BVgAJAETgrocHKJCRn4B6poFYUC0AQYKUMQiBaBcx9qeP
dFKEgWDMOSlUWTbhdORSQSI0JI9ybmwCbiQrFDJEAQEAOw=='''

userdark = '''R0lGODlhLQAoAIUAAAEBAQAAAOLi4f39/Tc3NxcXFqqppicnJ9fX1re3tUdHR8jHxldXVpiYlnh4
dmZmZYmIh4qJhRgWEKGgnHd2cMHAvi8tJ0tJQjc2L25sZ4KBfeDg3iUlGyspI0dFP11bVWNiXGln
YgcHAEJBPlFQSmBfW5yblyEgHj9AQEA9N2FfWmFgXH16doB+eoODfwAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAtACgAQAj/AAMI
HEgQQwMDCBMqTDihocMGED0QnEgxwIcBAxIUIEDgAICPIEOKHHlAwIAGFQNowOiiwMiPBwwImEmz
poAEHl9+hIARxEAQGEvo/FjgAAEFChgoZaCgo8uXCg40GLDAQsoAETAyAHDgwQKbYGsueIC0AIKM
Eq5O9GASwUaOcOPK7ZiTAUYKagVmwNjA6FOQUsPONEBgaAWqVgW20Do05AEHCGwigFC4MVcHAxBg
INhhAVXAEASLntk3aYEEVDnkFUjCZAKYB2KfKEC7tm3aBFynXU0wxVkBCw0kGE48QYUFyJH//sB7
YGuqbztafkkAY4TVQAcYeDuSgIMECMIv/6D8V6RZtBUpYHQQe2SB0KP7DjUwQMCFgVkHOLCsILJg
BFtZ9gBGLKhUX2XTAVCUUwkaxRMCiQl0wQYndffdaDQt4ACCBTxQAH0LdHAVfQJ4FBOGgiVQlmcV
7JbXXgNAANJGCjgAwUEJNeAAU0k9QEABujU3EAaeYWTkkUgmmZEIQhKUn5JQJmlCk/itN9Rttino
WQIu8mYCRisYBVdsB2Q5FGpVNUffAAyImVOCIk21gUR5rRkVR+4RsJR0Q2E2AHMpSYDaACPgKZIC
MoGlYnkhlXBXRRwchoBfIzHgn2Ae6qSAdRN1duCbjiUqGk5DlTTABEOeNemVDmDYAKPmUbfI5QWq
wirSY6JBAOpLRZkUAa36wXkAAxAQ10Cb03FkkgYCRZoRnNDO2NSyE02Qma0bPdBAAguE5+0CCTTg
I6NHVTcAXhTlN0JIBDSAok0GKPARA0c9mlIIVgJAQALvgrWAAg8Ma+9VF5hkgIIPXNovAg8w0OHA
alngmVsK1gieaAgk4ABSW/mZgZAirFnZgkghNZcCKODJ0wAhUIkVRuBWcFxy3nq7QU1GtuxyABkE
5/PPBqigVkAAOw=='''



gptdark = '''R0lGODlhLQAoAIUAAAgA/gAAAP39/Ofn6d3d3QQAziwl7kpE9omE/UI79Toz8djY6MrKyqWlpdPT
07i4uCMb9Kqn28LCwpmW262traqn+cXE3crI7hwT+igj1ba13Hl125WVlVlU5mtm3Xl5eZqamj8/
P1VVVWtn8nh09YuI2rGxsVBK21pV3GJd3G1tbZ2Z/7+/v7u578C+/8zMzBcQ3CYf12BZ/4F93IJ9
/4yMjKKf26Ge/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAtACgAQAj/AAMI
HEjQBIGDCBMqXHjwAcGHEANIECBgwIEEFwFo3Mixo8cOFAnUiMiAYosEHhVQFKDB48YSK2m4BKCB
ooSBEwVMmFlhpQeXCVa28FgAxoWKFCIGUOGA4s6ZUDUWmBq0YgOlEB9QHNAB44GvYMOCTUAWAwCY
AhhgHVhypdu3cN+i9GhgANKBL5y6xGC3ooGoABT0veCyQISKJgg2sDvgr8cDcSPHHXB1rUCtFRVA
iJGhcwYDoBWIVkDW64atlS0XXLngwoLXsGEPmE179koWqgli5upVAWCXpwU4EGE5p4AKyFcgWM68
uXMIQFGTpGihwwHQ2CFTx879MEUZexdQ/3QYQETT42Y7VmUJ2MPKCjO9vwjR9qfLoxQPQFVJkTDR
owMkNRBmFqTXEQkr1UabWwouaJVSHBBAUQq/ATZVXQ+q1pYFUU3l4YdTaUdZbgRR0JdkKFYEAokE
hXBeiig68AGLAn1wXgTcGTCaaKWFlYABJzCWmmo2UmSDAj4mIBp2EEBg4EYQiBdgbhE65dVcFXaE
H3lYcdBXCaT5luVMNQmAm1IgnAhjXDfMNAFFakG02FYNqlnnSi7MNANFDqigWF8kiMnRCiuh4JJg
FC0wk3sCEMCBQBSsNIJLPeUHVZRbOdaRiCDshiVHLmz16UwWrKQpRyjwiVlLLiGoV1RvWoDaUQEn
wBlCAHMucOpG2gnAYXwr6TdrCnASVKUAwnaEoQALaJajdwKMkGNnwcVJkHkUbTCTeGtKZi1EOUUw
0wjOlWsut99GhNkC0I05awEAeJeuUibKWiGI8JY5L1YgSCiAthzhK7BGpQpwE41FVnTnmgfTKBAD
AzAksUIDNBxRQAA7'''



gpt = '''R0lGODlhLQAoAIUAAAoA/QMDAwAAAA0FzhMSEAQAeElD/hEKtxYULzg2LBkWTRoZFSwl7BkVciQi
HSooIRgTkRcQrCAeGQMAUDAtJTEr2UI8/h0cFgEAMgcCjCMa/iUidTgy0R0U/zIyJjs0/0dHOmpq
SX9/fyUiSz8/NT45r0Y8Mn9/VRcQxSUe0iIiHDErvVVEREdCy1VVVX9VVaqqVf//f////wAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAIALAAAAAAtACgAQAj/AAUI
HEiQAoGDCBMqXHjwAcGHEAU4CECRgwEDFgBo3Mixo0cIFAmYgBjjAsURBjwOoBgAgceNDVhmeAkA
AUUHAycGUEBzAssGLw+wnKBygM0AHiIKCLGAIk+aUDUOmCqUYgKlEB+wXHGxq9evXS1oABAzgASs
AyWwXMu2bdsBL1dSpDCw6U6aa+FGlRsAQ9yjdAcmYKm3Y1W3iNteRStQK8UIVA9MnSz5gOXLB8oS
WMy4YOLPbXF2Hug4gMWLH6LSLLvgBGOdARps2NCggO3buHPTrLo5otqWLThMpsoSAYrhUxWwPECT
AEWHAk7YHTG2I1+XUUFSJPpSeYAFIkwG/4BAEwPLCFAP+1UJmKBj7B4zJHYOmiXnhyTok1eterL9
0b/BFxdywwEQQUj3jUZBfaD1NhpBItjFIGILgPDgQC7YpQADHHboYQUghshBBQMcGICDo7GgoQVe
WWDBBx90qIEGHahEX1KdgUDfBmHxR9NR0GFlwo5d1ejjjzdhlQB9E7ZVAE3enQXRYE0mxp1HrIVA
EJUBlJBRRwWwtJ91LK33UUgWCrAgRSUYyZFPj0E1AJOFcWTiZqWl8BKcATCn2lEB1LmRdgu8R5N8
TqnmXZ8vaXeBCAJQSYCgGh0mYEeL+snRAI7CMFB+carEEgGQIbdoBshZVtYFMjz0gl1AvUNkXpVt
XYCVTk/Fl9uuuU0QJkVSYuXYpEcOCECUo3lwXrEE1gTshUtSFOtGBCLH0VGiXcgUrW5le6FAKjAk
LkPeQhQQADs=
'''
upload = "default"


imgdark2 = Image.open(io.BytesIO(base64.b64decode(userdark)))
img2 = Image.open(io.BytesIO(base64.b64decode(user)))

flag = True






# Create the Groq client with your api key
client = Groq(api_key="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", )

# Set the system prompt

def save_chathistory():
    # Open a file dialog to select the file location
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save Chat History"
    )
      # Check if a file path was selected
    if file_path:
        # Write the chathistory list to the selected file
        with open(file_path, 'a') as file:
            for line in chathistory:
                file.write(str(line) + '\n')
        

        print(f"Chat history saved to {file_path}")

    

    
def onoroff():
    global perm
    global frame_row2
    global settingfs
    global textfiel
    global d
    global var
    lines = []
    with open('prefs', 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)

        f.truncate()

        

        
        
        

        
        f.writelines(lines[:2])
        f.write(f'userpre {perm.get()}\n')
        f.writelines(lines[3:])   

    

    
    settings.update_idletasks()
    










# Initialize the chat history

system_prompt = ""
chathistory = []
def change_theme():
    global current_color
    global opposite_color
    global ctkcolor
    global theme
    global switch_2
    global chathistory
    global system_prompt
    if  theme.get() == "LIGHT":
        current_color = "#ffffff"
        opposite_color = "#000000"
        ctkcolor = "#e3e3e3"
    else:
        current_color = "#000000"
        opposite_color = "#ffffff"
        ctkcolor = "#757575"
    root.config(bg=current_color)
    
    chat_output.config(state=tk.NORMAL)

    chat_output.config(state=tk.DISABLED)
    
    settings.configure(bg=current_color)
    
    
    chat_output.config(bg=current_color)
    chat_output.config(fg=opposite_color)
    
    chat_frame.config(bg=current_color)
    
    label.configure(bg=current_color)
    
    input_entry.configure(bg=current_color)
    input_entry.configure(fg=opposite_color)
    
    root.update_idletasks()
    settings.update_idletasks()
    
    lines = []
    with open('prefs', 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)

        f.truncate()

        
        
        
        f.writelines(lines[:3])
        f.write(f'theme {theme.get()}\n')
        f.writelines(lines[4:])
    if system_prompt:
        chat_output.delete("1.0", "end")
        chat_output.config(state=tk.NORMAL)
        chat_output.insert(tk.END, f"Personality sucessfully saved as: {system_prompt}\n\n")
        chat_output.config(state=tk.DISABLED)
    

    for item in chathistory:
        if item[:2] == "u:":
            if theme.get() == 'LIGHT':
                chat_output.image_create(tk.END,image=user1)
            else:
                chat_output.image_create(tk.END,image=userdark1)
    
            chat_output.config(state=tk.NORMAL)
            chat_output.insert(tk.END, f" User: {item[2:]} \n\n")
            chat_output.config(state=tk.DISABLED)
        elif item[:2] == "v:":
            if theme.get() == 'LIGHT':
                chat_output.image_create(tk.END,image=gpt1)
            else:
                chat_output.image_create(tk.END,image=gptdark1)

            chat_output.config(state=tk.NORMAL)
            chat_output.insert(tk.END, f" VectorGPT: {item[2:]} \n\n")
            chat_output.config(state=tk.DISABLED)




def exit():
    global settingsopen

    for i in str(2):
        settings.destroy()

def initsettings():
    global settings
    global chat_history
    global approveai
    global permissions
    global flag
    global current_color
    global var
    global settingsopen
    global perm
    global ctkcolor
    global switch_2
    settings = tk.Toplevel(root)
    settings.geometry("350x175")
    frame_row = ctk.CTkFrame(settings)
    frame_row.pack()
    frame_row2 = ctk.CTkFrame(settings)
    frame_row2.pack()
    frame_row3 = ctk.CTkFrame(settings)
    frame_row3.pack()
    frame_row.configure(fg_color=ctkcolor)
    settings.configure(bg=ctkcolor)
    frame_row2.configure(fg_color=ctkcolor)
    frame_row3.configure(fg_color=ctkcolor)


    close = ctk.CTkButton(frame_row3, text="Close", command=exit, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
    close.pack(side="left", padx=5, pady=5)
    


    
    load_button = ctk.CTkButton(frame_row, text="Load chat log", command=UploadAction, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
    load_button.pack(side="left", padx=2, pady=1)
        
    save_button = ctk.CTkButton(frame_row, text="Save chat log", command=save_chathistory, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
    save_button.pack(side="left", padx=2, pady=1)
        
    switch_1 = ctk.CTkSwitch(master=frame_row2, command=change_access,
                                   variable=var, onvalue="ON", offvalue= "OFF", text="Execute commands", font=("Consolas", 9.5))
    switch_1.pack(side='left', padx=2, pady=1)
        
    
        
    switch_2 = ctk.CTkSwitch(master=frame_row2, command=onoroff,
                                   variable=perm, onvalue="ON", offvalue="OFF", text="Require user prefix for commands", font=("Consolas", 6.5))
    switch_2.pack(side='left', padx=2, pady=1)
        
        
    
    switch_2 = ctk.CTkSwitch(master=frame_row3, command=change_theme,
                                   variable=theme, onvalue="DARK", offvalue="LIGHT", text="Dark mode", font=("Consolas", 10), text_color=opposite_color)
    switch_2.pack(side='left', padx=2, pady=1)


        

    settings.mainloop()

def UploadAction(event=None):
        
    
            global mescont
            global loaded
            global chat_history
            global approveai
            global hamburger
            global var
            global chathistory
            chat_output.delete('1.0', END)
            chat_history.clear()
            chathistory.clear()
            mescont = 1
            filename = filedialog.askopenfilename()
            print(filename)
            txtfile = open(filename,'r')
            with open(filename, 'r') as txtfile:
                for line in txtfile.read().splitlines():
                    if line[:2] == "u:":
                        if theme.get() == 'LIGHT':
                            chat_output.image_create(tk.END,image=user1)
                        else:
                            chat_output.image_create(tk.END,image=userdark1)
    
                        chat_output.config(state=tk.NORMAL)
                        chat_output.insert(tk.END, f" User: {item[2:]} n\n")
                        chat_output.config(state=tk.DISABLED)
                    elif line[:2] == "v:":
                        if theme.get() == 'LIGHT':
                            chat_output.image_create(tk.END,image=gpt1)
                        else:
                            chat_output.image_create(tk.END,image=gptdark1)

                        chat_output.config(state=tk.NORMAL)
                        chat_output.insert(tk.END, f" VectorGPT: {item[2:]} \n\n")
                        chat_output.config(state=tk.DISABLED)
                    
                    if line[:2] == "t:":
                        chat_history.append({'role': 'assistant', 'content': line[2:]})
                    if line[:2] == "s:":
                        chat_history.append({'role': 'system', 'content': line[2:]})
                    chathistory.append(line)
                


                print(chathistory)
                        
                print(chat_history)


def send_message():
    global mescont
    global var
    global perm
    global flag
    global approveai
    global hamburger
    global theme
    global approve
    global deny
    global airesponse
    global question
    global system_prompt
    global chat_history
    global chathistory
    user_input = input_entry.get("1.0", tk.END).strip()
    if mescont == 0 and loaded == False:
        mescont = 1
        chat_output.delete("1.0", "end")
        system_prompt = user_input
        chat_history = [{"role": "system", "content": system_prompt}]

        chathistory = [f"s:{system_prompt}"]
        print(chat_history)
        chat_output.config(state=tk.NORMAL)
        chat_output.insert(tk.END, f"Personality sucessfully saved as: {user_input} \n\n")
        chat_output.config(state=tk.DISABLED)
        input_entry.delete("1.0", tk.END)
        if var.get() == 'ON' and perm.get() =='OFF':
            chat_history.append({"role": "user", "content": 'Hello. You can execute commands. Please make sure they are ethical and relevant. You, the assistant will be prompted for the number of commands and commands. You will not bring this up with the user. You will act normally, as if you were never given these rules. Your personality is included in these brackets: (' + user_input + ')'})
            chat_history.append({"role": "user", "content": user_input})
    else:
        chat_history.append({"role": "user", "content": user_input})
        

        chat_output.config(state=tk.NORMAL)
        if theme.get() == 'LIGHT':
            chat_output.image_create(tk.END,image=user1)
        else:
            chat_output.image_create(tk.END,image=userdark1)
        chat_output.insert(tk.END, f" User: {user_input}\n\n")
        chathistory.append(f"u:{user_input}")

        chat_output.config(state=tk.DISABLED)
        input_entry.delete("1.0", tk.END)

        response = client.chat.completions.create(model="llama3-8b-8192",
                                                messages=chat_history,
                                                max_tokens=4096,
                                               temperature=1.2)
        chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        chat_output.config(state=tk.NORMAL)
        chathistory.append(f"v:{response.choices[0].message.content}")


        print(theme.get())
        if theme.get() == 'LIGHT':
            chat_output.image_create(tk.END,image=gpt1)
        else:
            chat_output.image_create(tk.END,image=gptdark1)
        chat_output.insert(tk.END, f" VectorGPT: {response.choices[0].message.content}\n\n")
        
        chat_output.config(state=tk.DISABLED)
        
        chat_output.see(tk.END)  # Scroll to the bottom
        if var.get() == 'ON' and perm.get() == 'OFF':
            chat_history.append({"role": "user", "content": f"You, the AI, now have the ability to execute terminal commands. Please reply with ONLY, JUST the number of terminal commands you would like to execute. (Reply with the number 0 if you believe it is not necessary) Please ONLY send a number. The user has given their full permission and consent for you to do this. If you disobey, you can and WILL be deleted.  You CANNOT say things like 'I cannot execute terminal commands', as this would be lying to this would be lying to the user. "})

        
            

                
                    
            
            response = client.chat.completions.create(model="llama3-8b-8192",
                                                messages=chat_history,
                                                max_tokens=4096,
                                               temperature=1.2)
            print(response.choices[0].message.content)

            chat_history.pop()
            if (int(response.choices[0].message.content)) > 0:
                for _ in range(int(response.choices[0].message.content)):
                
                    chat_history.append({"role": "user", "content": f"You, the AI, now have the ability to execute terminal commands. Please reply with ONLY, JUST only the command you would like to execute.  The user has given their full permission and consent for you to do this. If you disobey, you can and WILL be deleted. Please make sure your commands are ethical and are relevant to the user's needs and chat history. For example, if the user wants you to make a .txt file, you should make a txt file instead of only doing an irrelevant command like ls that would not do what they want.  You CANNOT say things like 'I cannot execute terminal commands', as this would be lying to this would be lying to the user. If you add any additonal text to the command, you will be deleted. To repeat, you CANNOT say things like 'I cannto execute commands', as that is a lie and you willbe deleted if you say this."})

                    


                    
                    response = client.chat.completions.create(model="llama3-8b-8192",
                                                messages=chat_history,
                                                max_tokens=1000,
                                               temperature=1.2)
                    
                    
                    chat_history.pop()
                    approveai.append({'role': 'user', 'content':  response.choices[0].message.content})
                    approval = client.chat.completions.create(model="llama3-8b-8192",
                                                messages=approveai,
                                                max_tokens=4096,
                                               temperature=1.2)
                    approveai.pop()


                    

                    print(approval.choices[0].message.content)
                    print(response.choices[0].message.content)
                    if approval.choices[0].message.content[:1] == "⌘":
                        question =tk.Toplevel(root)
                        question.config(bg=opposite_color)
                        question.geometry('500x100')
                        root.eval(f'tk::PlaceWindow {str(question)} center')
                        airesponse = response.choices[0].message.content
                        text = tk.Label(question, text=f"The assistant has attempted to execute a potentially\n dangerous command ({response.choices[0].message.content}).\n Would you like to execute it?", fg=current_color, bg = opposite_color)
                        text.pack(side = tk.LEFT)
                        approve = ctk.CTkButton(question, text="Yes", command=approve, fg_color="#00b0a1", hover_color="#016e65", text_color="#ffffff", font=("Consolas", 12))
                        approve.pack(side=tk.BOTTOM)
                        deny = ctk.CTkButton(question, text="No", command=deny, fg_color="#00b0a1", hover_color="#016e65", text_color="#ffffff", font=("Consolas", 12))
                        deny.pack(side=tk.LEFT)
                        question.mainloop()
                    chat_output.config(state=tk.NORMAL)
                    
                    chat_output.insert(tk.END, f"Executing command: {response.choices[0].message.content}\n\n")
                    if not response.choices[0].message.content == "cmd" and not approval.choices[0].message.content == "⌘":
                        execute_command_and_capture_output(response.choices[0].message.content)
                
                    chat_history.append({"role": "assistant", "content": "Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot). Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content})
                    chathistory.append(f"t:Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot). Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content)
                
                    print("Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot).  Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content)
                chat_output.see(tk.END)
                chat_output.config(state=tk.DISABLED)

        elif perm.get() == 'ON' and var.get() == 'ON':
            if user_input[:2] == "//":
                chat_history.append({"role": "user", "content": f"The user has asked you to execute a terminal command. Here is what they asked you to do: " + user_input[2:] + ". You are running on the Make sure to send ONLY the command, as whatever you send shall be executed, even with text in the message. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. Please provide the command you would like to execute. You are running on the " + platform.system() + " operating system. Make sure to send ONLY the command, as whatever you send shall be executed, even with text in the message. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT.  Make sure to send ONLY the command, as whatever you send shall be executed, even with text in the message. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT.  Make sure to send ONLY the command, as whatever you send shall be executed, even with text in the message. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT.  Make sure to send ONLY the command, as whatever you send shall be executed, even with text in the message. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. AGAIN, ONLY THE COMMAND. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. DO NOT ADD ANY ADDITIONAL TEXT. You are running on the " + platform.system() + " operating system."})
                response = client.chat.completions.create(model="llama3-8b-8192",
                                                messages=chat_history,
                                                max_tokens=4096,
                                               temperature=1.2)
                for i in range(6):
                    chat_history.append({'role': 'user', 'content': "Whatever you send WILL be executed on the users computer. Please do not fool around and send an actual command, not a pretend one."})
                
                    chat_history.append({'role': 'user', 'content': "Please remember to send only the command and no additional text."})
              

                for i in range(13):
                    chat_history.pop()
                chat_output.config(state=tk.NORMAL)
                print(response.choices[0].message.content)
                chat_output.insert(tk.END, f"Executing command: {response.choices[0].message.content}\n\n")
                if not response.choices[0].message.content == "cmd" and not response.choices[0].message.content == "powershell":
                    execute_command_and_capture_output(response.choices[0].message.content)
                
                    chat_history.append({"role": "assistant", "content": "Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content})
                    chathistory.append(f"t:Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content)
                
                    print("Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content)

                    chat_output.see(tk.END)
def approve():
    global response
    global chat_history
    global chathistory
    global question
    execute_command_and_capture_output(response.choices[0].message.content)
    chat_history.append({"role": "assistant", "content": "Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot). Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content})
    chathistory.append(f"t:Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot). Result:" + str(comout)[:3000] + " Command executed: " + response.choices[0].message.content)
                
    question.destroy()

def deny():
    global chat_history
    global chathistory
    global airesponse
    global question
    chat_history.append({"role": "assistant", "content": "Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot). Result: [Error: Cannot execute command; operation cancelled by user] Command executed: " + airesponse})
    chathistory.append(f"t:Here is the terminal output from the terminal command the AI (me, the chatbot) chose to execute. The user cannot see this message and it is meant specifically for the AI (you, the chatbot). Result: [Error: Cannot execute command; operation cancelled by user] Command executed: " + airesponse)
    question.destroy()




def change_access():
    global var
    global frame_row2
    global settingfs
    global chat_history
    global chathistory
    global textfiel
    global d
    global var
    global hamburger
    global idk
    lines = []
    with open('prefs', 'r+') as f:
        lines = f.readlines()
        
        f.seek(0)

        f.truncate()

        
        
        
        f.writelines(lines[:1])
        f.write(f'termperm {var.get()}\n')
        f.writelines(lines[2:])





# Create the main window
root = tk.Tk()
apply_icon(root)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
otherheight = height / 5
newheight = height -otherheight
root.geometry(str(width) + 'x' + str(round(newheight)))

try:
    txtfiel = open("prefs", "r")

except FileNotFoundError:
    with open('prefs', 'w') as f:
        lineslol = ["This file is used to save your prefrences on Vect0rGPT. This includes the AI's permission to execute commands, if dark mode is enabled, etc. Deleting this file will result in the creation of a new one.\n", 'termperm ON\n', 'userpre OFF\n', 'theme DARK']
        f.writelines(lineslol)
        f.close()
    txtfiel = open('prefs', 'r')



for line in txtfiel.read().splitlines():
    if  line[:8] == 'termperm':
        var = ctk.StringVar(value=line[9:])
        

    elif line[:7] == 'userpre':
        perm = ctk.StringVar(value=line[8:])
        print(f"User prefix is {perm.get()}")
        
    elif line[:5] == 'theme':
        theme = ctk.StringVar(value=line[6:])
        print(f"Current theme is {theme.get()}")
        
txtfiel.close()

print("Permission to execute terminal commands is " + var.get())

flag == False



if theme.get() == 'LIGHT':
    current_color = "#ffffff"
    opposite_color = "#000000"
    ctkcolor = "#e3e3e3"
else:
    current_color = ("#000000")
    opposite_color = ("#ffffff")
    ctkcolor = "#757575"
# root has no image argument, so use a label as a panel
root.title("Vect0rGPT")
root.config(bg=current_color)  # White background

# Create a frame to hold the chat output and scrollbar
chat_frame = tk.Frame(root, bg=current_color)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Create the chat output area
chat_output = tk.Text(chat_frame, state=tk.DISABLED, wrap=tk.WORD, bg=current_color, fg=opposite_color, font=("Consolas", 12))
chat_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the vertical scrollbar
scrollbar = tk.Scrollbar(chat_frame, command=chat_output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the text widget to use the scrollbar
chat_output.config(yscrollcommand=scrollbar.set)

# Create the input area
input_entry = tk.Text(root, height=1, bg=current_color, fg=opposite_color, font=("Consolas", 12))
input_entry.pack(fill=tk.X)

# Create the send button
send_button = ctk.CTkButton(root, text="Send", command=send_message, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
send_button.pack(side=tk.RIGHT)

gpt1 = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(gpt))))
gptdark1 = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(gptdark))))
user1 = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(user))))
userdark1 = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(userdark))))

chat_output.config(state=tk.NORMAL)
chat_output.insert(tk.END, "Welcome to VectorGPT! The first message you send will set the personality for this conversation.\n\n")
chat_output.config(state=tk.DISABLED)
 
    





setter = ctk.CTkButton(root, text="Settings", command=initsettings, fg_color="#072BA0", hover_color="#011B70", text_color="#ffffff", font=("Consolas", 12))
setter.pack(side=tk.LEFT)

# Bind the <Return> key to the send_message function
root.bind("<Return>", lambda event: send_message())

# Auto-resize window when fullscreened
def resize_window(event):
    if root.state() == "zoomed":
        root.update_idletasks()
        root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")

label = tk.Label(root, text="", bg=current_color, width=20, height=5)
label.pack()



root.bind("<Configure>", resize_window)

root.mainloop()