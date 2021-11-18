import quiz003

def test_number():
    assert quiz003.number("123") == 123
    assert quiz003.number("-1") == -1

def test_number_with_few():
    try:
        quiz003.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
