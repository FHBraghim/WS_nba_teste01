import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')

if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

#   Criando objeto e acessando elementos chamando o método find.
soup = BeautifulSoup(content,'html.parser')
table = soup.find(name='table')

#   Convertendo a variável em str e carregando dados em um Data Frame. O [0] representa a posição inicial da tabela (a contagem começa em 0 e não em 1).
table_str = str(table)
df = pd.read_html(table_str)[0]

# Caso a página possua mais de uma tabela, existem duas formas de fazer a extração. A primeira seria substituir o find
# por find_all, assim retornaria uma lista com todos os elementos encontrados, e seria possível acessar a tabela verificando
# a posição do vetor. A segunda maneira seria utilizando o argumento 'attrs' do método find, passando um dicionário que
# indicaria os atributos que o elemento obrigatotiamente deveria ter. Exemplo de como ficaria caso fosse extraído as
# colocações dos times na conferência Oeste (Western Conference).

    # table = soup.find(name='table', attrs={'id':'confs_standings_W'})

# Loop com range para iterar estatísticas de 2013 a 2018

def scrape_stats(base_url, year_start, year_end):
    years = range(year_start,year_end+1,1)

    final_df = pd.DataFrame()

    for year in years:
        print('Extraindo ano {}'.format(year))
        req_url = base_url.format(year)
        req = requests.get(req_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find('table', {'id':'totals_stats'})
        df = pd.read_html(str(table))[0]
        df['Year'] = year

        final_df = final_df.append(df)

        return final_df

    url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'

    df = scrape_stats(url, 2013,2018)
























