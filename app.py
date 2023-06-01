from fastapi import FastAPI

from config.config import ConfigValues
from config.get_logger import Logger
from model.request.product_info import ProductInfo
from repository.mongo_repo import MongoRepo
import re

app = FastAPI()

log = Logger.get_log()

config_values = ConfigValues()
mongo_client_product_info = MongoRepo(config_values.get_database(), config_values.get_collection_product_info())


@app.get("/mw/api/ping")
def read_root():
    return {"Night": "Move"}


@app.post("/mw/api/save-product")
def save_product(request: ProductInfo):
    data = dict(request)
    log.info('{}{}{}{}'.format('Enter:: ', 'save_product:: ', 'request: ', data))
    response = mongo_client_product_info.save_data(data)
    log.info('{}{}{}{}'.format('Exit:: ', 'save_product:: ', 'response: ', response))
    return response


@app.get("/mw/api/product-list")
def get_product_list():
    log.info('{}{}'.format('Enter:: ', 'get_product_list:: '))
    response = mongo_client_product_info.read_all()
    log.info('{}{}{}{}'.format('Exit:: ', 'get_product_list:: ', 'response: ', response))
    return response


@app.get("/mw/api/product-list-by-name")
def get_product_list_by_name(name: str):
    log.info('{}{}{}'.format('Enter:: ', 'get_product_list_by_name:: request: ', name))
    regex = re.compile(name, re.IGNORECASE)
    response = mongo_client_product_info.read_by_query(dict({"name": regex}))
    log.info('{}{}{}{}'.format('Exit:: ', 'get_product_list_by_name:: ', 'response: ', response))
    return response
