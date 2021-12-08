import quiz035
def test_number():
    assert quiz035.is_number("2") 

def test_number_with_few():
    try:
        quiz035.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz035.keisann(1) == 7
 







