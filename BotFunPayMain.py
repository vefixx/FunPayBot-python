from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle

url = r'https://funpay.com/account/login'
options = webdriver.ChromeOptions()
options.add_argument('headless=True')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')

driver = webdriver.Chrome(options=options)

print('Start')
driver.get(url)
#time.sleep(15)
#pickle.dump(driver.get_cookies(), open('FunPay_cookies', 'wb'))
#time.sleep(3)
time.sleep(1)
#load cookies for auto login
for cookie in pickle.load(open('FunPay_cookies', 'rb')):
    driver.add_cookie(cookie)
time.sleep(1)

#refresh browser
driver.refresh()
time.sleep(1)

driver.get('https://funpay.com/lots/222/trade')
time.sleep(1)

while True:
    f = open('data.txt', 'r').read()
    amount = f
    price = 6.9
    print(f'Get data from data.txt = {amount}')
    #found poduct on screen
    tovar = driver.find_element('xpath', '//*[@id="content"]/div/div/div[2]/div/div[2]/a').click()
    time.sleep(1)


    #Change product text on lot
    text = driver.find_element('name', 'fields[summary][ru]')
    text.clear()
    string = f"\u2604\uFE0F\u2604\uFE0FHypixel skyblock 1M - {str(price)}руб. В наличии {str(amount)}M! Безопасно и Быстро!\u2604\uFE0F\u2604\uFE0F"
    encoded = string.encode('utf-16')
    text.send_keys(encoded.decode('utf-16'))

    #change product amount in lot
    amount_values = driver.find_element('name', 'amount')
    amount_values.clear()
    amount_values.send_keys(str(amount))
    amount_values.send_keys(Keys.ENTER)

    time.sleep(10)

driver.close()
driver.quit()