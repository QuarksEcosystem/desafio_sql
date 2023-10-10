import csv
from collections import defaultdict

def analisar_csv(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        vendas_por_vendedor = defaultdict(float)
        vendas_por_cliente = defaultdict(int)
        vendas_por_tipo = defaultdict(list)
        venda_maior = None
        venda_menor = None

        for row in reader:
            vendedor = row['Vendedor']
            cliente = row['Cliente']
            tipo = row['Tipo']
            
            # Convertendo o formato brasileiro de número para formato padrão
            valor = float(row['Valor'].replace('R$ ', '').replace('.', '').replace(',', '.'))
            
            # Sumarizando valor por vendedor
            vendas_por_vendedor[vendedor] += valor

            # Contando vendas por cliente
            vendas_por_cliente[cliente] += 1

            # Armazenando valores por tipo de venda
            vendas_por_tipo[tipo].append(valor)

            # Identificando a venda de maior e menor valor
            if venda_maior is None or valor > venda_maior[1]:
                venda_maior = (cliente, valor)
            if venda_menor is None or valor < venda_menor[1]:
                venda_menor = (cliente, valor)

        # Ordenando vendas por vendedor
        vendas_ordenadas = sorted(vendas_por_vendedor.items(), key=lambda x: x[1], reverse=True)

        print("Vendas por Vendedor:")
        for v, val in vendas_ordenadas:
            print(f"{v}: R$ {val:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        print(f"\nCliente com venda de maior valor: {venda_maior[0]} (R$ {venda_maior[1]:,.2f})".replace(',', 'X').replace('.', ',').replace('X', '.'))
        print(f"Cliente com venda de menor valor: {venda_menor[0]} (R$ {venda_menor[1]:,.2f})".replace(',', 'X').replace('.', ',').replace('X', '.'))

        print("\nValor médio por Tipo de Venda:")
        for tipo, valores in vendas_por_tipo.items():
            media = sum(valores) / len(valores)
            print(f"{tipo}: R$ {media:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        print("\nNúmero de vendas por cliente:")
        for cliente, num_vendas in vendas_por_cliente.items():
            print(f"{cliente}: {num_vendas}")

if __name__ == "__main__":
    analisar_csv("DB_Teste.csv")
