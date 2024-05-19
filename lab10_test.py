from lab10 import getinfo
def test_line():
    line = ['6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q']
    actual = getinfo(line,"Квинстоун")
    expected = (0, 1)
    print(actual)
    assert actual == expected
def test_manylinesQ():
    line = ['16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
            '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
            '18,1,2,"Williams, Mr. Charles Eugene",male,,0,0,244373,13,,S',
            '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
            '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
            '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
            '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
            '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q']
    actual = getinfo(line,"Квинстоун")
    expected = (1, 1)
    print(actual)
    assert actual == expected
def test_manylinesS():
    line = ['16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
            '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
            '18,1,2,"Williams, Mr. Charles Eugene",male,,0,0,244373,13,,S',
            '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
            '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
            '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
            '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
            '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q']
    actual = getinfo(line,"Саутгемптон")
    expected = (3, 2)
    print(actual)
    assert actual == expected
def test_manylinesС():
    line = ['16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
            '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
            '18,1,2,"Williams, Mr. Charles Eugene",male,,0,0,244373,13,,S',
            '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
            '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
            '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
            '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
            '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q']
    actual = getinfo(line,"Шербур")
    expected = (1, 0)
    print(actual)
    assert actual == expected