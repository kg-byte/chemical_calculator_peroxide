import csv
from chemical import Chemical 
import ipdb 

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


	def h2o2_content(self, chemicals):
		h2o2 = None
		for chemical in chemicals:
			if chemical.name == 'hydrogen peroxide':
				h2o2 = chemical
		if h2o2 is None:
			return 0
		return float(h2o2.max_con)


