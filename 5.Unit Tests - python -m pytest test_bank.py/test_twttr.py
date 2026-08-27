from twttr import shorten


def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""


def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""


def test_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("Python Programming") == "Pythn Prgrmmng"


def test_numbers_and_punctuation():
    assert shorten("12345") == "12345"
    assert shorten("Hello, World!") == "Hll, Wrld!"


def test_words_without_vowels():
    assert shorten("rhythm") == "rhythm"