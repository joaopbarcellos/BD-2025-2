DROP TABLE IF EXISTS TREINAMENTO_EXERCICIO, TREINAMENTO, PLANILHA_TREINO, PLANILHA, MEDIDA,
    TREINO_EXERCICIO, EXERCICIO_ACADEMIA, EXERCICIO, ALUNO, PROFESSOR,
    ACADEMIA, ENDERECO, TIPO_LOGRADOURO, CIDADE, ESTADO, PAIS CASCADE;

CREATE TABLE PAIS (
    id_pais SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);


CREATE TABLE ESTADO (
    id_estado SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    FK_PAIS_id_pais INTEGER NOT NULL,
    CONSTRAINT fk_estado_pais FOREIGN KEY (FK_PAIS_id_pais) REFERENCES PAIS (id_pais)
);


CREATE TABLE CIDADE (
    id_cidade SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    FK_ESTADO_id_estado INTEGER NOT NULL,
    CONSTRAINT fk_cidade_estado FOREIGN KEY (FK_ESTADO_id_estado) REFERENCES ESTADO (id_estado)
);


CREATE TABLE TIPO_LOGRADOURO (
    id_tipo_logradouro SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);


CREATE TABLE ENDERECO (
    id_endereco SERIAL PRIMARY KEY,
    descricao VARCHAR(100),
    FK_CIDADE_id_cidade INTEGER NOT NULL,
    FK_TIPO_LOGRADOURO_id_tipo_logradouro INTEGER NOT NULL,
    CONSTRAINT fk_endereco_cidade FOREIGN KEY (FK_CIDADE_id_cidade) REFERENCES CIDADE (id_cidade),
    CONSTRAINT fk_endereco_tipo_logradouro FOREIGN KEY (
        FK_TIPO_LOGRADOURO_id_tipo_logradouro
    ) REFERENCES TIPO_LOGRADOURO (id_tipo_logradouro)
);


CREATE TABLE ACADEMIA (
    id_academia SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    FK_ENDERECO_id_endereco INTEGER,
    CONSTRAINT fk_academia_endereco FOREIGN KEY (FK_ENDERECO_id_endereco) REFERENCES ENDERECO (id_endereco)
);


CREATE TABLE PROFESSOR (
    id_professor SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    FK_ACADEMIA_id_academia INTEGER NOT NULL,
    CONSTRAINT fk_professor_academia FOREIGN KEY (FK_ACADEMIA_id_academia) REFERENCES ACADEMIA (id_academia)
);


CREATE TABLE ALUNO (
    id_aluno SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    data_nascimento DATE NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    data_inicio_academia DATE,
    FK_PROFESSOR_id_professor INTEGER,
    FK_ACADEMIA_id_academia INTEGER NOT NULL,
    CONSTRAINT fk_aluno_professor FOREIGN KEY (FK_PROFESSOR_id_professor) REFERENCES PROFESSOR (id_professor),
    CONSTRAINT fk_aluno_academia FOREIGN KEY (FK_ACADEMIA_id_academia) REFERENCES ACADEMIA (id_academia)
);


CREATE TABLE EXERCICIO (
    id_exercicio SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    FK_ACADEMIA_id_academia INTEGER NOT NULL,
    CONSTRAINT fk_exercicio_academia FOREIGN KEY (FK_ACADEMIA_id_academia) REFERENCES ACADEMIA (id_academia)
);


CREATE TABLE EXERCICIO_ACADEMIA (
    id_exercicio_academia SERIAL PRIMARY KEY,
    FK_ACADEMIA_id_academia INTEGER NOT NULL,
    FK_EXERCICIO_id_exercicio INTEGER NOT NULL,
    CONSTRAINT fk_exercicio_academia_academia FOREIGN KEY (FK_ACADEMIA_id_academia) REFERENCES ACADEMIA (id_academia),
    CONSTRAINT fk_exercicio_academia_exercicio FOREIGN KEY (FK_EXERCICIO_id_exercicio) REFERENCES EXERCICIO (id_exercicio)
);


CREATE TABLE TREINO (
    id_treino SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);


