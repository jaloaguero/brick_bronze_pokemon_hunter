#Messing around w a gui output first time please forgive the spagetti here

import tkinter as tk
from tkinter import ttk, messagebox
import time

from PIL import Image, ImageTk

from loop_logic import start

import threading


def validate_number_input(P):
    if P == "" or P.isdigit():
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def countdown(timer, callback):
    """Countdown function that updates the timer label."""
    for t in range(timer, -1, -1):
        countdown_label.config(text=f"Time left: {t} seconds")
        root.update()
        time.sleep(1)
    
    threading.Thread(target=callback, daemon=True).start()

def setup_gui(config):

    """Set up the main window and widgets."""
    global root, countdown_label, vcmd
    root = tk.Tk()
    root.title("Pokemon Brick Bronze Auto Hunter")
    root.geometry("650x800")  # Set the window size to 600x400
    root.iconbitmap("icons/program_icon.ico")
    root.resizable(False, False)

    s = ttk.Style()
    COLOR_YELLOW = "#FCC737"
    COLOR_PURPLE = "#7E1891"
    BACKGROUND_COLOR = "#b8c5ff"
    FOREGROUND_COLOR = "#473245"

    s.theme_create("yummy", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] }, "background": BACKGROUND_COLOR, },
    "TNotebook.Tab": {
    "configure": {"padding": [5, 1], "background": COLOR_YELLOW},
    "map":       {"background": [("selected", COLOR_PURPLE)],
    "expand": [("selected", [1, 1, 1, 0])] } } } )
    
    s.theme_use("yummy")
    s.configure('TNotebook', background="#352645")


    s.configure('TFrame', background=BACKGROUND_COLOR)
    s.configure('start.TButton', foreground=COLOR_YELLOW, background="#352645", font=('Impact', 20), padding=10)
    s.configure('TLabel', foreground=FOREGROUND_COLOR, background=BACKGROUND_COLOR, font=('Helvetica', 10))
    s.configure('TEntry', background=BACKGROUND_COLOR, font=('Helvetica', 10))

    
    vcmd = root.register(validate_number_input)

    # Create a Notebook widget (tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')
################swsswssws#######################
    # Tab 1: Basic features
    basic_tab = ttk.Frame(notebook)
    notebook.add(basic_tab, text="Start")


    padx_input = 30
    pady_input = 5

    
# Label to display output

    label_blurb = ttk.Label(basic_tab, text="I HOPE TO MAKE A LOGO SOMEDAY THAT GOES HERE LOL")
    label_blurb.pack(padx=padx_input, pady=pady_input)
    #label
    label_countdown_time = ttk.Label(basic_tab, text="Countdown Before Start (Seconds):")
    label_countdown_time.pack(padx=padx_input, pady=pady_input, anchor="nw")
    #text box
    entry_countdown_time = ttk.Entry(basic_tab, validate="key", validatecommand=(vcmd, "%P"))
    entry_countdown_time.pack(padx=padx_input, pady=pady_input, anchor="nw")
    entry_countdown_time.insert(0, config.countdown_time)  # Pre-fill with a predetermined number

    label_key1 = ttk.Label(basic_tab, text="Key 1:")
    label_key1.pack(padx=padx_input, pady=pady_input, anchor="nw")

    entry_key1 = ttk.Entry(basic_tab, validate="key")
    entry_key1.pack(padx=padx_input, pady=pady_input, anchor="nw")
    entry_key1.insert(0, config.key_1)  # Pre-fill with a predetermined number

    label_key2 = ttk.Label(basic_tab, text="Key 2:")
    label_key2.pack(padx=padx_input, pady=pady_input, anchor="nw")

    entry_key2 = ttk.Entry(basic_tab, validate="key")
    entry_key2.pack(padx=padx_input, pady=pady_input, anchor="nw")
    entry_key2.insert(0, config.key_2)  # Pre-fill with a predetermined number

    label_hold_time = ttk.Label(basic_tab, text="Key Hold Time (Seconds):")
    label_hold_time.pack(padx=padx_input, pady=pady_input, anchor="nw")
    

    entry_hold_time = ttk.Entry(basic_tab, validate="key", validatecommand=(vcmd, "%P"))
    entry_hold_time.pack(padx=padx_input, pady=pady_input, anchor="nw")
    entry_hold_time.insert(0, int(config.hold_time))  # Pre-fill with a predetermined number

    # Label to display the countdown
    countdown_label = ttk.Label(basic_tab)
    countdown_label.pack(pady=10)
    
   ########################################################################################## 

    # Tab 2: Advanced features
    advanced_tab = ttk.Frame(notebook)
    notebook.add(advanced_tab, text="Advanced")

    # Example advanced feature: An extra entry box
    advanced_label_threshold = ttk.Label(advanced_tab, text="Threshold:")
    advanced_label_threshold.pack(padx=padx_input, pady=pady_input)
    advanced_entry_threshold = ttk.Entry(advanced_tab, validate="key", validatecommand=(vcmd, "%P"))
    advanced_entry_threshold.pack(padx=padx_input, pady=pady_input)
    advanced_entry_threshold.insert(0, float(config.threshold))  # Pre-fill with a predetermined number

    #this doesn't work so its just there for show lol i will maybe get some config going later
    debug_button = ttk.Checkbutton(advanced_tab, variable='d', text='Debug', onvalue=True, offvalue=False)
    debug_button.pack(padx=padx_input, pady=pady_input)


    info_tab = ttk.Frame(notebook)
    notebook.add(info_tab, text="Info")

    label_info_text = ttk.Label(info_tab, text=startup_text())
    label_info_text.pack(padx=10, pady=10)

