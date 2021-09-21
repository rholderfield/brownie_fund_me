from scripts.helpful_scripts import get_account
from brownie import FundMe


def fund():
    fund_me = FundMe[-1]
    account = get_account
