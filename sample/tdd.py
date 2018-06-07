import unittest
from sample.strings_example import StringsExamples


class TestStringsExamples(unittest.TestCase):
    def test_concat_strings(self):
        string1 = "hola"
        string2 = "adios"
        result = StringsExamples.concat_strings(string1, string2)
        assert result=="holaadios"

    def test_concat_int_string(self):
        str1 = 1
        str2 = "adios"
        self.assertRaises (TypeError,StringsExamples.concat_strings,str1,str2)

    def test_concat_string_int(self):
        str1 = "hola"
        str2 = 2
        self.assertRaises(TypeError,StringsExamples.concat_strings,str1,str2)

    def test_concat_int(self):
        str1= 1
        str2=2
        self.assertRaises(TypeError, StringsExamples.concat_strings,str1, str2)


    def test_concat_two_strings(self):
        str1= "Espana"
        str2= "Belgica"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "EspanaBelgica"



    def test_concat_string1_1(self):
        str1="a"
        str2 = "b"
        result = StringsExamples.concat_strings(str1,str2)
        assert result=="ab"


    def test_concat_string1_2(self):
        str1="a"
        str2 = "bb"
        result = StringsExamples.concat_strings(str1,str2)
        assert result=="abb"


    def test_concat_string2_1(self):
        str1="aa"
        str2 = "b"
        result = StringsExamples.concat_strings(str1,str2)
        assert result == "aab"


    def test_concat_string2_2(self):
        str1="aa"
        str2 = "bb"
        result = StringsExamples.concat_strings(str1,str2)
        assert result == "aabb"

    def test_concat_string3_2(self):
        str1="aaa"
        str2 = "bb"
        result = StringsExamples.concat_strings(str1,str2)
        assert result == "aaabb"

    def test_concat_string3_3(self):
        str1="aaa"
        str2 = "bbb"
        result = StringsExamples.concat_strings(str1,str2)
        assert result == "aaabbb"

    def test_concat_string3_4(self):
        str1="aaa"
        str2 = "bbbb"
        result = StringsExamples.concat_strings(str1,str2)
        assert result == "aaabbbb"

    def test_concat_string4_4(self):
        str1="aaaa"
        str2 = "bbbb"
        result = StringsExamples.concat_strings(str1,str2)
        assert result == "aaaabbbb"

    def test_concat_string5_4(self):
        str1 = "aaaaa"
        str2 = "bbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaabbbb"

    def test_concat_string5_5(self):
        str1 = "aaaaa"
        str2 = "bbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaabbbbb"

    def test_concat_string5_6(self):
        str1 = "aaaa"
        str2 = "bbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaabbbbbb"

    def test_concat_string6_6(self):
        str1 = "aaaaaa"
        str2 = "bbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaabbbbbb"

    def test_concat_string6_7(self):
        str1 = "aaaaaa"
        str2 = "bbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaabbbbbbb"


    def test_concat_string7_7(self):
        str1 = "aaaa"
        str2 = "bbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaabbbbb"

    def test_concat_string8_7(self):
        str1 = "aaaaaaaa"
        str2 = "bbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaaaabbbbbbb"

    def test_concat_string8_8(self):
        str1 = "aaaaaaaa"
        str2 = "bbbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaaaabbbbbbbb"

    def test_concat_string8_9(self):
        str1 = "aaaaaaaa"
        str2 = "bbbbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaaaabbbbbbbbb"

    def test_concat_string9_9(self):
        str1 = "aaaaaaaaa"
        str2 = "bbbbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaaaaabbbbbbbbb"

    def test_concat_string9_10(self):
        str1 = "aaaaaaaaa"
        str2 = "bbbbbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaaaaabbbbbbbbbb"

    def test_concat_string10_10(self):
        str1 = "aaaaaaaaaa"
        str2 = "bbbbbbbbbb"
        result = StringsExamples.concat_strings(str1, str2)
        assert result == "aaaaaaaaaabbbbbbbbbb"




if __name__ == '__main__':
    unittest.main()
