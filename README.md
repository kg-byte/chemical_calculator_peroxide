# Chemical Calculator Peroxide
  This chemical calculator peroxide allows for calculations of hydrogen peroxide content and the content(Oa) in a mixture and determines whether the mixture is classified as an Organic Peroxide based on [49 CFR 173.128(a)(4)](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-173/subpart-D/section-173.128).
  
## Notes on cirpy Library
  cirpy library was used in this calculator to convert CAS number to [SMILES(The simplified molecular-input line-entry system)](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) structure to quickly identify the presence of the [-o-o-] group in a species for later calculations. To install:
  ```
  pip install cirpy
  ```

## Results
  #### Which of the provided formulated products meet the definition Organic Peroxide under CFR 173.128(a)(4)?
   - Product 2 and Product 3 
  #### Which of the provided formulated products do not meet the definition?
   - Product 1 and Product 4
  #### Which subsection under CFR 173.128(a)(4) was used to determine whether the product meets or does not meet the definition of an Organic Peroxide?
   - Both subsections were used to formulate the following criteria- a product is classfied as an Organic Peroxide when its:
     -  hydrogen peroxide content is greater than 7% OR
     -  hydrogen peroxide content is more than 1% and less than 7% while its content(Oa) is greater than 0.5% OR
     -  both hydrogen peroxide and content(Oa) are greater than 1 %  
  #### Are any of the products eligible for an exemption?
   - The following 2 edge cases were discovered and addressed:
     - Product 3, Species 2 (chemical name: Alcohols, C12-15, ethoxylated) is an undefined alcohol group, for which the cirpy library did not return a usable molecular weight or SMILE structure. However, as ethoxylated alcohol groups do not contain a peroxide group[-o-o-], it does not affect the Content(Oa) calculation and this inconsistency is addressed in [Calculator.oa_content function (Line 43)](https://github.com/kg-byte/chemical_calculator_peroxide/blob/main/src/calculator.py).
      - Product 3, Species 1 (chemical name: sodium percarbonate) is a compound that contains 1.5 parts of hydrogen peroxide per 1 part of sodium carbonate. A decision was made to use a weight fraction (32.5 wt%) to convert the amount of sodium percarbonate present into hydrogen peroxide ([Calculator.h2o2_content, line 33-34](https://github.com/kg-byte/chemical_calculator_peroxide/blob/main/src/calculator.py)). To avoid duplication, sodium percabonate is no longer used when calculating content(Oa) dispite the presence of [-o-o-] group ([Calculator.oa_content, line 44](https://github.com/kg-byte/chemical_calculator_peroxide/blob/main/src/calculator.py)). 

## Git Log (8 commits in total following TDD)
  - Initial commit- create data file
  - create chemical object with properties retrieved from cirpy
  - Calculator.read_data creates a list of chemical objects
  - Calculator.generate_products produces a dic of product(key) and list of chemicals(val)
  - Calculator.h2o2_content returns a float or 0 when given list of chemicals
  - Calculator.oa_content calculates oa percent given a list of chemical species
  - Calculator.analyze_product takes in a list of chemicals and returns its h2o2, oa content and classification
  - Calculator.analyze_list returns an array of results; modify conditional in line 44 to avoid double-counting sodium percarbonate

## Testing
1. Clone this repo
```
git clone git@github.com:kg-byte/chemical_calculator_peroxide.git
```

2. install pytest if applicable
```
pip install pytest'
```
3. run pytest at the root of this directory
```
pytest
```
4. sample results
```
============================================================================== test session starts ==============================================================================
platform darwin -- Python 3.8.9, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/xiaoleguo/kg_byte/fun/chemical_calculator
collected 7 items                                                                                                                                                               

test/test_calculator.py ......                                                                                                                                            [ 85%]
test/test_chemical.py .                                                                                                                                                   [100%]

============================================================================== 7 passed in 22.87s ===============================================================================
```

## Author(s)
 - Kim Guo ([@kg-byte](https://github.com/kg-byte), [LinkedIn](https://www.linkedin.com/in/xiaole-guo-5331b4158/))
