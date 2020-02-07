from ledgercommon.schema import dataclass, BaseModel


@dataclass
class DeviceRegisterParameters(BaseModel):
    pub_key: str
    workspace: str

@dataclass
class DeviceSearchParameters(BaseModel):
    pub_key: str
