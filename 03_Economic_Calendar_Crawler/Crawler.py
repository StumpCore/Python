import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
import datetime
import csv

def write_to_csv(economic_calendar_dict):
  save_path = "Your Path"
    with open(save_path + "\\" + "Economic_Calendar.csv", 'w') as f:  
        w = csv.DictWriter(f, economic_calendar_dict.keys())
        w.writeheader()
        w.writerow(economic_calendar_dict)


driver = webdriver.Firefox()
driver.get("https://tradingeconomics.com/calendar")
economic_calendar = {"Date":[], "Time":[], "Country":[], "Announcement": [], "Actual":[], "Previous":[], "Consensus":[], "Forecast":[]}

#Set effected Countries
driver.find_element_by_xpath("/html/body/form/div[4]/div/div/table/tbody/tr/td[1]/div/button").click()
driver.find_element_by_xpath("/html/body/form/div[4]/div/div/span/div/div[1]/span[1]").click()
driver.find_element_by_xpath("/html/body/form/div[4]/div/div/span/div/div[2]/div[3]/a").click()

#get start date
start_date = datetime.datetime(2021,12,1)
search_date = start_date
initial = True

while search_date != datetime.datetime(2022,1,1):
    if initial == True:
        search_date = start_date
        initial=False
    else:
        start_date += datetime.timedelta(days=1)
        search_date = start_date

    try:
        #Set Calendar Range
        driver.find_element_by_xpath("/html/body/form/div[4]/div/div/table/tbody/tr/td[1]/div/div[1]/button").click()
        driver.find_element_by_xpath('/html/body/form/div[4]/div/div/table/tbody/tr/td[1]/div/div[1]/ul/li[12]/a').click()
        start_elem = driver.find_element_by_xpath('//*[@id="startDate"]')
        end_elem = driver.find_element_by_xpath('//*[@id="endDate"]')
        time.sleep(3)
        start_elem.clear()
        start_elem.send_keys(search_date.strftime("%Y-%m-%d"))
        start_elem.send_keys(Keys.TAB)
        end_elem.clear()
        end_elem.send_keys(search_date.strftime("%Y-%m-%d"))
        end_elem.send_keys(Keys.TAB)
        btn = driver.find_element_by_xpath('/html/body/form/div[4]/div/div/div[1]/div/span[3]/button')
        btn.send_keys(Keys.RETURN)

        #wait for page to load
        time.sleep(5)

        #Get Calendar Table
        calender_html= driver.find_element_by_css_selector('div.table-responsive:nth-child(9)').get_attribute('innerHTML')

        #Use beautiful soup to get the values
        soup = BeautifulSoup(calender_html, "html.parser")

        try:
            #Get the Date of the Table
            table_header = soup.find("table", attrs={'id': 'calendar'})
            table_header = table_header.find("thead", attrs={'class': 'table-header'})
            table_header = table_header.find_all('th')
            date_reached = False
            for header in table_header:
                while date_reached==False:
                    date = header.text.strip()
                    day_text, monthname, day, year = date.split(" ")

                    datetime_object = datetime.datetime.strptime(monthname, "%B")
                    month_number = datetime_object.month

                    if month_number < 10:
                        month_number = "0" + str(month_number)
                    else:
                        month_number = str(month_number)

                    if int(day) < 10:
                        day = "0" + day
                    else:
                        day = day

                    date = str(year) + "-" + str(month_number) + "-" + str(day)

                    date_reached = True

            table = soup.find("table", attrs={'class': 'table table-hover table-condensed'})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                if len(cols)>3:
                    economic_calendar["Date"].append(date)
                    economic_calendar["Time"].append(cols[0])
                    economic_calendar["Country"].append(cols[1])
                    announcement = cols[4]
                    announcement = announcement.replace("\n                        ", " ")
                    economic_calendar["Announcement"].append(announcement)
                    economic_calendar["Actual"].append(cols[5])
                    economic_calendar["Previous"].append(cols[6])
                    economic_calendar["Consensus"].append(cols[7])
                    economic_calendar["Forecast"].append(cols[8])

            write_to_csv(economic_calendar)


        except:
            economic_calendar["Date"].append(search_date.strftime("%Y-%m-%d"))
            economic_calendar["Time"].append("00:00:00")
            economic_calendar["Country"].append("None")
            announcement = "No Events Scheduled"
            economic_calendar["Announcement"].append(announcement)
            economic_calendar["Actual"].append(0)
            economic_calendar["Previous"].append(0)
            economic_calendar["Consensus"].append(0)
            economic_calendar["Forecast"].append(0)

            write_to_csv(economic_calendar)

    except:
        economic_calendar["Date"].append(search_date.strftime("%Y-%m-%d"))
        economic_calendar["Time"].append("00:00:00")
        economic_calendar["Country"].append("None")
        announcement = "No Events Scheduled"
        economic_calendar["Announcement"].append(announcement)
        economic_calendar["Actual"].append(0)
        economic_calendar["Previous"].append(0)
        economic_calendar["Consensus"].append(0)
        economic_calendar["Forecast"].append(0)

        write_to_csv(economic_calendar)

write_to_csv(economic_calendar)

df = pd.DataFrame.from_dict(economic_calendar)
df.to_csv("Pandas_Calendar_december.csv")



