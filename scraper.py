from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import csv

def scrape_stock(driver, ticker_symbol):
   
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}'

    driver.get(url)

    stock = { 'ticker': ticker_symbol }

    current_market_price = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-testid="qsp-price"]').text

    stock['current_market_price'] = current_market_price
    
    print(stock)
    return stock

symbols = []

with open('symbols.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        symbols.extend(row)

print(symbols)

options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

driver.set_window_size(1150, 1000)

stocks = []

for ticker_symbol in symbols:
    stocks.append(scrape_stock(driver, ticker_symbol + '.JK'))

print(sys.argv[1:])

driver.quit()