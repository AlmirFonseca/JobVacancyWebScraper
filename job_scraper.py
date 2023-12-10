import random

import pandas as pd

from enum import Enum
from jobspy import scrape_jobs

SEED = 42
random.seed(SEED)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", 50) 

website_dict = {
    "LinkedIn": "linkedin",
    "Indeed": "indeed",
    "Glassdoor": "glassdoor",
    "ZipRecruiter": "zip_recruiter"
}

job_type_dict = {
    "Tempo integral": "fulltime",
    "Contrato": "contract",
    "Meio período": "parttime",
    "Temporário": "temporary",
    "Estágio": "internship",
    "Por dia": "perdiem",
    "Noturno": "nights",
    "De verão": "summer",
    "Voluntário": "volunteer",
    "Outros": "other"
}

country_dict = {
    "Rio de Janeiro": "rio de janeiro, brazil",
    "São Paulo": "sao paulo, brazil",
    "Brasília": "brasilia, brazil",
    "Belo Horizonte": "belo horizonte, brazil",
    "Curitiba": "curitiba, brazil",
    "Porto Alegre": "porto alegre, brazil",
    "Recife": "recife, brazil",
    "Fortaleza": "fortaleza, brazil",
    "Salvador": "salvador, brazil",
    "Goiânia": "goiania, brazil",
    "Manaus": "manaus, brazil",
    "Belém": "belem, brazil",
    "Guarulhos": "guarulhos, brazil",
    "Campinas": "campinas, brazil",
    "São Luís": "sao luis, brazil",
    "São Gonçalo": "sao goncalo, brazil",
    "Maceió": "maceio, brazil",
    "Duque de Caxias": "duque de caxias, brazil",
    "Natal": "natal, brazil",
    "Teresina": "teresina, brazil",
    "São Bernardo do Campo": "sao bernardo do campo, brazil",
    "Nova Iguaçu": "nova iguacu, brazil",
    # Pode adicionar mais, mas sem a garantia de encontrar vagas para localidades menores
}

keywords_dict = {
    "Cientista de dados": "data scientist",
    "Engenheiro de dados": "data engineer",
    "Analista de dados": "data analyst",
    "Analista de BI": "business intelligence analyst",
    "Matemático": "mathematician",
    "Estatístico": "statistician",
    "Engenheiro de machine learning": "machine learning engineer",
    "Engenheiro eletrônico": "electronic engineer"
    # Pode adicionar mais
}

remote_options_dict = {
    "Trabalho remoto": True,
    "Trabalho não remoto": False
}

jobs = scrape_jobs(
    site_name=random.sample(list(website_dict.values()), 1)[0],
    search_term=random.sample(list(keywords_dict.values()), 1)[0],
    location=random.sample(list(country_dict.values()), 1)[0],
    results_wanted=10, # Tome cuidado com o número de resultados, quanto maior, maior a chance de ser bloqueado (proxy rotativo deve funcionar)
    country_indeed="Brazil",
    is_remote=random.sample(list(remote_options_dict.values()), 1)[0],
    offset=25  # Procure por mais resultados, caso não encontre vagas suficientes

    # Use proxy caso a sua conexão seja bloqueada
    # proxy="http://jobspy:5a4vpWtj8EeJ2hoYzk@ca.smartproxy.com:20001",
    # proxy="socks5://jobspy:5a4vpWtj4EeJ2hoYzk@us.smartproxy.com:10001",
    # proxy="http://jobspy:5a4vpWtj4EeJ2hoYzk@us.smartproxy.com:10001",
    # proxy="https://jobspy:5a4vpWtj4EeJ2hoYzk@us.smartproxy.com:10001",
)

print(jobs.shape)

print(jobs.columns)

print(jobs)