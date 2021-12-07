import quiz028
def test_number():
    assert quiz028.is_number("2") 

def test_number_with_few():
    try:
        quiz028.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz028.keisann(3) == 6
    assert quiz028.keisann(-1) == 1








