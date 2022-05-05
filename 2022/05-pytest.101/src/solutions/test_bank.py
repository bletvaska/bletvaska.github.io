from multiprocessing.sharedctypes import Value
import pytest
from bank import BankAccount

@pytest.fixture
def empty_account():
    # setup
    ba = BankAccount('jano')

    yield ba

    # teardown


# bank account creation

def test_when_account_created_then_owner_has_name(empty_account):
    # assert
    assert empty_account.owner == "jano"


def test_when_account_created_then_ballance_is_0(empty_account):
    # assert
    assert empty_account.balance == 0



# withdraw
@pytest.mark.parametrize('amount', [None, '', True, 10.23, BankAccount('jano'), [], (), {}])
def test_when_invalid_amount_type_is_given_then_raise_type_error(amount, empty_account):
    # act
    with pytest.raises(TypeError):
        empty_account.withdraw(amount)


def test_when_negative_amount_is_given_then_raise_value_error(empty_account):
    # arrange
    amount = -10

    # act
    with pytest.raises(ValueError):
        empty_account.withdraw(amount)


