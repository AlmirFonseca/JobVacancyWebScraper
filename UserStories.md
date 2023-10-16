# Histórias de Usuário

## Sumário:

1. [História de Usuário 1](#história-de-usuário-1)
2. [História de Usuário 2](#história-de-usuário-2)
3. [História de Usuário 3](#história-de-usuário-3)
4. [História de Usuário 4](#história-de-usuário-4)
5. [História de Usuário 5](#história-de-usuário-5)

---

## História de Usuário 1:

### Seleção das Competências

**Como** um estudante em busca de estágio,

**Quero** selecionar e inserir minhas competências (por exemplo, Python, Javascript, Postgresql, C++, etc.),

**Para** que o sistema me mostre vagas que se alinhem com meu perfil.

### Critérios de Aceitação

- O usuário deve ser capaz de selecionar suas competências através de uma lista de _checkboxes_ ou de uma _dropdown list_;
- O usuário deve ser capaz de inserir outras competências não listadas através de um campo de texto.
- Após a seleção das competências, o usuário deve ser capaz de confirmar sua seleção através de um botão. Essas competências devem ser armazenadas como parte do perfil do usuário.

### Definição de Pronto

- O sistema deve ser capaz de armazenar as competências selecionadas pelo usuário;

---

## História de Usuário 2:

### Seleção do Nível de Senioridade

**Como** um estudante em busca de estágio com alguma experiência prévia,

**Quero** selecionar meu nível de senioridade (por exemplo, júnior, pleno, sênior, etc.),

**Para** que o sistema filtre os resultados que se alinhem com meu nível de experiência.

### Critérios de Aceitação

- O usuário deve ser capaz de selecionar seu nível de senioridade através de uma lista de _radio buttons_;
- Dentre as opções, deve haver uma opção para usuários sem experiência prévia;
- Após a seleção do nível de senioridade, o usuário deve ser capaz de confirmar sua seleção através de um botão. Esse nível de senioridade deve ser armazenado como parte do perfil do usuário.

### Definição de Pronto

- O sistema deve ser capaz de armazenar o nível de senioridade selecionado pelo usuário;

---

## História de Usuário 3:

### Cadastro no Sistema

**Como** um estudante não cadastrado no sistema,

**Quero** fazer o cadastro, inserindo minhas informações,

**Para** que o sistema crie minha conta de usuário e eu possa utilizar suas funcionalidades.

### Critérios de Aceitação

- O usuário deve ser capaz de preencher todos os campos;
- O usuário deve inserir uma senha segura (contendo letras maiúsculas e minúsculas, números e carcteres especiais e possuindo pelo menos 8 caracteres);
- O usuário cadastrado não deve se cadastrar novamente (o endereço de e-mail ou o nome de usuário inserido não podem ser utilizado por outro usuário no sistema);
- Os campos devem ser preencidos e validados;
- Após preencher seus dados, o usuário deve ser capaz de finalizar seu cadastro através de um botão.

### Definição de Pronto

- O sistema deve ser capaz de armazenar os dados de cadastro fornecidos pelo usuário;

---

## História de Usuário 4:

### Login no Sistema

**Como** um estudante querendo acessar o sistema,

**Quero** fazer o login,

**Para** que possa utilizar as funcionalidades do sistema.

### Critérios de Aceitação

- O usuário deve ser capaz de inserir suas credenciais e apertar um botão para realizar o login;
- Os campos devem estar preenchidos antes que seja possivel apertar o botão do login;
- O usuário já deve ter um cadastro registrado no sistema;
- O usuário deve ter uma opção para recuperar a senha, apertando um botão que o redicionará a uma página, que o envia um e-mail com instruções para redefinir a senha.

### Definição de Pronto

- O sistema deve ser capaz de autenticar o usuário e o redirecionar para página apropriada caso as credenciais estejam corretas ou informar o erro no login caso contrário. Deve manter a sessão do usuário ativa, após um login bem-sucedido.

---

## História de Usuário 5:

### Inserção de Currículo

**Como** um estudante querendo inserir o documento de currículo,

**Quero** fazer upload do currículo,

**Para** que possa enviar por email para as vagas.

### Critérios de Aceitação

- O usuário deve ser capaz de visualizar se já possui um documento inserido;
- O documento deve ter finalizado o upload antes da confirmação;
- O usuário já deve ter um cadastro registrado no sistema;
- O usuário deve ter uma opção para substituir um documento anterior, caso já tenha sido feito um upload.

### Definição de Pronto

- O sistema deve ser capaz de exibir um documento feito upload anteriormente e receber um novo documento que deve ser salvo e enviado por email para as vagas que o usuário se candidatar em uma funcionalidade posterior.
