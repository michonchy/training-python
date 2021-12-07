import quiz030
def test_number():
    assert quiz030.is_number("2") 

def test_number_with_few():
    try:
        quiz030.number("1.1")
        assert False
    except Exception as e:
        assert str(e) == "整数値を入力してください。"

def test_graph():
    assert quiz030.graph(3) == "***"
    assert quiz030.graph(-1) == ""








