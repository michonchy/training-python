import quiz026
def test_number():
    assert quiz026.is_number("2") 

def test_number_with_few():
    try:
        quiz026.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_keisann():
    assert quiz026.keisann("1") == "one"
    assert quiz026.keisann("2") == "two"
    assert quiz026.keisann("3") == "three"
    assert quiz026.keisann("5") == "others"







