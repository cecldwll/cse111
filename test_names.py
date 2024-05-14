from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Caitlyn', 'Caldwell') == "Caldwell; Caitlyn"
    assert make_full_name('Morgan', 'Chappell') == "Chappell; Morgan"
    assert make_full_name('Ty', 'Harvey') == "Harvey; Ty"
    assert make_full_name('John', 'John-Johnson') == "John-Johnson; John"

def test_extract_family_name():
    assert extract_family_name("Caldwell; Caitlyn") == "Caldwell"
    assert extract_family_name("Chappell; Morgan") == "Chappell"
    assert extract_family_name("Harvey; Ty") == "Harvey"
    assert extract_family_name("John-Johnson; John") == "John-Johnson"

def test_extract_given_name():
    assert extract_given_name("Caldwell; Caitlyn") == "Caitlyn"
    assert extract_given_name("Chappell; Morgan") == "Morgan"
    assert extract_given_name("Harvey; Ty") == "Ty"
    assert extract_given_name("John-Johnson; John") == "John"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
