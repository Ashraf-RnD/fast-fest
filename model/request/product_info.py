from pydantic import BaseModel


class ProductInfo(BaseModel):
    name: str
    type: str
    source: str
