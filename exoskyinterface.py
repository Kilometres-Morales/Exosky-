import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

colour_text = '#000C14'
colour_button_1 = '#788A99'
colour_button_2 = '#4C667C'
colour_bg_dark = '#D3D6DA'
colour_bg_light = '#EFE9E7'

header_font = ("Helvetica", 20, "bold")
text_font = ("Helvetica", 16)
italic_font = ("Helvetica", 14, "italic")


planetaimg = ctk.CTkImage(Image.open("Logo.png"), size=(26, 26))

class WelcomeScreen:
    def __init__(self, parent):
        self.parent = parent
        
        self.welcome_f = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.welcome_f.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.welcome_f.grid_rowconfigure((0,1, 2), weight=1, uniform="row")
        self.welcome_f.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        self.launch_b = ctk.CTkButton(self.welcome_f, text="LAUNCH", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_menu)
        self.launch_b.grid(row=1, column=1, sticky="nsew")

    def display(self):
        self.welcome_f.lift()
        
    def show_menu(self):
        self.menu = PlanetMenu(self.parent)
        self.menu.display()
    
class PlanetMenu:
    def __init__(self, parent):
        self.parent = parent 
       
        # Create the main menu frame but do not grid it yet
        self.planet_menu_f = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.planet_menu_f.place(relx=0, rely=0, relwidth=1, relheight=1)
    
        self.planet_menu_f.grid_rowconfigure((0, 2), weight=1, uniform="row")
        self.planet_menu_f.grid_rowconfigure(1, weight=6, uniform="row")
        self.planet_menu_f.grid_columnconfigure((0,2), weight=1, uniform="column")
        self.planet_menu_f.grid_columnconfigure(1, weight=6, uniform="column")
        
        self.key_b = ctk.CTkButton(self.planet_menu_f, text="KEY", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_key)
        self.key_b.grid(row=0, column=2, padx=20, pady=10)
        
        self.back_b = ctk.CTkButton(self.planet_menu_f, text="BACK", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_welcome)
        self.back_b.grid(row=0, column=0, padx=20, pady=10)
        
        self.planets_f = ctk.CTkFrame(self.planet_menu_f, fg_color=colour_bg_light)
        self.planets_f.grid(row=1, column=1, sticky="nsew")
        
        self.planets_f.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform="row")
        self.planets_f.grid_rowconfigure((0,1,2,3,4,5), weight=1, uniform="column")
        self.planets_f.grid_propagate(False) 
                
        # Main menu buttons
        self.planeta = ctk.CTkButton(self.planets_f, text="Planet A", image=planetaimg, fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_pa)
        self.planeta.grid(row=5, column=0, padx=20, pady=10)

        self.planetb = ctk.CTkButton(self.planets_f, text="Planet B", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_pb)
        self.planetb.grid(row=1, column=1, padx=20, pady=10)
        
        self.planetc = ctk.CTkButton(self.planets_f, text="Planet C", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_pc)
        self.planetc.grid(row=0, column=5, padx=20, pady=10)
        
        self.planetd = ctk.CTkButton(self.planets_f, text="Planet D", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_pd)
        self.planetd.grid(row=1, column=9, padx=20, pady=10)
        
        self.planete = ctk.CTkButton(self.planets_f, text="Planet E", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_pe)
        self.planete.grid(row=5, column=10, padx=20, pady=10)


    def display(self):
        # Show the main menu frame
        self.planet_menu_f.lift()
        
    def show_welcome(self):
        # Hide the center_frame and show the main_menu_frame
        self.welcome = WelcomeScreen(self.parent)
        self.welcome.display()
        
    def show_pa(self):
        self.pa = Planet(self.parent, 'a')
        self.pa.display()
        
    def show_pb(self):
        self.pb = Planet(self.parent, 'b')
        self.pb.display()
        
    def show_pc(self):
        self.pc = Planet(self.parent, 'c')
        self.pc.display()
        
    def show_pd(self):
        self.pd = Planet(self.parent, 'd')
        self.pd.display()
        
    def show_pe(self):
        self.pe = Planet(self.parent, 'e')
        self.pe.display()
        
    def show_key(self):
        self.key = Key(self.parent)
        self.key.display()
        
class Key:
    def __init__(self, parent):
        self.parent = parent
        
        self.key_f = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.key_f.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.key_f.grid_rowconfigure((0,1, 2), weight=1, uniform="row")
        self.key_f.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        self.key_center_f = ctk.CTkFrame(self.key_f, fg_color=colour_bg_light)
        self.key_center_f.grid(row=1, column=1, sticky="nsew")
        
        self.back_button = ctk.CTkButton(self.key_center_f, text="Back", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_menu)
        self.back_button.grid(row=1, column=1, sticky="nsew")
        
    def display(self):
        self.key_f.lift()
        
    def show_menu(self):
        self.menu = PlanetMenu(self.parent)
        self.menu.display()
        
class Planet:
    def __init__(self, parent, letter):
        self.parent = parent
        
        if letter == 'a':
            pass
        elif letter == 'b':
            pass
        elif letter == 'c':
            pass
        elif letter == 'd':
            pass
        elif letter == 'e':
            pass
        
        self.key_f = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.key_f.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.key_f.grid_rowconfigure((0,1, 2), weight=1, uniform="row")
        self.key_f.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        self.key_center_f = ctk.CTkFrame(self.key_f, fg_color=colour_bg_light)
        self.key_center_f.grid(row=1, column=1, sticky="nsew")
        
        self.back_button = ctk.CTkButton(self.key_center_f, text="Back", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_menu)
        self.back_button.grid(row=1, column=1, sticky="nsew")


    def display(self):
        self.key_f.lift()
        
    def show_menu(self):
        self.menu = PlanetMenu(self.parent)
        self.menu.display()
        

def main():
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root._state_before_windows_set_titlebar_color = 'zoomed'
    # _------------------
    root.title("Screen")
       
        # Create the main frame that fills the whole window
    main_frame = ctk.CTkFrame(root, fg_color=colour_bg_light)
    main_frame.pack(fill=ctk.BOTH, expand=True)
    
    # _------------------

    app = WelcomeScreen(main_frame)

    root.mainloop()

if __name__ == "__main__":
    main()