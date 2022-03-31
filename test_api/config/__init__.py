import yaml
import os

config_base_path = os.path.dirname(__file__)
config_data_path = os.path.join(config_base_path, 'configdata.yaml')
# print(config_data_path)
with open(config_data_path) as file:
    configdata = yaml.safe_load(file)
    # print(config_data)
