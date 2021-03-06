Userside module for python
==========================

Install
-------

You can install userside module via pip, from testPyPi for now

     python3 -m pip install --index-url https://test.pypi.org/simple/ pyuserside
     


Examples
--------

Sync API
~~~~~~~~~

.. code:: python

    from pyuserside.api.synchronous import UsersideAPI

    # Create UsersideAPI instance
    uapi = UsersideAPI(url='https://localhost/api.php', key='my_secret_key')

    # Find some device and get information about it
    device_id = uapi.device.get_device_id(object_type='switch', data_typer='ip', data_value='10.90.90.90')
    device = uapi.device.get_data(object_type='switch', object_id=device_id)[0]
    # We can access device name (raw text), ...
    print(device.name)
    # ..., date when device was added (converted to datetime), ...
    print(device.dateadd.isoformat())
    # .., or device IP-address (converted to ipaddress.ip_address)
    print(device.ip.exploded)

Or use 'with' statement:

.. code:: python

    from pyuserside.api.synchronous import UsersideAPI

    with UsersideAPI(url='https://localhost/api.php', key='my_secret_key') as uapi:
        device_id = uapi.device.get_device_id(object_type='switch', data_typer='ip', data_value='10.90.90.90')
        device = uapi.device.get_data(object_type='switch', object_id=device_id)[0]

Async API
~~~~~~~~~

Same categories, same methods, same respose models, except for asynchronous!

.. code:: python

    from pyuserside.api.asynchronous import UsersideAPI
    import asyncio

    # Create UsersideAPI instance
    uapi = UsersideAPI(url='https://localhost/api.php', key='my_secret_key')

    # Find some task and get information about it
    tasks = asyncio.run(uapi.task.get_list(type_id=157, state_id=1))
    interested_task_id = tasks[0]
    task = asyncio.run(uapi.task.show(id=interested_task_id))
    # We can access task description (raw text), ...
    print(task.description)
    # ..., date of creation/complete/etc (converted to datetime object), ...
    print(task.date.create.isoformat())
    print(task.date.complete.isoformat())
    # .., or device address (converted to Address object)
    print(task.address.text)
    print(task.address.addressId)

Or use 'async with' statement:

.. code:: python

    from pyuserside.api.asynchronous import UsersideAPI
    import asyncio

    async def main():
        async with UsersideAPI(url='https://localhost/api.php', key='my_secret_key') as uapi:
                tasks = await uapi.task.get_list(type_id=157, state_id=1)
                interested_task_id = tasks[0]
                task = await uapi.task.show(id=interested_task_id)
    
    asyncio.run(main())