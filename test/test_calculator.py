import pytest
import sys
sys.path.insert(1, '/Users/xiaoleguo/kg_byte/fun/chemical_calculator/src')
import calculator 
from chemical import Chemical 

class TestCalculator():
	def test_csv_import(self):
		calc = calculator.Calculator()
		results = calc.read_data()
		assert type(results) == list
		assert len(results) == 16
		assert isinstance(results[0], Chemical)
		
		