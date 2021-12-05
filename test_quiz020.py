import quiz020
def test_number():
    assert quiz020.is_number("2") 

def test_number_with_few():
    try:
        quiz020.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_kakezan():
    assert quiz020.keisann("12","5") == (2,10)



