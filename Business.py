class Business:
	def __init__(self, local_uid, name, phoneNumber, address, city,
                state, zip_code, openTime, businessType, reviews, posts, location):
		self.local_uid = local_uid
		self.name = name
		self.phoneNumber = phoneNumber
		self.address = phoneNumber
		self.openTime = openTime
		self.businessType = businessType
		self.reviews = reviews
		self.posts = posts
        self.location = location
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def __dict__():
        """ returns the all class attributes in dictionary format """
        returnDict = {'Local_uid' : self.local_uid, 'Name': self.name, 
                        'PhoneNumber': self.phoneNumber, 'Address' : self.address, 
                        'OpenTime' : self.openTime, 'Business Type' : self.businessType, 
                        'Reviews' : self.reviews, 'Posts' : self.posts}
        return returnDict

        