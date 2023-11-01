import csv

seller_sales = {}

with open('DB_Teste.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  
    for row in reader:
        seller = row[7]  
        sales = float(row[1].replace('R$ ', '').replace('.', '').replace(',', '.'))  
        if seller in seller_sales:
            seller_sales[seller] += sales  
        else:
            seller_sales[seller] = sales  


sorted_seller_sales = {k: v for k, v in sorted(seller_sales.items(), key=lambda item: item[1], reverse=True)}


print('Total sales by seller:')
for seller, sales in sorted_seller_sales.items():
    print(f'{seller}: R$ {sales:.2f}')
