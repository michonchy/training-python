import quiz038
def test_number():
    assert quiz038.is_number("2") 

def test_number_with_few():
    try:
        quiz038.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz038.keisann(0) == 'end'





