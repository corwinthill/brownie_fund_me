from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import time

def deploy_fund_me():
    account = get_account()
    # need to pass price feed contract address to FundMe contract
    # if on sepolia use 0x694AA1769357215DE4FAC081bf1f309aDC325306
    # else on dev and need to deploy mock contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    time.sleep(1)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()