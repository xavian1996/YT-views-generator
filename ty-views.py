from selenium import webdriver
from time import sleep


def getviews():
    driver = webdriver.Chrome("chromedriver.exe")
    url = input('YT Video URL => ')
    views = int(input("Number Of Views => "))
    start = 0

    while start <= views :
        driver.get(url)
        sleep(20)
    driver.close()
        

getviews()