CREATE TABLE TREINO_EXERCICIO (
    id_treino_exercicio SERIAL PRIMARY KEY,
    descanso INTEGER,
    repeticoes INTEGER,
    series INTEGER,
    FK_TREINO_id_treino INTEGER NOT NULL,
    FK_EXERCICIO_ACADEMIA_id_exercicio_academia INTEGER NOT NULL,
    CONSTRAINT fk_treino_exercicio_treino FOREIGN KEY (FK_TREINO_id_treino) REFERENCES TREINO (id_treino),
    CONSTRAINT fk_treino_exercicio_exercicio_academia FOREIGN KEY (
        FK_EXERCICIO_ACADEMIA_id_exercicio_academia
    ) REFERENCES EXERCICIO_ACADEMIA (id_exercicio_academia)
);


CREATE TABLE MEDIDA (
    id_medida SERIAL PRIMARY KEY,
    pescoco INTEGER,
    cintura INTEGER,
    peso FLOAT,
    quadril INTEGER,
    altura INTEGER,
    antebraco INTEGER,
    braco INTEGER,
    peitoral INTEGER,
    bf_perc FLOAT,
    coxa INTEGER,
    panturrilha INTEGER,
    ombro INTEGER
);


CREATE TABLE PLANILHA (
    id_planilha SERIAL PRIMARY KEY,
    data_inicio TIMESTAMP,
    data_fim TIMESTAMP,
    FK_PROFESSOR_id_professor INTEGER NOT NULL,
    FK_MEDIDA_id_medida INTEGER NOT NULL,
    FK_ALUNO_id_aluno INTEGER NOT NULL,
    CONSTRAINT fk_planilha_professor FOREIGN KEY (FK_PROFESSOR_id_professor) REFERENCES PROFESSOR (id_professor),
    CONSTRAINT fk_planilha_medida FOREIGN KEY (FK_MEDIDA_id_medida) REFERENCES MEDIDA (id_medida),
    CONSTRAINT fk_planilha_aluno FOREIGN KEY (FK_ALUNO_id_aluno) REFERENCES ALUNO (id_aluno)
);


CREATE TABLE PLANILHA_TREINO (
    id_planilha_treino SERIAL PRIMARY KEY,
    FK_PLANILHA_id_planilha INTEGER NOT NULL,
    FK_TREINO_id_treino INTEGER NOT NULL,
    CONSTRAINT fk_planilha_treino_planilha FOREIGN KEY (FK_PLANILHA_id_planilha) REFERENCES PLANILHA (id_planilha),
    CONSTRAINT fk_planilha_treino_treino FOREIGN KEY (FK_TREINO_id_treino) REFERENCES TREINO (id_treino)
);


CREATE TABLE TREINAMENTO (
    id_treinamento SERIAL PRIMARY KEY,
    data_inicio TIMESTAMP,
    data_fim TIMESTAMP,
    FK_TREINO_id_treino INTEGER NOT NULL,
    FK_ALUNO_id_aluno INTEGER NOT NULL,
    CONSTRAINT fk_treinamento_treino FOREIGN KEY (FK_TREINO_id_treino) REFERENCES TREINO (id_treino),
    CONSTRAINT fk_treinamento_aluno FOREIGN KEY (FK_ALUNO_id_aluno) REFERENCES ALUNO (id_aluno)
);


CREATE TABLE TREINAMENTO_EXERCICIO (
    id_treinamento_exercicio SERIAL PRIMARY KEY,
    repeticoes INTEGER,
    carga INTEGER,
    FK_TREINO_id_treino INTEGER NOT NULL,
    FK_EXERCICIO_ACADEMIA_id_exercicio_academia INTEGER NOT NULL,
    CONSTRAINT fk_treinamento_exercicio_treino FOREIGN KEY (FK_TREINO_id_treino) REFERENCES TREINO (id_treino),
    CONSTRAINT fk_treinamento_exercicio_exercicio_academia FOREIGN KEY (
        FK_EXERCICIO_ACADEMIA_id_exercicio_academia
    ) REFERENCES EXERCICIO_ACADEMIA (id_exercicio_academia)
);
