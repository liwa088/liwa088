import pandas as pd
from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class PokemonData:  # Define a class to manage Pokémon data

    def __init__(self):  # Define the initialization method
        self.original_csv_path = "pokemon.csv"  # Set the path to the original Pokémon data CSV file
        self.df = pd.read_csv(self.original_csv_path)  # Read the CSV file into a pandas DataFrame
        self.provided_names = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmeleon', 'Charizard', 'Charmander', 'Squirtle',
                               'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna',
                               'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot']  # List of provided Pokémon names
        self.filtered_df = self.df[self.df['Name'].isin(self.provided_names)]  # Filter DataFrame for provided Pokémon
        self.filtered_df = self.filtered_df[['#', 'Name', 'Type 1', 'HP', 'Attack']]  # Select specific columns
        self.filtered_df.columns = ['#', 'Name', 'Element', 'HP', 'Attack']  # Rename columns for clarity

        self.filtered_csv_path = 'filtered_pokemon.csv'  # Set the path for the filtered Pokémon data CSV file
        self.filtered_df.to_csv(self.filtered_csv_path, index=False)  # Save filtered DataFrame to CSV file
        print(f"Filtered data saved to {self.filtered_csv_path}")  # Print confirmation message


class BattleDataCollector:  # Define a class to collect battle data

    def __init__(self):  # Define the initialization method
        self.data = {  # Initialize a dictionary to store battle data
            'round': [],  # List to store round numbers
            'attack_number': [],  # List to store attack numbers
            'player_1': [],  # List to store player 1 names
            'player_2': [],  # List to store player 2 names
            'player_1_health': [],  # List to store player 1 health
            'player_2_health': [],  # List to store player 2 health
            'damage_done_by_p1': [],  # List to store damage done by player 1
            'damage_done_by_p2': [],  # List to store damage done by player 2
            'critical_1': [],  # List to store critical hit status for player 1
            'critical_2': [],  # List to store critical hit status for player 2
            'elemental_1': [],  # List to store elemental effectiveness for player 1
            'elemental_2': []  # List to store elemental effectiveness for player 2
        }
        self.round_number = 0  # Initialize round number
        self.attack_number = 1  # Initialize attack number

    def record_attack(self, player_1, player_2, player_1_health, player_2_health, damage_1, damage_2, critical_1, critical_2, elemental_1, elemental_2):
        # Record attack data into respective lists in the data dictionary
        self.data['round'].append(self.round_number)  # Append current round number
        self.data['attack_number'].append(self.attack_number)  # Append current attack number
        self.data['player_1'].append(player_1)  # Append player 1 name
        self.data['player_2'].append(player_2)  # Append player 2 name
        self.data['player_1_health'].append(player_1_health)  # Append player 1 health
        self.data['player_2_health'].append(player_2_health)  # Append player 2 health
        self.data['damage_done_by_p1'].append(damage_1)  # Append damage done by player 1
        self.data['damage_done_by_p2'].append(damage_2)  # Append damage done by player 2
        self.data['critical_1'].append(0 if critical_1 == 'N/A' else int(critical_1))  # Append critical hit status for player 1
        self.data['critical_2'].append(0 if critical_2 == 'N/A' else int(critical_2))  # Append critical hit status for player 2
        self.data['elemental_1'].append(0 if elemental_1 == 'N/A' else int(elemental_1))  # Append elemental effectiveness for player 1
        self.data['elemental_2'].append(0 if elemental_2 == 'N/A' else int(elemental_2))  # Append elemental effectiveness for player 2

    def next_round(self):  # Define method to proceed to the next round
        self.round_number += 1  # Increment round number
        self.attack_number = 1  # Reset attack number for the new round

    def next_attack(self):  # Define method to proceed to the next attack
        self.attack_number += 1  # Increment attack number

    def save_to_excel(self, filename):  # Define method to save battle data to an Excel file
        df = pd.DataFrame(self.data)  # Create a DataFrame from the collected data
        df.to_excel(filename, index=False)  # Save DataFrame to an Excel file without index


