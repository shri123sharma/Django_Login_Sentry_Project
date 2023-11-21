from django.test import TestCase
import unittest
from my_script import add_fish_to_aquarium
# Create your tests here.

class TestAddFish(unittest.TestCase):
    def test_add_fish_to_aquarium_sucess(self):
          actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
          expected={'tank_a': ['shark', 'tuna',]}
          self.assertEqual(actual, expected)
          
    def test_add_fish_to_aquarium_exception(self):
        too_many_fish=['shark']*25
        with self.assertRaises(ValueError) as e:
          add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(str(e.exception),"A maximum of 10 fish can be added to the aquarium")
        
        