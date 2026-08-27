from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True
    assert is_valid("ABCDEFG") == False


def test_start_with_letters():
    assert is_valid("123ABC") == False
    assert is_valid("1ABC") == False
    assert is_valid("A1") == False
    assert is_valid("AB1") == True


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS123") == True


def test_letters_after_numbers():
    assert is_valid("50CS") == False
    assert is_valid("CS5A") == False
    assert is_valid("AB12C") == False
    assert is_valid("AB123") == True


def test_punctuation():
    assert is_valid("CS-50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS50!") == False


def test_letters_only():
    assert is_valid("CS") == True
    assert is_valid("ABC") == True
    assert is_valid("HELLO") == True