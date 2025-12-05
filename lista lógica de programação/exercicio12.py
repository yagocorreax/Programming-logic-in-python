preço = float(input("Digite o valor do produto:"))
desconto = (preço * 5) / 100
promoçao = preço - desconto
print(f"Produto com 5% de desconto s/juros, de {preço} por apenas {promoçao}")