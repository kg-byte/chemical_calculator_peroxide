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
		content = 0 # if no h2o2 or sodium percabonate found, return 0
		for chemical in chemicals:
			# if species is h2o2, retrieve mass%
			if chemical.name == 'hydrogen peroxide':
				content = float(chemical.max_con)
			# handles exception sodium percarbonate (product 3, species2), which contains 32.5% h2o2 by weight
			# Na2CO3*1.5H2O2 -> %H2O2 = (1.5*34.0147)/(1.5*34.0147+105.9888)= 0.32496
			elif chemical.name == 'sodium percarbonate':
				content = float(chemical.max_con)*0.325
		return round(content,1)


	def oa_content(self, chemicals):
		oa_content = 0
		for chemical in chemicals:
			if chemical.smile is not None:
			# another exception - product 3 species #2 [alcohols c12-15] - unknown group which cirpy cannot provide mw/smile
			# no -o-o- group in this species so does not affect calculations
				if 'OO' in chemical.smile:
					# after deleting -o-o- group which is shown as 'OO' in smile structure
					# the difference in length divided by two is the number of -o-o- present (ni)
					new_len = len(chemical.smile.replace('OO', ''))
					ni = (len(chemical.smile) - new_len)/2
					ci = float(chemical.max_con)
					mi = float(chemical.mw)
					oa_content += 16 * (ni*ci/mi)
		return round(oa_content,1)
				

