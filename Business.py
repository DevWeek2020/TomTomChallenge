class Business:
	def __init__(self, local_uid, name, phoneNumber, address, openTime, businessType, reviews, posts):
		self.local_uid = local_uid
		self.name = name
		self.phoneNumber = phoneNumber
		self.address = phoneNumber
		self.openTime = openTime
		self.businessType = businessType
		self.reviews = reviews
		self.posts = posts
    
    def __dict__():
        """ returns the all class attributes in dictionary format """
        returnDict = {'Local_uid' : self.local_uid, 'Name': self.name, 'PhoneNumber': self.phoneNumber, 'Address' : self.address, 'OpenTime' : self.openTime, 'Business Type' : self.businessType, 'Reviews' : self.reviews, 'Posts' : self.posts}
        return returnDict
        
	