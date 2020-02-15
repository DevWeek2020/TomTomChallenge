from datetime import datetime

class Order:
	def __init__ (self, uid, orderTime, customer_id, business_id, items):
		self.uid = uid
		self.customer_id = customer_id
		self.business_id = business_id
		self.items = items
        self.orderTime = datetime.datetime.now()
        self.orderComplete = checkStock()
    
	def calculateTotalPrice (self):
		""" calculates the total price for an order"""
        totalPrice = 0
        for item in items:
            price = Item.getPriceForAnItem()
            totalPrice += price
        return totalPrice
    
    def checkStock (self):
        """ checks if the items to be orders is in stock"""
        """ if not in stock, return false"""
        for item in items:
            inStock = Business.checkAvailability(item)
            if inStock != true:
                return false
                s
    def __dict__ (self):
        returnDict = {'uid':self.uid, 'Customer ID':self.customer_id, 'Business ID': self.business_id,
                        'Items' : self.items, 'Order Time': self.orderTime, 'Order Complete':self.orderComplete}
        return returnDict