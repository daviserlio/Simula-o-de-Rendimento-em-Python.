# Trabalho - Aprendizagem de Máquina
# Equipe:
# Davi Lopes de Carvalho - 2414290032
# Pedro Henrique Rabelo do Nascimento – 2414290028
# Luiz Henrique Bayma Martins – 2414290084
# Jonathan Francisco Noé Galvão Cavalcante – 2414290168
# Gabriel Augusto Oliveira Souza – 2414290079
# Davi Serlio Lopes De Souza – 2414290102

while True:
    valor = float(input("Digite o valor do investimento (R$): "))
    dias = int(input("Digite o tempo da aplicação (em dias): "))

    taxa_anual = 0.1415
    taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1
    rendimento_bruto = valor * ((1 + taxa_diaria) ** dias - 1)

    tabela_iof = {
        1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83, 6: 0.80, 7: 0.76,
        8: 0.73, 9: 0.70, 10: 0.66, 11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53,
        15: 0.50, 16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33,
        21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16, 26: 0.13,
        27: 0.10, 28: 0.06, 29: 0.03, 30: 0.00
    }

    if dias <= 30:
        iof_percentual = tabela_iof.get(dias, 0)
        valor_iof = rendimento_bruto * iof_percentual
    else:
        valor_iof = 0

    rendimento_apos_iof = rendimento_bruto - valor_iof

    if dias <= 180:
        aliquota_ir = 0.225
    elif dias <= 360:
        aliquota_ir = 0.20
    elif dias <= 720:
        aliquota_ir = 0.175
    else:
        aliquota_ir = 0.15

    valor_ir = rendimento_apos_iof * aliquota_ir
    rendimento_liquido = rendimento_apos_iof - valor_ir
    valor_final = valor + rendimento_liquido

    print("\nValor líquido disponível: R$ {:.2f}".format(valor_final))
