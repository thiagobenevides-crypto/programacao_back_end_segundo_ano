
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
