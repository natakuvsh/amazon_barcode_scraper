from random import shuffle
from utils import my_webdriver, tk_interface
from utils.product_card_manager import *
from utils.barcode_compare import *


def run():
    """
    1. Get the filename from the user
    2. Create the new file and write header to it
    3. Start the driver and open amazon page
    4. Get barcodes from user file and enter every barcode in amazon searchbar
    5. Get card of each product, including name, price and url
    """

    # Getting the path to the file from user
    filepath_from_user = tk_interface.tk_interface()
    file = FileManager(filepath_from_user)
    print('Reading the file..')

    # Creating new file to store data from amazon.com
    amazon_file = file.generate_filename
    if os.path.exists(f'result_files/{amazon_file}'):
        os.remove(f'result_files/{amazon_file}')
    file.save_data_to_csv(record=None, is_new_file=True, header=['description', 'barcode', 'price', 'url'])
    print(f'Successfully created new file - {amazon_file}')

    # Getting barcodes column from the users file. Shuffle them
    barcodes_list = (file.get_barcode_from_users_file())
    shuffled_barcodes = shuffle(barcodes_list)

    # Starting the driver
    print('Starting the driver...')
    driver = my_webdriver.Driver()
    driver.get_url('https://www.amazon.com/')

    # Loading data for every barcode, saving it to the amazon file
    print('Found data for following products:\n')

    for i in range(len(barcodes_list)):
        try:
            search_key = str(int(barcodes_list[i]))
            url = f'https://www.amazon.com/s?k={search_key}'
            driver.get_url(url)
            cards = driver.find_all_cards()
            try:
                record = extract_card_data(cards[0], search_key)
                if record:
                    print(record)
                    file.save_data_to_csv(record)
            except IndexError:
                pass
        except ValueError:
            pass
        driver.sleep_for_random_interval()

    print('Closing the driver...')
    driver.exit_browser()
    print(f'The results were successfully saved to a file: result_files/{amazon_file}')

    # Reading the file from amazon
    data_from_amazon = pd.read_csv(f"result_files/{amazon_file}", encoding='utf-8-sig')

    # Merging two files into one on the barcode value
    new_df = pd.merge(file.data_from_user, data_from_amazon, left_on=f'{file.column_name}', right_on='barcode',
                      how='left')
    new_df.to_csv('result_files/my_compare.csv', encoding='utf-8-sig')
    print(f'Data from {file.user_filename} and {amazon_file} was saved to new file - result_files/my_compare.csv')









if __name__ == '__main__':
    run()