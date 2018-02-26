import unittest

from GedcomParser import parse_gedcom_file


class MarriageNotWithDescendantsTests(unittest.TestCase):
    """
    Test Cases for U.S. 17
    """          

    def test_marriage_descendants(self):
        """
        Validate if a family member has married their own descendants
        """
        gedcom_data = parse_gedcom_file("../sampledata/us17testdata.ged")
        for individual in gedcom_data[1]:
            spouse_ids = gedcom_data[1].get(individual).spouse            
            for id in spouse_ids:
                  self.assertTrue(gedcom_data[1].get(individual).validate_spouse(id))

      
if __name__ == "__main__":
    unittest.main()
