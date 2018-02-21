import unittest
import os

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)

include('GedcomParser.py')

class Unique_Name_B_Date_Test(unittest.TestCase):
    """
    Test the unique name and birthdate method

    """
    def test_unique_name(self):
        result=[('0','NOTE','Y','START OF TEST'),('0','INDI','Y','@I12@'),('1','NAME','Y','Elsie /Fudd/'),('2', 'GIVN','Y','Elsie'),
                ('2', 'SURN','Y','Elsie'),('2', '_MARNM','Y','Fudd'),('1','SEX','Y', 'F'), ('1', 'BIRT','Y'),('2', 'DATE','Y', '3 FEB 2018'),
                ('1','FAMC','Y','@F5@'),('0','INDI','Y','@I13@'),('1','NAME','Y','Elsie /Fudd/'),('2', 'GIVN','Y','Elsie'),
                ('2', 'SURN','Y','Elsie'),('2', '_MARNM','Y','Fudd'),('1','SEX','Y', 'F'), ('1', 'BIRT','Y'),('2', 'DATE','Y', '3 FEB 2019'),
                ('1','FAMC','Y','@F5@'),]
        
        data=parse_valid_results(result)
        self.assertFalse(unique_name_b_date(data[1]))  # Assert False name not unique
    def test_unique_birth(self):
        result=[('0','NOTE','Y','START OF TEST'),('0','INDI','Y','@I12@'),('1','NAME','Y','Betty /Fudd/'),('2', 'GIVN','Y','Betty'),
                ('2', 'SURN','Y','Betty'),('2', '_MARNM','Y','Fudd'),('1','SEX','Y', 'F'), ('1', 'BIRT','Y'),('2', 'DATE','Y', '3 FEB 2018'),
                ('1','FAMC','Y','@F5@'),('0','INDI','Y','@I13@'),('1','NAME','Y','Elsie /Fudd/'),('2', 'GIVN','Y','Elsie'),
                ('2', 'SURN','Y','Elsie'),('2', '_MARNM','Y','Fudd'),('1','SEX','Y', 'F'), ('1', 'BIRT','Y'),('2', 'DATE','Y', '3 FEB 2018'),
                ('1','FAMC','Y','@F5@'),]
        
        data=parse_valid_results(result)
        self.assertFalse(unique_name_b_date(data[1]))  # Assert False birthdate not unique


if __name__ == "__main__":
    unittest.main()
