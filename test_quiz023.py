import quiz023
def test_number():
    assert quiz023.is_number("2") 

def test_number_with_few():
    try:
        quiz023.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
        
def test_keisann():
    assert quiz023.keisann("9") == "OK"
    assert quiz023.keisann("11") == "NG"

