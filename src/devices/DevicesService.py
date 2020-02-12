from src.devices.Device import Device
from src.devices.DevicesParemeters import (
    DeviceRegisterParameters,
    DeviceSearchParameters,
)


class DevicesService:

    @classmethod
    def register(cls, device_data: DeviceRegisterParameters):
        # Create an instance of the Device class
        new_device = Device(workspace=device_data.workspace, pub_key=device_data.pub_key)
        new_device.save()
        return True

    @classmethod
    def get_workspaces(cls, device_data: DeviceSearchParameters):
        return [device.workspace for device in Device.get(pub_key=device_data.pub_key)]
