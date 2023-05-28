# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:51:53 2023

@author: Sajan Gaba
"""
import pandas as pd
import time
from selenium import webdriver
#%%
df = pd.read_csv('R300.csv')
df.head(3)
my_tickers = df['Ticker']
br = 0 #A tracker to track the number of items completed.
tickers_analysis = pd.DataFrame(columns=['Symbol','Margin','Rating','Surprise','next_q','current_year','next_year','Price','growth5','pe','peg','next_year_sales','next_year_earnings','Average_surprise'])
for j in my_tickers[:2]:
    driver2 = webdriver.Chrome()
    url2 = 'https://www.zacks.com/stock/quote/'+j+'/detailed-earning-estimates'
    driver2.get(url2)
    time.sleep(4)
    br = br+1
    try:
        most_accurate = driver2.find_element(by='xpath',value='//*[@id="quote_upside"]/table/tbody/tr[1]/td[2]').text
        most_accurate = float(most_accurate)
        print(most_accurate)
    except:
        pass
    try:
        zacks_estimate = driver2.find_element(by='xpath',value='//*[@id="quote_upside"]/table/tbody/tr[2]/td[2]').text
        zacks_estimate = float(zacks_estimate)
        print(zacks_estimate)
    except:
        pass
    try:
        zacks_rating = driver2.find_element(by='xpath',value='//*[@id="quote_ribbon_v2"]/div[2]/div[1]/p').text
        #zacks_rating = float(zacks_rating)
        print(zacks_rating)
    except:
        zacks_rating = 'NA'
    try:
        zacks_esp = driver2.find_element(by='xpath',value='//*[@id="quote_upside"]/table/tbody/tr[3]/td[2]/span').text
        zacks_esp = zacks_esp.strip('%')
        zacks_esp = float(zacks_esp)
        print(zacks_esp)
    except:
        zacks_esp = 'NA'
    try:
        next_q = driver2.find_element(by='xpath',value='//*[@id="detailed_earnings_estimates"]/table/tbody/tr[7]/td[3]').text
        next_q = next_q.strip('%')
        next_q = float(next_q)
        print(next_q)
    except:
        next_q = 'NA'
    try:
        current_year = driver2.find_element(by='xpath',value='//*[@id="detailed_earnings_estimates"]/table/tbody/tr[7]/td[4]').text
        current_year = current_year.strip('%')
        current_year = float(current_year)
        print(current_year)
    except:
        current_year = 'NA'
    try:
        next_year_earnings = driver2.find_element(by='xpath',value='//*[@id="detailed_earnings_estimates"]/table/tbody/tr[7]/td[5]').text
        next_year_earnings = next_year_earnings.strip('%')
        next_year_earnings = float(next_year_earnings)
        print(next_year_earnings)
    except:
        next_year_earnings = 'NA'
    try:
        next_year_sales = driver2.find_element(by='xpath',value='//*[@id="detailed_earnings_estimates"]/table/tbody/tr[6]/td[5]').text
        next_year_sales = next_year_sales.strip('%')
        next_year_sales = float(next_year_sales)
        print(next_year_sales)
    except:
        next_year_sales = 'NA'
    try:
        average_surprise = driver2.find_element(by='xpath',value='//*[@id="surprised_reported"]/table/tbody/tr[4]/td[6]/span').text
        average_surprise = average_surprise.strip('%')
        average_surprise = float(average_surprise)
        print(average_surprise)
    except:
        average_surprise = 'NA'
    try:
        stock_price = driver2.find_element(by='xpath',value='//*[@id="quote_ribbon_v2"]/div[1]/div/div/p[1]').text
        stock_price = stock_price.strip('USD')
        stock_price = stock_price.replace("$","")
        stock_price = float(stock_price)
        print(stock_price)
    except:
        stock_price = 'NA'
    try:
        growth_5 = driver2.find_element(by='xpath',value='//*[@id="earnings_growth_estimates"]/table/tbody/tr[6]/td[2]').text
        growth_5 = float(growth_5)
        print(growth_5)
    except:
        growth_5 = 'NA'
    try:
        pe = driver2.find_element(by='xpath',value='//*[@id="earnings_growth_estimates"]/table/tbody/tr[7]/td[2]').text
        pe = float(pe)
        print(pe)
    except:
        pe = "NA"
    try:
        peg = driver2.find_element(by='xpath',value='//*[@id="earnings_growth_estimates"]/table/tbody/tr[8]/td[2]/a').text
        peg = float(peg)
        print(peg)
    except:
        peg = "NA"
    try:
        eps_margin = most_accurate/zacks_estimate
        #eps_margin = float(eps_margin)
        print(eps_margin)
    except:
        eps_margin = "NA"
    #entry = {"_id":br,"Symbol":j,"most_accurate":most_accurate,"eps_margin":eps_margin,"growth_5":growth_5,"pe":pe,"peg":peg,"stock_price":stock_price,"current_year":current_year,"next_q":next_q,"zacks_estimate":zacks_estimate,'zacks_rating':zacks_rating,'zacks_esp':zacks_esp,"next_year_earnings":next_year_earnings,"next_year_sales":next_year_sales,"average_surprise":average_surprise}
    #collection.insert_one(entry)
    tickers_analysis = tickers_analysis.append({'Symbol':j,'Margin':eps_margin,'Rating':zacks_rating,'Surprise':zacks_esp,'next_q':next_q,'current_year':current_year,'next_year_sales':next_year_sales,'next_year_earnings':next_year_earnings,'Average_surprise':average_surprise,'Price':stock_price,'growth5':growth_5,'pe':pe,'peg':peg}, ignore_index=True)
    print('Done',br)
tickers_analysis.to_csv('R300_test.csv')
