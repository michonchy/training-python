import quiz021
def test_number():
    assert quiz021.is_number("2") 

def test_number_with_few():
    try:
        quiz021.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
        
def test_keisann():
    assert quiz021.keisann("6") == "OK"
    assert quiz021.keisann("1") == ""

