#!/usr/bin/python3

"""Test BaseModel"""

from datetime import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self) -> None:
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_init(self):
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_save(self):
        self.bm1.save()
        self.assertAlmostEqual(self.bm1.updated_at, datetime.now())