class item:
	def __init__(self, item_name, item_uid, business_uid, expire_time
				description, allergy_info, category, quantity, price, is_raw):
		self.item_name = item_name
		self.item_uid = item_uid
		self.business_uid = business_uid
		self.expire_time = expire_time
		self.description = description
		self.allergy_info = allergy_info
		self.category = category
		self.quantity = quantity
		self.price = price
		self.is_raw = is_raw
	
	def __dict__ (self):
		returnDict = {'Item Name': self.item_name, 'Item Uid:' : self.item_uid, 
						'Business Uid' : self.business_uid, 
						'Expiration date' : self.expire_time,
						'Description' : description, 
						'Allergy Information' : self.allergy_info,
						'Category' : self.category, 'Quantity': self.quantity, 
						'Price' : self.price, 'Raw' : self.is_raw}
		return returnDict
		
	