import pyautogui as pag
from time import sleep
import os
# Passos manuais para realizar o processo

# 1- Clicar e digitar o nome do usuário
os.chdir(os.path.dirname(__file__))
pag.click(980, 544, duration=0.5)
pag.write('jhonatan')
# 2- Clicar e digitar a senha do usuário
pag.click(969, 572, duration=0.5)
pag.write('123456')
# 3- Clicar em entrar
pag.click(846, 618, duration=0.2)
# 4- Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1 - Clicar e digitar produto
        pag.click(640, 525, duration=0.2)
        pag.write(produto)

        # 2 - Clicar e digitar quantidade
        pag.click(643, 553, duration=0.2)
        pag.write(quantidade)

        # 3 - Clicar e digitar o preço
        pag.click(637, 591, duration=0.2)
        pag.write(preco)
        # 4 - Clicar em registrar
        pag.click(513, 788, duration=0.5)
        sleep(1)
