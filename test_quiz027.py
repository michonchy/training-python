import quiz027
def test_number():
    assert quiz027.is_number("2") 

def test_number_with_few():
    try:
        quiz027.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz027.keisann(10) == 55
    assert quiz027.keisann(-1) == 0








