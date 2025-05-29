# BookAPI - Sistema de Gerenciamento de Biblioteca

API REST completa para gerenciamento de biblioteca desenvolvida com FastAPI e Python. Sistema robusto que permite controle total do acervo, operações CRUD para livros e gerenciamento de empréstimos através de uma arquitetura bem estruturada.

## Sobre o Projeto

Este projeto foi desenvolvido com foco em boas práticas de desenvolvimento, organização de código e padrões de API REST. Utiliza FastAPI para criar endpoints eficientes e documentação automática, ideal para estudos e implementações profissionais.

## Funcionalidades

- **Gerenciamento de Livros**: Criar, listar, atualizar e remover livros do acervo
- **Documentação Automática**: Interface Swagger UI e ReDoc integradas
- **Validação de Dados**: Usando Pydantic para garantir integridade
- **Arquitetura Modular**: Separação clara entre rotas, modelos e dados

## Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **FastAPI** - Framework web moderno e performático
- **Pydantic** - Validação e serialização de dados
- **Uvicorn** - Servidor ASGI para desenvolvimento

## Estrutura do Projeto

```
bookapi-fastapi/
├── main.py              # Arquivo principal da aplicação
├── routes/
│   └── livros.py        # Definição das rotas e endpoints
├── db/
│   └── fake_db.py       # Simulação de banco de dados
├── requirements.txt     # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Documentação do projeto
```

## Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. **Clone o repositório**
```bash
git clone https://github.com/yyhago/bookapi-fastapi.git
cd bookapi-fastapi
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
uvicorn main:app --reload
```

5. **Acesse a aplicação**
- **Aplicação**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **Documentação ReDoc**: http://localhost:8000/redoc

## Documentação da API

### Endpoints Disponíveis

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| `POST` | `/livros` | Adicionar novo livro | ❌ |
| `GET` | `/livros` | Listar todos os livros | ❌ |
| `PUT` | `/livros/{id}` | Atualizar informações do livro | ❌ |
| `DELETE` | `/livros/{id}` | Remover livro do acervo | ❌ |

**Legenda**: ✅ Implementado | 🔄 Em desenvolvimento | ❌ Não implementado

### Modelo de Dados

#### Livro
```json
{
  "id": 1,
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano_publicacao": 1899
}
```

## Exemplos de Uso

### Adicionar um novo livro
```bash
curl -X POST "http://localhost:8000/livros" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "O Cortiço",
    "autor": "Aluísio Azevedo",
    "ano_publicacao": 1890
  }'
```

### Listar todos os livros
```bash
curl -X GET "http://localhost:8000/livros"
```

## Desenvolvimento

### Status Atual
- [x] Estrutura base do projeto
- [x] Configuração FastAPI
- [x] Modelo de dados com Pydantic
- [ ] Endpoint POST /livros
- [ ] Simulação de banco de dados
- [ ] Endpoint GET /livros/busca
- [ ] Endpoint PUT /livros/{id}
- [ ] Endpoint DELETE /livros/{id}


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abrir um Pull Request

## Contato

**Yhago Felipe** - Engenharia de Software

- GitHub: [@yyhago](https://github.com/yyhago)
- LinkedIn: [yhagofelipe](https://linkedin.com/in/yhagofelipe)
- Instagram: [@yyhago_](https://instagram.com/yyhago_)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**