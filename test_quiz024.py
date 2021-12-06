import quiz024
def test_number():
    assert quiz024.is_number("2") 

def test_number_with_few():
    try:
        quiz024.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
        
def test_keisann():
    assert quiz024.keisann("-3") == "OK"
    assert quiz024.keisann("8") == "NG"

