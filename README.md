# 🎓 MentorAPI - Sistema de Mentores

Este repositório contém o **Mentores**, desenvolvido como parte do **Sistema de Gerenciamento de Monitorias** para a disciplina de **Engenharia de Software**.

A API tem como função central gerenciar o cadastro de mentores, permitir o agendamento de sessões de mentoria, e expor endpoints REST para integração com os demais módulos do sistema (como autenticação, CRUD central e painel do administrador).

---

## 🧩 Visão Geral do Sistema

O sistema completo de monitorias foi dividido entre três grupos:

- 🧠 **Mentores** (este repositório)
- 🗂️ Administrador/Suporte
- 💻 Mentorados

A API de Mentores funciona de forma independente, mas expõe seus dados via endpoints REST para ser consumida por outros módulos do sistema.

---

## 🚀 Funcionalidades da API de Mentores

- ✅ Cadastro de mentores
- ✅ Listagem de mentores
- ✅ Agendamento de sessões de mentoria
- ✅ Listagem de agendamentos
- ✅ Atualização do status do agendamento (aceito/rejeitado)

---

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)

---

## 📂 Como executar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/mentor_service.git
cd mentor_service
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

5. Acesse a docmentação automática:

```bash
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
```

## 👨‍💻 Desenvolvedores Responsáveis

Este módulo foi desenvolvido por:

- Anthony Bachiega
- Gabriel Chaves
- Pedro Polegato
- Rodrigo Rameh

Como parte do projeto da disciplina **Engenharia de Software**.
