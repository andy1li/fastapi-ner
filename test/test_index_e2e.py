from selenium import webdriver
import pytest

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(executable_path=r'/Applications/chromedriver')
    driver.get('http://localhost:8000')
    setattr(driver, 'find', lambda val: 
        driver.find_element_by_css_selector(f'[data-test-id="{val}"]')
    )
    yield driver
    driver.quit()

def test_browser_title_contains_app_name(driver):
    assert 'Named Entity' in driver.title

def test_page_heading_is_named_entity_finder(driver):
    heading = driver.find('heading').text
    assert 'Named Entity Finder' == heading

def test_page_has_input_for_text(driver):
    input_element = driver.find('input-text')
    assert input_element is not None

def test_page_has_button_for_submitting_text(driver):
    submit_button = driver.find('find-button')
    assert submit_button is not None

def test_page_has_ner_table(driver):
    input_element = driver.find('input-text')
    submit_button = driver.find('find-button')
    input_element.send_keys('地球是太阳系中由内及外的第三颗行星')
    submit_button.click()
    table = driver.find('ner-table')
    assert table is not None