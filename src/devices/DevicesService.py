from src.common.exceptions import ModelAlreadyExistException
from src.devices.Device import Device
from src.devices.DevicesParemeters import (
    DeviceRegisterParameters,
    DeviceSearchParameters,
)


class DevicesService:
    @classmethod
    def register(cls, device_data: DeviceRegisterParameters):
        try:
            new_device = Device(
                workspace=device_data.workspace, pub_key=device_data.pub_key
            )
            new_device.save()
        except ModelAlreadyExistException:
            cls.activate(device_data)
        return True

    @classmethod
    def deactivate(cls, device_data: DeviceRegisterParameters):
        device = Device.get(
            pub_key=device_data.pub_key, workspace=device_data.workspace
        )
        device.deactivate()
        return True

    @classmethod
    def activate(cls, device_data: DeviceRegisterParameters):
        device = Device.get(
            pub_key=device_data.pub_key, workspace=device_data.workspace
        )
        device.activate()
        return True

    @classmethod
    def get_workspaces(cls, device_data: DeviceSearchParameters):
        return [
            device.workspace
            for device in Device.find(pub_key=device_data.pub_key, active=True)
        ]
