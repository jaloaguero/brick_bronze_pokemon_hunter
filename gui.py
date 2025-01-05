import tkinter as tk
from tkinter import ttk, messagebox
import time

from loop_logic import start

import threading

def validate_number_input(P):
    if P == "" or P.isdigit():
        return True
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
    root.geometry("850x700")  # Set the window size to 600x400
    root.iconbitmap("icons/program_icon.ico")

    s = ttk.Style()
    # Create style used by default for all Frames
    s.configure('TFrame', foreground="blue", background="yellow", font=("Arial", 12))
    
    

    # Validate that inputs are numbers
    vcmd = root.register(validate_number_input)

    # Create a Notebook widget (tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')
#######################################
    # Tab 1: Basic features
    basic_tab = ttk.Frame(notebook)
    notebook.add(basic_tab, text="Basic Features")

    
# Label to display output

    label_blurb = ttk.Label(basic_tab, text=startup_text())
    label_blurb.pack(padx=10, pady=10)
    #label
    label_countdown_time = ttk.Label(basic_tab, text="Countdown Time:")
    label_countdown_time.pack(padx=5, pady=5, anchor="nw")
    #text box
    entry_countdown_time = tk.Entry(basic_tab, validate="key")
    entry_countdown_time.pack(padx=5, pady=5, anchor="nw")
    entry_countdown_time.insert(0, config.countdown_time)  # Pre-fill with a predetermined number

    label_key1 = tk.Label(basic_tab, text="Key 1:")
    label_key1.pack(padx=5, pady=5, anchor="nw")

    entry_key1 = tk.Entry(basic_tab, validate="key")
    entry_key1.pack(padx=1, pady=5, anchor="nw")
    entry_key1.insert(0, config.key_1)  # Pre-fill with a predetermined number

    label_key2 = tk.Label(basic_tab, text="Key 2:")
    label_key2.pack(padx=5, pady=5,anchor="nw")

    entry_key2 = tk.Entry(basic_tab, validate="key")
    entry_key2.pack(padx=5, pady=5, anchor="nw")
    entry_key2.insert(0, config.key_2)  # Pre-fill with a predetermined number

    label_hold_time = tk.Label(basic_tab, text="Key Hold Time (Seconds):")
    label_hold_time.pack(padx=5, pady=5, anchor="nw")
    

    entry_hold_time = tk.Entry(basic_tab, validate="key", validatecommand=(vcmd, "%P"))
    entry_hold_time.pack(padx=5, pady=5, anchor="nw")
    entry_hold_time.insert(0, int(config.hold_time))  # Pre-fill with a predetermined number

    # Label to display the countdown
    countdown_label = tk.Label(basic_tab, text="Time left: ")
    countdown_label.pack(pady=10)
    
   ########################################################################################## 

    # Tab 2: Advanced features
    advanced_tab = ttk.Frame(notebook)
    notebook.add(advanced_tab, text="Advanced Features")

    # Example advanced feature: An extra entry box
    advanced_label = tk.Label(advanced_tab, text="Advanced Input:")
    advanced_label.pack(padx=5, pady=5)
    advanced_entry = tk.Entry(advanced_tab, validate="key", validatecommand=(vcmd, "%P"))
    advanced_entry.pack(padx=5, pady=5)
    advanced_entry.insert(0, "50")  # Pre-fill with a predetermined number

    # Function to start the countdown
    def start_countdown():
        try:

            config.countdown_timer = int(entry_countdown_time.get())  # Use the first text box for the countdown timer
            config.key_1 = entry_key1.get()
            config.key_2 = entry_key2.get()
            config.hold_time = int(entry_hold_time.get())
            


            countdown(config.countdown_timer, on_countdown_complete)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the countdown.")

    #should be running on it's own thread
    def on_countdown_complete():
        #Calls START and loops forever
        while True:
            start(config)

    # Start button
    start_button = tk.Button(basic_tab, text="Start", command=start_countdown)
    start_button.pack(pady=10)

    # Run the GUI loop

    output_label = tk.Label(basic_tab, text="placeholder: output text should be here")
    output_label.pack(pady=10)



    root.mainloop()



def startup_text():

    return """
    Quick Start Instructions:
    
        1. please Open Roblox and head to the tall grass where you intend to do your shiny hunting with ample space to move around
        2. Please find the pokemon you are looking for from the following websites:

            Normal Hunting: https://play.pokemonshowdown.com/sprites/xyani/
            Shiny Hunting;  https://play.pokemonshowdown.com/sprites/xyani-shiny/
            
            Save As and store the pokemon in the image_folder.
        3. Hit Start and leave your computer on!
        Now you are free to leave the computer, and let it do its thing.
        When the program finds a match it will 'idle' to keep you connected, however please don't leave this program on for hours as that has not been tested.    
        """