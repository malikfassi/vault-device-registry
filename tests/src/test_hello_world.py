from src.devices.device import Device
from src.devices.devices_parameters import DeviceRegisterParameters, DeviceSearchParameters


def test_register_device(app, services):
    pub_key = 'abc'
    workspace = 'toto'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='ACTIVE')
    services.devices_service.register(device_data)
    registered_data = Device.find(pub_key=pub_key)
    assert registered_data.count() == 1
    assert registered_data[0].workspace == workspace
    assert registered_data[0].pub_key == pub_key

def test_register_same_device_in_two_workspaces(app, services):
    pub_key = 'abc'
    workspace = 'toto'
    workspace2 = 'toto2'
    device_data1 = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='ACTIVE')
    device_data2 = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace2, status='ACTIVE')
    services.devices_service.register(device_data1)
    services.devices_service.register(device_data2)
    registered_data = Device.find(pub_key=pub_key)

    assert registered_data.count() == 2
    assert registered_data[0].pub_key == pub_key
    assert registered_data[0].workspace == workspace
    assert registered_data[0].active == True
    assert registered_data[1].workspace == workspace2
    assert registered_data[1].pub_key == pub_key
    assert registered_data[1].active == True

def test_get_workpace_by_pub_key(app, services):
    workspace = 'toto'
    pub_key = 'abcdef'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='ACTIVE')
    services.devices_service.register(device_data)
    device_search_data = DeviceSearchParameters(pub_key=pub_key)
    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 1
    assert fetched_data[0] == workspace

def test_get_workspaces_by_pub_key_multiple(app, services):
    workspace = 'toto'
    workspace2 = 'toto2'
    pub_key = 'abcde'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='ACTIVE')
    services.devices_service.register(device_data)
    device_data2 = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace2, status='ACTIVE')
    services.devices_service.register(device_data2)
    device_search_data = DeviceSearchParameters(pub_key=pub_key)
    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 2
    assert fetched_data[0] == workspace
    assert fetched_data[1] == workspace2

def test_get_workpaces_by_pub_key_not_found(app, services):
    device_search_data = DeviceSearchParameters(pub_key='unknown')
    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 0

def test_deactivate_device(app, services):
    pub_key = 'abcd'
    workspace = 'toto'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='ACTIVE')
    services.devices_service.register(device_data)
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='SUSPENDED')
    services.devices_service.register(device_data)
    device_search_data = DeviceSearchParameters(pub_key=pub_key)

    # do not fetch deactivated data
    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 0

    registered_data = Device.find(pub_key=pub_key)
    assert registered_data[0].pub_key == pub_key
    assert registered_data[0].workspace == workspace
    assert registered_data[0].active == False

def register_deactivated_device(app, services):
    pub_key = 'abcd'
    workspace = 'toto'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace, status='SUSPENDED')
    services.devices_service.register(device_data)

    registered_data = Device.find(pub_key=pub_key)
    assert registered_data[0].pub_key == pub_key
    assert registered_data[0].workspace == workspace
    assert registered_data[0].active == False

    device_search_data = DeviceSearchParameters(pub_key=pub_key)

    # do not fetch deactivated data
    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 0

    services.devices_service.register(device_data)

    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 1

    registered_data = Device.find(pub_key=pub_key)
    assert registered_data[0].pub_key == pub_key
    assert registered_data[0].workspace == workspace
    assert registered_data[0].active == True

