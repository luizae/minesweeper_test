import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.maximize_window()

driver.get('https://mines.makecodes.dev/')

time.sleep(1)

set_rows = driver.find_element_by_id('rows')
set_rows.click()
set_rows.clear()
set_rows.send_keys(20)

set_cols = driver.find_element_by_id('cols')
set_cols.click()
set_cols.clear()
set_cols.send_keys(20)

set_mines = driver.find_element_by_id('mines')
set_mines.click()
set_mines.clear()
set_mines.send_keys(5)

apply_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/div[4]/button')
apply_button.click()

time.sleep(2)

def random_my_click():
    random_my_row = random.randint(1, 20)
    random_my_cell_row = random.randint(1, 20)
    cell = driver.find_element_by_css_selector(f'.board-row:nth-child({random_my_row}) .board-row-cell:nth-child({random_my_cell_row})')
    if 'revealed' in cell.get_attribute("class"):
        return random_my_click()
    cell.click()
    time.sleep(1)
    
end_game = False

while end_game == False:

    button_reset = driver.find_element_by_css_selector('.reset')
    emoji = button_reset.get_attribute('innerHTML')

    try:
        mined = driver.find_element_by_css_selector('.mined')
        end_game = True
        assert emoji == "👻"
        print(emoji)
        time.sleep(1)
    except:
        mined = None

    try:
        flagged = driver.find_element_by_css_selector('.flagged')
        end_game = True
        assert emoji == "😎"
        print(emoji)
        time.sleep(1)
    except:
        flagged= None

    if end_game is False:
        assert emoji == "🙂"
        print(emoji)
        random_my_click()

driver.quit()