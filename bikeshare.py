# Remaining issues but should be ok for a pass:
#  - truncation of columns when looking at the raw csv file
#
# created by: jonas sjöblom

#import packages needed

import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#create list with all the options for days so we don't need to repeat them over and over again
DAY_LIST = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

#create list with all the options for days so we don't need to repeat them over and over again (notice only jan-june)
MONTH_LIST = ['all','january', 'february', 'march', 'april', 'may' , 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # using the lower function so that it wont matter if the user uses capital or non capital letters
    city = input("Please pick a city (chicago, new york city or washington):\n").lower()
    
    #error handling when the choice is not in the list, then ask again
    while city not in CITY_DATA:
        city = input("You can only chose from chicago, new york city and washington, please try again ").lower()
  

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please input month name (all, january, february, ... , june): ").lower()
    
    while month not in MONTH_LIST:
        month = input("You can only chose from all, january, february, ... , june, please try again ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please input day name (all, monday, tuesday, ... sunday): ").lower()
    
    while day not in DAY_LIST:
        day = input("You can only chose from all, monday, tuesday, ... sunday, please try again").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #create dataframe and replace space with underscore_ 
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    
    #cast to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # lambda function %A = weekdayname
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['start_hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        # index starts with 0 so month 1 will be index 0+1
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        df.loc[df['month'] == month,:]
        
        
    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is:{}".format(str(df['month'].mode().values[0])))

    # TO DO: display the most common day of week
    print("The most common day of the week is:{}".format(str(df['day_of_week'].mode().values[0])))

    # TO DO: display the most common start hour
    print("The most common start hour is:{}".format(str(df['start_hour'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used startstation is:{}".format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used endstation is:{}".format(df['End Station'].mode().values[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['start2endstation'] = df['Start Station']+"/ "+df['End Station']
    print("The most commonly used c ombo is:{}".format(df['start2endstation'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print("total travel time is  {}".format(str(df['duration'].sum())))

    # TO DO: display mean travel time
    print("mean travel time is  {}".format(str(df['duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types 
    print("Therse are the cunts of user types: ") 
    print(df['User Type'].value_counts())

    
 
    # TO DO: Display counts of gender
    # how to handle it when column is missing ?
    
    if city == "washington":  
     print("Gender and birthyear is missning for Washington")
    if city != "washington":  
     print("Therse are the counts of Gender types: ") 
     print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
     print("This is the earliest year of birth: {}".format(int(df['Birth Year'].min())))
     print("This is the most recent year of birth: {}".format(int(df['Birth Year'].max())))
     print("This is the most common year of birth: {}".format(int(df['Birth Year'].mode().values[0])))
    

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def fileinfo(city):

    if city == "washington":
    # load the dataset
     csv_file = pd.read_csv("washington.csv", header=None)
          
    if city == "new york city":
    # load the dataset
     csv_file = pd.read_csv("new_york_city.csv", header=None)  
        
    if city == "chicago":
    # load the dataset
     csv_file = pd.read_csv("chicago.csv", header=None)
    
        
# print 5 rows of data
    
#   print("\n statistics about the "+city + ".csv file (RAW non filtered)\n----------------------------------------------------")
#    print(csv_file.describe())
    print("\n structure of the " +city +".csv file (RAW non filtered)\n------------------------------------------------------")
    print("number of lines: ")
    print(len(csv_file)) 
      
    # initial values
    start_line = 0
    max_line = 5
    
    
    
    while max_line <= csv_file.shape[0] -1:   #less than index 0
     print(csv_file.iloc[start_line:max_line,:])
     start_line += 5
     max_line += 5
     five_more = input("Do you want to see another 5? (yes/no): ").lower()
     while five_more not in ['yes','no']:
         five_more = input("Do you want to see another 5? (yes/no): ").lower()
     if five_more == "no":
      break

def main():

    
    while True:
        
        city, month, day = get_filters() # ok
        df = load_data(city, month, day) # ok

        time_stats(df) # ok
        station_stats(df) # ok
        trip_duration_stats(df) # ok
        user_stats(df, city) # ok
        
        raw_info = input("\nDo you want to see the raw file? Enter yes or no.\n")
        while raw_info not in ['yes','no']:
         raw_info = input("\nThat was not a valid choice,Do you want to see the raw file? Enter yes or no.\n").lower()
        if raw_info.lower() == 'yes':
           fileinfo(city)
     
        
        
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        while restart not in ['yes','no']:
         restart = input("\nThat was not a valid choice,Would you like to restart? Enter yes or no.\n").lower()
        if restart.lower() == 'no':
            break


if __name__ == "__main__":
	main()
