from cardnames import *

def test_empty_name() -> None:
	given = ""
	expected = False
	result = empty_name(given)
	assert result == expected

def test_space_case() -> None:
	given = "      "
	expected = False
	result = space_case(given)
	assert result == expected

def test_digit_case() -> None:
	given = "palavra1"
	expected = False
	result = digit_case(given)
	assert result == expected

def test_special_case() -> None:
	given = "palavra@!#$"
	expected = False
	result = special_case(given)
	assert result == expected

def test_is_uppercase() -> None:
	given = "Ronaldo"
	expected = "RONALDO"
	result = fit(given)
	assert result == expected

def test_is_strip() -> None:
	given = "  KAUA RONALDO  WESLEY     "
	expected = "KAUA RONALDO WESLEY"
	result = fit(given)
	assert result == expected

def test_space_between() -> None:
	given = "   KAUA   LUCAS   RENATO"
	expected = "KAUA LUCAS RENATO"
	result = space_between(given)
	assert result == expected

def test_remove_suffix() -> None:
	given = "KAUAN DOS SANTOS DA CRUZ DE DEUS"
	expected = "KAUAN SANTOS CRUZ DEUS"
	result = remove_suffix(given)
	assert result == expected

def test_abbreviation_undername() -> None:
	given = "WESLEY JUNIOR"
	expected = "WESLEY JR"
	result = abbreviation_undername(given)
	assert result == expected
	
def test_fit() -> None:
	given = "  Wesley   JUNIOR Neto Dos Santos portugual"
	expected = "WESLEY JR N SANTOS PORTUGU"
	result = fit(given)
	assert result == expected