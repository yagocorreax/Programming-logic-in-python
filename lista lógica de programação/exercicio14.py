km = float(input("Digite a quilometragem percorrida:"))
dias = int(input("Digite a quantidade de dias em que o carro permaneceu alugado:"))
valor_por_km = km * 0.2
valor_por_dia = dias * 90
valor_total = valor_por_km + valor_por_dia
print(f"O valor total a ser pago é de:{valor_total} ")