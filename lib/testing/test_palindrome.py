import pytest
from lib.palindrome import longest_palindromic_substring


# ==============================
# Basic Functionality Tests
# ==============================

@pytest.mark.parametrize("input_str, expected_outputs", [
    ("babad", {"bab", "aba"}),
    ("cbbd", {"bb"}),
    ("racecar", {"racecar"}),
])
def test_basic_cases(input_str, expected_outputs):
    result = longest_palindromic_substring(input_str)
    assert result in expected_outputs


# ==============================
# Single Character & Small Inputs
# ==============================

@pytest.mark.parametrize("input_str", [
    "a",
    "z",
])
def test_single_character(input_str):
    result = longest_palindromic_substring(input_str)
    assert result == input_str


@pytest.mark.parametrize("input_str, expected_outputs", [
    ("ac", {"a", "c"}),
])
def test_two_characters(input_str, expected_outputs):
    result = longest_palindromic_substring(input_str)
    assert result in expected_outputs


# ==============================
# All Same Characters
# ==============================

@pytest.mark.parametrize("input_str", [
    "aaaaa",
    "bbbb",
])
def test_all_same_characters(input_str):
    result = longest_palindromic_substring(input_str)
    assert result == input_str


# ==============================
# No Palindrome Longer Than 1
# ==============================

@pytest.mark.parametrize("input_str", [
    "abcde",
    "xyz",
])
def test_no_long_palindrome(input_str):
    result = longest_palindromic_substring(input_str)
    assert len(result) == 1
    assert result in input_str


# ==============================
# Even vs Odd Length Palindromes
# ==============================

@pytest.mark.parametrize("input_str, expected", [
    ("aba", "aba"),
    ("abba", "abba"),
    ("bb", "bb"),
])
def test_even_and_odd_palindromes(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result == expected


# ==============================
# Empty String
# ==============================

def test_empty_string():
    result = longest_palindromic_substring("")
    assert result == ""


# ==============================
# Numeric Strings
# ==============================

@pytest.mark.parametrize("input_str, expected", [
    ("12321", "12321"),
    ("1223", "22"),
])
def test_numeric_strings(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result == expected


# ==============================
# Case Sensitivity
# ==============================

def test_case_sensitivity():
    result = longest_palindromic_substring("Aa")
    assert result in {"A", "a"}


# ==============================
# Large Input
# ==============================

def test_large_input():
    prefix = "".join(str(i % 10) for i in range(500))
    suffix = "".join(str((i + 3) % 10) for i in range(500))
    long_string = prefix + "racecar" + suffix

    result = longest_palindromic_substring(long_string)
    assert result == "racecar"


# ==============================
# Invalid Input Handling
# ==============================

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["a", "b"],
])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        longest_palindromic_substring(invalid_input)