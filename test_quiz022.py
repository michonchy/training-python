import quiz022
def test_number():
    assert quiz022.is_number("2") 

def test_number_with_few():
    try:
        quiz022.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
        
def test_keisann():
    assert quiz022.keisann("11") == "OK"
    assert quiz022.keisann("1") == ""

