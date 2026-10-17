from calculadora import soma, subtrai


def test_soma():
    assert soma(2, 3) == 5


def test_subtrai():
    assert subtrai(5, 3) == 2
