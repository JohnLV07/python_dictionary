# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

''' Problem Statement: Develop a program that:

-Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
-Implement functions to:
-Open a new service ticket.
-Update the status of an existing ticket.
-Display all tickets or filter by status.
-Initialize with some sample tickets and include functionality for additional ticket entry.
-Example ticket structure:
'''

def new_ticket(tickets,ticket_id, user_id, issue, status):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"Customer": user_id, "Issue": issue, "Status": status}
        print(f"New ticket claim claim for '{user_id}' initiated.")
    else:
        print(f"ticket '{tickets}' or user '{user_id}' was not found.")

    
def update_status(tickets, user_id, status):
    if user_id in tickets:
        tickets[user_id]["status"] = status
        print(f"{user_id}'s ticket status updated to {status}. ")
    pass

def display_tickets(tickets):
    for tid, details in tickets.items():
        customer = details.get('Customer')
        issue = details.get('Issue')
        status = details.get('Status')
        print(f"Ticket Id: {tid}\nCustomer: {customer}\nIssue: {issue}\nStatus: {status}")

     

service_tickets = {}


while True:
    print("\nTicket Service System")
    print("1: New service Ticket\n2: Update Status on existing ticket\n3: Display all tickets\n5: Exit")
    choice = input("please Select an option: ")

    if choice == '1':
        tid =input("Enter your ticket number: ")
        usn = input("Enter your username: ")
        issue = input("Enter your issue or details: ")
        status = input("Enter status (open/close): ") 
        new_ticket(service_tickets, tid, usn, issue, status)
        new_ticket()

    elif choice == '2':
        tid = input("Enter the ticket id: ")
        status = input("Enter status (open/close): ")
        update_status(service_tickets, tid, status)

    elif choice == '3':
        display_tickets(service_tickets)
        
    elif choice == '4':
        print("Exiting The ticket system.")
        break