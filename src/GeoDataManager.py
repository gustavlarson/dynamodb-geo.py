
"""
Purpose: A wrapper on the top of DynamoDBManager for performing CRUD operation on our DynamoBD table
"""
import GeoDataManagerConfiguration
from DynamoDBManager import DynamoDBManager
from model import PutPointInput
from model import GetPointInput


class GeoDataManager:

    def __init__(self, config):
        self.config = config
        self.dynamoDBManager = DynamoDBManager(config)

    def put_Point(self, putPointInput):
        return self.dynamoDBManager.put_Point(putPointInput)

    def get_Point(self, getPointInput):
        return self.dynamoDBManager.get_Point(getPointInput)

    def batch_write_points(self):
        pass

    def update_point(self):
        pass

    def delete_point(self):
        pass
