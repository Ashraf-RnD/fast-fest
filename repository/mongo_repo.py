from pymongo import MongoClient


from config.config import ConfigValues
from config.get_logger import Logger

log = Logger.get_log()
config_values = ConfigValues()


def get_item_data(documents):
    output = [{item: data[item] for item in data if item != '_id'} for data in documents]
    return output


class MongoRepo:
    def __init__(self, database, collection):
        log.info('{},{},{}'.format(config_values.get_mongodb_endpoint(), database, collection))
        self.client = MongoClient(config_values.get_mongodb_endpoint())

        # database = config_values.get_mongodb_database()
        # collection = config_values.get_mongodb_collection_product_info()
        cursor = self.client[database]
        self.collection = cursor[collection]

    def save_data(self, data):
        response = self.collection.insert_one(data)
        return {'status': 'Successfully Inserted', 'document_id': str(response.inserted_id)}

    def read_all(self):
        log.info('Read all data')
        return get_item_data(self.collection.find())

    def read_by_query(self, query):
        log.info('{}{}'.format('Read data by name:: ', query))
        return get_item_data(self.collection.find(query))