class WelcomeWindow(Frame):  # Define a class for the welcome window

    pokemon_image_mapping = {  # Dictionary to map Pokémon names to their image file paths
        "Bulbasaur": "images/Bulbasaur.png",  # Bulbasaur image file path
        "Squirtle": "images/Squirtle.png",  # Squirtle image file path
        "Charmander": "images/Charmander.png",  # Charmander image file path
        "Caterpie": "images/Caterpie.png",  # Caterpie image file path
        "Weedle": "images/Weedle.png",  # Weedle image file path
        "Pidgey": "images/Pidgey.png",  # Pidgey image file path
    }

    def __init__(self, parent, player):  # Define the initialization method
        Frame.__init__(self, parent)  # Initialize the frame
        self.parent = parent  # Set the parent window
        self.player = player  # Set the player number
        self.selected_pokemon = None  # Initialize selected Pokémon to None
        self.labels()  # Create labels
        self.button_click()  # Create button for clicking
        self.listbox()  # Create listbox for selecting Pokémon
        self.image()  # Display default image
        parent.title("pokemon!")  # Set window title
        parent.geometry("350x350+300+300")  # Set window geometry

    def labels(self):  # Define method to create labels
        label = Label(self, text=f"Player {self.player} chooses a Pokémon!", font=("times new roman", 12))  # Label for choosing Pokémon
        label.grid(row=1, column=1, columnspan=2)  # Set grid for label

    def listbox(self):  # Define method to create listbox
        self.listbox = Listbox(self, selectmode="single", height=8)  # Create listbox
        for pokemon_name in self.pokemon_image_mapping:  # Populate listbox with Pokémon names
            self.listbox.insert(END, pokemon_name)
        self.listbox.grid(row=2, column=1, padx=5, pady=5)  # Set grid for listbox
        self.listbox.bind("<<ListboxSelect>>", self.update_image)  # Bind listbox selection event to update_image method

    def button_click(self):  # Define method for button click action
        button = Button(self, text="choose!", command=self.button_action)  # Create button
        button.grid(row=3, column=2, sticky="nswe", padx=5, pady=5)  # Set grid for button

    def button_action(self):  # Define method for button action
        self.selected_pokemon = self.listbox.get(self.listbox.curselection())  # Get selected Pokémon from listbox
        print(f"Player {self.player} selected Pokémon: {self.selected_pokemon}")  # Print selected Pokémon
        self.parent.quit()  # Quit parent window after selection

    def image(self):  # Define method to display default image
        default_pokemon = r"C:\Users\mohammed masri\advanced programming\MP2\MP2Files\images\none.png"  # Default image path
        self.selected_image = PhotoImage(file=default_pokemon).subsample(3, 2)  # Load default image
        self.image_label = Label(self, image=self.selected_image)  # Create label for image
        self.image_label.grid(row=2, column=2)  # Set grid for image label

    def update_image(self, event):  # Define method to update image based on listbox selection
        selected_pokemon = self.listbox.get(self.listbox.curselection())  # Get selected Pokémon from listbox
        image_filename = self.pokemon_image_mapping.get(selected_pokemon)  # Get image filename from mapping

        self.selected_image = PhotoImage(file=image_filename).subsample(3, 2)  # Load selected Pokémon image
        self.image_label.config(image=self.selected_image)  # Configure image label with selected image
        self.image_label.image = self.selected_image  # Set image attribute of label to prevent garbage collection

    def get_selected_pokemon(self):  # Define method to get the selected Pokémon
        if self.listbox.curselection():  # If a Pokémon is selected in the listbox
            return self.selected_pokemon  # Return the selected Pokémon
        else:
            return None  # Otherwise, return None


