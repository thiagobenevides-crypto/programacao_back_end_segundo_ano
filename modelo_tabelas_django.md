
Aqui estão relacionadas as tabelas que precisaremos para o nosso projeto em Django


# 1. Modelo: Professor 

Essa tabela armazena informações sobre os professores. 


|Campo           | Tipo                            | Descrição                  | Observações                 |
|---             |---                              |---                         |---                          |
|id              | AutoField                       | Identificador único        |Chave primária               |
|nome            | CharField (max_length =100      | Nome Completo do professor | Obrigatório                 |
|email           | EmailField                      | Email institucional        | Único, para notificações    |
|especialidade   | CharField (max_length=50)       | Área de expertise          | Para análises por disciplina|
|data_contratacao| DateField                       | Data de admissão           | para métricas de retenção   |
|criado_em       | DateTimeField(auto_now_add=True)| Data de criação do registro| Auditoria                   |
|atualizado_em   | DateTimeField(auto_now_add=True)| Data de última atualização | Auditoria                   |


__Relacionamentos__: Um professor pode lecionar múltiplas diciplinas e turmas.


# 2. Modelo: Disciplina

Armazena disciplinas ofertadas na escola.

|Campo        |Tipo                             |Descrição                   |Observações                      |
|---          |---                              |---                         |---                              |
|id           | AutoField                       | Identificador Único        | Chave primária                  |
|nome         | CharField(max_length=100)       | Nome da disciplina         | Obrigátorio, único              |
|codigo       | CharField(max_length=50)        | Código abreviado           | Para relatórios                 |
|carga_horaria| IntegerField                    | Horas totais no semetre/ano| Para cálculos de presença mínima|
|descricao    | TextField|Descrição breve       | Descrição breve            | Opcional, para contexto         |
|criado_em    | DateTimeField(auto_now_add=True)| Data de criação            | Auditoria                       |
|atualizado_em| DateTimeField(auto_now_add=True)|Data de atualização         | Auditoria                       |

__Relacionamento__: ManyToMany com professor (um professor pode ensinar várias disciplinas e Turma


# 3. Modelo Turma

Representa turmas:


|Campo                |Tipo                                                                                       |Descrição                     |Observações                        |
|---                  |---                                                                                        |---                           |---                                |
|id                   | AutoField                                                                                 | Identificador Único          | Chave primária                    |
|nome                 | CharField(max_length=50)                                                                  | Nome da disciplina           | Obrigátorio,                      |
|ano_letivo           | IntegerField                                                                              | Ano escolar                  | Para fins temporais               |
|turno                | CharField(max_length=20,choices = [('Manhã','Manhã'),('Tarde','Tarde'),('Noite','Noite')] | Turno que se encontra a turma| Para análise de padrões diários   |
|capacidade           | IntegerField                                                                              | Número máximo de alunos      | Para métricas de lotação          |
|professor_responsável| ForeignKey(Professor, on_delete=SET_NULL,null=True                                        | Professor coordenador        | Opcional                          |
|criado_em            | DateTimeField(auto_now_add=True)| Data de criação                                         | Auditoria                    | Auditoria                         |                                  |
|atualizado_em        | DateTimeField(auto_now_add=True)|Data de atualização                                      | Auditoria                    | Auditoria                         |


__Relacionamentos__:

 * ManyToMany com Disciplina (uma turma tem várias disciplinas).
*  OneToMany com Aluno (uma turma tem muitos alunos).


# 4. Modelo Aluno







