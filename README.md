Bike Share Data for UDACITY NanoDegree Program
-----------------------------------------------------------------------------------
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I will be using data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.



The Datasets
-----------------------------------------------------------------------------------
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
    -	Start Time (e.g., 2017-01-01 00:07:57)
    -	End Time (e.g., 2017-01-01 00:20:53)
    -	Trip Duration (in seconds - e.g., 776)
    -	Start Station (e.g., Broadway & Barry Ave)
    -	End Station (e.g., Sedgwick St & North Ave)
    -	User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

    -	Gender
    -	Birth Year


Python Script to Explore US Bikeshare Data
-----------------------------------------------------------------------------------
This Python script is written for Project 2 of Udacity's Data Analyst Nanodegree (DAND) and is used to explore data related to bike share systems for Chicago, New York City, and Washington. It imports data from csv files and compute descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.


How to run the script
-----------------------------------------------------------------------------------
You can run the script using a Python integrated development environment (IDE) such as Jupyter Notebook. To install Jupyter, you will need to [download the Anaconda installer](https://www.anaconda.com/download/). This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.