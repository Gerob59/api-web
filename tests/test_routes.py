import unittest
from fastapi.testclient import TestClient

import sys
import os

# Ajoutez le chemin du dossier parent au chemin de recherche de modules
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Maintenant, vous devriez pouvoir importer le module main depuis src
from src.main import app
from src.router import client_router

class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        
    def test_get_all_clients(self):
        response = self.client.get("/client/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        
        
if __name__ == "__main__":
    unittest.main()
