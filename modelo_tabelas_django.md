
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


Armazena aunos. 


|Campo          |Tipo                                  | Descrição                 | Observações            |
|---            |---                                   |---                        |---                     |
|id             | AutoField                            | Identificador único       | Chave Primária         |
|nome           | CharField(max_length=100)            | Nome Completo do Aluno    | Obrigátorio            |
|matrícula      | CharField(max_length=20)             | Número da matrícula       | Único                  |
|data_nascimento| DateField                            | Data de nascimento        | Para idade e demografia|
|turma          | ForeignKey(Turma, on_delete=CASCADE) | Turma Associada           | Obrigatório            |
|email          | EmailField                           | Email do aluno/responsável| Opcional               |
|criado_em      | DateTimeField(auto_now_add=True)     | Data de Criação           | Auditoria              |
|atualizado_em  | DateTimeField(auto_now_add=True)     | Data de Atualização       | Auditoria              |


# 5. Modelo: CalendarioEscolar 
   Para calcular dias letivos. Essa tabela armazena datas letivas, feriados etc. Permite queries para contar dias totais por turma/disciplina

   | Campo | Tipo | Descrição | Observações |
   |-------|------|-----------|-------------|
   | id | AutoField | Identificador único | Chave primária |
   | data | DateField | Data do dia letivo | Único por turma/disciplina se necessário |
   | tipo | CharField(max_length=20, choices=[('Letivo', 'Letivo'), ('Feriado', 'Feriado'), ('Recesso', 'Recesso')]) | Tipo de dia | Default: 'Letivo' |
   | turma | ForeignKey(Turma, on_delete=CASCADE, null=True) | Turma associada (se calendário variar) | Opcional |
   | disciplina | ForeignKey(Disciplina, on_delete=SET_NULL, null=True) | Disciplina associada (para horários específicos) | Opcional |
   | descricao | TextField | Motivo (ex.: Feriado nacional) | Opcional |
   | criado_em | DateTimeField(auto_now_add=True) | Data de criação | Auditoria |

   

# 6. **Modelo: Faltas 
   Tabela central para registrar faltas. 

   | Campo | Tipo | Descrição | Observações |
   |-------|------|-----------|-------------|
   | id | AutoField | Identificador único | Chave primária |
   | aluno | ForeignKey(Aluno, on_delete=CASCADE) | Aluno associado | Obrigatório |
   | disciplina | ForeignKey(Disciplina, on_delete=CASCADE) | Disciplina da falta | Obrigatório |
   | data | DateField | Data da aula | Obrigatório |
   | status | CharField(max_length=20, choices=[('Presente', 'Presente'), ('Falta', 'Falta'), ('Atraso', 'Atraso'), ('Justificada', 'Justificada')]) | Status de presença | Default: 'Presente' |
   | motivo | CharField(max_length=50, choices=[('Saúde', 'Saúde'), ('Transporte', 'Transporte'), ('Familiar', 'Familiar'), ('Outros', 'Outros')]) | Motivo da falta | Opcional, para categorização |
   | professor | ForeignKey(Professor, on_delete=SET_NULL, null=True) | Professor que registrou | Para auditoria |
   | criado_em | DateTimeField(auto_now_add=True) | Data de criação | Auditoria |
   | atualizado_em | DateTimeField(auto_now=True) | Data de atualização | Auditoria |

   **Cálculos**:
   - Dias letivos totais: Contar entradas no CalendarioEscolar.
   - Faltas do aluno: `Faltas.objects.filter(aluno=some_aluno, status='Falta').count()`.
   - Presença mínima: (dias_letivos - faltas) / dias_letivos >= 0.75 (implemente em views ou signals do Django).

#### Relacionamentos Gerais
- **Professor-Disciplina**: ManyToManyField em Professor (um prof. ensina várias disciplinas).
- **Turma-Disciplina**: ManyToManyField em Turma (uma turma tem várias disciplinas).
- **Turma-Aluno**: ForeignKey em Aluno apontando para Turma.
- **Faltas**: ForeignKeys para Aluno, Disciplina e Professor.





Essa estrutura é robusta, escalável e pronta para insights. Se precisar de código Django específico ou ajustes, me avise!




