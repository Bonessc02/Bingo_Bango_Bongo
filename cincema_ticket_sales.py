""" 
Name : Sebastian Costa
Title: Cinema Pre-Sales Ticket Application
Date: January 22,2026
Assignment : Ticket Sales Accumulation Program

Description:

This program allows a user to simulate a cinema pre-sales ticketing system.
A total of 20 tickets are available for purchase. Each purchaser may buy between 
1 to 4 tickets per transaction. The program will continue to operate until all
20 are sold and displays a total for the number of buyers.
"""

def get_ticket_request(remaining_tickets):
	"""
	prompts the user to enter the number of movie tickets they want to purchase.
	
	Parameters:
	remaining_tickets (int): The number of tickets currently currently available.
	
	Returns:
	int: The number of tickets reqeusted by the customer.
	"""
	print(f"\nTickets remaining: {remaining_tickets}")
	tickets = int(input("How many tickets are you planning on buying?(1-4)"))
	return tickets
	
def sell_tickets():
	"""
	Controls the ticket selling procedure.
	Tracks remaining tickets available, validates the input and counts buyers.
	"""
	TOTAL_TICKETS = 10
	remaining_tickets = TOTAL_TICKETS
	total_buyers = 0 # accumulator for purchases for one buyer
	
	while remaining_tickets > 0:
	    tickets_requested = get_ticket_request(remaining_tickets)
	    
	    if tickets_requested < 1 or tickets_requested > 4:
	    	print("Invalid number of tickets requested. Please enter a number of tickets between 1 and 4. ")
	    	
	    elif tickets_requested > remaining_tickets:
	    		print("Not enough tickets remaining for purchase.")
	    		
	    else:
	    	remaining_tickets -= tickets_requested
	    	total_buyers += 1
	    	print(f"You Purchased {tickets_requested} tickets(s).")
	    	print(f"Tickets Remaining: {remaining_tickets}")
	    	
	    	
	print("\nAll tickets have been sold!")
	print(f"The total number of people whom purchased tickets is: {total_buyers}")
	    	
	    	
	    	
# Program execution starts
sell_tickets()
	    		
	    		
	
