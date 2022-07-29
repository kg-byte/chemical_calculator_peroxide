import pytest
import sys
sys.path.insert(1, '/Users/xiaoleguo/kg_byte/fun/chemical_calculator/src')
import calculator 
from chemical import Chemical 

class TestCalculator():
	calc = calculator.Calculator()
	data = calc.read_data()
	products = calc.generate_products(data)

	def test_csv_import(self):
		result = TestCalculator.data
		assert type(result) == list
		assert len(result) == 16
		assert isinstance(result[0], Chemical)
		
	
	def test_generate_products(self):
		result = TestCalculator.products
		assert type(result) == dict
		assert len(result.keys()) == 4
		assert isinstance(list(result.values())[0][0], Chemical)

	def test_h2o2_content(self):
		result_1 = TestCalculator.calc.h2o2_content(TestCalculator.products['Product 1'])
		result_2 = TestCalculator.calc.h2o2_content(TestCalculator.products['Product 2'])
		result_3 = TestCalculator.calc.h2o2_content(TestCalculator.products['Product 3'])
		result_4 = TestCalculator.calc.h2o2_content(TestCalculator.products['Product 4'])
		assert result_1 == 0
		assert result_2 == 1.8
		assert result_3 == 11.4
		assert result_4 == 1.0

	def test_oa_content(self):
		result_1 = TestCalculator.calc.oa_content(TestCalculator.products['Product 1'])
		result_2 = TestCalculator.calc.oa_content(TestCalculator.products['Product 2'])
		result_3 = TestCalculator.calc.oa_content(TestCalculator.products['Product 3'])
		result_4 = TestCalculator.calc.oa_content(TestCalculator.products['Product 4'])
		assert result_1 == 0.7
		assert result_2 == 0.5
		assert result_3 == 0
		assert result_4 == 0

	def test_analyze_product(self):
		result = TestCalculator.calc.analyze_product('Product 1', TestCalculator.products['Product 1'])
		assert result == 'Product 1 contains 0% hydrogen peroxide and 0.7% content(Oa); it is not an Organic Peroxide'

	def test_analyze_list(self):
		result = TestCalculator.calc.analyze_list()
		assert result[0] == 'Product 1 contains 0% hydrogen peroxide and 0.7% content(Oa); it is not an Organic Peroxide'
		assert result[1] == 'Product 2 contains 1.8% hydrogen peroxide and 0.5% content(Oa); it is not an Organic Peroxide'
		assert result[2] == 'Product 3 contains 11.4% hydrogen peroxide and 0% content(Oa); it is an Organic Peroxide'
		assert result[3] == 'Product 4 contains 1.0% hydrogen peroxide and 0% content(Oa); it is not an Organic Peroxide'
