# Casos de Uso:

## Sumário:

1. [Caso de Uso 1](#caso-de-uso-1)
2. [Caso de Uso 2](#caso-de-uso-2)
3. [Caso de Uso 3](#caso-de-uso-3)
4. [Caso de Uso 4](#caso-de-uso-4)


---

## Caso de Uso 1:

### Seleção das Competências

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado e logado no sistema.

**Fluxo Principal**:
1. O estudante navega até a seção de seleção de competências;
2. O estudante visualiza e analisa uma lista de competências;
3. O estudante seleciona as competências que deseja;
4. O estudante confirma sua seleção;

**Fluxo Alternativo**:
3. Caso o estudante não encontre uma competência desejada na lista, ele pode inserir uma nova competência através de um campo de texto.

**Pós-condições**: O sistema armazena as competências selecionadas pelo estudante.

---

## Caso de Uso 2:

### Seleção do Nível de Senioridade

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado e logado no sistema.

**Fluxo Principal**:
1. O estudante navega até a seção de seleção de nível de senioridade;
2. O estudante visualiza e analisa uma lista de níveis de senioridade;
3. O estudante seleciona o nível de senioridade que deseja dentre as opções disponíveis (por exemplo: sem experiência, júnior, pleno, sênior, etc.);
4. O estudante confirma sua seleção;

**Pós-condições**: O sistema armazena o nível de senioridade selecionado pelo estudante.

---

## Caso de Uso 3:

### Cadastro no Sistema

**Ator**: Estudante

**Pré-condições**: Não há

**Fluxo Principal**:
1. O estudante entra no sistema;
2. O estudante clica na opção de criar conta;
3. O sistema exibe o formulário de cadastro com os campos de nome completo, nome de usuário, e-mail e senha;
4. O estudante preenche os campos;
5. O sistema valida os campos;
6. O sistema verifica a unicidade do nome de usuário e do e-mail no banco de dados;
7. O sistema cria uma conta para o estudante com os dados fornecidos;
8. O sistema envia um e-mail de confirmação para endereço dado;
9. O sistema redireciona o estudante para página de login.

**Fluxo Alternativo**:
- 5A. Senha invalida:
    1. O sistema informará que a senha é invalida e solicitará ao estudante o preenchimento adequado;
    2. O estudante reinsere uma senha;
    3. Continua com o passo 5 do fluxo principal.

- 5B. Campo vazio:
    1. O sistema informará que há algum campo vazio e solicitará ao estudante o preenchimento adequado;
    2. Continua com o passo 4 do fluxo principal.

- 6A. Endereço de e-mail já registrado:
    1. O sistema informará que o e-mail já está registrado e solicitará ao estudante o preenchimento adequado;
    2. O estudante reinsere um e-mail;
    3. Continua com o passo 5 do fluxo principal.

- 6B. Nome de usuário já registrado:
    1. O sistema informará que o nome de usuário já está registrado e solicitará ao estudante o preenchimento adequado;
    2. O estudante reinsere um nome de usuário;
    3. Continua com o passo 5 do fluxo principal.


**Pós-condições**: O estudante está registrado no sistema e pode fazer o login.

---

## Caso de Uso 4:

### Login no Sistema

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado no sistema

**Fluxo Principal**:
1. O estudante entra no sistema;
2. O estudante clica na opção de login;
3. O sistema exibe o formulário de login com os campos de e-mail e senha;
4. O estudante preenche os campos;
5. O sistema valida os campos;
6. O sistema verifica as credenciais no banco de dados;
7. O sistema redireciona o estudante para a página apropriada após o login bem-sucedido.

**Fluxo Alternativo**:

- 3A. Recuperação de Senha:
    - Se o estudante clica na opção de recuperação de senha:
        1. O sistema exibe o formulário de recuperação de senha com os campos de e-mail e nova senha;
        2. O sistema envia um e-mail ao estudante informando e confirmando a mudança de senha;
        3. O sistema pede para que o e-mail seja confirmado;
        4. Continua com o passo 4 do fluxo principal.


- 5A. Campo vazio:
    1. O sistema informa que há algum campo vazio e solicita ao estudante o preenchimento adequado;
    2. Continua com o passo 4 do fluxo principal.

- 6A. Endereço de e-mail não registrado:
    1. O sistema informa que o e-mail não está associado a uma conta e solicita ao estudante o preenchimento adequado;
    2. O estudante reinsere um e-mail;
    3. Continua com o passo 5 do fluxo principal.

- 6B. Senha incorreta < 3: 
    1. O sistema informa que a senha está incorreta e solicita ao estudante o preenchimento adequado;
    2. O estudante reinsere uma senha;
    3. Continua com o passo 5 do fluxo principal.

- 6C. Senha incorreta >= 3: 
    1. O sistema informa que a senha está incorreta e informa que o acesso a conta foi bloqueado temporariamente;
    2. O sistema bloqueia o acesso da conta;
    3. O sistema envia um e-mail informando a tentativa de acesso.
    4. Caso de uso é encerrado.



**Pós-condições**: O estudante está autenticado a pode acessar as funcionalidades do sistema. 