from src.devices.Device import Device
from src.devices.DevicesParemeters import DeviceRegisterParameters


class DevicesService:

    @classmethod
    def register(cls, request_args: DeviceRegisterParameters):
        # Create an instance of the Device class
        new_device = Device(workspace=request_args.workspace, pub_key=request_args.pub_key)
        new_device.save()
        return True

    @classmethod
    def get_workspaces(cls, pub_key: str):
        return [device.workspace for device in Device.get(pub_key=pub_key)]
