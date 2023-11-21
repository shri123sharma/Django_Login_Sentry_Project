import unittest
import pandas as pd
from faker import Faker
from  mymodule import generate_fake_data_and_save_csv
import datatest as dt

class TestFakeDataAndSaveCsvFile(unittest.TestCase):
    
    def setUp(self) -> None:
        global df
        num_rows=1000
        output_file='dataframetestfile.csv'
        df=generate_fake_data_and_save_csv(num_rows,output_file)
    
    def test_generate_fake_data_and_save_csv(self):
        num_rows=1000
        self.assertEqual(len(df),num_rows)
        

    def test_generate_fake_data_check_colums_csv_file(self):
        expected_columns = ['Name', 'Email', 'Phone', 'Address','Job','Company','City','Country','Date of Birth','Credit Card Number','Color','Word','Sentence','Paragraph','ISBN','Currency Code','Latitude','Longitude','Boolean','Hex Color','URL','IPv4','Password']
        actual_columns = df.columns.tolist()
        self.assertEqual(expected_columns, actual_columns, "Column lists should be equal.")
        
    # def test_title(self):
    #     self.assertRegexpMatches(df['Name'], r'^[A-Z]')
    
    
    # def test_generate_fake_data_check_Boolean_value(self):
    #     self.assertEqual(
    #         df['Boolean'],
    #         {'True', 'False'},
    #     )
        
