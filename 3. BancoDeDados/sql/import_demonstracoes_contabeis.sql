COPY demonstracoes_contabeis
FROM 'C:/Program Files/PostgreSQL/17/data/import/demonstracoes_contabeis_unificado.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';