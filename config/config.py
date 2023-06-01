import os

from config.get_logger import Logger
from config.get_properties import EnvironmentRead

log = Logger.get_log()
env = os.environ.get('ENV')
env_reader = EnvironmentRead(env)
ENV, _config = env_reader.get_all()


class ConfigValues:
    def __init__(self):
        self.mongodb_endpoint = _config[ENV]['mongodb_endpoint']
        self.mongodb_port = _config[ENV]['mongodb_port']
        self.mongodb_database = '{}{}{}'.format(str(ENV).lower(), '_', _config[ENV]['mongodb_database'])
        self.mongodb_collection_product_info = '{}{}{}'.format(str(ENV).lower(), '_',
                                                               _config[ENV]['mongodb_collection_product_info'])

    def get_mongodb_endpoint(self):
        return self.mongodb_endpoint

    def get_mongodb_port(self):
        return int(self.mongodb_port)

    def get_database(self):
        return self.mongodb_database

    def get_collection_product_info(self):
        return self.mongodb_collection_product_info
