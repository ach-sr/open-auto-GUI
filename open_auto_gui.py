# pyinstaller open_auto_gui.py --noconsole --onefile --icon=open_auto_gui.ico --hidden-import os --hidden-import sys --hidden-import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import sys
import os
import json
import webbrowser
import configparser
import ast

text = (state='normal')
text.pack()

# Create a ConfigParser object
config = configparser.ConfigParser()

program_directories = []
urls = []

if os.path.isfile('config.ini'):
    # Read an existing .ini file
    config.read('config.ini')

    # Get a value from the config file
    program_directories = ast.literal_eval(config.get('config', 'path'))
    urls = ast.literal_eval(config.get('config', 'url'))



# Create a window
window = tk.Tk()
window.title("open_auto_gui")
window.geometry("600x500")

# Create a function to get the text field value
def get_directory():
    directory = directory_text_field.get()
    if directory == '':
        messagebox.showinfo("ERROR", "Please enter a file path")
    elif directory.isspace():
        messagebox.showinfo("ERROR", "Please enter a valid file")
    else:
        program_directories.append(directory)
        directory_show.config(text="Added directories: " + str(program_directories))
        print(f'program_directories: {program_directories}')

def clear_directories():
    program_directories.clear()
    directory_show.config(text="Added directories: " + str(program_directories))
    print(program_directories)

def get_browser_links():
    browserlink = browser_text_field.get()
    if browserlink == '':
        messagebox.showinfo("ERROR", "Please enter a url")
    elif browserlink.isspace():
        messagebox.showinfo("ERROR", "Please enter a valid url")
    else:
        urls.append(browserlink)
        browserlink_show.config(text="Added Chrome links: " + str(urls))
        print(f'Browswer links: {urls}')

def clear_browserlinks():
    urls.clear()
    browserlink_show.config(text="added browser links: " + str(urls))
    print(urls)

def browse_directory():
    # Show the file dialog and get the selected directory
    #selected_directory = filedialog.askdirectory()
    selected_directory = filedialog.askopenfilename(filetypes=(("All Files", "*.*"),))

    # Update the text box with the selected directory
    directory_text_field.delete(0, tk.END)
    directory_text_field.insert(0, selected_directory)

top_label = tk.Label(window, text="NOTE: when adding directories, please specify the FULL FILE PATH and include the .exe as well. \nEX:    C:\\user\\desktop\\example.exe\n\nANOTHER NOTE: You do not need to specify your browser's file path before adding links,\nyou can add them immediately.")
top_label.pack(side="top", pady=(10, 20))

top_labeltwo = tk.Label(window, text='Once all directories and links are added, click "OPEN PROGRAMS".')



directory_text_field = tk.Entry(window, width=55)   # Create a text field
directory_text_field.pack()   # Pack the text field into the window

browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack(pady=0)

get_directory_btn = tk.Button(window, text="Add directory", command=get_directory)  # Create a button to get the text field value
get_directory_btn.pack(pady=0)

directory_show = tk.Label(window, text='')
directory_show.pack()
directory_show.config(text="Added directories: " + str(program_directories))

clear_directories_btn = tk.Button(window, text = "Clear all directories", command=clear_directories)
clear_directories_btn.pack(pady=0)



browser_text_field = tk.Entry(window, width=55) # Create a text field
browser_text_field.pack(pady=(40, 0))

get_browswerlink_btn = tk.Button(window, text="Add browser url", command=get_browser_links)  # Create a button to get the text field value (chrome link)
get_browswerlink_btn.pack(pady=0)

browserlink_show = tk.Label(window, text='')
browserlink_show.pack(pady=0)
browserlink_show.config(text="Added browser urls: " + str(urls))

clear_browserlink_btn = tk.Button(window, text="Clear all urls", command=clear_browserlinks)
clear_browserlink_btn.pack(pady=0)



def open_programs():
    for url in urls:
        webbrowser.open(url, new=1, autoraise=True)
        print('opening ', url)

    for directory in program_directories:
        os.startfile(directory)
        print('opening ', directory)

def save_info():
    # create a new ConfigParser object
    config = configparser.ConfigParser()

    # add a new section called "Settings"
    config.add_section('config')

    # set a key-value pair in the "Settings" section
    config.set('config', 'path', str(program_directories))
    config.set('config', 'url', str(urls))

    # write the changes to a file
    with open('config.ini', 'w') as f:
        config.write(f)

    messagebox.showinfo("", "Successfully saved")

startBtn = tk.Button(window, text = "OPEN PROGRAMS", command=open_programs)
startBtn.pack(pady=(50, 0))

save_info_btn = tk.Button(window, text="SAVE", command=save_info)
save_info_btn.pack(pady=5)

window.mainloop()