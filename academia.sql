DROP DATABASE IF EXISTS academia;
CREATE DATABASE academia;


CREATE SEQUENCE admin_id_seq INCREMENT 1;
CREATE SEQUENCE aluno_id_seq INCREMENT 1;
CREATE SEQUENCE professor_id_seq INCREMENT 1;
CREATE SEQUENCE matricula_id_seq INCREMENT 1;
CREATE SEQUENCE treino_id_seq INCREMENT 1;


CREATE TABLE admin (
  id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('admin_id_seq'::regclass),
  nome text NOT NULL,
  email text NOT NULL,
  usuario text NOT NULL,
  senha text NOT NULL
);


CREATE TABLE aluno (
  id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('aluno_id_seq'::regclass),
  nome text NOT NULL,
  email text NOT NULL,
  nascimento text NOT NULL,
  altura  FLOAT NOT NULL,
  peso FLOAT NOT NULL
);

CREATE TABLE professor (
  id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('professor_id_seq'::regclass),
  nome text NOT NULL,
  email text NOT NULL,
  usuario text NOT NULL,
  senha text NOT NULL,
  nascimento text NOT NULL,
  atuacao text[]

);

CREATE TABLE matricula (
  id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('matricula_id_seq'::regclass),
  esporte text NOT NULL,
  professor_id INTEGER,
  aluno_id INTEGER NOT NULL

);

CREATE TABLE treino (
  id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('treino_id_seq'::regclass),
  professor_id INTEGER NOT NULL,
  aluno_id INTEGER NOT NULL,
  descricao text
);



INSERT INTO admin (nome, email, usuario, senha) VALUES ('admin','admin','admin','admin')