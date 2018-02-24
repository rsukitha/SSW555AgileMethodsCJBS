import unittest

from GedcomParser import parse_gedcom_file


class GenderForRoleTests(unittest.TestCase):
    """
    Test Cases for U.S. 25
    """

    def test_hs(self):
        """
        Validate that if a family contains an invalid id, regardless of where you are in the script, false is returned
        """
        gedcom_data = parse_gedcom_file("./sampledata/us25testdata.ged")
        for family in gedcom_data[0]:
            children_ids = gedcom_data[0].get(family).children
            for id in children_ids:
                if id in gedcom_data[1]:
                    gedcom_data[1].get(id)
                    if id == "hs":
                        self.assertFalse(gedcom_data[0].get(family).validate_children(gedcom_data[1]))

    def test_hs2(self):
        """
        Validate that if a family contains an invalid id, regardless of where you are in the script, false is returned
        """
        gedcom_data = parse_gedcom_file("./sampledata/us25testdata.ged")
        for family in gedcom_data[0]:
            children_ids = gedcom_data[0].get(family).children
            for id in children_ids:
                if id in gedcom_data[1]:
                    gedcom_data[1].get(id)
                    if id == "hs2":
                        self.assertFalse(gedcom_data[0].get(family).validate_children(gedcom_data[1]))

    def test_hs3(self):
        """
        Validate that if a family contains an invalid id, regardless of where you are in the script, false is returned
        """
        gedcom_data = parse_gedcom_file("./sampledata/us25testdata.ged")
        for family in gedcom_data[0]:
            children_ids = gedcom_data[0].get(family).children
            for id in children_ids:
                if id in gedcom_data[1]:
                    gedcom_data[1].get(id)
                    if id == "hs3":
                        self.assertFalse(gedcom_data[0].get(family).validate_children(gedcom_data[1]))

    def test_hs4(self):
        """
        Validate that if a family contains an invalid id, regardless of where you are in the script, false is returned
        """
        gedcom_data = parse_gedcom_file("./sampledata/us25testdata.ged")
        for family in gedcom_data[0]:
            children_ids = gedcom_data[0].get(family).children
            for id in children_ids:
                if id in gedcom_data[1]:
                    gedcom_data[1].get(id)
                    if id == "hs4":
                        self.assertFalse(gedcom_data[0].get(family).validate_children(gedcom_data[1]))


if __name__ == "__main__":
    unittest.main()