class AttackWindow(Frame):  # Define a class for the attack window

    pokemon_image_mapping = {  # Dictionary mapping Pokémon names to their image file paths
        "Bulbasaur": "images/Bulbasaur.png",  # Bulbasaur image file path
        "Squirtle": "images/Squirtle.png",  # Squirtle image file path
        "Charmander": "images/Charmander.png",  # Charmander image file path
        "Caterpie": "images/Caterpie.png",  # Caterpie image file path
        "Weedle": "images/Weedle.png",  # Weedle image file path
        "Pidgey": "images/Pidgey.png",  # Pidgey image file path
        "Beedrill": "images/Beedrill.png",  # Beedrill image file path
        "Blastoise": "images/Blastoise.png",  # Blastoise image file path
        "Butterfree": "images/Butterfree.png",  # Butterfree image file path
        "Charizard": "images/Charizard.png",  # Charizard image file path
        "Charmeleon": "images/Charmeleon.png",  # Charmeleon image file path
        "Kakuna": "images/Kakuna.png",  # Kakuna image file path
        "Ivysaur": "images/Ivysaur.png",  # Ivysaur image file path
        "Pidgeotto": "images/Pidgeotto.png",  # Pidgeotto image file path
        "Pidgeot": "images/Pidgeot.png",  # Pidgeot image file path
        "Wartortle": "images/Wartortle.png",  # Wartortle image file path
        "Venusaur": "images/Venusaur.png",  # Venusaur image file path
        "Metapod": "images/Metapod.png"  # Metapod image file path
    }

    def __init__(self, parent, player, p1_choice, p2_choice, p1_health, p2_health, player_attack, p1_element,
                 p2_element, p1_score, p2_score, battle_data_collector):
        Frame.__init__(self, parent)  # Initialize the frame
        self.parent = parent  # Set the parent window
        self.player = player  # Set the player number
        self.p1_choice = p1_choice  # Set player 1's Pokémon choice
        self.p2_choice = p2_choice  # Set player 2's Pokémon choice
        self.p1_health = p1_health  # Set player 1's initial health
        self.p2_health = p2_health  # Set player 2's initial health
        self.p1_health_ingame = self.p1_health  # Initialize player 1's in-game health
        self.p2_health_ingame = self.p2_health  # Initialize player 2's in-game health
        self.p1_attack = player_attack  # Set player 1's attack power
        self.p2_attack = player_attack  # Set player 2's attack power
        self.current_player = player  # Set the current player
        self.setup_window()  # Set up the window components
        self.player_one_element = p1_element  # Set player 1's elemental type
        self.player_two_element = p2_element  # Set player 2's elemental type
        self.score_label(p1_score, p2_score)  # Create score labels
        self.battle_data_collector = battle_data_collector  # Set battle data collector

    def setup_window(self):  # Define method to set up window components
        if self.parent and self.parent.winfo_exists():  # Check if the parent window exists
            self.parent.title(f"Attack Window")  # Set window title
            self.parent.geometry("750x380+300+300")  # Set window geometry
            self.labels()  # Create labels
            self.p1_physical()  # Create player 1's physical attack button
            self.p2_physical()  # Create player 2's physical attack button
            self.p1_HP_par()  # Create player 1's health progress bar
            self.p2_HP_par()  # Create player 2's health progress bar
            self.p1_elemental()  # Create player 1's elemental attack button
            self.p2_elemental()  # Create player 2's elemental attack button
            self.p1_character()  # Display player 1's Pokémon image
            self.p2_character()  # Display player 2's Pokémon image
            self.update_p1_HP_par(self.p1_health)  # Update player 1's health progress bar
            self.update_p2_HP_par(self.p2_health)  # Update player 2's health progress bar
            if self.player == 1:  # If it's player 1's turn
                self.player_one_move()  # Enable player 1's moves
            else:  # If it's player 2's turn
                self.player_two_move()  # Enable player 2's moves
        else:  # If the parent window has been destroyed
            print("Parent window is destroyed.")  # Print a message indicating the parent window is destroyed

    def labels(self):  # Define method to create labels
        # Create labels for player indicators and health indicators
        label1 = Label(self, text="Player 1")
        label2 = Label(self, text="Player 2")
        label5 = Label(self, text=" ")
        label6 = Label(self, text=" ")
        label7 = Label(self, text=f"{self.p1_health_ingame}/{self.p1_health}")
        label8 = Label(self, text=f"{self.p2_health_ingame}/{self.p2_health}")
        # Grid labels
        label1.grid(row=1, column=3, columnspan=2, sticky="news")
        label2.grid(row=1, column=8, columnspan=2, sticky="news")
        label5.grid(row=1, column=1, sticky="nesw", padx=25, columnspan=2)
        label6.grid(row=1, column=6, sticky="nesw", padx=25, columnspan=2)
        label7.grid(row=3, column=4)
        label8.grid(row=3, column=10)

    def score_label(self, p1_score, p2_score):  # Define method to create score labels
        # Create labels to display player scores
        p1_score_c = p1_score
        p2_score_c = p2_score
        label3 = Label(self, text=f"score {p1_score_c}")
        label4 = Label(self, text=f"score {p2_score_c}")
        # Grid score labels
        label3.grid(row=2, column=3, columnspan=2, sticky="news")
        label4.grid(row=2, column=8, columnspan=2, sticky="news")

    def game_loop(self):  # Define game loop method
        if self.parent:  # If the parent window exists
            if self.current_player == 1:  # If it's player 1's turn
                self.player_one_move()  # Enable player 1's moves
            else:  # If it's player 2's turn
                self.player_two_move()  # Enable player 2's moves
            # Check if any player's health is zero
            if self.p1_health_ingame <= 0:  # If player 1's health is zero
                print("Player Two wins!")  # Print message indicating player 2 wins
                self.quit_game()  # Quit the game
                return  # Exit the method
            elif self.p2_health_ingame <= 0:  # If player 2's health is zero
                print("Player One wins!")  # Print message indicating player 1 wins
                self.quit_game()  # Quit the game
                return  # Exit the method
        else:  # If the parent window has been destroyed
            print("Parent window is destroyed.")  # Print a message indicating the parent window is destroyed

    def quit_game(self):  # Define method to quit the game
        if self.parent:  # If the parent window exists
            self.battle_data_collector.save_to_excel('battle_data.xlsx')  # Save battle data to Excel file
            self.parent.quit()  # Quit the window
        else:  # If the parent window has been destroyed
            print("Parent window is destroyed.")  # Print a message indicating the parent window is destroyed

    def player_one_move(self):  # Define method to handle player one's move
        # Enable player 1's buttons and disable player 2's buttons
        self.button_p1_p.config(state="normal")
        self.button_p1_e.config(state="normal")
        self.button_p2_p.config(state="disabled")
        self.button_p2_e.config(state="disabled")

    def player_two_move(self):  # Define method to handle player two's move
        # Enable player 2's buttons and disable player 1's buttons
        self.button_p1_p.config(state="disabled")
        self.button_p1_e.config(state="disabled")
        self.button_p2_p.config(state="normal")
        self.button_p2_e.config(state="normal")

    elemental_relations = {  # Dictionary defining elemental relations
        "Water": ["Fire"],  # Water is strong against Fire
        "Fire": ["Grass"],  # Fire is strong against Grass
        "Grass": ["Water"],  # Grass is strong against Water
        "Bug": ["Normal"],  # Bug is strong against Normal
        "Normal": ["Bug"]  # Normal is strong against Bug
    }

    def is_element_stronger(self, attacker_element, defender_element):  # Define method to check if element is stronger
        # Get the list of elements stronger against the attacker's element
        stronger_elements = self.elemental_relations.get(attacker_element, [])
        # Check if defender's element is in the list of stronger elements
        is_stronger = defender_element in stronger_elements
        is_critical = is_stronger and random.random() <= 0.8  # 80% chance of doubling damage if element is stronger
        return is_stronger, is_critical

    def is_critical_hit(self, attacker_element, defender_element):  # Define method to check if it's a critical hit
        return self.is_element_stronger(attacker_element, defender_element)

    def p1_physical(self):  # Define method to create player 1's physical attack button
        self.button_p1_p = Button(self, text="physical", command=self.p1_physical_attack)  # Create button
        self.button_p1_p.grid(row=5, column=3, sticky="e")  # Grid button

    def p1_physical_attack(self):  # Define method for player 1's physical attack action
        if self.current_player == 1:  # If it's player 1's turn
            print(f"Player {self.current_player} used a physical attack!")  # Print action message
            damage_percentage = random.uniform(0.75, 1.0)  # Random damage between 75% and 100%
            damage = int(self.p1_attack * damage_percentage)  # Calculate damage
            self.p2_health_ingame -= damage  # Reduce player 2's health
            is_critical_hit = self.is_critical_hit(self.player_one_element, self.player_two_element)  # Check for critical hit
            self.update_p2_HP_par(self.p2_health_ingame)  # Update player 2's health progress bar
            self.current_player = 2  # Switch control to player 2
            self.battle_data_collector.record_attack(self.p1_choice, self.p2_choice, self.p1_health_ingame,
                                                     self.p2_health_ingame, damage, 0, False, False, False,
                                                     False)  # Record the attack
            messagebox.showinfo(f"{self.p1_choice} attacks", f"{self.p1_choice} hit with {damage} damage!")  # Show attack message
            self.battle_data_collector.next_attack()  # Move to the next attack
            self.game_loop()  # Run the game loop

    def p2_physical(self):  # Define method to create player 2's physical attack button
        self.button_p2_p = Button(self, text="physical", command=self.p2_physical_attack)  # Create button
        self.button_p2_p.grid(row=5, column=9, sticky="e")  # Grid button

    def p2_physical_attack(self):  # Define method for player 2's physical attack action
        if self.current_player == 2:  # If it's player 2's turn
            print(f"Player {self.current_player} used a physical attack!")  # Print action message
            damage_percentage = random.uniform(0.75, 1.0)  # Random damage between 75% and 100%
            damage = int(self.p2_attack * damage_percentage)  # Calculate damage
            self.p1_health_ingame -= damage  # Reduce player 1's health
            is_critical_hit = self.is_critical_hit(self.player_one_element, self.player_two_element)  # Check for critical hit
            self.update_p1_HP_par(self.p1_health_ingame)  # Update player 1's health progress bar
            self.current_player = 1  # Switch control back to player 1
            self.battle_data_collector.record_attack(self.p1_choice, self.p2_choice, self.p1_health_ingame,
                                                     self.p2_health_ingame, 0, damage, False, False, False,
                                                     False)  # Record the attack
            messagebox.showinfo(f"{self.p2_choice} attacks", f"{self.p2_choice} hit with {damage} damage!")  # Show attack message
            self.battle_data_collector.next_attack()  # Move to the next attack
            self.game_loop()  # Run the game loop

    def p1_elemental(self):  # Define method to create player 1's elemental attack button
        self.button_p1_e = Button(self, text="Elemental", command=self.p1_elemental_attack)  # Create button
        self.button_p1_e.grid(row=5, column=4)  # Grid button

    def p1_elemental_attack(self):  # Define method for player 1's elemental attack action
        if self.current_player == 1:  # If it's player 1's turn
            print(f"Player {self.current_player} used an elemental attack")  # Print action message
            damage_percentage = random.uniform(0.5, 1.0)  # Random damage between 50% and 100%
            damage = int(self.p1_attack * damage_percentage)  # Calculate damage
            is_stronger, is_critical_hit = self.is_element_stronger(self.player_one_element, self.player_two_element)  # Check for critical hit
            if is_stronger:  # If element is stronger
                if is_critical_hit:  # If it's a critical hit
                    damage *= 2  # Double the damage
            self.p2_health_ingame -= damage  # Reduce player 2's health
            if is_critical_hit:  # If it's a critical hit
                messagebox.showinfo("Critical hit?", "⚠️ Critical hit!!!")  # Show critical hit message
            self.update_p2_HP_par(self.p2_health_ingame)  # Update player 2's health progress bar
            self.current_player = 2  # Switch control to player 2
            self.battle_data_collector.record_attack(self.p1_choice, self.p2_choice, self.p1_health_ingame,
                                                     self.p2_health_ingame, damage, 0, is_critical_hit, False, True,
                                                     False)  # Record the attack
            messagebox.showinfo(f"{self.p1_choice} attacks", f"{self.p1_choice} hit with {damage} damage!")  # Show attack message
            self.battle_data_collector.next_attack()  # Move to the next attack
            self.game_loop()  # Run the game loop

    def p2_elemental(self):  # Define method to create player 2's elemental attack button
        self.button_p2_e = Button(self, text="Elemental", command=self.p2_elemental_attack)  # Create button
        self.button_p2_e.grid(row=5, column=10, sticky="w")  # Grid button

    def p2_elemental_attack(self):  # Define method for player 2's elemental attack action
        if self.current_player == 2:  # If it's player 2's turn
            print(f"Player {self.current_player} used an elemental attack")  # Print action message
            damage_percentage = random.uniform(0.5, 1.0)  # Random damage between 50% and 100%
            damage = int(self.p2_attack * damage_percentage)  # Calculate damage
            is_stronger, is_critical_hit = self.is_element_stronger(self.player_two_element, self.player_one_element)  # Check for critical hit
            if is_stronger:  # If element is stronger
                if is_critical_hit:  # If it's a critical hit
                    damage *= 2  # Double the damage
            self.p1_health_ingame -= damage  # Reduce player 1's health
            if is_critical_hit:  # If it's a critical hit
                messagebox.showinfo("Critical hit?", "⚠️ Critical hit!!!")  # Show critical hit message
            self.update_p1_HP_par(self.p1_health_ingame)  # Update player 1's health progress bar
            self.current_player = 1  # Switch control back to player 1
            self.battle_data_collector.record_attack(self.p1_choice, self.p2_choice, self.p1_health_ingame,
                                                     self.p2_health_ingame, 0, damage, False, is_critical_hit, False,
                                                     True)  # Record the attack
            messagebox.showinfo(f"{self.p2_choice} attacks", f"{self.p2_choice} hit with {damage} damage!")  # Show attack message
            self.battle_data_collector.next_attack()  # Move to the next attack
            self.game_loop()  # Run the game loop

    def p1_HP_par(self):  # Define method to create player 1's health progress bar
        s = ttk.Style()  # Create a ttk style
        s.theme_use('clam')  # Use the clam theme
        s.configure("red.Horizontal.TProgressbar", foreground='green', background='red')  # Configure style
        # Create player 1's health progress bar
        self.health_bar_p1 = ttk.Progressbar(self, orient='horizontal', mode='determinate', length=240,
                                             maximum=self.p1_health, style="red.Horizontal.TProgressbar")
        self.health_bar_p1.grid(row=3, column=3, sticky="e")  # Grid progress bar

    def p2_HP_par(self):  # Define method to create player 2's health progress bar
        s = ttk.Style()  # Create a ttk style
        s.theme_use('clam')  # Use the clam theme
        s.configure("red.Horizontal.TProgressbar", foreground='green', background='red')  # Configure style
        # Create player 2's health progress bar
        self.health_bar_p2 = ttk.Progressbar(self, orient='horizontal', mode='determinate', length=240,
                                             maximum=self.p2_health, style="red.Horizontal.TProgressbar")
        self.health_bar_p2.grid(row=3, column=9)  # Grid progress bar

    def update_p1_HP_par(self, value):  # Define method to update player 1's health progress bar
        self.health_bar_p1['value'] = value  # Update health progress bar value
        self.labels()  # Update labels

    def update_p2_HP_par(self, value):  # Define method to update player 2's health progress bar
        self.health_bar_p2['value'] = value  # Update health progress bar value
        self.labels()  # Update labels

    def p1_character(self):  # Define method to display player 1's Pokémon image
        character_p1 = self.p1_choice  # Get player 1's Pokémon choice
        character_filename = self.pokemon_image_mapping.get(character_p1)  # Get Pokémon image file path
        # Load and display player 1's Pokémon image
        self.selected_image_1 = PhotoImage(file=character_filename).subsample(3, 2)
        self.image_label_1 = Label(self, image=self.selected_image_1)
        self.image_label_1.grid(row=4, column=3)  # Grid image label

    def p2_character(self):  # Define method to display player 2's Pokémon image
        character_p2 = self.p2_choice  # Get player 2's Pokémon choice
        character_filename = self.pokemon_image_mapping.get(character_p2)  # Get Pokémon image file path
        # Load and display player 2's Pokémon image
        self.selected_image_2 = PhotoImage(file=character_filename).subsample(3, 2)
        self.image_label_2 = Label(self, image=self.selected_image_2)
        self.image_label_2.grid(row=4, column=9)  # Grid image label


