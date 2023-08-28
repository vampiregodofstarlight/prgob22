# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:45:05 2023

@author: david
"""

class Cinema:
    def __init__(self, name, total_seats, ticket_prices):
        self.name = name
        self.total_seats = total_seats
        self.ticket_prices = ticket_prices

    def calculate_revenue(self, num_pensioner_tickets, num_adult_tickets, num_child_tickets):
        # Compute the total amount of tickets sold
        total_tickets_sold = num_pensioner_tickets + num_adult_tickets + num_child_tickets
        # Compute the revenue by multiplying amount of sold tickets with each respective price
        revenue = (num_pensioner_tickets * self.ticket_prices[0]) + \
                  (num_adult_tickets * self.ticket_prices[1]) + \
                  (num_child_tickets * self.ticket_prices[2])
        # Return the revenue and the total amount of tickets sold
        return revenue, total_tickets_sold

    def calculate_occupancy(self, total_tickets_sold):
        # Compute occupancy percent by dividing the amount of sold tickets by the total amount of seats in the cinema and multiplying with 100
        occupancy_percent = (total_tickets_sold / self.total_seats) * 100
        # Returns occupancy percent
        return occupancy_percent

# Function to check if a given string is a valid name
def is_valid_name(name):
    # A valid name should not consist of only numeric characters
    return not name.isdigit()

# Function to read cinema information from a text file
def read_cinema_file():
    # Ask the user for the file name
    file_input = input('Choose an existing cinema file: ')
    cin_list = []
    
    try:
        # Open the file and read its contents
        with open(file_input + '.txt', 'r', encoding="utf-8") as cin_file:
            for line in cin_file:
                line = line.rstrip()
                cinema_info = line.split(', ')
                
                # Check if the first item is a valid name
                if not is_valid_name(cinema_info[0]):
                    raise ValueError('Invalid format in the cinema file. First item should be a valid name.')
                
                # Check the total number of elements in each line
                if len(cinema_info) != 5:
                    raise ValueError('Invalid format in the cinema file.')
                
                # Check if elements 2 to 5 are valid integers
                for i, element in enumerate(cinema_info[1:5], start=1):
                    if not element.isdigit():
                        raise ValueError('Invalid format in the cinema file. Element at index {} is not a valid integer.'.format(i))
                
                # Add the cinema information to the list
                cin_list.append(cinema_info)
        return cin_list
    except FileNotFoundError:
        print('File does not exist, try again!')
        return read_cinema_file()
    except ValueError as e:
        print(str(e))
        return read_cinema_file()

# Function to validate ticket prices
def validate_ticket_prices(ticket_prices):
    # Check if there are exactly 3 ticket prices
    if len(ticket_prices) != 3:
        raise ValueError("Invalid number of ticket prices.")
    
    # Check if each ticket price is a valid integer
    for price in ticket_prices:
        if not price.isdigit():
            raise ValueError("Ticket price must be a valid integer.")
    
    # Convert ticket prices to integers
    pensioner_price, adult_price, child_price = map(int, ticket_prices)
    
    # Check if the ticket price order is valid
    if not (adult_price > pensioner_price > child_price):
        raise ValueError("Invalid ticket price order. Prices should be in the format: adult > pensioner > child.")
    
    # Return the validated ticket prices as integers
    return [pensioner_price, adult_price, child_price]

def process_option_1(cinema_info):
    cinema_name, total_seats, *ticket_prices = cinema_info
    total_seats = int(total_seats)
    
    try:
        ticket_prices = validate_ticket_prices(ticket_prices)
    except ValueError as e:
        print(e)
        return None
    
    # Get number of tickets sold for different categories
    num_pensioner_tickets = int(input("Enter number of pensioner tickets sold: "))
    num_adult_tickets = int(input("Enter number of adult tickets sold: "))
    num_child_tickets = int(input("Enter number of child tickets sold: "))
    
    # Create a Cinema object with validated data
    cinema = Cinema(cinema_name, total_seats, ticket_prices)
    
    # Calculate revenue and occupancy using Cinema's methods
    revenue, total_tickets_sold = cinema.calculate_revenue(
        num_pensioner_tickets, num_adult_tickets, num_child_tickets
    )
    occupancy_percent = cinema.calculate_occupancy(total_tickets_sold)
    
    # Print cinema information
    print(f"\n{cinema.name}")
    print(f"Revenue: {revenue} kr")
    print(f"Occupancy: {occupancy_percent:.2f}%")
    
    # Return relevant data
    return cinema_name, occupancy_percent, revenue

def process_option_2(cinema_info):
    cinema_name, total_seats, *ticket_prices = cinema_info
    total_seats = int(total_seats)
    ticket_prices = list(map(int, ticket_prices))
    
    # Get the total cash in the register
    total_cash = int(input("Enter the total cash in the register: "))
    
    solutions = []  # To store valid solutions
    
    # Calculate the maximum number of tickets for each category
    max_pensioner_tickets = min(total_cash // ticket_prices[0], total_seats)
    max_adult_tickets = min(total_cash // ticket_prices[1], total_seats)
    max_child_tickets = min(total_cash // ticket_prices[2], total_seats)
    
    # Iterate over possible ticket quantities
    for num_pensioner_tickets in range(max_pensioner_tickets + 1):
        for num_adult_tickets in range(max_adult_tickets + 1):
            for num_child_tickets in range(max_child_tickets + 1):
                revenue = (
                    num_pensioner_tickets * ticket_prices[0] +
                    num_adult_tickets * ticket_prices[1] +
                    num_child_tickets * ticket_prices[2]
                )
                total_tickets_sold = (num_pensioner_tickets + num_adult_tickets + num_child_tickets)
                
                if total_tickets_sold <= total_seats and revenue == total_cash:
                    solutions.append((num_pensioner_tickets, num_adult_tickets, num_child_tickets))
    
    if not solutions:
        print("No valid solutions found.")
        return None
    
    # Print cinema name
    print(f"\n{cinema_name}")
    print("Valid solutions:")
    for i, solution in enumerate(solutions, start=1):
        pensioner_tickets, adult_tickets, child_tickets = solution
        print(f"Solution {i}:")
        print(f"Pensioner tickets: {pensioner_tickets}, Adult tickets: {adult_tickets}, Child tickets: {child_tickets}")
    
    # Return relevant data
    return cinema_name, solutions

def print_cinema_info(cinema_info):
    cinema_name, occupancy_percent, revenue = cinema_info
    print(f"{cinema_name} - Occupancy: {occupancy_percent:.2f}%, Revenue: {revenue} kr")

# Function to print total revenue
def print_total_revenue(total_revenue):
    print("\nTotal revenue of all cinemas:", total_revenue, "kr")

def main():
    while True:
        print("\n1. Calculate revenue and occupancy")
        print("2. Calculate ticket quantities")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            cinemas = read_cinema_file()
            total_revenue = 0
            cinema_data = []

            for cinema_info in cinemas:
                result = process_option_1(cinema_info)
                if result is not None:
                    cinema_name, occupancy_percent, revenue = result
                    total_revenue += revenue
                    cinema_data.append((cinema_name, occupancy_percent, revenue))

            sorted_cinemas = sorted(cinema_data, key=lambda x: x[1], reverse=True)
            print("\nCinemas sorted by occupancy:")
            for cinema_info in sorted_cinemas:
                print_cinema_info(cinema_info)
            print_total_revenue(total_revenue)

        elif choice == "2":
            cinemas = read_cinema_file()
            
            print("\nAvailable Cinemas:")
            for i, cinema_info in enumerate(cinemas, start=1):
                print(f"{i}. {cinema_info[0]}")
            
            selected_cinema_index = int(input(f"Choose a cinema (1-{len(cinemas)}): ")) - 1
            selected_cinema_info = cinemas[selected_cinema_index]
            
            result = process_option_2(selected_cinema_info)
            if result is not None:
                cinema_name, solutions = result
                print(f"\n{cinema_name}")
                print("Valid solutions:")
                for i, solution in enumerate(solutions, start=1):
                    pensioner_tickets, adult_tickets, child_tickets = solution
                    print(f"Solution {i}:")
                    print(f"Pensioner tickets: {pensioner_tickets}, Adult tickets: {adult_tickets}, Child tickets: {child_tickets}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()