import unittest


from GedcomParser import parse_gedcom_file


class ResultsParseTest(unittest.TestCase):
    
    def test_valid_parse_fam(self):
        result=[('0','NOTE','Y','START OF TEST'),('0','FAM','Y','f2'),]
        data=parse_valid_results(result)
        sz_dict_0=len(data[0])
        sz_dict_1=len(data[1])
        self.assertEqual((1,0),(sz_dict_0,sz_dict_1))   # Assert result is valid family dictionary entry
        for fam_id, family in (data[0].items()):
            test_fam=[family.id]
        self.assertEqual((['f2']),(test_fam))   # Assert valid result in correct dictionary
    def test_valid_parse_ind(self):
        result=[('0','NOTE','Y','START OF TEST'),('0','INDI','Y','i2'),]
        data=parse_valid_results(result)
        sz_dict_0=len(data[0])
        sz_dict_1=len(data[1])
        self.assertEqual((0,1),(sz_dict_0,sz_dict_1))  # Assert result is valid individual dictionary entry
        for indi_id, individual in (data[1].items()):
            test_ind=[individual.id]
        self.assertEqual((['i2']),(test_ind))  # Assert valid result in correct dictionary
        result=[('0','NOTE','Y','START OF TEST'),('0','FAM','Y','f2'),('0','FAM','Y','f2'),]
        data=parse_valid_results(result)
        sz_dict_0=len(data[0])
        sz_dict_1=len(data[1])
        sz_list_1=len(data[2])
        self.assertEqual((1,0,1),(sz_dict_0,sz_dict_1,sz_list_1))   # Assert duplicate family is captured in list entry
    def test_valid_parse_dup_ind(self):
        result=[('0','NOTE','Y','START OF TEST'),('0','INDI','Y','i2'),('0','INDI','Y','i2'),]
        data=parse_valid_results(result)
        sz_dict_0=len(data[0])
        sz_dict_1=len(data[1])
        sz_list_2=len(data[3])
        self.assertEqual((0,1,1),(sz_dict_0,sz_dict_1,sz_list_2))   # Assert duplicate individual is captured in list entry


if __name__ == "__main__":
    unittest.main()
