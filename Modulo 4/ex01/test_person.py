import pytest
from person import Person

testdata = [
    ("Alice", 30 ),
    ("Ronaldo", 27 ),
    ("Pessoa", 10 )
]

testdata2 = [
    ("Alice", 30, 31 ),
    ("Pessoa", 10, 11 ),
    ("Ronaldo", 27, 28 )
]


@pytest.mark.parametrize("name_p, age_p", testdata)
def test_person_initialization(name_p: str, age_p: int) -> None:
    """make a test of valid_password"""
    p = Person(name_p, age_p)
    assert p.name == name_p
    assert p.age == age_p
    
@pytest.mark.parametrize("name_p2, age_p2, age_expected", testdata2)
def test_person_birthday(name_p2: str, age_p2: int, age_expected: int) -> None:
    """make a test of valid_password"""
    p = Person(name_p2, age_p2)
    p.birthday()
    assert p.name == name_p2
    assert p.age == age_expected