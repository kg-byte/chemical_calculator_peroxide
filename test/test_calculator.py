import pytest
import sys
sys.path.insert(1, '/Users/xiaoleguo/kg_byte/fun/chemical_calculator/src')
import calculator 
from chemical import Chemical 

class TestCalculator():
	calc = calculator.Calculator()
	parsed_data = calc.read_data()

	def test_csv_import(self):
		result = TestCalculator.parsed_data
		assert type(result) == list
		assert len(result) == 16
		assert isinstance(result[0], Chemical)
		
	
	def test_generate_products(self):
		result = TestCalculator.calc.generate_products(TestCalculator.parsed_data)
		assert type(result) == dict
		assert len(result.keys()) == 4
		assert isinstance(list(result.values())[0][0], Chemical)