class Game:
    # Dictionary representing the evolution chain of Pokémon
    evolution_chain = {
        "Bulbasaur": ["Ivysaur", "Venusaur"],
        "Ivysaur": ["Venusaur"],
        "Charmander": ["Charmeleon", "Charizard"],
        "Charmeleon": ["Charizard"],
        "Squirtle": ["Wartortle", "Blastoise"],
        "Wartortle": ["Blastoise"],
        "Caterpie": ["Metapod", "Butterfree"],
        "Metapod": ["Butterfree"],
        "Weedle": ["Kakuna", "Beedrill"],
        "Kakuna": ["Beedrill"],
        "Pidgey": ["Pidgeotto", "Pidgeot"],
        "Pidgeotto": ["Pidgeot"]
    }

    # Constructor method for initializing game state
    def __init__(self, player_one_choice, player_two_choice):
        # Initialize player choices, stats, scores, and round count
        self.player_one_choice_of_char = player_one_choice
        self.player_two_choice_of_char = player_two_choice
        self.player_one_hp = None
        self.player_one_attack = None
        self.player_one_element = None
        self.player_two_hp = None
        self.player_two_attack = None
        self.player_two_element = None
        self.player_one_score = 0  # Initialize scores for both players
        self.player_two_score = 0
        self.rounds = 0
        self.player_one_evolution_level = 1  # New instance variable
        self.player_two_evolution_level = 1  # New instance variable
        self.csv_reader()  # Read data from CSV
        self.battle_data_collector = BattleDataCollector()  # Initialize battle data collector
        self.start_game()  # Start the game

    # Method to read data from CSV file
    def csv_reader(self):
        with open("filtered_pokemon.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assign stats based on player choices
                if row['Name'] == self.player_one_choice_of_char:
                    self.player_one_hp = int(row['HP'])
                    self.player_one_attack = int(row['Attack'])
                    self.player_one_element = row['Element']
                elif row['Name'] == self.player_two_choice_of_char:
                    self.player_two_hp = int(row['HP'])
                    self.player_two_attack = int(row['Attack'])
                    self.player_two_element = row['Element']

    # Method to start the game
    def start_game(self):
        # Initialize player scores
        p1_score = self.player_one_score
        p2_score = self.player_two_score
        # Main game loop
        while p1_score < 3 and p2_score < 3:
            # Increment round count
            self.rounds += 1
            self.battle_data_collector.next_round()  # Update battle data for next round
            # Get current player health
            self.player_one_hp_r = self.get_character_health(self.player_one_choice_of_char)
            self.player_two_hp_r = self.get_character_health(self.player_two_choice_of_char)
            # Record attack data
            self.battle_data_collector.record_attack(self.player_one_choice_of_char, self.player_two_choice_of_char,
                                                     self.player_one_hp_r,
                                                     self.player_two_hp_r, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')
            # Create and display attack window
            root = Tk()
            attack_window = AttackWindow(root, 1, self.player_one_choice_of_char, self.player_two_choice_of_char,
                                         self.get_character_health(self.player_one_choice_of_char),
                                         self.get_character_health(self.player_two_choice_of_char),
                                         self.player_one_attack,
                                         self.get_character_element(self.player_one_choice_of_char),
                                         self.get_character_element(self.player_two_choice_of_char), p1_score, p2_score,
                                         self.battle_data_collector)
            attack_window.pack(fill="both", expand=True)
            root.mainloop()
            root.destroy()

            # Update player health after the round
            self.player_one_hp = attack_window.p1_health
            self.player_two_hp = attack_window.p2_health

            # Check if any player's health is depleted
            if self.player_one_hp <= 0:
                p2_score += 1
                if p2_score == 3:
                    messagebox.showinfo("Game Over",
                                        "Player Two wins the game by reaching level 3 and defeating Player One!")
                    return   # End the game
                else:
                    self.evolve_pokemon(2)  # Player Two evolves their Pokémon
                    self.csv_reader()  # Update the stats of the evolved Pokémon
                    if p1_score > 0:  # Ensure the score doesn't go below 0
                        p1_score -= 1  # Decrease player one's score
                    self.player_one_choice_of_char = self.choose_new_pokemon(1)  # Player One chooses a new character

            elif self.player_two_hp <= 0:
                p1_score += 1
                if p1_score == 3:
                    messagebox.showinfo("Game Over",
                                        "Player One wins the game by reaching level 3 and defeating Player Two!")
                    return   # End the game
                else:
                    self.evolve_pokemon(1)  # Player One evolves their Pokémon
                    self.csv_reader()  # Update the stats of the evolved Pokémon
                    if p2_score > 0:  # Ensure the score doesn't go below 0
                        p2_score -= 1  # Decrease player two's score
                    self.player_two_choice_of_char = self.choose_new_pokemon(2)  # Player Two chooses a new character

            # Allow the loser to select their character for the next round
            if p1_score < 3 and p2_score < 3:
                current_player = attack_window.current_player
                if current_player == 1:
                    p2_score += 1
                    # Handle player Two's turn
                    if p1_score == 3:
                        messagebox.showinfo("Game Over",
                                            "Player One wins the game by reaching level 3 and defeating Player Two!, you now may analyze the players performance")
                    elif p2_score == 3:
                        messagebox.showinfo("Game Over",
                                            "Player two wins the game by reaching level 3 and defeating Player one!, you now may analyze the players performance")
                    else:
                        messagebox.showinfo("Round Over",
                                            f"Player Two wins! player 2 character evolves to the next level, player 1 please choose a new character ")
                        self.player_one_choice_of_char = self.choose_new_pokemon(current_player)
                        if p1_score > 0:  # Ensure the score doesn't go below 0
                            p1_score -= 1
                else:
                    p1_score += 1
                    # Handle player One's turn
                    if p1_score == 3:
                        messagebox.showinfo("Game Over",
                                            "Player One wins the game by reaching level 3 and defeating Player Two!, you now may analyze the players performance")
                    elif p2_score == 3:
                        messagebox.showinfo("Game Over",
                                            "Player two wins the game by reaching level 3 and defeating Player one!, you now may analyze the players performance")
                    else:
                        messagebox.showinfo("Round Over",
                                            f"Player One wins! player 1 character evolves to the next level, player 2 please choose a new character ")
                        self.player_two_choice_of_char = self.choose_new_pokemon(current_player)
                        if p2_score > 0:  # Ensure the score doesn't go below 0
                            p2_score -= 1

                # Evolution mechanic only for the winner
                if current_player == 1:
                    self.evolve_pokemon(current_player)
                else:
                    self.evolve_pokemon(current_player)
        if p1_score == 3 or p2_score == 3:
            # Generate battle graphs
            graphs = BattleGraphs("battle_data.xlsx")
            graphs.plot_graphs()
            return

    # Method to retrieve the element of a character
    def get_character_element(self, character_name):
        # Retrieve the element associated with the character from the dataset
        with open("filtered_pokemon.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == character_name:
                    return row['Element']
        return None  # Return None if character not found (should not happen in this context)

    # Method to evolve a Pokémon
    def evolve_pokemon(self, current_player):
        # Determine the player who is not the current player
        player = 2 if current_player == 1 else 1

        # Evolve Pokémon for the respective player
        if player == 1:
            self.player_one_choice_of_char = \
                self.evolution_chain.get(self.player_one_choice_of_char, [self.player_one_choice_of_char])[0]
            self.player_one_evolution_level += 1  # Increase evolution level
        else:
            self.player_two_choice_of_char = \
                self.evolution_chain.get(self.player_two_choice_of_char, [self.player_two_choice_of_char])[0]
            self.player_two_evolution_level += 1  # Increase evolution level

    # Method to choose a new Pokémon
    def choose_new_pokemon(self, current_pokemon):
        root = Tk()
        welcome_window = WelcomeWindow(root, current_pokemon)
        welcome_window.pack(fill="both", expand=True)
        root.mainloop()
        new_pokemon = welcome_window.get_selected_pokemon()
        root.destroy()
        return new_pokemon

    # Method to retrieve the health of a character
    def get_character_health(self, character_name):
        # Retrieve the health value associated with the character from the dataset
        with open("filtered_pokemon.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == character_name:
                    return int(row['HP'])*5
        return 0  # Return 0 if character not found


class BattleGraphs:
    def __init__(self, file_name):
        # Initialize with data from the Excel file and plot graphs
        self.df = pd.read_excel(file_name)
        self.plot_graphs()

    def plot_graphs(self):
        # Create subplots for health, damage, and critical hits analysis
        fig, axs = plt.subplots(3, figsize=(10, 15))

        # Plot Health Data
        axs[0].plot(self.df['player_1_health'], label='Player 1')
        axs[0].plot(self.df['player_2_health'], label='Player 2')
        axs[0].set_title('Health Analysis')
        axs[0].set_xlabel('Round')
        axs[0].set_ylabel('Health')
        axs[0].legend()

        # Plot Damage Data
        axs[1].plot(self.df['damage_done_by_p1'], label='Player 1')
        axs[1].plot(self.df['damage_done_by_p2'], label='Player 2')
        axs[1].set_title('Damage Analysis')
        axs[1].set_xlabel('Round')
        axs[1].set_ylabel('Damage')
        axs[1].legend()

        # Plot Critical Hits Data
        crit_data_p1 = self.df.groupby('player_1')['critical_1'].sum()
        crit_data_p2 = self.df.groupby('player_2')['critical_2'].sum()
        width = 0.35  # Width of the bars
        axs[2].bar(crit_data_p1.index, crit_data_p1.values, width, label='Player 1')
        axs[2].bar(crit_data_p2.index, crit_data_p2.values, width, label='Player 2', align='edge')
        axs[2].set_title('Critical Hits Analysis')
        axs[2].set_xlabel('Pokemon')
        axs[2].set_ylabel('Number of Critical Hits')
        axs[2].legend()

        plt.tight_layout()
        plt.show()


def main():
    # Initialize Pokemon data and welcome windows for both players
    data = PokemonData()
    root1 = Tk()
    welcome_window1 = WelcomeWindow(root1, 1)
    welcome_window1.pack(fill="both", expand=True)
    root1.mainloop()
    player_one_choice = welcome_window1.get_selected_pokemon()
    root1.destroy()  # Destroy the first window

    root2 = Tk()
    welcome_window2 = WelcomeWindow(root2, 2)
    welcome_window2.pack(fill="both", expand=True)
    root2.mainloop()
    player_two_choice = welcome_window2.get_selected_pokemon()
    root2.destroy()

    # Start the game with chosen Pokemon
    game = Game(player_one_choice, player_two_choice)


if __name__ == "__main__":
    main()

