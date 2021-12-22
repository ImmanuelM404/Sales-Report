import pandas as pd 
import numpy as np 



SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

print("*" * DORKY_LINE_LENGTH)


#Count the amounts of each type of melon that were sold
melon_tallies = {'Musk':0, 'Hybrid': 0, 'Watermelon':0, 'Winter':0}
melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
def melonCount():
    file = open('orders-by-type.txt')

    total_revenue = 0 
    for line in file:
        data = line.split('|')
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    
    #Calculate the revenue from those melon tallies 
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print("We sold", melon_tallies[melon_type], melon_type, 'at price', price, 'for a total revenue', revenue)
melonCount()

 


#Separates sales into online sales and phone sales
def sales_data():
    sale_file = open('orders-with-sales.txt')

    phone_sales = 0
    online_sales = 0 

    for line in sale_file:
        data = line.split('|')
        if data[1] == '0':
            online_sales += float(data[3])
        else:
            phone_sales += float(data[3])
    print(f"Salespeople generated ${phone_sales:.2f} in revenue.")
    print(f"Internet sales generated ${online_sales:.2f} in revenue.")
    #Produces fancy report to summarize the info for our CEO 
    if online_sales > phone_sales:
        print('Machine Learning on the rise')
    else:
        print('Human touch is still effective')
sales_data()
