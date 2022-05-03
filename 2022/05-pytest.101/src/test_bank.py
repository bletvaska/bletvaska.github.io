from multiprocessing.sharedctypes import Value
import pytest
from bank import BankAccount

@pytest.fixture
def empty_account():
    ba = BankAccount('jano')
    yield ba


# bank account creation

def test_when_account_created_then_owner_has_name():
    # arrange
    owner = "jano"

    # act
    ba = BankAccount(owner)

    # assert
    assert ba.owner == "jano"


def test_when_account_created_then_ballance_is_0():
    # arrange
    owner = 'jano'

    # act
    ba = BankAccount(owner)

    # assert
    assert ba.balance == 0



# withdraw
@pytest.mark.parametrize('amount', [None, '', True, 10.23, BankAccount('jano'), [], (), {}])
def test_when_invalid_amount_type_is_given_then_raise_type_error(amount):
    # arrange
    owner = 'jano'
    ba = BankAccount(owner)

    # act
    with pytest.raises(TypeError):
        ba.withdraw(amount)

    # assert


def test_when_negative_amount_is_given_then_raise_value_error():
    # arrange
    owner = 'jano'
    ba = BankAccount(owner)
    amount = -10

    # act
    with pytest.raises(ValueError):
        ba.withdraw(amount)

    # assert



@pytest.mark.parametrize("word",
    ['hello', 'World', '123', ''])
def test_when_not_uppercase_word_is_given_then_false(word):
    assert word.isupper() == False


def test_when_zero_is_given_then_raise_zerodivisionerror():
    # arrange
    value = 0

    # act
    with pytest.raises(ZeroDivisionError):
        10 / value


def test_when_none_is_given_then_raise_typeerror():
    # arrange
    value = None

    # act
    with pytest.raises(TypeError):
        assert str.isupper(value)
