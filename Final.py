from customtkinter import *
from tkinter import *
from tkinter import messagebox

set_appearance_mode('dark')
# menu: Categories: Items: Price
menu = {
    "Main Dishes":
    {
        "Pizza": 150,
        "Burger": 100,
        "Shawerma": 75,
        "Ma7shy": 100,
        "Molokheya": 75
    },
    "Side Dishes":
    {
        "Chicken Nuggets": 75,
        "Salad": 15,
        "French Fries": 40,
        "Onion Rings": 50,
        "Soup":50
    },
    "Desserts":
    {
        "Cheese Cake": 50,
        "Donuts": 20,
        "Ice Cream": 10,
        "Apple Pie": 60,
        "Indomi": 10
    },
    "Drinks":
    {
        "Soda": 10,
        "Lemonade": 15,
        "Coffee": 20,
        "Milkshake": 30,
        "Tea": 5
    }
}


# items pic paths
pics = {
    "Pizza": "Pizza.gif",
    "Burger": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Burger.gif",
    "Shawerma": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Shawerma.gif",
    "Ma7shy": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Ma7shy.gif",
    "Molokheya": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Molokheya.gif",
    "Chicken Nuggets": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Chicken_Nuggets.gif",
    "Salad": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Salad.gif",
    "French Fries": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\French_Fries.gif",
    "Onion Rings": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Onion_Rings.gif",
    "Soup": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Soup.gif",
    "Cheese Cake": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Cheese_Cake.gif",
    "Donuts": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Donuts.gif",
    "Ice Cream": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Ice_Cream.gif",
    "Apple Pie": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Apple_Pie.gif",
    "Indomi": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Indomi.gif",
    "Soda": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Soda.gif",
    "Lemonade": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Lemonade.gif",
    "Coffee": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Coffee.gif",
    "Milkshake": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Milkshake.gif",
    "Tea": r"D:\OneDrive - Nile University\My Files\Material\Fall 2024\CSCI102\Project\Final\GIFs\Tea.gif",
}

# Declarations
global menu_tab, window_tab
global total, receipt
total = 0
receipt = []


def show_menu():
    # menu_window configurations
    global menu_window
    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.config(bg='#202020')
    menu_window.attributes('-fullscreen', True)
    
    # Place all items in menu
    row = 0
    for category, items in menu.items():
        column = 0
        row +=1
        Label(menu_window, text = category, font = ("Times New Roman", 34, "bold"), fg = "#FFFFFF", bg = "#202020").grid(row = row, column = 2, padx = 10, pady = 15)
        row += 1
        for item, price in items.items():
            CTkButton(master = menu_window, 
                text = f"{item} \n ${price:.2f}",
                width = 250,
                height = 50,
                corner_radius = 32, 
                fg_color = 'transparent',
                hover_color = '#000000',
                border_color = "#000000",
                font = ("Times New Roman", 14),
                border_width = 3,
                command = lambda 
                item = item, 
                price = price
                :order(item, price)
                ).grid(row = row, column = column, padx = 25, pady = 20)

            column += 1
    # Checkout Button
    CTkButton(master = menu_window, 
        text = "Checkout", 
        font=('Times New Roman', 28), 
        command = checkout, 
        width = 400,
        height = 100,
        fg_color = '#0000FF',
        border_color = '#000000',
        corner_radius = 45, 
        hover_color = '#8e44ad'
        ).grid(row = 9, column = 1, columnspan = 3, pady = 15)

def order(item, price):

    # order_window configurations
    global total
    order_window = Toplevel(root)
    order_window.title(f"Order {item}")
    order_window.config(bg='#202020')
    order_window.geometry("+450+50")


    # getting quantity input
    Label(order_window, 
        text = f"How many items of {item} would you like to have?", 
        font=('Times New Roman', 20), 
        fg='#FFFFFF', 
        bg='#202020'
        ).pack(pady = 25, padx = 2)
    
    quantity_entry = Entry(order_window, font=('Times New Roman', 16))
    quantity_entry.pack(pady=10)

    # Item Picture
    image = PhotoImage(file = pics[item])
    label_img = Label(order_window, image = image, borderwidth = 0)
    label_img.image = image
    label_img.pack(pady = 10, padx = 25)
    
    # Functionality
    def add_to_receipt():
        global total
        try:
            quantity = int(quantity_entry.get())
            if quantity <= 0:
                messagebox.showerror("Invalid Input", "Quantity must be more than 0")
                return
            item_price = price * quantity
            receipt.append((item, quantity, item_price))
            total += item_price
            messagebox.showinfo("Successfull Transaction", f"Successfully added {quantity} order/s of {item} to your order!")
            order_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

    CTkButton(master = order_window, 
        text = "Add to Order",
        font = ("Times New Roman", 24),
        command = add_to_receipt,
        hover_color = "#0F0F0F",
        text_color = '#FFFFFF',
        fg_color = "#00FF00",
        corner_radius = 28,
        ).pack(pady = 25, ipady = 5)
    
def checkout():
    global receipt, total
    if not receipt:
        messagebox.showwarning("Empty Order", "You haven't ordered anything yet!")
        return
    
    # Receipt_window configurations
    receipt_window = Toplevel(root)
    receipt_window.title(f"Receipt")
    receipt_window.config(bg='#202020')
    receipt_window.geometry("+550+200")

    # Calculating Total bills
    receipt_items = "\n".join([f"{item} x {qty} - ${total:.2f}" for item, qty, total in receipt])
    receipt_total = f"Your total is: ${total:.2f}"
    
    # Each Item Price
    Label(receipt_window,
        text = receipt_items,
        font=('Times New Roman', 24), 
        fg='#FFFFFF', 
        bg='#202020'
        ).pack(pady = 10, padx = 5)
    

    # Total Price
    Label(receipt_window,
        text = receipt_total,
        fg = "#FFFFFF",
        bg = "#202020",
        font = ("Times New Roman", 32, "bold")
        ).pack(pady = 30, padx = 10)

    def thanks():
        Label(receipt_window,
            text = "Thank you for choosing us\n Enjoy your meal!",
            fg = "#00FF00",
            bg = "#202020",
            font = ("Times New Roman", 32, "bold")
            ).pack(pady = 30, padx = 10)
            
    # Pay now button
    Button(receipt_window,
        text = "Pay Now!",
        fg = "#FFFFFF",
        bg = "#0000FF",
        command = thanks,
        font = ("Times New Roman", 32, "bold"),
        ).pack(pady = 30, padx = 10)

    receipt = []
    total = 0



# Root Configuration
root = Tk()
root.title("Restaurant")
root.configure(bg = "#202020")
root.geometry("+500+200")
icon = PhotoImage(file = './JPGs/icon.png')
root.iconphoto(True, icon)  

# Root Text and Menu Button
Label(root, text="Welcome to Our Restaurant", font=('Times New Roman', 34, 'bold'), fg='#FFFFFF', bg='#202020').pack(pady=20, padx = 20)
Label(root, text = "Click here to view our menu", font=('Times New Roman', 28, 'bold'), fg='#FFFFFF', bg='#202020').pack()
CTkButton(master = root, text="View Menu", font=('Times New Roman', 40, 'bold'), command = show_menu, width = 250, height = 75, text_color = "#FFFFFF", border_color = "#D00000", border_width = 3, fg_color = '#D00000', hover_color = "#000000", corner_radius = 40).pack(pady=50)

root.mainloop()