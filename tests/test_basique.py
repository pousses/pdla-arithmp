from arithmp.parser import Parser



def test_add () :
    parse = Parser().parse
    assert parse(None, "3 + 4")== 7
    assert parse(None, "0 + 4")== 4

