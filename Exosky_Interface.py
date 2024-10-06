import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

colour_text = '#000C14'
colour_button_1 = '#788A99'
colour_button_2 = '#4C667C'
#colour_bg_dark = '#D3D6DA'
colour_bg_light = '#EFE9E7'
black = '#080404'
colour_bg_dark = black

header_font = ("Helvetica", 20, "bold")
text_font = ("Helvetica", 16)
italic_font = ("Helvetica", 14, "italic")

#planetaimg = ctk.CTkImage(Image.open("Logo.png"), size=(26, 26))

class WelcomeScreen:
    def __init__(self, parent):
        self.parent = parent
        
        self.welcome_f = ctk.CTkFrame(self.parent, fg_color=black)
        self.welcome_f.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.welcome_f.grid_rowconfigure((0,1, 2), weight=1, uniform="row")
        self.welcome_f.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        self.rockimg = Image.open("RocketFin.jpg")
        self.rockimgfin = ImageTk.PhotoImage(self.rockimg)
        
        self.rocket = ctk.CTkLabel(self.welcome_f, text = '', fg_color=black, image = self.rockimgfin)
        self.rocket.grid(row=0, column=0, rowspan = 3, columnspan = 3, sticky = "nsew")
        
        self.launch_b_img = Image.open("LaunchButtonFin.jpg")
        self.launch_b_img_fin = ImageTk.PhotoImage(self.launch_b_img)
        
        self.launch_b = ctk.CTkButton(self.welcome_f, text = '', fg_color=black, image = self.launch_b_img_fin, command=self.show_menu)
        self.launch_b.grid(row=2, column=1)

        
        self.rocket.lower(self.launch_b)
    

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
    
        self.bg_image = ctk.CTkImage(Image.open("SpaceFin.jpg"), size=(self.planet_menu_f.winfo_screenwidth(), self.planet_menu_f.winfo_screenheight()))
        self.background_label = ctk.CTkLabel(self.planet_menu_f, image=self.bg_image, text="")
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
            
        self.planet_menu_f.grid_rowconfigure((0, 2), weight=1, uniform="row")
        self.planet_menu_f.grid_rowconfigure(1, weight=6, uniform="row")
        self.planet_menu_f.grid_columnconfigure((0,2), weight=1, uniform="column")
        self.planet_menu_f.grid_columnconfigure(1, weight=6, uniform="column")
        

        self.keybimg = Image.open("KeyButtonFin.png")
        self.keybimgfin = ImageTk.PhotoImage(self.keybimg)
        
        self.key_b = ctk.CTkButton(self.planet_menu_f, text='', fg_color=black, image = self.keybimgfin, command=self.show_key)
        self.key_b.grid(row=0, column=2, padx=20, pady=10)
        
        self.backbimg = Image.open("BackButton.png")
        self.backbimgfin = ImageTk.PhotoImage(self.backbimg)
        
        self.back_b = ctk.CTkButton(self.planet_menu_f, text = '', fg_color=black, image = self.backbimgfin, command=self.show_welcome)
        self.back_b.grid(row=0, column=0, padx=20, pady=10)
        
        self.planets_f = ctk.CTkFrame(self.planet_menu_f, fg_color="transparent")
        self.planets_f.grid(row=1, column=1, sticky="nsew")
        
        self.planets_f.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1, uniform="row")
        self.planets_f.grid_rowconfigure((0,1,2,3,4,5), weight=1, uniform="column")
        self.planets_f.grid_propagate(False) 

        self.bg_image = ctk.CTkImage(Image.open("SpaceFin.jpg"), size=(self.planets_f.winfo_screenwidth(), self.planets_f.winfo_screenheight()))
        self.background_label = ctk.CTkLabel(self.planets_f, image=self.bg_image, text="")
        self.background_label.grid(row=0, column=0, columnspan=12, rowspan=6)
                
        # Main menu buttons
        self.planeta = ctk.CTkButton(self.planets_f, text="Proxima Centauri b", fg_color='#00764B', hover_color='#056847', command=self.show_pa)
        self.planeta.grid(row=5, column=0, padx=20, pady=10,  columnspan = 2, sticky="nsew")

        self.planetb = ctk.CTkButton(self.planets_f, text="Wolf 1061 b", fg_color='#00764B', hover_color='#056847', command=self.show_pb)
        self.planetb.grid(row=2, column=1, padx=20, pady=10,  columnspan = 2, sticky="nsew")
        
        self.planetc = ctk.CTkButton(self.planets_f, text="Laland 21185 - b", fg_color='#C5051C', hover_color='#760311', command=self.show_pc)
        self.planetc.grid(row=0, column=5, padx=20, pady=10,  columnspan = 2, sticky="nsew")
        
        self.planetd = ctk.CTkButton(self.planets_f, text="Teegarden's Star d", fg_color='#22689C', hover_color='#174268', command=self.show_pd)
        self.planetd.grid(row=2, column=9, padx=20, pady=10,  columnspan = 2, sticky="nsew")
        
        self.planete = ctk.CTkButton(self.planets_f, text="Kepler-22B", fg_color='#00764B', hover_color='#056847', command=self.show_pe)
        self.planete.grid(row=5, column=10, padx=20, pady=10, columnspan = 2, sticky="nsew")
        
        self.rocket = Image.open("RocketOnly.jpg")
        self.rocket = ImageTk.PhotoImage(self.rocket)
        
        self.rocketimage = ctk.CTkLabel(self.planets_f, text = '', fg_color=black, image = self.rocket)
        self.rocketimage.grid(row=2, column=5, padx=20, pady=10, rowspan = 4, columnspan = 2)

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
        
        self.key_f.grid_rowconfigure((0,1,2), weight=1, uniform="row")
        self.key_f.grid_columnconfigure((0,1,2), weight=1, uniform="column")

        self.key_center_f = ctk.CTkFrame(self.key_f, fg_color=colour_bg_light)
        self.key_center_f.grid(row=0, column=1, rowspan = 3, sticky="nsew")
        
        self.backbimg = Image.open("BackButton.png")
        self.backbimgfin = ImageTk.PhotoImage(self.backbimg)
        
        self.back_b = ctk.CTkButton(self.key_f, text = '', fg_color=black, image = self.backbimgfin, command=self.show_menu)
        self.back_b.grid(row=0, column=0)
        
        self.key_center_f.grid_rowconfigure((0), weight=1, uniform="row")
        self.key_center_f.grid_columnconfigure((0), weight=1, uniform="column")
        
        self.keyimg = Image.open("KeyFin.jpg")
        self.keyimg.thumbnail((7000, 7000))
        self.keyimgfin = ImageTk.PhotoImage(self.keyimg)
        
        self.keyimg_label = ctk.CTkLabel(self.key_center_f, image=self.keyimgfin, text='', bg_color=colour_bg_dark)
        self.keyimg_label.grid(row=0, column=0, sticky = "nsew")


        
    def display(self):
        self.key_f.lift()
        
    def show_menu(self):
        self.menu = PlanetMenu(self.parent)
        self.menu.display()
        
