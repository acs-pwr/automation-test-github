import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import hashlib
import pytest

@pytest.fixture
def setup(): 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://github.com/login?return_to=%2Fjoin%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home")
    driver.maximize_window()
    driver.implicitly_wait(6)
    time.sleep(3)
    yield driver
    driver.close()
    
@pytest.mark.xray('JIRA-2')
def test_case_b(setup):
    #username
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys("Wdhus")
    time.sleep(3)
    #password
    setup.find_element_by_xpath("//html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys("wkwkwk")
    #click login
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()
    time.sleep(3)
    time.sleep(3)
    response = setup.find_element_by_xpath("/html/body/div[3]/main/div/div[2]/div/div").text
    time.sleep(3)
    assert 'Incorrect username or password.' in response
    time.sleep(3)
    print ("\n Invalid Password ! \n")
    
@pytest.mark.xray('JIRA-3')    
def test_case_c(setup):
    #username
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys("hihih")
    time.sleep(3)
    #password
    setup.find_element_by_xpath("//html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys("Purworejo1234")
    time.sleep(2)
    #click login
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()
    time.sleep(3)
    response_c = setup.find_element_by_xpath("/html/body/div[3]/main/div/div[2]/div/div").text
    time.sleep(3)
    assert 'Incorrect username or password.' in response_c
    print ("\n Invalid Username ! \n")
    
@pytest.mark.xray('JIRA-4')    
def test_case_d(setup): 
    #username
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys("")
    time.sleep(3)
    #password
    setup.find_element_by_xpath("//html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys("Purworejo1234")
    time.sleep(2)
    #click login
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()
    time.sleep(3)
    response_d = setup.find_element_by_xpath("/html/body/div[3]/main/div/div[2]/div/div").text
    time.sleep(3)
    assert 'Incorrect username or password.' in response_d    
    time.sleep(3)
    print ("\n Invalid Username and Password ! \n")

@pytest.mark.xray('JIRA-5')
def test_case_e(setup): 
    #username
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys("Wdhus")
    time.sleep(2)
    #password
    passwrd = "Purworejo1234"
    password_md5 = hashlib.md5(passwrd.encode()).hexdigest()
    setup.find_element_by_xpath("//html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys(password_md5)
    time.sleep(2)
    #click login
    setup.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()
    time.sleep(3)
    response_e = setup.find_element_by_xpath("/html/body/div[3]/main/div/div[2]/div/div").text
    time.sleep(3) 
    assert 'Incorrect username or password.' in response_e
    print ("\n Login failed, using password hash md5 ! \n")