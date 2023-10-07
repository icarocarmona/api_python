CREATE TABLE IF NOT EXISTS pessoas (
    id CHAR(36) PRIMARY KEY,
    apelido VARCHAR(32) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL,
    stack JSON,
    stack_concat VARCHAR(255)
);

show tables;

SELECT  id, apelido, nome, nascimento , stack  FROM pessoas;

SELECT  id, apelido, nome, nascimento , stack  FROM pessoas
WHERE stack_concat LIKE  '%Py%';