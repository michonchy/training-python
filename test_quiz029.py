import quiz029
def test_number():
    assert quiz029.is_number("2") 

def test_number_with_few():
    try:
        quiz029.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"










