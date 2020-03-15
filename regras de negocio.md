
## agenda
OK:

        ### admin:
        #### regras de negocio

        - "Nao deve ser possivel 
            criar mais de uma agenda
            para um medico em um mesmo dia"
        - "Não deve ser possível 
            criar uma agenda para um médico
            em um dia passado"

    
    
### api :   

OK:

    #### especialidade :   

    ### filtro
    - "nome da especialidade"
        

    #### medico :
    ### filtros :
    - "Identificador de uma ou 
                mais especialidades;"
    - Nome do médico (termo 
            de pesquisa).
        
#### consulta :

OK.

    regras de negocio:
    - A listagem não deve exibir 
        consultas para dia e horário passados;
    - Os itens da listagem 
                devem vir ordenados por
                ordem crescente do dia e 
                horário da consulta
#### agenda:

OK.

    filtros:
    - Identificador de um
                    ou mais medicos
    - Identificador de uma 
                    ou mais especialidades
    - Intervalo de data


Regras de negócio
* As agendas devem vir ordenadas por ordem crescente de data
* Agendas para datas passadas ou que todos os seus horários já foram preenchidos devem ser excluídas da listagem
* Horários dentro de uma agenda que já passaram ou que foram preenchidos devem ser excluídos da listagem

consulta:
marcar consulta:

```
POST /consultas/
{
  "agenda_id": 1,
  "horario": "14:15"
}
```
#### Retorno

```json
{
  "id": 2,
  "dia": "2020-03-01",
  "horario": "09:00",
  "data_agendamento": "2020-02-01T10:45:0-03:00",
  "medico": {
    "id": 1,
    "crm": 3711,
    "nome": "Drauzio Varella",
    "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
  }
}
```
Regras de negócio
* A data em que o agendamento foi feito deve ser salva ao se marcar uma consulta
* Não deve ser possível marcar uma consulta para um dia e horário passados
* Não deve ser possível marcar uma consulta se o usuário já possui uma consulta marcada no mesmo dia e horário
* Não deve ser possível marcar uma consulta se o dia e horário já foram preenchidos


### Desmarcar consulta
Desmarca uma consulta marcada pelo usuário



#### Regras de negócio
* Não deve ser possível desmarcar uma consulta que não foi marcada pelo usuário logado
* Não deve ser possível desmarcar uma consulta que nunca foi marcada (identificador inexistente)
* Não deve ser possível desmarcar uma consulta que já aconteceu
