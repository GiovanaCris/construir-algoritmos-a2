
import datetime
import requests

def cotar():
    cotacoes = []
    hoje = datetime.date.today()

    for dia in range(365):
        data = hoje - datetime.timedelta(days=dia)

        data_formatada = data.strftime("%m-%d-%Y")

        url = (
            "https://olinda.bcb.gov.br/olinda/servico/"
            "PTAX/versao/v1/odata/"
            "CotacaoDolarDia(dataCotacao=@dataCotacao)"
            f"?@dataCotacao='{data_formatada}'"
            "&$top=1"
            "&$format=json"
            "&$select=cotacaoCompra"
        )

        resposta = requests.get(url)
        dados = resposta.json()["value"]

        if dados:
            cotacoes.append(dados[0]["cotacaoCompra"])
        else:
            cotacoes.append(None)

    return cotacoes
print(cotar())
