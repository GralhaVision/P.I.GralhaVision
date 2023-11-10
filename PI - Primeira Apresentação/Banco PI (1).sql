CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL
);
CREATE TABLE estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    descricao TEXT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    data_entrada DATE NOT NULL,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE fornecedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_fornecedor VARCHAR(100) NOT NULL,
    contato VARCHAR(100),
    endereco VARCHAR(200)
);
CREATE TABLE ordens_servico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    descricao_problema TEXT,
    status ENUM('Aberta', 'Em Andamento', 'Concluída') NOT NULL DEFAULT 'Aberta',
    data_abertura DATETIME NOT NULL,
    data_conclusao DATETIME
);
CREATE TABLE suporte (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao_problema TEXT,
    status ENUM('Aberto', 'Em Andamento', 'Fechado') NOT NULL DEFAULT 'Aberto',
    data_abertura DATETIME NOT NULL,
    data_fechamento DATETIME
);
