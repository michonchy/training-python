import quiz012

def test_number():
    assert quiz012.is_number("2") == True

def test_number_with_few():
    try:
        quiz012.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

