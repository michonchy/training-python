import quiz037
def test_number():
    assert quiz037.is_number("2") 

def test_number_with_few():
    try:
        quiz037.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz037.keisann(1) == 6
 







