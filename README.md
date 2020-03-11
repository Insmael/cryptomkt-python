# TODO
especificar que las llaves deben ser validas para acceder a endpoints autenticados
# CryptoMarket
The official Python library for the [CryptoMarket API v1](https://developers.cryptomkt.com).

# Installation
To install Cryptomarket, simply use pip:
```
pip install cryptomarket
```
# Documentation

The first things you'll need to do is [sign up with CryptoMarket](https://www.cryptomkt.com/account/register).

## API Key + Secret
If you're writing code for your own CryptoMarket account, [enable an API key](https://www.cryptomkt.com/account2#api_tab).

Next, create a Client object for interacting with the API:

```
from cryptomarket.exchange.client import Client

client = Client(api_key, api_secret)
```

# Usage

## [Public endpoints](https://developers.cryptomkt.com/es/#endpoints-publicos)

### Get markets
```python
client.get_markets()
```
***Expected Output***
```python
{
  "data": [
    "ETHCLP",
    "ETHARS",
    "ETHEUR",
    "ETHBRL",
    "ETHMXN",
    "XLMCLP",
    "XLMARS",
    "XLMEUR",
    "XLMBRL",
    "XLMMXN",
    "BTCCLP",
    "BTCARS",
    "BTCEUR",
    "BTCBRL",
    "BTCMXN",
    "EOSCLP",
    "EOSARS",
    "EOSEUR",
    "EOSBRL",
    "EOSMXN"
  ]
}
```

### Get ticker
```python

client.get_ticker()

#can recieve market as an optional parameter, in that case will return only the ticker of the specified market.

client.get_ticker(market="XLMCLP")
```

***Expected Output***
```python
{
  "data": [
    {
      "ask": "43.5",
      "bid": "42.3",
      "high": "44.9",
      "last_price": "44.8",
      "low": "41.05",
      "market": "XLMCLP",
      "timestamp": "2020-03-09T19:03:34.762778",
      "volume": "151939.515080441682524"
    }
  ]
}
```


### Get book
```python
#can receive "page" as an optional argument.

client.get_book(market="ETHCLP", type="sell", page=1)
```

***Expected Output***
```python
{
  "data": [
    {
      "amount": "0.5045",
      "price": "167600",
      "timestamp": "2020-03-09T19:10:40.043"
    },
    {
      "amount": "0.4865",
      "price": "167600",
      "timestamp": "2020-03-09T19:12:20.360"
    },
    {
      "amount": "0.1387",
      "price": "167460",
      "timestamp": "2020-03-09T19:08:58.451"
    },
        #...
  ]
}
```

### Get trades
```python
client.get_trades(market="ETHCLP")
```

***Expected Output***
```python
{
  "data": [
    {
      "amount": "0.014669811320754716",
      "market": "ETHCLP",
      "market_taker": "buy",
      "price": "169600",
      "timestamp": "2020-03-09T19:25:09"
    },
    {
      "amount": "0.0876",
      "market": "ETHCLP",
      "market_taker": "buy",
      "price": "169600",
      "timestamp": "2020-03-09T19:10:38"
    },
    {
      "amount": "0.471698113207547169",
      "market": "ETHCLP",
      "market_taker": "buy",
      "price": "169600",
      "timestamp": "2020-03-09T19:09:21"
    }
    #...
  ]
}
```

### Get Prices
```python
#"timeframe" value in minutes can be = "1,5,15,60,240,1440,10080".
#can receive "page" and "limit" as optional arguments.

client.get_prices(market="ETHCLP",timeframe=10080)
```

***Expected Output***
```python
{
  "ask": [
    {
      "candle_date": "2020-02-15 12:15",
      "candle_id": 48027,
      "close_price": "227220",
      "hight_price": "227280",
      "low_price": "227220",
      "open_price": "227280",
      "tick_count": "11",
      "volume_sum": "227220"
    },
    {
      "candle_date": "2020-02-15 12:14",
      "candle_id": 48026,
      "close_price": "227300",
      "hight_price": "227340",
      "low_price": "227300",
      "open_price": "227340",
      "tick_count": "3",
      "volume_sum": "227300"
    },
   #...
  ],
  "bid": [
    {
      "candle_date": "2020-03-09 19:49",
      "candle_id": 332723,
      "close_price": "167220",
      "hight_price": "167280",
      "low_price": "167220",
      "open_price": "167280",
      "tick_count": "2",
      "volume_sum": "0"
    },
    {
      "candle_date": "2020-03-09 19:48",
      "candle_id": 332701,
      "close_price": "167400",
      "hight_price": "167500",
      "low_price": "167280",
      "open_price": "167500",
      "tick_count": "3",
      "volume_sum": "0"
    },
 #...
  ]
}
```

### Get account 
```python
client.get_account();
```

***Expected Output***
```python
{
  "bank_accounts": [
    {
      "agency": "",
      "bank": "BANCO DEL ESTADO DE CHILE",
      "clabe": "",
      "country": "CL",
      "description": "",
      "dv": "",
      "id": 00000,
      "number": "123456789"
    }
  ],
  "blocked_withdrawals": false,
  "deposit_debts": {
    "BTC": "0",
    "EOS": "0",
    "ETH": "0",
    "XLM": "0"
  },
  "email": "juan.rojas@gmail.com",
  "name": "Juan Rojas",
  "rate": {
    "market_maker": "0.0039",
    "market_taker": "0.0068"
  }
}
```

### Get Active Orders
```python
#can receive page and limit as optional parameters.

client.get_active_orders(market="ETHCLP",page=1,limit=2)
```

***Expected Output***
```python
{
  "data": [
    {
      "amount": {
        "original": "1",
        "remaining": "1"
      },
      "created_at": "2020-03-09T20:41:58.146000",
      "execution_price": null,
      "id": "O1734261",
      "market": "XLMCLP",
      "price": "100",
      "status": "active",
      "type": "sell",
      "updated_at": "2020-03-09T20:41:58.212557"
    },
    #...
  ]
}
```

### Get Executed Orders
```python
#can receive page and limit as optional parameters.

client.get_executed_orders(market="XLMCLP")
```

***Expected Output***
```python
{
  "data": [
    {
      "amount": {
        "executed": "1",
        "original": "1"
      },
      "created_at": "2020-03-09T21:55:26.096000",
      "executed_at": "2020-03-09T21:55:26",
      "execution_price": "43.45",
      "fee": "0.295",
      "id": "O0000001",
      "market": "XLMCLP",
      "price": "40",
      "status": "executed",
      "type": "sell"
    },
    {
      "amount": {
        "executed": "1",
        "original": "1"
      },
      "created_at": "2020-03-05T22:19:41.317000",
      "executed_at": "2020-03-06T03:20:48",
      "execution_price": "49.9",
      "fee": "0.194",
      "id": "O0000002",
      "market": "XLMCLP",
      "price": "49.9",
      "status": "executed",
      "type": "sell"
    },
    #...
  ]
}
```

### Create Order
```python
#"price" is an optional argument, is required only if "type" is "limit" or "stop-limit".

#"limit" is an optional argument, is required only if "type" is "stop-limit".

#"type" can be "limit", "stop-limit" or "market".


client.create_order(market="XLMCLP", type="limit", amount="1", price=50, side="sell")
```

***Expected Output***
```python
{
  "amount": {
    "executed": "0",
    "original": "1"
  },
  "avg_execution_price": "0",
  "created_at": "2020-03-09T23:07:35.185000",
  "fee": "0",
  "id": "O0000001",
  "market": "XLMCLP",
  "price": "50",
  "side": "sell",
  "status": "queued",
  "stop": null,
  "type": "limit",
  "updated_at": "2020-03-09T23:07:35.234007"
}
```

### Get Status of an Order
```python
client.get_status_order(id="O1744570")
```

***Expected Output***
```python

```

### Cancel an order
```python
client.cancel_order()
```

***Expected Output***
```python

```

### Get Balance
```python
client.get_balance()
```
***Expected Output***
```python
{
  "data": [
    {
      "available": "0",
      "balance": "0",
      "currency_big_name": "Peso Chileno",
      "currency_decimal": 0,
      "currency_postfix": "",
      "currency_prefix": "$",
      "wallet": "CLP"
    },
    {
      "available": "0",
      "balance": "0",
      "currency_big_name": "Peso Argentino",
      "currency_decimal": 2,
      "currency_postfix": "",
      "currency_prefix": "$",
      "wallet": "ARS"
    },
    {
      "available": "0.0052612795",
      "balance": "0.0052612795",
      "currency_big_name": "Real Brasile\u00f1o",
      "currency_decimal": 2,
      "currency_postfix": "",
      "currency_prefix": "R$",
      "wallet": "BRL"
    },
   #...
  ]
}
```

### Get Transactions
```python
#can recieve "page" and "limit" as optional arguments

client.get_transactions(currency="CLP")
```

***Expected Output***
```python
{
  "data": [
    {
      "address": null,
      "amount": "43.45",
      "balance": "735.98669",
      "blocks": null,
      "currency": "CLP",
      "date": "2020-03-09T21:55:26",
      "fee_amount": "0.295",
      "fee_percent": "0+0.680%",
      "hash": null,
      "id": "T000001",
      "memo": null,
      "type": 1
    },
    {
      "address": null,
      "amount": "49.9",
      "balance": "692.83215",
      "blocks": null,
      "currency": "CLP",
      "date": "2020-03-06T03:20:48",
      "fee_amount": "0.194",
      "fee_percent": "0+0.390%",
      "hash": null,
      "id": "T000002",
      "memo": null,
      "type": 1
    },
 #...
  ]
}
```

### Notify Deposit
```python
#"bank_account" receives the bank account id as a string, you can obtain de id using "get_account()"

client.notify_deposit(bank_account="12345", amount="10000")
```

***Expected Output***
```python
{
  "data": "",
  "pagination": null
}
```

### Notify Withdrawal
```python
#"bank_account" receives the bank account id as a string, you can obtain this id using "client.get_account()".

client.notify_withdrawal(bank_account="12345", amount="10000")
```

***Expected Output***
```python
{
  "data": "",
  "pagination": null
}
```
### Transfer
```python
#can receive "memo" as an optional argument.
client.transfer(address="",amount=0.02,currency="ETH")
```

***Expected Output***
```python
{ status: 'success', data: '' }
```

