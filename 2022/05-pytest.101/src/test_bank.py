import pytest

from bank import BankAccount


@pytest.fixture
def empty_account():
    # setup
    ba = BankAccount()

    yield ba

    # teardown


# ked sa ucet vytvori, tak zostatok bude 0
def test_when_account_is_created_then_ballance_is_0(empty_account):
    assert empty_account.ballance == 0, "Po vytvoreni ma byt zostatok na ucte 0"


def test_when_account_is_created_and_ballance_is_provided_then_ballannce_should_be_returned():
    ba = BankAccount(ballance=100)
    assert ba.ballance == 100


def test_when_amount_is_deposit_to_empty_account_then_ballance_is_same(empty_account):
    # Arrange
    amount = 100
    expected = 100

    # Act
    empty_account.deposit(amount)

    # Assert
    assert empty_account.ballance == expected


def test_when_deposit_to_account_with_balance_then_return_summary(empty_account):
    # Arrange
    empty_account.deposit(200)
    amount = 100
    expected = 300

    # Act
    empty_account.deposit(amount)

    # Assert
    assert empty_account.ballance == expected


def test_when_negative_amount_is_deposit_then_raise_exception_valueerror(empty_account):
    # Arrange
    amount = -100

    # Act / Assert
    with pytest.raises(ValueError):
        empty_account.deposit(amount)

@pytest.mark.wip
@pytest.mark.parametrize("amount",
            [None, 'hello', 123.45, True, [], (), {}, BankAccount()])
def test_when_invalid_type_is_deposit_then_raise_typeerror(amount, empty_account):
    # Act
    with pytest.raises(TypeError):
        empty_account.deposit(amount)

