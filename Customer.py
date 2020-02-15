class Customer:
    password = 'defaultPassword'
	def __init__(self, local_uid, name, phoneNumber, address, email, shoppingCart):
		# SHA1 hashed from email
		self.local_uid = local_uid
		self.name = name
		self.phoneNumber = phoneNumber
		self.address = address
		self.email = email
		self.shoppingCart = shoppingCart
    
    def __dict__():
        """ returns the all class attributes in dictionary format """
        returnDict = {'Local_uid' : local_uid, 'Name': name, 'PhoneNumber': phoneNumber, 'Address' : address, 'Email' : email, 'Shopping Cart' : shoppingCart}
        return returnDict