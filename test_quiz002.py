import quiz002

def test_mod():
    assert quiz002.mod(12345, 7) == 4


def test_mod_0():
    try:
        quiz002.mod(7, 0)
    except Exception as e:
        assert str(e) == "0で割ってはいけません。"