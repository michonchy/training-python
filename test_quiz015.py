import quiz015

def test_number():
    assert quiz015.is_number("2") == True

def test_number_with_few():
    try:
        quiz015.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "正の整数値を入力してください。"



