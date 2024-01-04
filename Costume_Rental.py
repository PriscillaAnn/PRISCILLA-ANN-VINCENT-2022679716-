import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox 

class CostumeRentalSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Costume Rental System")

        # Connect to your MySQL database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="costume_rental"
        )
        # Create a cursor object to execute SQL queries
        self.mycursor = self.mydb.cursor()

        # Set custom color scheme
        root.configure(bg="aquamarine")

        # Create labels and entry widgets with adjusted text colors
        self.label_name = tk.Label(root, text="Costume Name:", bg="aquamarine", fg="black")
        self.entry_name = tk.Entry(root)

        self.label_price = tk.Label(root, text="Costume Price:", bg="aquamarine", fg="black")
        self.entry_price = tk.Entry(root)

        self.label_quantity = tk.Label(root, text="Costume Quantity:", bg="aquamarine", fg="black")
        self.entry_quantity = tk.Entry(root)

        # Create buttons with adjusted text colors
        self.add_button = tk.Button(root, text="Add Costume", command=self.add_costume, bg="pink", fg="black")
        self.display_button = tk.Button(root, text="Display Costumes", command=self.display_costumes, bg="pink", fg="black")

        # Create treeview with adjusted text colors
        self.tree = ttk.Treeview(root, columns=("Name", "Price", "Quantity", "Total_Cost"), show="headings", selectmode='browse')
        self.tree.heading("Name", text="Costume Name")
        self.tree.heading("Price", text="Costume Price")
        self.tree.heading("Quantity", text="Costume Quantity")
        self.tree.heading("Total_Cost", text="Total Cost")

        # Pack widgets
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.label_price.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_price.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.label_quantity.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_quantity.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=50)

        # Create button for calculating total cost with adjusted text colors
        self.calculate_button = tk.Button(root, text="Calculate Total Cost", command=self.calculate_total_cost, bg="pink", fg="black")
        self.calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Create button for updating costume with adjusted text colors
        self.update_button = tk.Button(root, text="Update Costume", command=self.update_costume, bg="pink", fg="black")
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_costume(self):
        costume_name = self.entry_name.get()
        costume_price = self.entry_price.get()
        costume_quantity = self.entry_quantity.get()

        # Check if all fields are filled
        if costume_name and costume_price and costume_quantity:
            # Inserting data into the 'costumes' table
            sql = "INSERT INTO `costume` (Costume_Name, Costume_Price, Costume_Quantity) VALUES (%s, %s, %s)"
            val = (costume_name, costume_price, costume_quantity)

            try:
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print("Data inserted successfully!")

                # Display success message (you can customize this)
                print(f"Costume {costume_name} added successfully!")

                # Recalculate total cost after adding a costume
                self.calculate_total_cost()
                
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.mydb.rollback()

    def display_costumes(self):
        # Clear existing data in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch costumes from the database
        try:
            self.mycursor.execute("SELECT * FROM `costume`")
            costumes = self.mycursor.fetchall()

            # Insert costumes into the treeview with total cost
            for costume in costumes:
                costume_name, costume_price, costume_quantity = costume[1], costume[2], costume[3]
                total_cost = float(costume_price) * int(costume_quantity) if costume_quantity else 0
                self.tree.insert("", tk.END, values=(costume_name, costume_price, costume_quantity, total_cost))

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def calculate_total_cost(self):
        # Clear existing data in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        total_cost_sum = 0  # Initialize a variable to store the total cost sum

        # Fetch costumes from the database
        try:
            self.mycursor.execute("SELECT * FROM `costume`")
            costumes = self.mycursor.fetchall()

            # Insert costumes into the treeview with total cost
            for costume in costumes:
                costume_name, costume_price, costume_quantity = costume[1], costume[2], costume[3]
                total_cost = float(costume_price) * int(costume_quantity) if costume_quantity else 0
                total_cost_sum += total_cost  # Accumulate the total cost
                self.tree.insert("", tk.END, values=(costume_name, costume_price, costume_quantity, total_cost))

            # Insert a row at the end with the total cost sum
            self.tree.insert("", tk.END, values=("Total Cost", "", "", total_cost_sum))

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Update the treeview
        self.tree.update()
    
    def update_costume(self):
        costume_name = self.entry_name.get()
        costume_price = self.entry_price.get()
        costume_quantity = self.entry_quantity.get()

        # Check if all fields are filled
        if costume_name and costume_price and costume_quantity:
            # Updating data in the 'costumes' table
            sql = "UPDATE `costume` SET Costume_Price = %s, Costume_Quantity = %s WHERE Costume_Name = %s"
            val = (costume_price, costume_quantity, costume_name)

            try:
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print("Data updated successfully!")

                # Display success message (you can customize this)
                print(f"Costume {costume_name} updated successfully!")

                # Recalculate total cost after adding a costume
                self.calculate_total_cost()
                
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.mydb.rollback()

if __name__ == "__main__":
    root = tk.Tk()
    app = CostumeRentalSystem(root)
    root.mainloop()
