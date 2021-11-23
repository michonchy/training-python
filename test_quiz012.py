import quiz012

def test_number():
    assert quiz012.number(1) == "Hello World!"

def test_number_with_few():
    try:
        quiz012.number(1.1)
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"


