# Pyuserside
Python API client library for [Userside](https://www.python.org/)

### Installation
Install with the following command:
```shell
pip install pyuserside
```

### Quickstart

```python
from pyuserside import UsersideAPI
api = UsersideAPI(url='https://my.userside.domain/api.php', key='my_secret_key')
customer_login = 'abonent001'
customer_id = api.customer.get_abon_id(data_typer='login', data_value=customer_login)
customer_data = api.customer.get_data(customer_id=customer_id)
```

### API Reference
Userside API has its own [wiki](https://wiki.userside.eu/API)