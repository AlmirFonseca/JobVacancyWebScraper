# Casos de Uso:

## Sumário:

1. [Caso de Uso 1](#caso-de-uso-1)
2. [Caso de Uso 2](#caso-de-uso-2)
3. [Caso de Uso 3](#caso-de-uso-3)
4. [Caso de Uso 4](#caso-de-uso-4)
5. [Caso de Uso 5](#caso-de-uso-5)
6. [Caso de Uso 6](#caso-de-uso-6)
7. [Caso de Uso 7](#caso-de-uso-7)
8. [Caso de Uso 8](#caso-de-uso-8)
9. [Caso de Uso 9](#caso-de-uso-9)
10. [Caso de Uso 10](#caso-de-uso-10)
11. [Caso de Uso 11](#caso-de-uso-11)

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

---

## Caso de Uso 5:

### Inserção de currículo

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado e logado no sistema.

**Fluxo Principal**:

1. O estudante navega até a seção de seleção de currículo;
2. O estudante clica na opção de fazer upload de currículo;
3. O estudante visualiza os arquivos presentes em seu dispositivo para seleção;
4. O estudante confirma o upload do currículo;

**Fluxo Alternativo**:

2. Caso o estudante já tenha feito upload de algum documento, deve visualizar o documento inserido e ter a opção de substituir esse documento.

**Pós-condições**: O sistema armazena o currículo enviado pelo estudante.

---

## Caso de Uso 6:

### Registro de email para envio de currículos

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado e logado no sistema.

**Fluxo Principal**:

1. O estudante navega até a seção de registro de email;
2. O estudante clica na opção de inserir novo email;
3. O estudante insere endereço e senha do email;

**Fluxo Alternativo**:
- Email já cadastrado:
1. O estudante navega até a seção de registro de email;
2. O estudante clica na opção de alterar email;
3. O estudante insere endereço e senha do email;

**Pós-condições**: O sistema guarda localmente o email e senha registrados.

--- 

## Caso de Uso 7:

### Envio de email

**Ator**: Estudante

**Pré-condições**: O estudante deve ter realizado uma pesquisa de vagas, ter vagas identificadas e ter email de envio já cadastrado.

**Fluxo Principal**:

1. O estudante navega até a seção de lista de vagas;
2. O estudante visualiza as vagas que foram encontradas pra ele;
3. O estudante deve conseguir selecionar as vagas que deseja enviar o email;
4. O estudante deve conseguir inserie um texto personalizado para ir no corpo do email;
5. O estudante confirma no fim e deve aguardar um carregamento do envio de cada email;
6. O estudante deve visualizar a confirmação de emails enviados;

**Fluxo Alternativo**:

2. Caso o estudante não tenha realizado a pesquisa ainda, deve receber a informação que deve receber a pesquisa de vagas antes.
3. Caso o estudante não tenha registrado o email de envio, ele deve ser direcionado até a seção de registro de email.

**Pós-condições**: O sistema armazena as vagas que foram enviadas email pelo usuário.

--- 

## Caso de Uso 8:

### Notificação de Novas Vagas

**Ator**: Estudante

**Pré-condições**: O estudante deve estar logado e ter feito a seleção de competências e de nível de senioridade.

**Fluxo Principal**:

1. O usuário acessa a seção de configurações de notificações de novas vagas no sistema.
2. O sistema exibe opções para configurar a frequência das notificações, como diária, semanal ou mensal.
3. O usuário seleciona a frequência desejada para receber as notificações.
4. O sistema envia regularmente e-mails ao usuário com resumos das novas vagas que correspondem às suas preferências e critérios de pesquisa.

**Fluxo Alternativo**:

1. Se o usuário desejar ajustar ou alterar a frequência das notificações após a configuração inicial, ele pode acessar as configurações de notificação e fazer as alterações necessárias.

**Pós-condições**: O usário recebe regularmente e-mails contendo resumos das novas vagas que correspodem às suas preferências e critérios de pesquisa, mantendoó atualizado sobre as oportunidades mais recentes no mercado de trabalho.

---

## Caso de Uso 9

### Visualização do Dashboard de Vagas

**Ator**: Estudante

**Pré-condições**: O estudante deve estar logado e ter feito a seleção de competências e de nível de senioridade.

**Fluxo Principal**:
1. O estudante navega até a seção de dashboard de vagas.
2. O dashboard exibe uma visão geral das vagas de emprego/estágio compatíveis com as seleções de competência e nível de senioridade feitas pelo estudante.

**Fluxo Alternativo**:
1. Se não houver vagas correpondentes as seleções do usuário, o sisteme exibe uma mensagem indicando a ausência de resultados.

**Pós-condições**: O usuário obtém uma visão abrangente e organizada de emprego/estágio disponíveis.

---

## Caso de Uso 10

### Acompanhamento de Candidaturas

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado e logado no sistema.

**Fluxo Principal**:
1. O estudante navega até a seção de acompanhamento de candidaturas.
2. O sistema exibe uma lista de vagas para as quais o estudante se candidatou.
3. O estudante pode visualizar o status de cada candidatura, como por exemplo, se o email enviado foi respondido.

**Fluxo Alternativo**:
1. Se o estudante não tiver se candidatado a nenhuma vaga, o sistema exibe uma mensagem indicando a ausência de resultados.

**Pós-condições**: O estudante pode acompanhar o status de suas candidaturas.

---

## Caso de Uso 11

### Análise de Tendências

**Ator**: Estudante

**Pré-condições**: O estudante deve estar registrado e logado no sistema.

**Fluxo Principal**:
1. O estudante navega até a seção de análise de tendências.
2. O sistema exibe um painel contendo informações sobre as tendências do mercado de trabalho, como por exemplo, as competências mais demandadas.

**Pós-condições**: O estudante pode obter informações relevantes sobre o mercado de trabalho.