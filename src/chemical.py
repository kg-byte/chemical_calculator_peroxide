import cirpy 

class Chemical:
	def __init__(self, name, cas, max_con, product_name):
		self.name = name.lower()
		self.mw = cirpy.resolve(cas, 'MW')
		self.smile = cirpy.resolve(cas, 'smiles') 
		self.max_con = max_con 
		self.product_name = product_name 