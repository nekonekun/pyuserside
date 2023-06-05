# Pyuserside

[![MIT License](https://img.shields.io/github/license/nekonekun/pyuserside)](https://opensource.org/licenses/MIT)
[![Supported python versions](https://img.shields.io/pypi/pyversions/pyuserside)](https://pypi.org/project/pyuserside/)
[![PyPi Package Version](https://img.shields.io/pypi/v/pyuserside)](https://pypi.org/project/pyuserside/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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