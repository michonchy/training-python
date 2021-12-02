import quiz015

def test_number():
    assert quiz015.is_number("2") 

def test_number_with_few():
    try:
        quiz015.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "正の整数値を入力してください。"

def test_number_count():
    assert quiz015.number_count(4) == '''0
2
4
'''

