import pytest
from brownie import MyToken, accounts
#from ..contracts import MyToken

TOTAL_SUPPLY_LIMIT = 1000000 * 10**18
MINT_AMOUNT = 100000 * 10**18

@pytest.fixture
def token():
    return MyToken.deploy([accounts[0], accounts[1], accounts[2]], accounts[0], {'from': accounts[0]})


def test_initial_mint(token):
    assert token.balanceOf(accounts[0]) == MINT_AMOUNT
    assert token.balanceOf(accounts[1]) == MINT_AMOUNT
    assert token.balanceOf(accounts[2]) == MINT_AMOUNT


def test_total_supply_limit(token):
    assert token.totalSupply() == 3 * MINT_AMOUNT


def test_mint_by_owner(token):
    token.mint(accounts[3], MINT_AMOUNT, {'from': accounts[0]})
    assert token.balanceOf(accounts[3]) == MINT_AMOUNT
    assert token.totalSupply() == 4 * MINT_AMOUNT


def test_mint_fail_exceeds_limit(token):
    with pytest.raises(Exception):
        token.mint(accounts[3], TOTAL_SUPPLY_LIMIT, {'from': accounts[0]})


def test_only_owner_can_mint(token):
    with pytest.raises(Exception):
        token.mint(accounts[3], MINT_AMOUNT, {'from': accounts[1]})