import quiz018
def test_number():
    assert quiz018.is_number("2") 

def test_number_with_few():
    try:
        quiz018.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"



