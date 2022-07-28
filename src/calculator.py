import csv
from chemical import Chemical 

class Calculator:
	def read_data(self):
		chemical_list = []
		with open('./data/Product_List.csv', newline='') as csv_file:
		    reader = csv.reader(csv_file)
		    next(reader, None)  
		    for ProductID, CAS, ChemicalName, minVal, maxVal in reader:
		        chemical_list.append(Chemical(ChemicalName, CAS, maxVal, ProductID))
		return chemical_list

	def generate_products(self, data):
		products = {}
		for chemical in data:
			if products.__contains__(chemical.product_name):
				products[chemical.product_name].append(chemical)
			else:
				products[chemical.product_name] = [chemical]
		return products
