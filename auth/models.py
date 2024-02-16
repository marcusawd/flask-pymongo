from pymongo.collection import Collection


class User:
    def __init__(self, db: Collection):
        self.db = db

    def create_user(self, user_data: dict):
        result = self.db.insert_one(user_data)
        return result.acknowledged

    def get_user(self, user_email: str):
        user = self.db.find_one({'email': user_email})
        return user
