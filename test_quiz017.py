import quiz017
def test_number():
    assert quiz017.is_number("2") 

def test_number_with_few():
    try:
        quiz017.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"
def test_number_count():
    assert quiz017.number_array(4) == '''0
1
2
3
'''



