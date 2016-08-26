from comscore_analytics import ComscoreConnection
from comscore_reporting import Reporting
import datetime
import pandas as pd
import numpy as np
import os
import time

csconn = ComscoreConnection()
print('connecting to reporting library...')
rep = Reporting(csconn = csconn)
    

concats = ["year","month","day"]
dir_path = os.getcwd()
folder = 'reports'
if not os.path.isdir(folder): 
	os.makedirs(folder)


timestr = time.strftime("%Y%m%d")

print('making csv files...')
print('1')

df1 = rep.pull_n_url_visits_per_day()
df1['date'] = pd.to_datetime(df1[concats])
df1.drop(concats, axis=1, inplace=True)
df1.sort_values(by='date', inplace=True)
df1.set_index('date', inplace=True)

filename = "urlvisits-{}.csv".format(timestr)
fullpath = os.path.join(dir_path, folder, filename)
df1.to_csv(fullpath)


print('2')
df3 = rep.pull_n_searches_per_day()
df3['date'] = pd.to_datetime(df3[concats])
df3.drop(concats, axis=1, inplace=True)
df3.sort_values(by='date', inplace=True)
df3.set_index('date', inplace=True)

filename = "searches-{}.csv".format(timestr)
fullpath = os.path.join(dir_path, folder, filename)
df3.to_csv(fullpath)


print('3')
df2 = rep.pull_n_unique_users_per_day()
df2['date'] = pd.to_datetime(df2[concats])
df2.drop(concats, axis=1, inplace=True)
df2.sort_values(by='date', inplace=True)
df2.set_index('date', inplace=True)

filename = "uniqueusers-{}.csv".format(timestr)
fullpath = os.path.join(dir_path, folder, filename)
df2.to_csv(fullpath)


print('4')
df4 = rep.pull_n_in_tab_users_per_month()
df4.sort_values(by='month_id', inplace=True)
df4.set_index('month_id', inplace=True)


filename = "intab-{}.csv".format(timestr)
fullpath = os.path.join(dir_path, folder, filename)
df4.to_csv(fullpath)
