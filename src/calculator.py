import csv
import ipdb
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

