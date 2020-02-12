import pytest

from src.common.exceptions import ModelAlreadyExistException
from src.devices.Device import Device
from src.devices.DevicesParemeters import DeviceRegisterParameters, DeviceSearchParameters


def test_register_device(app, services):
    pub_key = 'abc'
    workspace = 'toto'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace)
    services.devices_service.register(device_data)
    registered_data = Device.get(pub_key=workspace)
    assert registered_data.count() == 1
    assert registered_data[0] == workspace


def test_register_same_device_in_two_workspaces(app, services):
    pub_key = 'abc'
    workspace = 'toto'
    workspace2 = 'toto2'
    device_data1 = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace)
    device_data2 = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace2)
    services.devices_service.register(device_data1)
    services.devices_service.register(device_data2)
    registered_data = Device.get(pub_key=workspace)
    assert registered_data.count() == 2
    assert registered_data[0] == workspace
    assert registered_data[1] == workspace2

def test_register_already_knwon_device(app, services):
    pub_key = 'abc'
    workspace = 'toto'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace)
    services.devices_service.register(device_data)
    with pytest.raises(ModelAlreadyExistException):
        services.devices_service.register(device_data)

def test_get_workpace_by_pub_key(app, services):
    workspace = 'toto'
    pub_key = 'abc'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace)
    services.devices_service.register(device_data)
    device_search_data = DeviceSearchParameters(pub_key=pub_key)
    fetched_data = services.devices_service.get_workspaces(device_search_data)
    assert len(fetched_data) == 1
    assert fetched_data[0] == workspace

def test_get_workspaces_by_pub_key_multiple(app, services):
    workspace = 'toto'
    workspace2 = 'toto2'
    pub_key = 'abc'
    device_data = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace)
    services.devices_service.register(device_data)
    device_data2 = DeviceRegisterParameters(pub_key=pub_key, workspace=workspace2)
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
