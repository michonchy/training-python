import quiz034
def test_number():
    assert quiz034.is_number("2") 

def test_number_with_few():
    try:
        quiz034.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def get_rid():
    assert quiz034.get_rid(5) == "1234789"





