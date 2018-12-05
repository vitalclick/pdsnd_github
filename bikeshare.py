import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n------------------------------------------------------------------------')
    print('Hello! This is Anthony. Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please enter the city for which you would like to see the statistics by typing one of the following: Chicago, New York City, or Washington...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if city in CITY_DATA.keys():
            print("Sorry, I do not understand your input. Please input either Chicago, New York, or Washington.\n")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nPlease enter the month of the year for which you would like to see the statistics by typing one of the following. Jan, Feb, Mar, Apr, May, Jun. Otherwise, enter 'all' to access data from all six months...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if month not in ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All'):
            print("Sorry, I do not understand your input. Please input either: Jan, Feb, Mar, Apr, May, Jun.  Or 'all' for data from all months.\n")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nWhich day? Please type a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Otherwise, enter 'all' to access data from the entire week...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print("Sorry, I do not understand your input.  Type the full day name like Monday, Tuesday, etc.  Or use 'all' for the entire week.\n")
        else:
            break

    print('-'*40)
    return city, month, day



#--------------------------------------------------------------------------------------------------------
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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df



#--------------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month of travel was " + str(popular_month) + ".\n")

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of travel was " + popular_day + ".\n")

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print("The most common hour of travel was " + str(popular_hour) + ".\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



#--------------------------------------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station was " + popular_start_station + ".\n")

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station was " + popular_end_station + ".\n")

    # display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + " | " + df['End Station']
    popular_station_combo = df['Station Combo'].mode()[0]
    print("The most frequent combination of start station and end station trip was " + popular_station_combo + ".\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#--------------------------------------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    m, s = divmod(int(df['Trip Duration'].sum()), 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("Total Travel Time: " + str(d) + " days, " + str(h) + " hours, " + str(m) + " minutes, " + str(s) + " seconds.")

    # display mean travel time
    m, s = divmod(int(df['Trip Duration'].mean()), 60)
    h, m = divmod(m, 60)
    print("Mean Travel Time: " + str(h) + " hours, " + str(m) + " minutes, " + str(s) + " seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#--------------------------------------------------------------------------------------------------------
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types...")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city not in('Chicago', 'New York City'):
        print("\nSorry, gender statistics for Washington are not available.")
    else:
        print("\nGender statistics of users...")
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if city not in('Chicago', 'New York City'):
        print("\nSorry, No available birth statistics for Washington.")
    else:
        print("\nThe earliest, most recent, and most common year of birth are as follows...")
        print("The earliest year of birth is: " + str(int(df['Birth Year'].min())))
        print("The most recent year of birth is: " + str(int(df['Birth Year'].max())))
        print("The most common year of birth is: " + str(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#--------------------------------------------------------------------------------------------------------
def disp_raw_data(df):
    """Displays the data used to compute the stats."""
	
    #omit irrelevant columns from visualization
    df = df.drop(['month'], axis = 1)
    row_index = 0

    see_data = input("\nWould you like to see the rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()	
		

#--------------------------------------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        disp_raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
