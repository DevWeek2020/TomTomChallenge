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
        returnDict = {'Local_uid' : local_uid, 'Name': name, 'PhoneNumber': phoneNumber, 'Address' : address, 'OpenTime' : openTime, 'Business Type' : businessType, 'Reviews' : reviews, 'Posts' : posts}
        return returnDict
        
	