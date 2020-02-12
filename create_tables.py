
import yaml

from src.common.Database import Database
from src.devices.Device import Device

with open('conf.yaml') as file:
    config = yaml.load(file)
db_config = config['PRODUCTION']['DATABASE']
db = Database(config=db_config)
db.create_all_tables()
