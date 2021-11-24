import quiz014

def test_number():
    assert quiz014.is_number("2") == True

def test_number_with_few():
    try:
        quiz014.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"



