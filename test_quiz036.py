import quiz036
def test_number():
    assert quiz036.is_number("2") 

def test_number_with_few():
    try:
        quiz036.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz036.keisann(0,1) == 21
 