class Planet:
    def __init__(self, parent, letter):
        self.parent = parent
        if letter == 'a':
            self.name = "Proxima Centauri b"
            self.img = "Planet A.png"
        elif letter == 'b':
            self.name = "Wolf 1061 b"
            self.img = "Planet B.png"
        elif letter == 'c':
            self.name = "Laland 21185 - b"
            self.img = "Planet C.png"
        elif letter == 'd':
            self.name = "Teegarden's Star d"
            self.img = "Planet D.png"
        elif letter == 'e':
            self.name = "Kepler-22B"
            self.img = "Planet E.png"
            
        
        self.key_f = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.key_f.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.key_f.grid_rowconfigure((0, 2), weight=1, uniform="row")
        self.key_f.grid_rowconfigure((1), weight=7, uniform="row")
        self.key_f.grid_columnconfigure((0,2), weight=1, uniform="column")
        self.key_f.grid_rowconfigure((1), weight=7, uniform="row")
        
        self.image = Image.open(self.img)
        self.image.thumbnail((7000, 7000))
        self.imagefin = ImageTk.PhotoImage(self.image)
        self.image_label = ctk.CTkLabel(self.key_f, image=self.imagefin, text='')
        self.image_label.grid(row=1, column=1, sticky="nsew")
        
        
        self.backbimg = Image.open("BackButton.png")
        self.backbimgfin = ImageTk.PhotoImage(self.backbimg)
        
        self.back_b = ctk.CTkButton(self.key_f, text = '', fg_color=black, image = self.backbimgfin, command=self.show_menu)
        self.back_b.grid(row=0, column=0)


    def display(self):
        self.key_f.lift()
        
    def show_menu(self):
        self.menu = PlanetMenu(self.parent)
        self.menu.display()
        

def main():
    ctk.set_appearance_mode("dark")
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