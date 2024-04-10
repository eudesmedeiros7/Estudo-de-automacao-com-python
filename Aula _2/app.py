import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site https://www.novaliderinformatica.com.br/computadores-gamers
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')
# extrair todos os títulos
# para extrair o titulo, podemos usar o XPATH que usar uma nomeclatura assim:
# //tag[@atributo='valor']
# eu encontrei o atributo dos títulos inspecionando os elementos e encontrando uma classe
# chamada class=nome-produto //a[@class='nome-produto']
titulos = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")
# existem 29 itens com titulos
# extrair todos os preços
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")
# existem 21 itens com precos

# criando uma planilha excel
workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')

sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produtos'
sheet_produtos['B1'].value = 'Preços'
# inserir na planilha
for titulo, preco in zip(titulos, precos):
    # usamos o zip para associar os iteráveis, mas qnd titulos[i] != precos[i], para de atribuir
    # fizemos isso pq existem 29 titulos e 21 precos
    sheet_produtos.append([titulo.text, preco.text])
workbook.save('produtos.xlsx')
