from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    # Req. 2
    def to_dict(self):
        return dict(self.data)

    # Req. 3
    @classmethod
    def list_dicts(cls):
        return list(cls._collection.find({}, {"_id": 0}))
