import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# ========== ТЕСТЫ ДЛЯ capitalize ==========


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   test", "   test"),
    ("@skypro", "@skypro"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# ========== ТЕСТЫ ДЛЯ trim ==========


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   123", "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# ========== ТЕСТЫ ДЛЯ contains ==========


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    ("SkyPro", "Pro", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("abc", "", False),  # ДЕФЕКТ: может вернуть True
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# ========== ТЕСТЫ ДЛЯ delete_symbol ==========


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("abracadabra", "a", "brcdbr"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("abc", "", "abc"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
