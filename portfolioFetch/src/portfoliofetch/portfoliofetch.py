import os
import glob
import pickle
import time
from db import database

import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OnvistaInstance:
    def __init__(self,name,pw):
        self.name = name
        self.pw = pw
        self.link = r'https://webtrading.onvista-bank.de/login'
        self.driver = None
        self.session = database()

        self.cashamount = 0
        self.netAmount = 0
        self.portfolio = None


        self.__driver()
        self.__connect()

    def __driver(self):
        self.driver = webdriver.Firefox()

    def __connect(self):
        try:
            self.driver.get(self.link)
            cookies = pickle.load(open('cookies.pkl', 'rb'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            print('Cookies not yet saved.\nStart Webdriver without cookies.')
            self.driver.get(self.link)

        self.startLogin()
        self.startDownload()

        pickle.dump(self.driver.get_cookies(),open('cookies.pkl','wb'))
        self.driver.quit()

    def __getLastFile(self):
        home = os.path.expanduser("~")
        downloadspath = os.path.join(home, "Downloads")
        list_of_files = glob.glob(downloadspath + "\*.csv")  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

    def startDownload(self):
        # get financial overview position
        kbVisible = (WebDriverWait(self.driver,10)
                     .until(EC.element_to_be_clickable((By.XPATH,
                                                        '//*[@id="brs-ui-grid-block-financial-overview"]'))))
        if kbVisible:
            time.sleep(2)
            currentCash = self.driver.find_element(By.XPATH,
                                                   '/html/body/div/main/div/brs-ui-grid-gridster/div[2]/div[2]/ul/li[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/table[2]/tbody/tr[4]/td')
            self.cashamount= float(currentCash.text.replace('€', '').replace('.', '').replace(',','.'))

            currentNet = self.driver.find_element(By.XPATH,
                                                   '/html/body/div/main/div/brs-ui-grid-gridster/div[2]/div[2]/ul/li[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/table[2]/tfoot/tr/td[2]')
            self.netAmount= float(currentNet.text.replace('€', '').replace('.', '').replace(',','.'))

            burgerMenu = self.driver.find_element(By.XPATH,
                                                  '/html/body/div/main/div/brs-ui-grid-gridster/div[2]/div[2]/ul/li[3]/div/div/div/div/div/div/div[1]/div[2]/button')
            burgerMenu.click()

            csvLink = self.driver.find_element(By.XPATH,
                                               '/html/body/div/main/div/brs-ui-grid-gridster/div[2]/div[2]/ul/li[3]/div/div/div/div/div/div/div[1]/div[2]/ul/li[4]/a')
            csvLink.click()

            file = self.__getLastFile()

            df = pd.read_csv(file,sep =';', header=4)
            df_nona = df.dropna('Name')




    def startLogin(self):
        kbVisible = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div/div/div/div[1]/form/div[3]/div[3]/ul/div/div[1]/li[2]/a")))

        if kbVisible:
            toggleKeyb = self.driver.find_element(By.XPATH, '/html/body/div/main/div/div/div/div/div[1]/form/div[3]/div[3]/ul/div/div[1]/li[2]/a')
            toggleKeyb.click()

            # Locate the login window
            pwVisible =WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
            if pwVisible:
                nameField= self.driver.find_element(By.XPATH,'//*[@id="login"]')
                nameField.clear()
                nameField.send_keys(name)

                pwField = self.driver.find_element(By.XPATH,'//*[@id="password"]')
                pwField.clear()
                pwField.send_keys(pw)

                loginButton = self.driver.find_element(By.XPATH, '//*[@id="performLoginButton"]')
                loginButton.click()

    def getCred(self):
        print(name,pw)

if __name__ == "__main__":
    name = pw = None
    rootPath = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(fr'{rootPath}/.env') as file:
            content = file.readlines()

        for line in content:
            if 'LOGIN' in line:
                name = line.split('=')[1].replace('\n','')
            elif 'PW' in line:
                pw = line.split('=')[1]
    except:
        name = input('Add your login name: ')
        pw = input('Add your login pw: ')

    if pw != None and name!=None:
        webPortal = OnvistaInstance(name, pw)
        webPortal.getCred()