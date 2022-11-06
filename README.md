#  CL-Stock Analysis.
## Repository for the Code Louisville Data Analysis Project

#  ***** NOTE: ***** Some of the cells in this notebook call functions which require user input!!!
## *** If you select "Run All" from the menu bar then you will be prompted to input the requested information for each of those cells.

## **REQUIREMENTS**
### Python interpreter version 3.10.6 64 bit
### Jupyter  v2022.9.1202862440 
### Pandas
### Datetime
### Matplotlib
### Numpy
### Math
### Seaborn

## Project requirments met:
>   Catagory 1.
      1. Read in data from a local csv, excel file, json, or any other file type.
    Catagory 2.
      1. Use built-in pandas or numpy functions to do things like remove 0’s and null values where they don’t belong in your dataset. 
    Catagory 3.
      1. Do 5 basic calculations with Pandas, like finding the sum(), median(), mean(), or mode() of a column.
      2. Write custom functions to operate on your data.
    Catagory 4.
      1. Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.
    Catagory 5.
      1. Write markdown cells in Jupyter explaining your thought process and code.


## Basic Functionality:
> The functions in the stock_analysis_funcs.ipynb file requests the user to imput a valid stock symbol and in some cases a valid year from the list provided below the input field. 
> Valid symbols can be entered in lower, upper or mixed case. It takes that input and reads in data from the corrosponding local .csv file. 
> It then cleans/transforms the data into a pandas dataframe.
> The user only gets three attempts to enter a valid stock symbol from the list provided and then the function terminates and returns a message.
> If no corrosponding file is found the function terminates and returns a message.

## Primary thesis:
> A stock can be listed as a good or bad candidate for the Iron Condor options trading method based on analysis of average Open/Close,
> High/Low, and Price/Volume metrics.

## Result:
> Although these are fundamentals for that thesis a much more granular analysis is necessary.