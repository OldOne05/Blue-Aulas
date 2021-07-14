### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

itensComprados = []
total_quantidade_geral = 0

estoque = {"coca":15, "Chocolate":6, "batata":11, "papel":3, "presunto":26}

continuar = input("Bem vindo! Deseja ir as compras (s/n)?").lower()
while continuar not in ["s","n"]:
    continuar = input("invalido. Deseja ir as compras (s/n)?").lower()

    while continuar == "s":
        print()
        print("Nossos produtos")

        for i in estoque:
            if estoque[i] > 0:
                print(i)
            
        print()

        produto = input("O  que vc quer comprar?")
        quantidade_atual = estoque.get(produto,-1)

        if quantidade_atual == -1:
            print("Produto invalido")
        elif quantidade_atual == 0:
            print("Produto indisponivel")
        else:
            quantidade = int(input("Qual a quantidade desejada?"))
            if quantidade > quantidade_atual:
                print(f"Quantidade solicitada n disponivel. No momento temos apenas a quantidade {quantidade} em estoque")
            else:
                estoque[produto] = quantidade_atual - quantidade 
                if produto not in itensComprados:
                    itensComprados.append(produto)
                total_quantidade_geral += quantidade
                print("Compra realizada com sucesso")

        continuar = input("Deseja continuar as compras? (s/n)")
        while continuar not in ["s","n"]:
            continuar = input("invalido. Deseja continuar as compras (s/n)?").lower()