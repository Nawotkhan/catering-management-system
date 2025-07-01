import tkinter as tk
from tkinter import messagebox, simpledialog

# Define a class for MenuItem
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

# Define a class for Customer
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact}"

# Define a class for Order
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total_price = 0.0
        self.status = "Pending"

    def add_item(self, menu_item, quantity):
        self.items.append((menu_item, quantity))
        self.total_price += menu_item.price * quantity

    def __str__(self):
        details = f"Order for {self.customer}\n"
        for item, qty in self.items:
            details += f"{item.name} x{qty} - ${item.price * qty:.2f}\n"
        details += f"Total: ${self.total_price:.2f}\n"
        details += f"Status: {self.status}"
        return details

# Define a class for Event
class Event:
    def __init__(self, name, date, customer):
        self.name = name
        self.date = date
        self.customer = customer

    def __str__(self):
        return f"Event: {self.name}, Date: {self.date}, Customer: {self.customer}"

# Define a class for Inventory
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}"

# Catering Management System Class
class CateringManagementSystem:
    def __init__(self):
        self.menu = []
        self.customers = []
        self.orders = []
        self.events = []
        self.inventory = []

    # Menu management
    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)
        print(f"Added menu item: {item}")

    def show_menu(self):
        return "\n".join(str(item) for item in self.menu) if self.menu else "No menu items available."

    # Customer management
    def add_customer(self, name, contact):
        customer = Customer(name, contact)
        self.customers.append(customer)
        print(f"Added customer: {customer}")

    def show_customers(self):
        return "\n".join(str(customer) for customer in self.customers) if self.customers else "No customers available."

    # Order management
    def create_order(self, customer_name):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if not customer:
            print(f"Customer {customer_name} not found.")
            return None
        order = Order(customer)
        self.orders.append(order)
        print(f"Created order for {customer_name}")
        return order

    def show_all_orders(self):
        return "\n\n".join(str(order) for order in self.orders) if self.orders else "No orders available."

    # Event management
    def add_event(self, name, date, customer_name):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if not customer:
            print(f"Customer {customer_name} not found.")
            return None
        event = Event(name, date, customer)
        self.events.append(event)
        print(f"Added event: {event}")

    def show_events(self):
        return "\n".join(str(event) for event in self.events) if self.events else "No events available."

    # Inventory management
    def add_inventory_item(self, name, quantity):
        item = InventoryItem(name, quantity)
        self.inventory.append(item)
        print(f"Added inventory item: {item}")

    def show_inventory(self):
        return "\n".join(str(item) for item in self.inventory) if self.inventory else "No inventory items available."

  # GUI Implementation using Tkinter
  class CateringGUI:
    def __init__(self, root, system):
        self.root = root
        self.system = system
        self.root.title("Catering Management System")

        # Frame setup
        self.setup_frames()

        # Display area
        self.display_area = tk.Text(self.display_frame, height=15, width=60)
        self.display_area.pack()

    def setup_frames(self):
        self.menu_frame = tk.Frame(self.root)
        self.customer_frame = tk.Frame(self.root)
        self.order_frame = tk.Frame(self.root)
        self.event_frame = tk.Frame(self.root)
        self.inventory_frame = tk.Frame(self.root)
        self.display_frame = tk.Frame(self.root)

        self.menu_frame.pack(padx=10, pady=5)
        self.customer_frame.pack(padx=10, pady=5)
        self.order_frame.pack(padx=10, pady=5)
        self.event_frame.pack(padx=10, pady=5)
        self.inventory_frame.pack(padx=10, pady=5)
        self.display_frame.pack(padx=10, pady=5)

        self.setup_buttons()

    def setup_buttons(self):
        # Menu management
        tk.Button(self.menu_frame, text="Add Menu Item", command=self.add_menu_item).pack()
        tk.Button(self.menu_frame, text="Show Menu", command=self.show_menu).pack()

        # Customer management
        tk.Button(self.customer_frame, text="Add Customer", command=self.add_customer).pack()
        tk.Button(self.customer_frame, text="Show Customers", command=self.show_customers).pack()

        # Order management
        tk.Button(self.order_frame, text="Create Order", command=self.create_order).pack()
        tk.Button(self.order_frame, text="Show Orders", command=self.show_all_orders).pack()

        # Event management
        tk.Button(self.event_frame, text="Add Event", command=self.add_event).pack()
        tk.Button(self.event_frame, text="Show Events", command=self.show_events).pack()

        # Inventory management
        tk.Button(self.inventory_frame, text="Add Inventory Item", command=self.add_inventory_item).pack()
        tk.Button(self.inventory_frame, text="Show Inventory", command=self.show_inventory).pack()

    def add_menu_item(self):
        name = simpledialog.askstring("Menu Item", "Enter the name:")
        price = simpledialog.askfloat("Menu Item", "Enter the price:")
        if name and price is not None:
            self.system.add_menu_item(name, price)
            messagebox.showinfo("Success", "Menu item added!")

    def show_menu(self):
        self.display_area.delete(1.0, tk.END)
        self.display_area.insert(tk.END, self.system.show_menu())

    def add_customer(self):
        name = simpledialog.askstring("Customer", "Enter customer name:")
        contact = simpledialog.askstring("Customer", "Enter customer contact:")
        if name and contact:
            self.system.add_customer(name, contact)
            messagebox.showinfo("Success", "Customer added!")

    def show_customers(self):
        self.display_area.delete(1.0, tk.END)
        self.display_area.insert(tk.END, self.system.show_customers())

    def create_order(self):
        customer_name = simpledialog.askstring("Order", "Enter customer name for the order:")
        order = self.system.create_order(customer_name)
        if order:
            quantity = simpledialog.askinteger("Order", "Enter quantity of items to add:")
            if quantity and order.items:
                item_name = simpledialog.askstring("Order", "Enter menu item name to add:")
                menu_item = next((item for item in self.system.menu if item.name == item_name), None)
                if menu_item:
                    order.add_item(menu_item, quantity)
                    messagebox.showinfo("Success", "Item added to order!")
                else:
                    messagebox.showerror("Error", "Menu item not found.")
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, str(order))

    def show_all_orders(self):
        self.display_area.delete(1.0, tk.END)
        self.display_area.insert(tk.END, self.system.show_all_orders())

    def add_event(self):
        name = simpledialog.askstring("Event", "Enter event name:")
        date = simpledialog.askstring("Event", "Enter event date (YYYY-MM-DD):")
        customer_name = simpledialog.askstring("Event", "Enter customer name for the event:")
        if name and date and customer_name:
            self.system.add_event(name, date, customer_name)
            messagebox.showinfo("Success", "Event added!")

    def show_events(self):
        self.display_area.delete(1.0, tk.END)
        self.display_area.insert(tk.END, self.system.show_events())

    def add_inventory_item(self):
        name = simpledialog.askstring("Inventory Item", "Enter inventory item name:")
        quantity = simpledialog.askinteger("Inventory Item", "Enter inventory item quantity:")
        if name and quantity is not None:
            self.system.add_inventory_item(name, quantity)
            messagebox.showinfo("Success", "Inventory item added!")

    def show_inventory(self):
        self.display_area.delete(1.0, tk.END)
        self.display_area.insert(tk.END, self.system.show_inventory())

    def main():
      root = tk.Tk()
      system = CateringManagementSystem()
      gui = CateringGUI(root, system)
      root.mainloop()
    main()
