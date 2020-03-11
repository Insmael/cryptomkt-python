from __future__ import print_function
import cryptomarket.exchange.client as c
import cryptomarket.exchange.socket as s
import time

def received(data):
    print('data received')

keyspath= "../Desktop/folder/untitled"
with open(keyspath) as keysfile:
   keys = keysfile.read().split('\n')

   client = c.Client(keys[0], keys[1])

#    print(str(client.notify_deposit(amount="4", bank_account="63305")))

# s.socketio.Client.connect()

  
    