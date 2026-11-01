from arithmp.parser import Parser



def test_add () :
    parse = Parser().parse
    assert parse("3 + 4")== 7.0
    assert parse("0 + 4")== 4

