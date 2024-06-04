#importing stufffz
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, ttk, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import webbrowser
from pathlib import Path
import random

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=15, weight="bold", slant="italic")
        self.title("Recipe Generator")
        self.saved_recipes = []  

        self.resizable(False,False)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, RecipePage, CreditPage, MeatPage, VegetablePage, SavedRecipesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
        if page_name == "SavedRecipesPage":
            frame.update_recipes()

        page_geometries = {
            "MainMenu": "611x700",
            "RecipePage": "757x704",
            "CreditPage": "803x747",
            "VegetablePage": "894x1141",
            "MeatPage": "891x1132"
        }

        if page_name in page_geometries:
            self.geometry(page_geometries[page_name])
            
        if page_name in page_geometries:
                self.geometry(page_geometries[page_name])
            if page_name == "SavedRecipesPage":
                self.resizable(True,True)
            else:
                self.resizable(False,False)
    
    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you want to quit?'):
            self.destroy()

    def update_saved_recipes_page(self):
        self.frames["SavedRecipesPage"].update_recipes()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Faiz Adri\proj\tugas akhir\menuframe\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=770,
            width=612,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        try:

            def create_image(x, y, file):
                img = PhotoImage(file=relative_to_assets(file))
                self.canvas.create_image(x, y, image=img)
                return img

            def create_button(x, y, width, height, file, command):
                btn_img = PhotoImage(file=relative_to_assets(file))
                Button(
                    self,
                    image=btn_img,
                    borderwidth=0,
                    highlightthickness=0,
                    command=command,
                    relief="flat"
                ).place(x=x, y=y, width=width, height=height)
                return btn_img

            images_info = [
                (305.0, 102.0, "image_1.png"), (306.0, 404.0, "image_2.png"),
                (195.0, 305.0, "image_3.png"), (47.0, 181.0, "image_4.png"),
                (47.0, 279.0, "image_5.png"), (47.0, 379.0, "image_6.png"),
                (119.0, 181.0, "image_7.png"), (111.0, 279.0, "image_8.png"),
                (124.0, 379.0, "image_9.png"), (192.0, 223.0, "image_10.png"),
                (192.0, 321.0, "image_11.png"), (192.0, 420.0, "image_12.png"),
                (79.0, 147.0, "image_13.png"), (195.0, 567.0, "image_14.png"),
                (48.0, 509.0, "image_15.png")
            ]

            self.images = [create_image(x, y, file) for x, y, file in images_info]

            buttons_info = [
                (386.0, 147.0, 211.82, 45.0, "FindNGen.png", lambda: self.controller.show_frame('RecipePage')),
                (386.0, 201.0, 211.734, 44.0, "SavedRecipes.png", lambda: self.controller.show_frame('SavedRecipesPage')),
                (18.0, 648.0, 212.0, 32.0, "Credits.png", lambda: self.controller.show_frame('CreditPage'))
            ]

            self.buttons = [create_button(x, y, width, height, file, command) for x, y, width, height, file, command in buttons_info]

        except Exception as e:
            print(f"Error loading images or creating widgets: {e}")

        self.canvas.pack()

class RecipePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Faiz Adri\proj\tugas akhir\recipeframe\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=704,
            width=757,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        try:
            # Helper functions
            def create_image(x, y, file):
                img = PhotoImage(file=relative_to_assets(file))
                self.canvas.create_image(x, y, image=img)
                return img

            def create_button(x, y, width, height, file, command):
                btn_img = PhotoImage(file=relative_to_assets(file))
                btn = Button(
                    self,
                    image=btn_img,
                    borderwidth=0,
                    highlightthickness=0,
                    command=command,
                    relief="flat"
                )
                btn.place(x=x, y=y, width=width, height=height)
                return btn_img, btn

            # Background image
            self.image_image_1 = create_image(378.0, 352.0, "image_1.png")

            # Create buttons
            buttons_info = [
                (102.0, 437.0, 574.0, 45.68, "GenRec.png", lambda:self.random_recipe()),
                (229.411, 491.482, 318.241, 40.79, "FindRec.png", lambda:self.find_recipe()),
                (400.0, 541.0, 275.598, 22.782, "MeatRec.png", lambda: self.controller.show_frame('MeatPage')),
                (102.0, 541.0, 275.598, 22.782, "VegRec.png", lambda: self.controller.show_frame('VegetablePage')),
                (45.316, 628.685, 133.475, 42.515, "Menu.png", lambda: self.controller.show_frame('MainMenu')),
                (599.325, 628.685, 133.475, 42.515, "Credits.png", lambda: self.controller.show_frame('CreditPage'))
            ]
            self.buttons = [create_button(x, y, width, height, file, command) for x, y, width, height, file, command in buttons_info]

            # Create the Entry widget with an image background
            self.canvas.create_rectangle(
                106.0,
                49.0,
                760.0,
                254.0,
                outline=""
            )

        except Exception as e:
            print(f"Error loading images or creating widgets: {e}")

        self.canvas.pack()

        self.text = tk.Text(self, height=10, width=60)
        self.text.pack()
        self.text.place(x=150.017, y=150)

        # Create ComboBoxes directly on top of the GenerateRecipe button
        self.combobox1 = ttk.Combobox(self, values=["Meat", "Vegetables"])
        self.combobox1.place(x=215.017, y=355.0, width=353.115, height=20)

        self.combobox2 = ttk.Combobox(self, values=["", "Meat", "Vegetables"])
        self.combobox2.place(x=215.017, y=390.0, width=353.115, height=20)

    def find_recipe(self):
        value1 = self.combobox1.get()
        value2 = self.combobox2.get()

        if value1 == "Meat" and value2 == "":
            self.controller.show_frame('MeatPage')
        elif value1 == "Vegetables" and value2 == "":
            self.controller.show_frame('VegetablePage')
        else:
            messagebox.showwarning("Selection Error", "Please select a main ingredient and optionally a sub ingredient.")

    def random_recipe(self):
        print('test')
        value1 = self.combobox1.get()
        value2 = self.combobox2.get()
        
        if value1 == "Meat" and value2 == "":
            self.random_meat_recipe()
        elif value1 == "Vegetables" and value2 == "":
            self.random_vegetable_recipe()
        elif value1 == "Meat" and value2 == "Vegetables" or value1 == "Vegetables" and value2 == "Meat":
            self.random_meatveggie_recipe()
        else:
            messagebox.showwarning("Selection Error", "Please select a main ingredient and optionally a sub ingredient.")

    def random_meat_recipe(self):
        utilities = ["pan", "grill", "oven"]
        addons = ["olive oil", "butter", "garlic"]
        meat_ingredients = ["chicken breast", "beef steak", "pork chops"]
        temperature = random.randint(150, 200)
        seasoning = ["salt", "pepper", "paprika"]
        teaspoon = ["1 teaspoon", "2 teaspoons"]
        rest = random.randint(5, 15)

        recipe = (
            f"On a {random.choice(utilities)}, sizzling already with {random.choice(addons)}, cook {random.choice(meat_ingredients)} at {temperature} Celsius\n"
            f"Add {random.choice(teaspoon)} of {random.choice(seasoning)}\n"
            f"Then let the {random.choice(meat_ingredients)} rest for about {rest} minutes before serving!"
        )
        self.display_recipe(recipe)

    def random_vegetable_recipe(self):
        utilities = ["sink", "bowl"]
        vegetable_ingredients = ["carrots", "broccoli", "spinach"]
        toppings = ["sesame seeds", "chopped nuts", "grated cheese"]
        rest = random.randint(5, 15)

        recipe = (
            f"Wash the {random.choice(vegetable_ingredients)} in a {random.choice(utilities)} for {rest} minutes\n"
            f"Top it off with some {random.choice(toppings)} and serve!"
        )
        self.display_recipe(recipe)
    
    def random_meatveggie_recipe(self):
        utilities = ["pot", "pan"]
        unnamed = ["water", "broth"]
        unnamedno2 = ["carrots", "potatoes"]
        meat_ingredients = ["chicken breast", "beef steak", "pork chops"]
        vegetable_ingredients = ["carrots", "broccoli", "spinach"]
        temperature = random.randint(150, 200)
        rest = random.randint(5, 15)

        recipe = (
            f"Mix {random.choice(unnamed)} and {random.choice(unnamedno2)} in a {random.choice(utilities)} together, let it boil at {temperature} Celsius for about {rest} minutes.\n"
            f"Once it's all mixed properly, put {random.choice(meat_ingredients)} before {random.choice(vegetable_ingredients)} so the soup can absorb the meat's juices and make the vegetables more tasty.\n"
            f"Keep stirring for {rest} minutes before serving! Vóila!"
        )
        self.display_recipe(recipe)

    def display_recipe(self, recipe):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, recipe)
        self.text.config(state=tk.DISABLED)

class MeatPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Faiz Adri\proj\tugas akhir\meatframe\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1132,
            width=891,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollable_frame = tk.Frame(self.canvas, bg="#FFFFFF")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.inputGet()
        self.images = {}

        try:
            def create_image(x, y, file):
                img_path = relative_to_assets(file)
                img = PhotoImage(file=img_path)
                self.canvas.create_image(x, y, image=img)
                return img

            def create_button(x, y, width, height, file, command):
                btn_img_path = relative_to_assets(file)
                btn_img = PhotoImage(file=btn_img_path)
                btn = Button(
                    self,
                    image=btn_img,
                    borderwidth=0,
                    highlightthickness=0,
                    command=command,
                    relief="flat"
                )
                btn.place(x=x, y=y, width=width, height=height)
                return btn_img, btn   
            
            image_info = [
                (447.0, 573.0, "image_1.png"),
                (77.0, 318.0, "image_2.png")
            ]

            self.images = [create_image(x, y, file) for x, y, file in image_info]

            buttons_info = [
                #main buttons
                (2.0, 0.0, 282.2731628417969, 54.0, "button_1.png", lambda: controller.show_frame('MainMenu')),
                (284.0, 0.0, 328.0, 54.0, "button_2.png", lambda: controller.show_frame('RecipePage')),
                (612.0, 0.0, 282.2731628417969, 54.0, "button_3.png", lambda: controller.show_frame('CreditPage')), 
                #recipe titles
                (166.0, 94.0, 202.0, 54.0, "button_4.png", lambda: self.FilipinoWindow()),
                (389.0, 94.0, 202.0, 54.0, "button_5.png", lambda: self.SPAPCWindow()),
                (612.0, 94.0, 202.0, 54.0, "button_8.png", lambda: self.BSLidersWindow()),
                #more
                (166.0, 546.559, 646.214, 34.0, "button_6.png", lambda: self.Extras()),
                #description (bottom row to top row)
                (166.0,154.0,202.0,366.0, "button_16.png", lambda: print('test')),
                (390.0,154.0,202.0,366.0, "button_17.png", lambda: print('test')),
                (614.0,154.0,202.0,366.0, "button_15.png", lambda: print('test'))
            ]

            self.buttons = [create_button(x, y, width, height, file, command) for x, y, width, height, file, command in buttons_info]

        except Exception as e:
            print(f"Error loading images or creating widgets: {e}")

        self.canvas.pack()

    def closewindow(self, window):
        window.destroy()

    def FilipinoWindow(self):
        OpenWindow = Toplevel(self)
        filipinoscorch = LabelFrame(OpenWindow, text='Filipino Beef Steak')
        filipinoscorch.pack(padx=20, pady=10)  

        buttonInfo = Button(OpenWindow, text='Show Ingredients', command=self.info1)
        checkbutton = Checkbutton(filipinoscorch, variable=self.CheckButton1_var,
                                  command=lambda: self.save_recipe(self.CheckButton1_var, 'Filipino Beef Steak', self.Filipino_Beef_Steak_Recipe()) )

        label = Label(filipinoscorch, text=self.Filipino_Beef_Steak_Recipe())

        checkbutton.pack()
        buttonInfo.pack()
        label.pack()

        buttonexit = Button(OpenWindow, text='Exit', command=lambda: self.closewindow(OpenWindow))
        buttonexit.pack()

    def SPAPCWindow(self):
        OpenWindow = Toplevel(self)
        sweetpotatoskin = LabelFrame(OpenWindow, text="Stuffed Sweet Potato Skin Tacos")
        sweetpotatoskin.pack(padx=20, pady=10)  

        button2Info = tk.Button(OpenWindow, text='Show Ingredients', command=self.info2)
        CheckButton2 = tk.Checkbutton(OpenWindow, variable=self.CheckButton2_var,
                                      command=lambda: self.save_recipe(self.CheckButton2_var, 'Stuffed Sweet Potato Skin Tacos', self.Sweet_Potato_Skin_Recipe()))
        label2 = tk.Label(OpenWindow, text=self.Sweet_Potato_Skin_Recipe())

        label2.pack()
        button2Info.pack()
        CheckButton2.pack()

        buttonexit = Button(OpenWindow, text='Exit', command=lambda: self.closewindow(OpenWindow))
        buttonexit.pack()

    def BSLidersWindow(self):
        OpenWindow = Toplevel(self)
        beefsliders = LabelFrame(OpenWindow, text="Beef Sliders")
        beefsliders.pack(padx=20, pady=10)  # Center the label frame with fill

        button3Info = tk.Button(OpenWindow, text='Show Ingredients', command=self.info3)
        CheckButton3 = tk.Checkbutton(OpenWindow, variable=self.CheckButton3_var,
                                      command=lambda: self.save_recipe(self.CheckButton3_var, 'Beef Sliders', self.Beef_Sliders_Recipe()))
        label3 = tk.Label(OpenWindow, text=self.Beef_Sliders_Recipe())

        label3.pack()
        button3Info.pack()
        CheckButton3.pack()

        buttonexit = Button(OpenWindow, text='Exit', command=lambda: self.closewindow(OpenWindow))
        buttonexit.pack()

    def open_url(self, url):
        webbrowser.open_new(url)

    def Extras(self):
        OpenWindow = Toplevel(self)

        recipes = [
            ("Honey Garlic Chicken Breasts", "https://www.recipetineats.com/honey-garlic-chicken/"),
            ("Marry Me Chicken", "https://littlesunnykitchen.com/marry-me-chicken/"),
            ("Creamy Garlic Chicken", "https://www.budgetbytes.com/creamy-garlic-chicken/")
        ]

        for recipe_name, url in recipes:
            link = Label(OpenWindow, text=recipe_name, fg='blue', cursor='hand2', font=('Times New Roman', 20))
            link.pack()
            link.bind('<Button-1>', lambda e, url=url: self.open_url(url))

    def inputGet(self):
        self.CheckButton1_var = tk.IntVar()
        self.CheckButton2_var = tk.IntVar()
        self.CheckButton3_var = tk.IntVar()
    
    def Filipino_Beef_Steak_Recipe(self):
        return (
            'Step 1\n'
            'Place sliced beef in a large bowl. Whisk together lemon juice, soy sauce, sugar, salt, and pepper in a small bowl; pour over beef and toss to coat. Stir in cornstarch. Cover and refrigerate for 1 hour to overnight.\n'
            '\nStep 2\n'
            'Heat vegetable oil in a large skillet over medium heat.\n'
            '\nStep 3\n'
            'Remove beef slices from marinade, shaking to remove any excess liquid. Discard marinade.\n'
            '\nStep 4\n'
            'Working in batches, fry beef slices in hot oil until they start to firm and are reddish-pink and juicy in the center, 2 to 4 minutes per side. Transfer beef slices to a serving platter.\n'
            '\nStep 5\n'
            'Heat olive oil in a small skillet over medium heat. Cook and stir onion and garlic in hot oil until onion is golden brown, 5 to 7 minutes; spoon over beef slices.'
        )

    def Sweet_Potato_Skin_Recipe(self):
        return (
            'Step 1\n'
            'Preheat the oven to 400 degrees F (200 degrees C) and line a sheet pan with foil.\n'
            '\nStep 2\n'
            'Slice each sweet potato in half lengthwise, and rub cut surfaces and skins with olive oil. Evenly sprinkle about 1 tablespoon taco seasoning all over sweet potatoes and place on the prepared pan, cut side down.\n'
            '\nStep 3\n'
            'Roast in the preheated oven for 15 minutes, then turn and continue roasting until potatoes are fork-tender, about 15 minutes more.\n'
            '\nStep 4\n'
            'Meanwhile, heat a large skillet over medium heat. Cook and stir ground beef in the hot skillet until browned and crumbly, breaking up clumps with a spatula, 5 to 8 minutes; drain excess fat.\n'
            '\nStep 5\n'
            'Sprinkle meat with remaining 2 tablespoons taco seasoning mix and stir in water. Simmer until liquid is evaporated, about 5 minutes.\n'
            '\nStep 6\n'
            'Place roasted sweet potatoes on a cutting board and scoop out most of the sweet potato flesh, leaving about 1/4-inch flesh inside the skins. Cut the sweet potato flesh into bite-sized pieces and stir into the ground beef mixture.\n'
            '\nStep 7\n'
            'Fill each sweet potato shell with beef and sweet potato mixture, gently pressing to fill. Place filled sweet potato skins on a serving plate and top with taco toppings.'
        )
    
    def Beef_Sliders_Recipe(self):
        return (
            'Step 1\n'
            'Preheat the oven to 350 degrees F (175 degrees C). Brush the bottom and sides of a 9x13-inch baking dish with melted butter until lightly coated.\n'
            '\nStep 2\n'
            'Place bottom half of rolls in baking dish and top evenly with roast beef slices. Drizzle BBQ sauce evenly over roast beef and dollop cheese sauce evenly over the top. Place top roll halves on top.\n'
            '\nStep 3\n'
            'Stir together remaining butter, garlic powder, and onion powder and brush evenly over bun tops.  Sprinkle with bagel seasoning.\n'
            '\nStep 4\n'
            'Bake in the preheated oven until the center is warm and melted, and bread is toasted and golden brown, 12 to 14 minutes.'
        )

    def info1(self):
        messagebox.showinfo("Ingredients for Filipino Beef Steak", 
                            "Ingredients:\n- Beef\n- Lemon juice\n- Soy sauce\n- Sugar\n- Salt\n- Pepper\n- Cornstarch\n- Vegetable oil\n- Onion\n- Garlic\n- Olive oil")

    def info2(self):
        messagebox.showinfo("Ingredients for Stuffed Sweet Potato Skin Tacos", 
                            "Ingredients:\n- Sweet potatoes\n- Olive oil\n- Taco seasoning\n- Ground beef\n- Water\n- Taco toppings")

    def info3(self):
        messagebox.showinfo("Ingredients for Roasted Beef Sliders:",
                            "\n- 4 tablespoons butter, melted, divided\n- 1 (12 roll) package Hawaiian rolls, split in half horizontally\n- 12 ounces deli roast beef\n- 1/2 cup  thin tangy BBQ sauce, such as Arby's® Original Sauce\n- 1 cup Cheddar cheese sauce\n- 1/4 teaspoon garlic powder\n- 1/4 teaspoon onion powder\n- 2 teaspoons everything bagel seasoning")

    def save_recipe(self, var, title, recipe):
        if var.get() == 1:
            if (title, recipe) not in self.controller.saved_recipes:
                self.controller.saved_recipes.append((title, recipe))
        else:
            if (title, recipe) in self.controller.saved_recipes:
                self.controller.saved_recipes.remove((title, recipe))
        self.controller.update_saved_recipes_page()
    
    def uncheck_all(self):
        self.CheckButton1_var.set(0)
        self.CheckButton2_var.set(0)
        self.CheckButton3_var.set(0)


class VegetablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Faiz Adri\proj\tugas akhir\vegetableframe\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=3000,
            width=891,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.create_veggie_recipes()

        self.images = {}

        try:
            def create_image(x, y, file):
                img_path = relative_to_assets(file)
                img = PhotoImage(file=img_path)
                self.canvas.create_image(x, y, image=img)
                return img

            def create_button(x, y, width, height, file, command):
                btn_img_path = relative_to_assets(file)
                btn_img = PhotoImage(file=btn_img_path)
                btn = Button(
                    self,
                    image=btn_img,
                    borderwidth=0,
                    highlightthickness=0,
                    command=command,
                    relief="flat"
                )
                btn.place(x=x, y=y, width=width, height=height)
                return btn_img, btn   
            
            image_info = [
                (447.0, 573.0, "image_1.png"),
                (77.0, 318.0, "image_2.png"),
                (77.0, 848.0, "image_3.png")
            ]

            self.images = [create_image(x, y, file) for x, y, file in image_info]

            buttons_info = [
                #main buttons
                (2.0, 0.0, 282.2731628417969, 54.0, "button_1.png", lambda: controller.show_frame('MainMenu')),
                (284.0, 0.0, 328.0, 54.0, "button_2.png", lambda: controller.show_frame('RecipePage')),
                (612.0, 0.0, 282.2731628417969, 54.0, "button_3.png", lambda: controller.show_frame('CreditPage')), 
                #recipe titles
                (166.0, 94.0, 202.0, 54.0, "button_4.png", lambda: self.VFTWINDOW()),
                (389.0, 94.0, 202.0, 54.0, "button_5.png", lambda: self.SP2CWINDOW()),
                (612.0, 94.0, 202.0, 54.0, "button_8.png", lambda: self.VPancakesWINDOW()),
                #more
                (166.0, 546.559, 646.214, 34.0, "button_6.png", lambda: self.Extras),
                #description (bottom row to top row)
                (166.0,154.0,202.0,366.0, "button_16.png", lambda: print('Tis a placeholder!')),
                (390.0,154.0,202.0,366.0, "button_17.png", lambda: print('Tis a placeholder!')),
                (614.0,154.0,202.0,366.0, "button_15.png", lambda: print('Tis a placeholder!'))
                #check
            ]

            self.buttons = [create_button(x, y, width, height, file, command) for x, y, width, height, file, command in buttons_info]

        except Exception as e:
            print(f"Error loading images or creating widgets: {e}")

        self.canvas.pack()

    def save_recipe(self, var, title, recipe_func):
        if var.get() == 1:
            self.controller.frames['SavedRecipesPage'].add_recipe(title, recipe_func())

    def VFTWINDOW(self):
        NewWindowOpen = Toplevel(self)
        VFT = LabelFrame(NewWindowOpen, text='Vegan French Toast')
        VFT.pack(padx=20, pady=10, anchor='center')  # Center the label frame with fill

        buttonInfo = Button(NewWindowOpen, text='Show Ingredients', command=self.info1)
        buttonexit = Button(NewWindowOpen, text='Exit', command=lambda: self.closewindow(NewWindowOpen))
        CheckButton = tk.Checkbutton(NewWindowOpen, variable=self.CheckButton1_var,
                                      command=lambda: self.save_recipe(self.CheckButton1_var, 'Vegan French Toast', self.VFT_Recipe()))


        label = Label(NewWindowOpen, text=self.VFT_Recipe())

        CheckButton.pack()
        buttonInfo.pack()
        label.pack()
        buttonexit.pack()

    def SP2CWINDOW(self):
        SP2CWINDOW = Toplevel(self)
        SP2C = LabelFrame(SP2CWINDOW, text="Sweet Potato and Peanut Curry")
        SP2C.pack(padx=20, pady=10, anchor='center')  # Center the label frame with fill

        button2Info = Button(SP2CWINDOW, text='Show Ingredients', command=self.info2)
        label2 = Label(SP2CWINDOW, text=self.SPAPC_Recipe())
        CheckButton = tk.Checkbutton(SP2CWINDOW, variable=self.CheckButton2_var,
                                      command=lambda: self.save_recipe(self.CheckButton2_var, 'Sweet Potato and Peanut Curry', self.SPAPC_Recipe()))

        buttonexit = Button(SP2CWINDOW, text='Exit', command=lambda: self.closewindow(SP2CWINDOW))

        CheckButton.pack()
        button2Info.pack()
        label2.pack()
        buttonexit.pack()

    def VPancakesWINDOW(self):
        VPWINDOW = Toplevel(self)
        SP2C = LabelFrame(VPWINDOW, text="Vegan Pancakes")
        SP2C.pack(padx=20, pady=10, anchor='center')  # Center the label frame with fill

        button2Info = Button(VPWINDOW, text='Show Ingredients', command=self.info2)
        label2 = Label(VPWINDOW, text=self.VeganPANCAKES())
        CheckButton = tk.Checkbutton(VPWINDOW, variable=self.CheckButton3_var,
                                      command=lambda: self.save_recipe(self.CheckButton3_var, 'Vegan Pancakes', self.VeganPANCAKES()))

        buttonexit = Button(VPWINDOW, text='Exit', command=lambda: self.closewindow(VPWINDOW))

        CheckButton.pack()
        button2Info.pack()
        label2.pack()
        buttonexit.pack()

        self.canvas.pack()

    def open_url(self, url):
        webbrowser.open_new(url)

    def Extras(self):
        OpenWindow = Toplevel(self)

        recipes = [
            ("Strawberry Kanten Japanese Jelly", "https://www.forksoverknives.com/recipes/vegan-desserts/strawberry-kanten-japanese-jelly-treats/"),
            ("Perfect Summer Fruit Salad", "https://www.allrecipes.com/recipe/214947/perfect-summer-fruit-salad/"),
            ("Creamy Vegan Mushroom Stroganoff", "https://rainbowplantlife.com/creamy-vegan-mushroom-stroganoff/")
        ]

        for recipe_name, url in recipes:
            link = Label(OpenWindow, text=recipe_name, fg='blue', cursor='hand2', font=('Times New Roman', 20))
            link.pack()
            link.bind('<Button-1>', lambda e, url=url: self.open_url(url))

    def create_veggie_recipes(self):
        self.CheckButton1_var = tk.IntVar()
        self.CheckButton2_var = tk.IntVar()
        self.CheckButton3_var = tk.IntVar()

    def VFT_Recipe(self):
        return (
            'Step 1\n'
            'In a blender combine milk, cashews, and dates and blend until smooth.\n'
            '\nStep 2\n'
            'While still blending add the rest of ingredients.\n'
            '\nStep 3\n'
            'Pour the batter into a pie or cake dish, dip both sides of each slice of bread in the batter, or use a spatula to evenly spread a layer of batter on the slice of bread.\n'
            '\nStep 4\n'
            'Then brown in a lightly oiled skillet.\n'
            '\nStep 5\n'
            'Top with pure maple syrup or your favorite fruit topping.'
        )

    def SPAPC_Recipe(self):
        return (
            'Step 1\n'
            'Melt 1 tbsp coconut oil in a saucepan over a medium heat and soften 1 chopped onion for 5 mins. Add 2 grated garlic cloves and a grated thumb-sized piece of ginger, and cook for 1 min until fragrant.\n'
            '\nStep 2\n'
            'Stir in 3 tbsp Thai red curry paste, 1 tbsp smooth peanut butter and 500g sweet potato, peeled and cut into chunks, then add 400ml coconut milk and 200ml water.\n'
            '\nStep 3\n'
            'Bring to the boil, turn down the heat and simmer, uncovered, for 25-30 mins or until the sweet potato is soft.\n'
            '\nStep 4\n'
            'Stir through 200g spinach and the juice of 1 lime, and season well. Serve with cooked rice, and if you want some crunch, sprinkle over a few dry roasted peanuts.'
        )
    
    def VeganPANCAKES(self):
        return (
            'Step 1\n'
            'Whisk the flour, baking powder, sugar, vanilla extract and a pinch of salt in a bowl using a balloon whisk until mixed. Slowly pour in the milk until you get a smooth, thick batter.\n'
            '\nStep 2\n'
            'Heat a little of the oil in a non-stick frying pan over a medium-low heat, and add 2 tbsp batter into the pan at a time to make small, round pancakes. You will need to do this in batches of two-three at a time. Cook for 3-4 mins until the edges are set, and bubbles are appearing on the surface. Flip the pancakes over and cook for another 2-3 mins until golden on both sides and cooked through. Keep warm in a low oven while you cook the remaining pancakes.\n'
            '\nStep 3\n'
            'Serve stacked with lots of toppings of your choice, or serve with bowls of toppings for everyone to help themselves.\n'
        )

    def info1(self):
        messagebox.showinfo("Ingredients for Vegan French Toast:",
                            "\n- 1 Cup organic soy or rice milk\n- 1 Cup cashews unsalted\n- 3/4 Cup Dates Pitted\n- 2 tbsp egg replacer\n- 1/2 tsp sea salt\n- 1 tbsp vanilla\n- 8-10 slices of your favorite bread")

    def info2(self):
        messagebox.showinfo("Ingredients for Roasted Sweet Potato and Peanut Curry:",
                            "\n- 1 tbsp coconut oil\n- 1 onion, chopped\n- 2 garlic cloves, grated\n- thumb-sized piece ginger, grated\n- 3 tbsp Thai red curry paste (check the label to make sure its vegetarian/ vegan)\n- 1 tbsp smooth peanut butter\n- 500g sweet potato, peeled and cut into chunks\n- 400ml can coconut milk\n- 200g bag spinach\n- 1 lime, juiced\n- cooked rice, to serve (optional)\n- dry roasted peanuts, to serve (optional)")

    def info3(self):
        messagebox.showinfo("Ingredients for Vegan Pancakes:",
                            "\n- 4 300g self-raising flour\n- 1 tsp baking powder\n- 1 tbsp sugar (any kind)\n- 1 tbsp vanilla extract\n 400ml plant-based milk (such as oat, almond or soya)\n 1 tbsp vegetable oil for cooking")

    def closewindow(self, window):
        window.destroy()

    def save_recipe(self, var, title, recipe):
        if var.get() == 1:
            if (title, recipe) not in self.controller.saved_recipes:
                self.controller.saved_recipes.append((title, recipe))
        else:
            if (title, recipe) in self.controller.saved_recipes:
                self.controller.saved_recipes.remove((title, recipe))
        self.controller.update_saved_recipes_page()
    
    def uncheck_all(self, window):
        self.CheckButton1_var.set(0)
        self.CheckButton2_var.set(0)

class SavedRecipesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.buttonMenu = tk.Button(self, text="Return to Main Menu", 
                               command=lambda: controller.show_frame('MainMenu'))
        self.buttonMenu.pack(padx=5, pady=5)

        canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(canvas)

        scrollbar = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='n')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def update_recipes(self):
        # Clear the scrollable frame content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not self.controller.saved_recipes:
            label = tk.Label(self.scrollable_frame, text="No saved recipes.", font=self.controller.title_font)
            label.pack(side='top', fill='x', pady=10)
        else:
            for title, recipe in self.controller.saved_recipes:
                frame = tk.LabelFrame(self.scrollable_frame, text=title)
                frame.pack(padx=20, pady=10, fill='x', expand=True) 
                label = tk.Label(frame, text=recipe)
                label.pack()

        clearButton = tk.Button(self.scrollable_frame, text='Clear All', command=self.AYS)
        clearButton.pack(pady=10)

    def AYS(self):
        if self.controller.saved_recipes and messagebox.askyesno(title="Clear All", message="Are you sure you would like to clear your saved recipes?"):
            self.clear_recipes()
        else:
            messagebox.showinfo("", "There is nothing.")

    def clear_recipes(self):
        self.controller.saved_recipes.clear()
        self.update_recipes()

class CreditPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Faiz Adri\proj\tugas akhir\creditsframe\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def create_image(x, y, file):
            img = PhotoImage(file=relative_to_assets(file))
            self.canvas.create_image(x, y, image=img)
            return img

        def create_button(x, y, width, height, file, command):
            btn_img = PhotoImage(file=relative_to_assets(file))
            Button(
                self,
                image=btn_img,
                borderwidth=0,
                highlightthickness=0,
                command=command,
                relief="flat"
            ).place(x=x, y=y, width=width, height=height)
            return btn_img

        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=747,
            width=803,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack()

        try:
            # Create images
            self.image_image_1 = create_image(401.0, 373.0, "image_1.png")
            self.image_image_2 = create_image(401.0, 373.0, "image_2.png")
            self.image_image_3 = create_image(577.0, 404.0, "image_3.png")

            # Create button
            self.button_image_1 = create_button(330.467, 666.998, 141.682, 45.284, "button_1.png", command=lambda: self.controller.show_frame('MainMenu'))

            # Create text
            text_specs = [
                (190.0, 330.0, "Muhammad Faiz Adri Ar Rasyid", "InriaSerif Bold", 32),
                (220.0, 109.0, "Jurusan Teknik Komputer", "Inter Bold", 32),
                (276.0, 161.0, "Angkatan 2023", "Inter Bold", 32),
                (289.0, 380.0, "21120123140183", "InriaSerif Bold", 32)
            ]
            for x, y, text, font, size in text_specs:
                self.canvas.create_text(x, y, anchor="nw", text=text, fill="#000000", font=(font, size * -1))

            # Create rectangles
            rectangle_specs = [
                (157.0, 373.0, 645.0, 374.0),
                (156.0, 152.0, 645.0, 154.0)
            ]
            for x1, y1, x2, y2 in rectangle_specs:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="")
        except Exception as e:
            print(f"Error loading images or creating widgets: {e}")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
