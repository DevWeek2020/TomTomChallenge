cimport json
import * from dev20_api

def generate_json_from_business_list(business_list, fileName):
	file = access_file_in_data(fileName, 2)
	for business in business_list:
		json.dump(business.__dict__, file)

def generate_json_from_customer_list(customer_list, fileName):
	file = access_file_in_data(fileName)
	for customer in customer_list:
		json.dump(customer.__dict, file)

def