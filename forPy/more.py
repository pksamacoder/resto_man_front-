import datetime

class HotelManagement:
    def __init__(self):
        self.customers = []
        self.rooms = {i: ("AC" if i <= 10 else "Non-AC", None) for i in range(1, 16)}
        self.room_prices = {
            "AC": 4000,
            "Non-AC": 3500
        }
        self.menu = {
            1: ("Tea", 10),
            2: ("Cold Drink", 20),
            3: ("Breakfast Combo", 50),
            4: ("Lunch", 100),
            5: ("Dinner", 150)
        }
        self.food_orders = {}
    
    def is_valid_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def check_room_availability(self):
        print("\nRoom Availability:")
        for room, (room_type, customer) in self.rooms.items():
            status = "Available" if customer is None else f"Booked by {customer}"
            print(f"Room {room} ({room_type}) - {status}")
    
    def book_room(self):
        name = input("Enter customer name: ")
        phno = input("Enter phone number: ")
        adhaar = input("Enter Aadhaar number as ID proof: ")
        checkin = input("Enter check-in date (dd/mm/yyyy): ")
        while not self.is_valid_date(checkin):
            print("Invalid date format!")
            checkin = input("Enter check-in date (dd/mm/yyyy): ")
        
        print("Available Rooms:")
        available_rooms = [room for room, (_, customer) in self.rooms.items() if customer is None]
        if not available_rooms:
            print("No rooms available!")
            return
        for room in available_rooms:
            print(f"Room {room} ({self.rooms[room][0]}) - Rs. {self.room_prices[self.rooms[room][0]]}/day")
        
        room_choice = self.get_int_input("Enter room number to book: ")
        if room_choice in self.rooms and self.rooms[room_choice][1] is None:
            self.rooms[room_choice] = (self.rooms[room_choice][0], name)
            self.customers.append({
                "name": name,
                "phone": phno,
                "adhaar": adhaar,
                "checkin": checkin,
                "room": room_choice,
                "room_type": self.rooms[room_choice][0]
            })
            self.food_orders[room_choice] = 0  # Initialize food order total
            print(f"Room {room_choice} booked successfully!")
        else:
            print("Invalid or already booked room!")
    
    def order_food(self):
        room_number = self.get_int_input("Enter your room number: ")
        if room_number not in self.rooms or self.rooms[room_number][1] is None:
            print("Invalid room number or room is not booked!")
            return
        
        print("Restaurant Menu:")
        for key, value in self.menu.items():
            print(f"{key}. {value[0]} - Rs. {value[1]}")
        
        while True:
            item = self.get_int_input("Enter menu item number to order (0 to finish): ")
            if item == 0:
                break
            if item in self.menu:
                self.food_orders[room_number] += self.menu[item][1]
            else:
                print("Invalid item number!")
        
        print(f"Total Food Bill for Room {room_number}: Rs. {self.food_orders[room_number]}")
    
    def check_customer_status(self):
        if not self.customers:
            print("No customers are currently staying.")
            return
        
        print("Current Customers:")
        for customer in self.customers:
            print(f"Customer Name: {customer['name']}, Room: {customer['room']} ({customer['room_type']}), Check-in: {customer['checkin']}")
    
    def checkout_customer(self):
        room_number = self.get_int_input("Enter room number to check out: ")
        for customer in self.customers:
            if customer["room"] == room_number:
                stay_days = self.get_int_input("Enter number of days stayed: ")
                room_cost = stay_days * self.room_prices[customer["room_type"]]
                food_cost = self.food_orders.get(room_number, 0)
                total_bill = room_cost + food_cost
                
                print("\nBill Receipt")
                print("---------------------------")
                print(f"Customer Name: {customer['name']}")
                print(f"Room: {room_number} ({customer['room_type']})")
                print(f"Stay Duration: {stay_days} days")
                print(f"Room Charges: Rs. {room_cost}")
                print(f"Food Charges: Rs. {food_cost}")
                print(f"Total Bill: Rs. {total_bill}")
                print("---------------------------")
                
                self.customers.remove(customer)
                self.rooms[room_number] = (self.rooms[room_number][0], None)
                self.food_orders.pop(room_number, None)
                print(f"Room {room_number} is now available.")
                return
        print("No customer found in this room.")
    
    def run(self):
        while True:
            print("\nHotel Management System")
            print("1. Book a Room")
            print("2. Order Food")
            print("3. Check Room Availability")
            print("4. Check Customer Status")
            print("5. Checkout Customer")
            print("6. Exit")
            choice = self.get_int_input("Enter your choice: ")
            
            if choice == 1:
                self.book_room()
            elif choice == 2:
                self.order_food()
            elif choice == 3:
                self.check_room_availability()
            elif choice == 4:
                self.check_customer_status()
            elif choice == 5:
                self.checkout_customer()
            elif choice == 6:
                print("Thank you for using our system!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    hotel = HotelManagement()
    hotel.run()
