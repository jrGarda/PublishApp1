import unittest
from connection import Data

class TestConnectionErrors(unittest.TestCase):

    def test_database_opens_successfully(self):
        db = Data("publish_db.db")
        self.assertTrue(db.create_connection())

    def test_database_name(self):
        db = Data("publish_db.db")
        self.assertEqual(db.db_name, "publish_db.db")

if __name__ == "__main__":
    unittest.main()
