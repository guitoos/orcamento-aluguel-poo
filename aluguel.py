import csv

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
        if self.tipo in ["Apartamento", "Casa"]:
            if self.garagem:
                valor += 300

        # Estúdio - vaga individual
        if self.tipo == "Estúdio":
            if self.vagas_estudio >= 2:
                valor += 250
                vagas_extra = self.vagas_estudio - 2
                if vagas_extra > 0:
                    valor += vagas_extra * 60

        # Desconto para apartamento sem crianças
        if self.tipo == "Apartamento" and not self.tem_criancas:
            valor *= 0.95  # 5% de desconto

        return valor

def gerar_csv(valor_mensal):
    parcelas = []
    for i in range(1, 13):
        parcelas.append([f"Parcela {i}", round(valor_mensal, 2)])

    with open("parcelas_orcamento.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Parcela", "Valor (R$)"])
        writer.writerows(parcelas)

    print("\nArquivo CSV gerado com sucesso: parcelas_orcamento.csv")

def main():
    print("=== Sistema de Orçamento Imobiliário R.M ===")

    tipo = input("Tipo de imóvel (Apartamento / Casa / Estúdio): ")
    tipo = tipo.capitalize()

    quartos = 1
    garagem = False
    vagas_estudio = 0

    if tipo in ["Apartamento", "Casa"]:
        quartos = int(input("Quantidade de quartos (1 ou 2): "))
        garagem = input("Deseja garagem? (s/n): ").lower() == "s"
        tem_criancas = input("Possui crianças? (s/n): ").lower() == "s"
        valor_base = 700 if tipo == "Apartamento" else 900

    elif tipo == "Estúdio":
        valor_base = 1200
        vagas_estudio = int(input("Quantas vagas de estacionamento deseja? "))
        tem_criancas = True  # Não afeta estúdio

    contrato = 2000
    parcelas_contrato = int(input("Em quantas parcelas quer pagar o contrato? (1 a 5): "))
    valor_parcela_contrato = contrato / parcelas_contrato

    imovel = Imovel(tipo, quartos, valor_base, garagem, vagas_estudio, tem_criancas)
    valor_mensal = imovel.calcular_aluguel() + valor_parcela_contrato

    print(f"\nValor mensal do aluguel: R$ {round(imovel.calcular_aluguel(), 2)}")
    print(f"Valor mensal com contrato parcelado: R$ {round(valor_mensal, 2)}")

    gerar_csv(valor_mensal)

if __name__ == "__main__":
    main()
