import quiz013

def test_number():
    assert quiz013.is_number("2")

def test_number_with_few():
    try:
        quiz013.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_get_hello_world_test():
    assert quiz013.get_hello_world_set(2) == '''0
1
2
'''
