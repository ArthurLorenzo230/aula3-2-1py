valores = [
    10,                
    3 + 2j,            
    3.14,              
    "texto",           
    True,              
    [1, 2, 3],         
    {"chave": "valor"},
    None               
]

for valor in valores:
    print(f"valor: {valor} tipo: {type(valor).__name__}")
