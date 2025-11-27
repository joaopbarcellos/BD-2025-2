INSERT INTO PAIS (nome) VALUES
('Brasil'),
('Argentina'),
('Chile'),
('Estados Unidos'),
('Portugal');


INSERT INTO ESTADO (nome, FK_PAIS_id_pais) VALUES
('São Paulo', 1),
('Rio de Janeiro', 1),
('Buenos Aires', 2),
('Lisboa', 5),
('Califórnia', 4);


INSERT INTO CIDADE (nome, FK_ESTADO_id_estado) VALUES
('Campinas', 1),
('Rio de Janeiro', 2),
('Buenos Aires', 3),
('Lisboa', 4),
('Los Angeles', 5);


INSERT INTO TIPO_LOGRADOURO (nome) VALUES
('Rua'),
('Avenida'),
('Travessa'),
('Alameda'),
('Praça');


INSERT INTO ENDERECO (descricao, FK_CIDADE_id_cidade, FK_TIPO_LOGRADOURO_id_tipo_logradouro) VALUES
('Rua das Flores, 123', 1, 1),
('Avenida Central, 50', 2, 2),
('Travessa da Luz, 22', 3, 3),
('Alameda das Oliveiras, 10', 4, 4),
('Praça da Liberdade, 5', 5, 5);


INSERT INTO ACADEMIA (nome, login, senha, FK_ENDERECO_id_endereco) VALUES
('Academia Corpo Forte', 'corpoforte', 'senha123', 1),
('FitMax', 'fitmax', '123456', 2),
('PowerGym', 'powergym', 'abc123', 3),
('Vida Ativa', 'vidaativa', 'pass123', 4),
('Top Shape', 'topshape', 'senha456', 5);


INSERT INTO PROFESSOR (nome, login, senha, FK_ACADEMIA_id_academia) VALUES
('Carlos Silva', 'carlos', 'senha1', 1),
('Fernanda Lima', 'fernanda', 'senha2', 2),
('João Souza', 'joao', 'senha3', 3),
('Mariana Alves', 'mariana', 'senha4', 4),
('Ricardo Gomes', 'ricardo', 'senha5', 5);


INSERT INTO ALUNO (nome, data_nascimento, login, senha, data_inicio_academia, FK_PROFESSOR_id_professor, FK_ACADEMIA_id_academia) VALUES
('Ana Paula', '1995-03-10', 'ana', '123', '2024-01-10', 1, 1),
('Bruno Costa', '1990-07-22', 'bruno', '123', '2024-02-15', 2, 2),
('Clara Souza', '1998-09-12', 'clara', '123', '2024-03-01', 3, 3),
('Diego Santos', '1992-05-18', 'diego', '123', '2024-04-05', 4, 4),
('Eduarda Rocha', '1997-11-30', 'eduarda', '123', '2024-05-20', 5, 5);


INSERT INTO EXERCICIO (nome, FK_ACADEMIA_id_academia) VALUES
('Supino Reto', 1),
('Agachamento Livre', 2),
('Remada Curvada', 3),
('Desenvolvimento de Ombros', 4),
('Rosca Direta', 5);


INSERT INTO EXERCICIO_ACADEMIA (FK_ACADEMIA_id_academia, FK_EXERCICIO_id_exercicio) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);


INSERT INTO TREINO (nome) VALUES
('Treino A - Peito e Tríceps'),
('Treino B - Costas e Bíceps'),
('Treino C - Pernas'),
('Treino D - Ombros e Trapézio'),
('Treino E - Abdômen');


INSERT INTO TREINO_EXERCICIO (descanso, repeticoes, series, FK_TREINO_id_treino, FK_EXERCICIO_ACADEMIA_id_exercicio_academia) VALUES
(60, 12, 3, 1, 1),
(90, 10, 4, 2, 2),
(120, 15, 3, 3, 3),
(60, 12, 3, 4, 4),
(45, 20, 4, 5, 5);


INSERT INTO MEDIDA (pescoco, cintura, peso, quadril, altura, antebraco, braco, peitoral, bf_perc, coxa, panturrilha, ombro) VALUES
(35, 80, 70.5, 95, 175, 28, 35, 95, 15.2, 55, 36, 110),
(37, 82, 78.0, 98, 180, 29, 36, 100, 14.0, 57, 37, 112),
(33, 75, 65.2, 90, 165, 26, 33, 85, 17.5, 50, 35, 105),
(38, 90, 85.3, 105, 185, 30, 38, 110, 12.3, 60, 39, 118),
(34, 78, 68.9, 92, 170, 27, 34, 88, 16.1, 53, 36, 108);


INSERT INTO PLANILHA (data_inicio, data_fim, FK_PROFESSOR_id_professor, FK_MEDIDA_id_medida, FK_ALUNO_id_aluno) VALUES
('2024-01-01', '2024-03-01', 1, 1, 1),
('2024-02-01', '2024-04-01', 2, 2, 2),
('2024-03-01', '2024-05-01', 3, 3, 3),
('2024-04-01', '2024-06-01', 4, 4, 4),
('2024-05-01', '2024-07-01', 5, 5, 5);


INSERT INTO PLANILHA_TREINO (FK_PLANILHA_id_planilha, FK_TREINO_id_treino) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);


INSERT INTO TREINAMENTO (data_inicio, data_fim, FK_TREINO_id_treino, FK_ALUNO_id_aluno) VALUES
('2024-03-01', '2024-03-31', 1, 1),
('2024-04-01', '2024-04-30', 2, 2),
('2024-05-01', '2024-05-31', 3, 3),
('2024-06-01', '2024-06-30', 4, 4),
('2024-07-01', '2024-07-31', 5, 5);


INSERT INTO TREINAMENTO_EXERCICIO (repeticoes, carga, FK_TREINO_id_treino, FK_EXERCICIO_ACADEMIA_id_exercicio_academia) VALUES
(12, 50, 1, 1),
(10, 80, 2, 2),
(15, 40, 3, 3),
(12, 45, 4, 4),
(20, 30, 5, 5);
