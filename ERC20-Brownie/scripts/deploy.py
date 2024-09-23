from brownie import MyToken, accounts

def main():
    deployer = accounts.load('account_for_deploy')
    
    token = MyToken.deploy([deployer.address], deployer.address, {'from': deployer})
    print(f'Token deployed to: {token.address}')