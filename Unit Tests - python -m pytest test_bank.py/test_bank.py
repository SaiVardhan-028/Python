from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0


def test_h_greeting():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("Howdy") == 20


def test_other_greetings():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("Goodbye") == 100