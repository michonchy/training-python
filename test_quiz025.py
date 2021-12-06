import quiz025
def test_number():
    assert quiz025.is_number("2") 

def test_number_with_few():
    try:
        quiz025.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
        
def test_keisann():
    assert quiz025.keisann("-11") == "range1"
    assert quiz025.keisann("-8") == "range2"
    assert quiz025.keisann("8") == "range3"

