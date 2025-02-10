import pytest
from seasons import get_birth_date, calculate_mins, convert_to_words

def test_gbd():
    birth_date = get_birth_date('2020-06-01')
    mins = calculate_mins(birth_date)
    assert convert_to_words(mins) == 'Two million, four hundred sixty-nine thousand, six hundred minutes'

def test_get_birth_date():
    with pytest.raises(SystemExit):  # Expect sys.exit on invalid input
        get_birth_date('hi')
