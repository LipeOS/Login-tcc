# Projeto Flask com MySQL - Sistema de Autenticação de Usuário

Este é um projeto básico utilizando Flask com integração ao MySQL para gerenciar autenticação de usuário, recuperação de senha e um painel de controle.

## Pré-requisitos

- Python: [Download Python](https://www.python.org/downloads/)
- Flask: Instale usando `pip install Flask`
- MySQL Server: Baixe e instale em [dev.mysql.com](https://dev.mysql.com/downloads/mysql/)
- Flask-SQLAlchemy: Instale usando `pip install Flask-SQLAlchemy`
- PyMySQL: Instale usando `pip install PyMySQL`
- Flask-Mail: Instale usando `pip install Flask-Mail`

## Configuração

1. Clone o repositório ou baixe o código-fonte.
2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o MySQL:
   - Crie um banco de dados chamado `school_db`.
   - Execute o script SQL para criar a tabela de usuários dentro do banco de dados.

    ```sql
    CREATE DATABASE IF NOT EXISTS school_db;

    USE school_db;

    CREATE TABLE user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(150) NOT NULL UNIQUE,
        email VARCHAR(150) NOT NULL UNIQUE,
        senha VARCHAR(150) NOT NULL
    );
    ```

5. Edite as configurações do MySQL no arquivo `app.py` conforme necessário.

6. Configure o Mailtrap para envio de e-mails:
    - Adicione as seguintes configurações no arquivo `app.py`:

    ```python
    app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 587  # Ou 25, 465, ou 2525
    app.config['MAIL_USERNAME'] = '3d37637170985f'
    app.config['MAIL_PASSWORD'] = 'c23a15666abd6a'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = 'seu_email@exemplo.com'  # Substitua pelo seu e-mail de remetente
    ```

## Executando o Projeto

1. No terminal, navegue até o diretório do projeto.
2. Execute o comando:

    ```bash
    python app.py
    ```

3. Abra seu navegador e vá para `http://localhost:5000/` para acessar a aplicação.

## Funcionalidades

- Registro de usuários
- Login de usuários
- Redefinição de senha
- Painel de controle do usuário

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou reportar problemas.

## Autor

Seu Nome

## Licença

Este projeto está licenciado sob a licença MIT.
