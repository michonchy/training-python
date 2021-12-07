import quiz032
def test_number():
    assert quiz032.is_number("2") 

def test_number_with_few():
    try:
        quiz032.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_multiple():
    assert quiz032.multiple(20) == "1234bar6789bar11121314bar16171819bar"





