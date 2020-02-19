from ledgercommon.flask.config import Config as BaseConfig


class Config(BaseConfig):
    env_var_prefix = 'VAULT_DEVICE_REGISTRY'
