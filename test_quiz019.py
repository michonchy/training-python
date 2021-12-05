import quiz019
def test_number():
    assert quiz019.is_number("2") 

def test_number_with_few():
    try:
        quiz019.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"



