import os

from src.common.config import Config
from src.common.database import Database
from src.devices.device import Device

SCRIPT_PATH = os.path.realpath(__file__)
ROOT_PATH = os.path.dirname(SCRIPT_PATH)

config = Config(ROOT_PATH, defaults={'ENV': 'PRODUCTION'}).from_yaml('conf.yaml')

db_config = config.get('DATABASE')

db = Database(config=db_config)
db.create_all_tables()
