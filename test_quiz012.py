import quiz012

def test_number():
    assert quiz012.is_number("2") 

def test_number_with_few():
    try:
        quiz012.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_get_hello_world_test():
    assert quiz012.get_hello_world_set(2) == '''Hello World!
Hello World!
'''