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
			# another exception - product 3 species #2 [alcohols c12-15] - unknown group which cirpy cannot provide mw/smile
			# no -o-o- group in this species so does not affect calculations
		oa_content = 0
		for chemical in chemicals:
			if chemical.smile is not None:
				if 'OO' in chemical.smile and chemical.name != 'sodium percarbonate' and chemical.name != 'hydrogen peroxide':
					# after deleting -o-o- group which is shown as 'OO' in smile structure
					# the difference in length divided by two is the number of -o-o- present (ni)
					# avoid double counting sodium percarbonate which is handled in h2o2_content function
					new_len = len(chemical.smile.replace('OO', ''))
					ni = (len(chemical.smile) - new_len)/2
					ci = float(chemical.max_con)
					mi = float(chemical.mw)
					# formula in n 49 CFR 173.128(a)(4)
					oa_content += 16 * (ni*ci/mi)
		return round(oa_content,1)
				


	def analyze_product(self, product, chemical_list):
		content_h2o2 = self.h2o2_content(chemical_list)
		content_oa = self.oa_content(chemical_list)
		# a product can be classified as an Organic Peroxide only when
			# 1. h2o2 content is greater than 7%
			# 2. h2o2 is more than 1% but no more than 7% + oa_content is greater than 0.5%
			# 3. both h2o2 and oa content are greater than 1 % 
		if content_h2o2 > 7.0:
			is_peroxide = True 
		elif content_h2o2 <= 7.0 and content_h2o2 > 1.0 and content_oa > 0.5:
			is_peroxide = True
		elif content_h2o2 > 1.0 and content_oa > 1.0:
			is_peroxide = True
		else:
			is_peroxide = False
		if is_peroxide == True:
			return f"{product} contains {content_h2o2}% hydrogen peroxide and {content_oa}% content(Oa); it is an Organic Peroxide"
		else:
			return f"{product} contains {content_h2o2}% hydrogen peroxide and {content_oa}% content(Oa); it is not an Organic Peroxide"

	def analyze_list(self):
		data = self.read_data()
		result = []
		products = self.generate_products(data)
		for product, chemical_list in products.items():
			result.append(self.analyze_product(product, chemical_list))
		return result

