import quiz009

def test_number():
    assert quiz009.number("1") == "positive"
    assert quiz009.number("-2") == "negative"
    assert quiz009.number("0") == "zero"


