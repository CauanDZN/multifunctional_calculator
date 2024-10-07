from fractions import Fraction
import math

def resolver_proporcao(a, b, c):
    """Resolve a proporção a/b = c/x."""
    return (b * c) / a

def resolver_equacao(a, b, c):
    """Resolve a equação ax + b = c."""
    return (c - b) / a

def fatorar_raiz_quadrada(numero):
    """Retorna a raiz quadrada do número."""
    return math.sqrt(numero)

def decimal_para_fracao(numero):
    """Converte um número decimal em fração."""
    return Fraction(numero).limit_denominator()

def decimal_para_porcentagem(numero):
    """Converte um número decimal em porcentagem."""
    return numero * 100

def fracao_para_decimal(fracao):
    """Converte uma fração em decimal."""
    return float(fracao)

def fracao_para_porcentagem(fracao):
    """Converte uma fração em porcentagem."""
    return fracao_para_decimal(fracao) * 100

def porcentagem_para_decimal(porcentagem):
    """Converte uma porcentagem em decimal."""
    return porcentagem / 100

def porcentagem_para_fracao(porcentagem):
    """Converte uma porcentagem em fração."""
    return decimal_para_fracao(porcentagem)

def menu():
    print("Calculadora Multifuncional")
    print("1. Resolver Proporção (a/b = c/x)")
    print("2. Resolver x em Equação (ax + b = c)")
    print("3. Fatorar Raiz Quadrada")
    print("4. Converter Decimal em Fração")
    print("5. Converter Decimal em Porcentagem")
    print("6. Converter Fração em Decimal")
    print("7. Converter Fração em Porcentagem")
    print("8. Converter Porcentagem em Decimal")
    print("9. Converter Porcentagem em Fração")
    print("0. Sair")

    while True:
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            a = float(input("Digite a: "))
            b = float(input("Digite b: "))
            c = float(input("Digite c: "))
            x = resolver_proporcao(a, b, c)
            print(f"O valor de x é: {x}")
        elif escolha == "2":
            a = float(input("Digite a: "))
            b = float(input("Digite b: "))
            c = float(input("Digite c: "))
            x = resolver_equacao(a, b, c)
            print(f"O valor de x é: {x}")
        elif escolha == "3":
            numero = float(input("Digite um número: "))
            raiz = fatorar_raiz_quadrada(numero)
            print(f"A raiz quadrada de {numero} é: {raiz}")
        elif escolha == "4":
            numero = float(input("Digite um número decimal: "))
            fracao = decimal_para_fracao(numero)
            print(f"O número {numero} em fração é: {fracao}")
        elif escolha == "5":
            numero = float(input("Digite um número decimal: "))
            porcentagem = decimal_para_porcentagem(numero)
            print(f"O número {numero} em porcentagem é: {porcentagem}%")
        elif escolha == "6":
            fracao = input("Digite uma fração (ex: 1/2): ")
            decimal = fracao_para_decimal(Fraction(fracao))
            print(f"A fração {fracao} em decimal é: {decimal}")
        elif escolha == "7":
            fracao = input("Digite uma fração (ex: 1/2): ")
            porcentagem = fracao_para_porcentagem(Fraction(fracao))
            print(f"A fração {fracao} em porcentagem é: {porcentagem}%")
        elif escolha == "8":
            porcentagem = float(input("Digite uma porcentagem: "))
            decimal = porcentagem_para_decimal(porcentagem)
            print(f"A porcentagem {porcentagem}% em decimal é: {decimal}")
        elif escolha == "9":
            porcentagem = float(input("Digite uma porcentagem: "))
            fracao = porcentagem_para_fracao(porcentagem)
            print(f"A porcentagem {porcentagem}% em fração é: {fracao}")
        elif escolha == "0":
            print("Saindo da calculadora.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
