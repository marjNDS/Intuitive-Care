COPY operadoras_ativas
FROM 'C:/Program Files/PostgreSQL/17/data/import/Relatorio_cadop_utf8.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';
