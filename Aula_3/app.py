import openpyxl
import pyautogui
import pyperclip

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']
for linha in sheet_produtos.iter_rows(min_row=2):
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1285,313,duration=0.5)
    pyautogui.hotkey('ctrl','v')
    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1268,428,duration=0.5)
    pyautogui.hotkey('ctrl','v')
    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1228,577,duration=0.5)
    pyautogui.hotkey('ctrl','v')
    codigo_prod = linha[3].value
    pyperclip.copy(codigo_prod)
    pyautogui.click(1199,680,duration=0.5)
    pyautogui.hotkey('ctrl','v')
    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1159,800,duration=0.5)
    pyautogui.hotkey('ctrl','v')
    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1141,905,duration=0.5)
    pyautogui.hotkey('ctrl','v')
    # preco = linha[6].value
    # quantidade_em_estoque = linha[7].value
    # data_de_validade = linha[8].value
    # cor = linha[9].value
    # tamanho = linha[10].value
    # material = linha[11].value
    # fabricante = linha[12].value
    # pais_de_origem = linha[13].value
    # observacoes = linha[14].value
    # codigo_de_barras = linha[15].value
    # localizacao_armazem = linha[16].value
# entrar na planilha
# copiar informações de um campo e colar no seu campo
# repetir esses passos para outros campos até preencher campos daquela pagina
# clicar em próxima
# repetir os mesmos passos e ir para a proxima pagina (pag. 2)
# repetir o msm passo e finalizar o cadastro daquele produto e clicar em concluir
# clicar em ok para finalizar o processo
# clicar no ok mais uma vez na mensagem para confirmação de salvamento no banco de dados
# clicar em adicionar mais 1
