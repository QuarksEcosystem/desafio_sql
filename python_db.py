import csv

seller_sales = {}
highest_sale = 0
highest_sale_client = ''
lowest_sale = float('inf')
lowest_sale_client = ''
sales_by_type = {'Serviços': 0, 'Licenciamento': 0, 'Produtos': 0}
count_by_type = {'Serviços': 0, 'Licenciamento': 0, 'Produtos': 0}
sales_by_customer = {}

with open('DB_Teste.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  

    for row in reader:
        seller = row[7]
        sales = float(row[1].replace('R$ ', '').replace('.', '').replace(',', '.'))
        sales_type = row[4]
        customer = row[2]

        if seller in seller_sales:
            seller_sales[seller] += sales
        else:
            seller_sales[seller] = sales

        if sales > highest_sale:
            highest_sale = sales
            highest_sale_client = customer

        if sales < lowest_sale:
            lowest_sale = sales
            lowest_sale_client = customer

        sales_by_type[sales_type] += sales
        count_by_type[sales_type] += 1

        if customer in sales_by_customer:
            sales_by_customer[customer] += 1
        else:
            sales_by_customer[customer] = 1

sorted_seller_sales = {k: v for k, v in sorted(seller_sales.items(), key=lambda item: item[1], reverse=True)}

print('Total sales by seller:')
for seller, sales in sorted_seller_sales.items():
    print(f'{seller}: R$ {sales:.2f}')

print(f'Customer with highest sale: {highest_sale_client} (R$ {highest_sale:.2f})')
print(f'Customer with lowest sale: {lowest_sale_client} (R$ {lowest_sale:.2f})')

avg_sales_by_type = {k: v / count_by_type[k] for k, v in sales_by_type.items() if count_by_type[k] > 0}

print('Average sales by type:')
for sales_type, avg_sales in avg_sales_by_type.items():
    print(f'{sales_type}: R$ {avg_sales:.2f}')

print('Number of sales by customer:')
for customer, sales_count in sales_by_customer.items():
    print(f'{customer}: {sales_count}')
