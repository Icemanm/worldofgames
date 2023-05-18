from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys

# it’s purpose is to test our web service. It will get the application
# URL as an input, open a browser to that URL, select the score element in our web page,
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
def test_scores_service(url):
    service = Service('C:\\Users\\moshi\\Downloads\\chromeDriver\\chromedriver.exe')
    my_driver = webdriver.Chrome(service=service)
    my_driver.get(url)
    score = my_driver.find_element(By.ID, 'score')
    s = int(score.text)
    my_driver.quit()
    if 1 <= s <= 1000:
        return True
    else:
        return False


# call our tests function. The main function will return -1 as an OS exit
# code if the tests failed and 0 if they passed.


def main_function(url='http://127.0.0.1:8777/'):
    result = test_scores_service(url)
    if result == True:
        sys.exit(0)
    elif result == False:
        sys.exit(1)
    else:
        print("unknown result")

        
main_function()

