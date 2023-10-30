import csv

# Create an empty dictionary to store the total sales for each seller
seller_sales = {}

# Open the CSV file and iterate through each row
with open('DB_Teste.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # skip header row
    for row in reader:
        seller = row[7]  # extract seller's name
        sales = float(row[1].replace('R$ ', '').replace('.', '').replace(',', '.'))  # extract sales value and convert to float
        if seller in seller_sales:
            seller_sales[seller] += sales  # add sales value to existing seller's total sales
        else:
            seller_sales[seller] = sales  # create new seller with initial total sales value

# Sort the dictionary of total sales in descending order
sorted_seller_sales = {k: v for k, v in sorted(seller_sales.items(), key=lambda item: item[1], reverse=True)}

# Print out the results
print('Total sales by seller:')
for seller, sales in sorted_seller_sales.items():
    print(f'{seller}: R$ {sales:.2f}')
