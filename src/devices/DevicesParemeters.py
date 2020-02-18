from ledgercommon.schema import BaseModel, dataclass


@dataclass
class DeviceRegisterParameters(BaseModel):
    pub_key: str
    workspace: str
    status: str


@dataclass
class DeviceSearchParameters(BaseModel):
    pub_key: str
