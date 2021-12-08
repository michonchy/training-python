import quiz033
def test_number():
    assert quiz033.is_number("2") 

def test_number_with_few():
    try:
        quiz033.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def get_rid():
    assert quiz033.get_rid(5) == "12346789"





