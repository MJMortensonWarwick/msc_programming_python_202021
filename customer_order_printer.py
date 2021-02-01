
# coding: utf-8

# In[ ]:

# order printer function to take a customer name, and check 
# all their current orders
def order_printer(customer, customers, orders): # customer is the customer's first name
	# check the customer is in the dictionary
	if customer in customers:
		# check that the length of the orders value 
		# (the # of orders) is > 0
		if len(customers[customer]['orders']) > 0:
			# print the customer name
			print('Customer: ' + str(customer))
			# loop through the customer's orders
			for order in customers[customer]['orders']:
				# print each of the values stored.
				# wrapped in try statements in case the value is missing
				try:
					print('Date: ' + 						str(orders[order]['date']))
					print('Product: ' + 						orders[order]['product'])
					print('Quantity: ' + 						orders[order]['quantity'])
				except:
					pass
			# print a lne break after the customer orders
			print('\n')
		else:
			# if the customer has no orders print this to screen
			print('Customer: ' + str(customer) + ' has no orders')
			# print a lne break after the customer orders
			print('\n')
	else:
		# if the customer is not in the customers dictionary 
		# print an error message
		print('Customer name not found. Please try again')

