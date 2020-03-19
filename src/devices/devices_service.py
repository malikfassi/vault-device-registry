from typing import List

from src.devices.device import Device
from src.devices.devices_parameters import (
    DeviceRegisterParameters,
    DeviceSearchParameters,
)


class DevicesService:
    @classmethod
    def register(cls, device_data: DeviceRegisterParameters):
        new_device = Device(workspace=device_data.workspace, pub_key=device_data.pub_key, active=(device_data.status == "ACTIVE"))
        new_device.save()

    @classmethod
    def update(cls, device_data: DeviceRegisterParameters):
        device = Device.get(
            pub_key=device_data.pub_key, workspace=device_data.workspace
        )
        device.update_active(device_data.status == "ACTIVE")

    @classmethod
    def get_workspaces(cls, device_data: DeviceSearchParameters) -> List[str]:
        return [
            device.workspace
            for device in Device.find(pub_key=device_data.pub_key, active=True)
        ]
