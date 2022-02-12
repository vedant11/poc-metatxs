from web3 import Web3

ganache_url = "http://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xB1955bEE47A97aDe63F678a51E266aC0ecc5A85A"
account_2 = "0x5314C072e47C6d1455E94405Af098b5EdeA7203c"

account_1_pvt_key = "0x1347ffcab4a67b291ee815e1c716adc9a23c810638d548f5d9d87b13f218d662"

nonce = web3.eth.getTransactionCount(account_1)

signed_tx = web3.eth.account.signTransaction({
    "nonce":nonce,
    "to":account_2,
    "value":web3.toWei(1, 'ether'),
    "gas": 200000,
    "gasPrice":web3.toWei('50', 'gwei')
}, account_1_pvt_key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(tx_hash)
