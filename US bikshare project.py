# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:17:38 2021

@author: YUSUF_JAKADA
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
  while True:
    city = input('input city please :').lower()
    if city  not in CITY_DATA:
        print('wrong input')
        continue
    else:
        break
  while True:
     time = input('input month, day, all or none please: ').lower()
     if time == 'month':
         month = input('which month? january, february, march, april, may, june: ').lower()
         break
     elif time == 'day':
         day = input('which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday: ').lower()
         break
     elif time == 'all':
         month = input('which month? january, february, march, april, may, june: ').lower()
         day = input('which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday: ').lower()
         break
     elif time == 'none':
         break
     else:
         input('wrong input please try again')
         break
     print(city)
     print(month)
     print(day)
     print('-'*40)
     return city, month, day
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     month = months.index(month) + 1
     df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        return df

def time_stats(df):
    print('\n the most frequent time of the travel is being calculated...\n')
    start_time = time.time()
    print(df['month'].mode()[0])
    print(df['day_of_week'].mode()[0])
    print(df['hour'].mode()[0])
    print("\n This has taken %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    print('\n most popular station trip is being calculated...\n')
    start_time = time.time()
    print(df['Start Station'].mode()[0])
    print(df['End Station'].mode()[0]) 
    most_frequent_star_and_end_station = df.group_by(['Start Station', 'End Station'])
    print(most_frequent_star_and_end_station)
    print("\n This has taken %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n trip duration is being calculated ...\n')
    start_time = time.time()
    print(df['Trip Duration'].sum())
    print(['Trip Duration'].mean())
    print("\nThis has taken %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    print('\n The user stats is being calculated...')
    start_time = time.time()
    print(df['User Type'].value_counts())
    if city != 'washington':
     print(df['Gender'].value_counts())
     print(df['Birth Year'].min())
     print(df['Birth Year'].max())
     print(df['Birth Year'].mode()[0])
    print("\n This has taken %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df
def data(df):
    raw_data = 0
    while True:
        answer = input('would you like to see the raw data? Yes or No').lower()
        if answer not in ['Yes', 'No']:
            answer = input('you entered wrong input please input Yes or No').lower()
        elif answer == 'Yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input('Would you like to see more? Yes or No').lower()
            if again == 'No':
                break
            elif answer == 'No':
                return

def main():
       city = ''
       month = ''
       day = ''
       while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        restart = input('\n Do you like to come again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
