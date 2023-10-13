CREATE TABLE IF NOT EXISTS pessoas (
    id CHAR(36) PRIMARY KEY,
    apelido VARCHAR(32) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL,
    stack JSON,
    stack_concat VARCHAR(255)
);

-- @block 
show tables;

-- @block
SELECT  id, apelido, nome, nascimento , stack  FROM pessoas;

-- @block
SELECT  id, apelido, nome, nascimento , stack  FROM pessoas
WHERE stack_concat LIKE  '%Py%';

-- @block
INSERT INTO pessoas (
    id,
    apelido,
    nome,
    nascimento,
    stack,
    stack_concat
  )
VALUES (
    'id:char',
    'apelido:varchar',
    'nome:varchar',
    'nascimento:date',
    'stack:longtext',
    'stack_concat:varchar'
  );