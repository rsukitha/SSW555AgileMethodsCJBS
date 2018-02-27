import unittest

from GedcomParser import parse_gedcom_file


class IndividualFamilyDateTests(unittest.TestCase):
    """
    Test Cases for U.S. 01 and 02
    """

    def test_us_01_marriages(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/basetestdata.ged")
        families = gedcom_data[0]
        dates = []
        for fam_id in families:
            family = families[fam_id]
            result = family.verify_date_not_future(fam_id, family.married, "FAMILY MARRIAGE")
            if result:
                dates.append(result)
        self.assertTrue(dates == [])

    def test_us_01_divorces(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/basetestdata.ged")
        families = gedcom_data[0]
        dates = []
        for fam_id in families:
            family = families[fam_id]
            result = family.verify_date_not_future(fam_id, family.divorced, "FAMILY DIVORCE")
            if result:
                dates.append(result)
        self.assertTrue(dates == [])

    def test_us_01_birthdays(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/basetestdata.ged")
        individuals = gedcom_data[1]
        dates = []
        for indi_id in individuals:
            individual = individuals[indi_id]
            result = individual.verify_date_not_future(individual.id, individual.birthday,
                                                       "INDIVIDUAL BIRTHDAY")
            if result:
                dates.append(result)
        self.assertTrue(dates == [])

    def test_us_01_marriages_neg(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/US01futuredatestests.ged")
        families = gedcom_data[0]
        dates = []
        for fam_id in families:
            family = families[fam_id]
            result = family.verify_date_not_future(fam_id, family.married, "FAMILY MARRIAGE")
            if result:
                dates.append(result)
        self.assertFalse(dates == [])

    def test_us_01_divorces_neg(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/US01futuredatestests.ged")
        families = gedcom_data[0]
        dates = []
        for fam_id in families:
            family = families[fam_id]
            result = family.verify_date_not_future(fam_id, family.divorced, "FAMILY DIVORCE")
            if result:
                dates.append(result)
        self.assertFalse(dates == [])

    def test_us_01_birthdays_neg(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/US01futuredatestests.ged")
        individuals = gedcom_data[1]
        dates = []
        for indi_id in individuals:
            individual = individuals[indi_id]
            result = individual.verify_date_not_future(individual.id, individual.birthday,
                                                       "INDIVIDUAL BIRTHDAY")
            if result:
                dates.append(result)
        self.assertFalse(dates == [])

    def test_us_01_death_neg(self):
        """
        Validate Dates are not before current date.
        """
        gedcom_data = parse_gedcom_file("./sampledata/proj02test.ged")
        individuals = gedcom_data[1]
        dates = []
        for indi_id in individuals:
            individual = individuals[indi_id]
            result = individual.verify_date_not_future(individual.id, individual.death,
                                                       "INDIVIDUAL DEATH")
            if result:
                dates.append(result)
        self.assertFalse(dates == [])

    def test_us_02(self):
        """
        Validate Birthday does not occur before Marriage
        """
        gedcom_data = parse_gedcom_file("./sampledata/basetestdata.ged")
        families = gedcom_data[0]
        individuals = gedcom_data[1]
        results = []
        for fam_id in families:
            family = families[fam_id]
            result = family.birth_before_marriage(individuals)
            if not result:
                results.append(result)
        self.assertTrue(results == [])

    def test_us_02_neg(self):
        """
        Validate Birthday does not occur before Marriage
        """
        gedcom_data = parse_gedcom_file("./sampledata/US01futuredatestests.ged")
        families = gedcom_data[0]
        individuals = gedcom_data[1]
        results = []
        for fam_id in families:
            family = families[fam_id]
            result = family.birth_before_marriage(individuals)
            if not result:
                results.append(result)
        self.assertFalse(results == [])


if __name__ == "__main__":
    unittest.main()
