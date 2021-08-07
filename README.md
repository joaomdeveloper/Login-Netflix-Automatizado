# Login Netflix Automatizado

### COMO O SCRIPT FUNCIONA?

- Fizemos a importação de três bibliotecas sendo elas: selenium, pyautogui & time.
- Nas quatros primeiras linhas, o email e a senha da netflix é coletada, nosso navegador é aberto e já entra no site de login.
- Nas outras 8 linhas, é estabelecido um tempo para que cada comando execute após a página ser totalmente carregada, a coleta do xpath dos campos de texto e inserido as informações (Email e Senha) coletada antes.

### PORQUE EU USEI O SELENIUM E PYAUTOGUI?

- O Selenium serviu apenas para clicar nos campos, caso eu utilizasse o pyautogui teria que capturar a posição de cada input e botão de entrar, entretanto, esse tipo de script só funcionaria bem para minha resolução (1920x1080), caso eu quissese passar para um amigo de trabalho, escola, faculdade, teria que formatar o código para a resolução dele.

- Já o PyAutoGui serviu para inserir as informações coletadas pelo nosso input nas duas primeiras linhas do código.

### REQUISITOS PARA RODAR O SCRIPT

- Ter o Python 3
- Ter o Chrome Driver (Veja a versão do seu navegador Chrome e instale)


### É um sistema bem simples, entretanto, o código pode ser implementado em outro caso seja da vontade do usuários.
