# Amazon barcode scraper

An app which uses Selenium library to scrape data from amazon according to the given barcodes.
* Asks for users file, from which it can pull barcodes.
* Creates new file for amazon data in result_files folder.
* Merge users file and amazon file into a new file on same barcodes.

## • How To Install and Use

Install required libraries:
```
pip install requirements.txt
```
To run the script:
```
python3 amazon_search_barcode.py
```

To-Do's:
- [ ] Add option of choosing desired columns for a new file
- [ ] Add ann option of choosing another card of the product, if current is marked as 'sponsored' or 'protected'
