num1 = float(input("Digite o primeiro número:"))
op = input("Digite a operação:")
num2 = float(input("Digite o segundo número:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("operação inválida")
    

