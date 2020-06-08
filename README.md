#  API Medicar (v0.1)

API para Estacionamento
### Sumário
+ [Pré Requisitos](#pré-requisitos)
+ [Comandos da aplicação](#comandos-da-aplicação)
+ [Desenvolvido com](#desenvolvido-com)
+ [Desenvolvido por](#desenvolvido-por)
 
### Pré Requisitos
+ [python](https://docs.docker.com/compose/)
+ [Django](https://docs.docker.com/compose/)
+ [Django rest](https://www.django-rest-framework.org/)

### Comandos da aplicação
- Apartir da rais Primeiro comando:
```
# docker-compose up 
``` 

- Aplicação localhost:3001
- Backend localhost:8000
- Só será possivel entrar na api se você for superuser ou possuir um token válido.

**Rotas**

|Verb  |URI Pattern              
:----:|-------------------------|
| POST |consultas/             
| GET  |consultas/  
| GET  |medicos/          
| GET  |especialidades/               
| GET  |agendas/          
| GET  |usuario/          


### Desenvolvido com
+ [Django](https://docs.djangoproject.com/en/3.0/) - Framework Django
+ [Django Rest Framework](https://www.django-rest-framework.org/) - Django Rest Framework

### Desenvolvido por
+ **Amaro Cesar** 