import unittest

from GedcomParser import parse_gedcom_file


class MarriageBeforeDivorce(unittest.TestCase):
    """
    Test Cases for U.S. 04
    """
    
    def test_marriage_before_divorce(self):
        """
        Validate if divorce date has happened before marriage date
        """
        gedcom_data = parse_gedcom_file("../sampledata/us04testdata.ged")
        for family in gedcom_data[0]:
              if gedcom_data[0].get(family).married != "NA" or gedcom_data[0].get(family).divorced != "NA":              
                    self.assertTrue(gedcom_data[0].get(family).validate_marriage_divorce_date(gedcom_data[0].get(family).married))

      
if __name__ == "__main__":
    unittest.main()
