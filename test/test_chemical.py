import pytest
import sys
sys.path.insert(1, '/Users/xiaoleguo/kg_byte/fun/chemical_calculator/src')
import chemical 

class TestChemical():
	def test_chemical_properties(self):
		sample = chemical.Chemical('water', '7732-18-5', '35', 'product_1')
		assert sample.name == 'water'
		assert sample.mw == '18.0152'
		assert sample.smile == 'O'
		assert sample.product_name == 'product_1'
		assert sample.max_con == '35'
