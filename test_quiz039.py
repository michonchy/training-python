import quiz039
def test_number():
    assert quiz039.is_number("2") 

def test_number_with_few():
    try:
        quiz039.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz039.keisann(0) == None





