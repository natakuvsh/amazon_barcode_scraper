import csv
import os
import re
from datetime import datetime
import pandas as pd


class FileManager:
    def __init__(self, user_filepath):
        self.barcodes = None
        self.new_file = None
        self.user_filepath = user_filepath
        self.user_filename = os.path.basename(user_filepath)

    @property
    def generate_filename(self):
        """
        Generating the filename in format "search_term_dmY.csv"
        """
        timestamp = datetime.now().strftime("%d%m%Y")
        self.new_file = f'{self.user_filename.split(".xlsx")[0]}_amazon' + '_' + timestamp + '.csv'
        return self.new_file

    def save_data_to_csv(self, record, is_new_file=False, header=None):
        """
        Write header to the csv file, if the file is new.
        Write record to the csv file, if not new.
        """
        if is_new_file:
            with open(f'result_files/{self.new_file}', 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(header)
        else:
            with open(f'result_files/{self.new_file}', 'a+', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(record)

    def get_barcode_from_users_file(self):
        """
        Choose the column with barcode values using regex matcher.
        return: list[889698429313.0, 889698466264.0, 830395022666.0, 889698514842.0,...]
        """
        self.data_from_user = pd.read_excel(fr'{self.user_filepath}', engine='openpyxl')

        data_top = self.data_from_user.head()
        pattern = re.compile("[0-9]{7,}")

        for column in data_top:
            col = self.data_from_user[column].tolist()
            count = 0
            for x in col:
                if pattern.match(str(x)):
                    count += 1
                    if count > 10:
                        self.barcodes = col
                        self.column_name = column
                        break
                else:
                    break
        return self.barcodes

