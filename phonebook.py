import tkinter as tk
from tkinter import messagebox
import json

class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        # Create the labels and entry boxes for the name and phone number
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_phone = tk.Label(master, text="Phone:")
        self.label_phone.grid(row=1, column=0)
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=1, column=1)

        # Create the buttons for adding, displaying, and deleting contacts
        self.button_add = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=2, column=0)

        self.button_display = tk.Button(master, text="Display Contact", command=self.display_contact)
        self.button_display.grid(row=2, column=1)

        self.button_delete = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=2, column=2)

        # Load the contacts from a file
        try:
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        # Save the contacts to a file
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f)

    def add_contact(self):
        # Add the name and phone number to the dictionary
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        self.contacts[name] = phone

        # Clear the entry boxes
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

        # Save the contacts to a file
        self.save_contacts()

    def display_contact(self):
        # Display the phone number for the entered name
        name = self.entry_name.get()
        phone = self.contacts.get(name)

        if phone is not None:
            # Display the phone number in a message box
            tk.messagebox.showinfo("Phone Number", f"The phone number for {name} is {phone}.")
        else:
            # Display an error message if the name is not found
            tk.messagebox.showerror("Error", f"No contact found for {name}.")

        # Clear the entry box
        self.entry_name.delete(0, tk.END)

    def delete_contact(self):
        # Delete the contact for the entered name
        name = self.entry_name.get()

        if name in self.contacts:
            # Delete the contact and display a message
            del self.contacts[name]
            tk.messagebox.showinfo("Delete Contact", f"{name} has been deleted from your contacts.")

            # Save the contacts to a file
            self.save_contacts()
        else:
            # Display an error message if the name is not found
            tk.messagebox.showerror("Error", f"No contact found for {name}.")

        # Clear the entry box
        self.entry_name.delete(0, tk.END)

# Create the main window and run the program
root = tk.Tk()
app = ContactBook(root)
root.mainloop()
