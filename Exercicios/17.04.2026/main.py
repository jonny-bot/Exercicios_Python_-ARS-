import json

def main():
    with open('lista_produtos.json', 'r') as f:
        data = json.load(f)
    
    for contador, lista in enumerate(data):
        print(f"{contador + 1}. Produto: {lista['produto']}, Preço: {lista['preco']}")

if __name__ == "__main__":
    main()
