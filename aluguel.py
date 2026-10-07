"""Sistema de orçamento de aluguel da imobiliária fictícia R.M Imóveis."""

import csv

VALOR_CONTRATO = 2000
MESES_ORCAMENTO = 12
VALORES_BASE = {"Apartamento": 700, "Casa": 900, "Estúdio": 1200}


class Imovel:
    def __init__(self, tipo, quartos, valor_base, garagem=False, vagas_estudio=0, tem_criancas=True):
        self.tipo = tipo
        self.quartos = quartos
        self.valor_base = valor_base
        self.garagem = garagem
        self.vagas_estudio = vagas_estudio
        self.tem_criancas = tem_criancas

    def calcular_aluguel(self):
        valor = self.valor_base

        # Regras de quartos
        if self.tipo == "Apartamento" and self.quartos == 2:
            valor += 200
        elif self.tipo == "Casa" and self.quartos == 2:
            valor += 250

        # Regras de garagem
        if self.tipo in ("Apartamento", "Casa") and self.garagem:
            valor += 300

        # Estúdio: pacote de 2 vagas por R$ 250 e R$ 60 por vaga adicional
        if self.tipo == "Estúdio" and self.vagas_estudio >= 2:
            valor += 250
            valor += (self.vagas_estudio - 2) * 60

        # Desconto para apartamento sem crianças
        if self.tipo == "Apartamento" and not self.tem_criancas:
            valor *= 0.95  # 5% de desconto

        return round(valor, 2)


def gerar_parcelas(valor_aluguel, parcelas_contrato):
    """Retorna as 12 parcelas: o contrato é cobrado apenas nas primeiras N parcelas."""
    valor_parcela_contrato = round(VALOR_CONTRATO / parcelas_contrato, 2)
    parcelas = []
    for mes in range(1, MESES_ORCAMENTO + 1):
        contrato = valor_parcela_contrato if mes <= parcelas_contrato else 0
        parcelas.append((mes, valor_aluguel, contrato, round(valor_aluguel + contrato, 2)))
    return parcelas


def gerar_csv(parcelas, caminho="parcelas_orcamento.csv"):
    with open(caminho, mode="w", newline="", encoding="utf-8-sig") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow(["Parcela", "Aluguel (R$)", "Contrato (R$)", "Total (R$)"])
        for mes, aluguel, contrato, total in parcelas:
            writer.writerow([f"Parcela {mes}", f"{aluguel:.2f}", f"{contrato:.2f}", f"{total:.2f}"])
    print(f"\nArquivo CSV gerado com sucesso: {caminho}")


def perguntar_opcao(mensagem, opcoes):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in opcoes:
            return resposta
        print(f"Opção inválida. Responda com: {', '.join(opcoes)}.")


def perguntar_inteiro(mensagem, minimo, maximo=None):
    while True:
        resposta = input(mensagem).strip()
        if resposta.isdigit() and int(resposta) >= minimo and (maximo is None or int(resposta) <= maximo):
            return int(resposta)
        faixa = f"entre {minimo} e {maximo}" if maximo is not None else f"a partir de {minimo}"
        print(f"Valor inválido. Digite um número inteiro {faixa}.")


def main():
    print("=== Sistema de Orçamento Imobiliário R.M ===")

    tipos = {"apartamento": "Apartamento", "casa": "Casa", "estudio": "Estúdio", "estúdio": "Estúdio"}
    tipo = tipos[perguntar_opcao("Tipo de imóvel (Apartamento / Casa / Estúdio): ", list(tipos))]

    quartos, garagem, vagas_estudio, tem_criancas = 1, False, 0, True
    if tipo in ("Apartamento", "Casa"):
        quartos = perguntar_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)
        garagem = perguntar_opcao("Deseja garagem? (s/n): ", ["s", "n"]) == "s"
        if tipo == "Apartamento":
            tem_criancas = perguntar_opcao("Possui crianças? (s/n): ", ["s", "n"]) == "s"
    else:
        vagas_estudio = perguntar_inteiro("Quantas vagas de estacionamento deseja? ", 0)

    parcelas_contrato = perguntar_inteiro("Em quantas parcelas quer pagar o contrato? (1 a 5): ", 1, 5)

    imovel = Imovel(tipo, quartos, VALORES_BASE[tipo], garagem, vagas_estudio, tem_criancas)
    aluguel = imovel.calcular_aluguel()
    parcelas = gerar_parcelas(aluguel, parcelas_contrato)

    print(f"\nValor mensal do aluguel: R$ {aluguel:.2f}")
    print(f"Contrato: R$ {VALOR_CONTRATO:.2f} em {parcelas_contrato}x de R$ {parcelas[0][2]:.2f}")
    print(f"Primeira parcela (aluguel + contrato): R$ {parcelas[0][3]:.2f}")

    gerar_csv(parcelas)


if __name__ == "__main__":
    main()
