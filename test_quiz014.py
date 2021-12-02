import quiz014

def test_number():
    assert quiz014.is_number("2")

def test_number_with_few():
    try:
        quiz014.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_number_count():
    assert quiz014.number_count(2) == '''2
1
0
'''