#########################################################################################################
######## IDK HOW THIS WORKS I GOT IT FROM ONLINE BUT IT THOUGHT IT WAS PRETTY BUT IF SOMETHING ##########
################### BREAKS BECAUSE OF THIS JUST THROW IT AWAY ITS JUST FOR DECORATION ###################
#########################################################################################################
                                                                                                        #
    def animate_gif(label, frames, delay, idx=0):                                                       #                           #
        frame = frames[idx]                                                                             #
        gif_img = ImageTk.PhotoImage(frame)                                                             #
        label.config(image=gif_img)                                                                     #
        label.image = gif_img                                                                           #
        root.after(delay, animate_gif, label, frames, delay, (idx + 1) % len(frames))                   #
                                                                                                        #
    def load_gif():                                                                                     #                                                      #
        gif = Image.open(config.img_dir)                                                                #
        frames = [gif.copy().convert("RGBA") for frame in range(gif.n_frames) if not gif.seek(frame)]   #
        return frames, int(1000 / gif.info["duration"])                                                 #
    
    gif_name_label = ttk.Label(basic_tab, text="LOOKING FOR")
    gif_name_label.pack(padx=padx_input, pady=pady_input, anchor="se")
                                                                                                        #
    gif_label = ttk.Label(basic_tab)                                                                    #
    gif_label.pack(padx=padx_input, pady=pady_input, anchor="se")                                                                             #
                                                                                                        #
    try:                                                                                                #
        gif_frames, gif_delay = load_gif()                                                              #
        animate_gif(gif_label, gif_frames, gif_delay)                                                   #
    except Exception as e:                                                                              #
        pass                                                                                            #
#########################################################################################################

    #Gets ball rolling, does try catch on countodnw, if fails, its because of a bad output so it stops and sends message box
    def start_countdown():
        try:

            config.countdown_timer = int(entry_countdown_time.get()) 
            config.key_1 = entry_key1.get()
            config.key_2 = entry_key2.get()
            config.hold_time = int(entry_hold_time.get())

            config.threshold = float(advanced_entry_threshold.get())


            countdown(config.countdown_timer, on_countdown_complete)
        except ValueError:
            messagebox.showerror("Invalid Input", " Invalid Input: Please double check your inputs and try again")

    #should be running on it's own thread
    def on_countdown_complete():
        #Calls START and loops forever
        label_start = ttk.Label(basic_tab, text="RUNNING", style="start.TLabel")
        label_start.pack(padx=10, pady=10)
        while True:
            start(config)

    # Start button
    start_button = ttk.Button(basic_tab, text="START", style="start.TButton",command=start_countdown)
    start_button.pack(pady=10)

    root.mainloop()



def startup_text():

    return """
    This Program is an auto pokemon finder for Pokemon Brick Bronze in Roblox.
    This program takes over and uses image recognition and auto key movements to automate
    Pokemon Hunting. This program can also be used to find shinys if you want.
    
    Quick Start Instructions:
    
        1. please Open Roblox and head to the tall grass 
            where you intend to do your shiny hunting with ample space to move around
        2. Please find the pokemon you are looking for from the following websites:

            Normal Hunting: https://play.pokemonshowdown.com/sprites/xyani/
            Shiny Hunting;  https://play.pokemonshowdown.com/sprites/xyani-shiny/
            
            Save As and store the pokemon in the image_folder.

        3. Hit Start and leave your computer on!
            Now you are free to leave the computer, and let it do its thing.
            When the program finds a match it will 'idle' to keep you connected, however 
            please don't leave this program on for hours as that has not been tested.

        Other Notes:

        This program only works for 16x9 monitors so no CRTS or ultrawide screens as I don't have
        those.

        I have a general "threshold" that works on most pokemon, if you are having trouble with
        false negatives or positives, please bring it down and check with the debug function.

        In the Advanced section, you have a threshold, which is 0.3 by standard. If you are having
        false positives (saying there is a pokemon match when there is not), bring it down by 
        dividing in half until you are not. If you are having false negatives (missing a match),
        double the threshold until you get a match. 

        If you are doing shiny hunting, 0.3 seems to work just fine for most things, however this 
        program has only caught shinys that are dramatically different than their non-shiny 
        counterparts.It sometimes struggles with shinys like Pidgey which variation is very slight. 
        Please test before usage as while this works well on my machine, I cannot vouch for yours.
        
        I tried to make it dummy proof but if you manage to break it, tell me how!

        https://github.com/jaloaguero
        jaloaguero@gmail.com
        
        """