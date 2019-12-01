- Aluno:Breno Filipe Ferreira da Silva
- RA:21901629

### Como compilar e executar o programa no linux com o python3 e o git instalados:

- Instalar python3 no terminal Linux: sudo apt-get install python3
- Instalar git no terminal Linux: sudo apt-get install git
#### No terminal Linux digitar os seguintes comandos:
- git clone https://github.com/breno12filipe/Sistemas-operacionais.git
- cd Sistemas-operacionais
- python3 Trabalho_so.py

### Como compilar e executar o programa no windows com o Python e o Git instalados:

- Instalar Python no Windows, acessar o site: https://www.python.org/downloads/ fazer o download e instalação do Python
- Instalar Git no Windows, acessar o site: https://gitforwindows.org/ fazer o download e instalação do Git
#### No prompt de comando do Windows digitar:
- mkdir Pasta
- cd Pasta
- git clone https://github.com/breno12filipe/Trabalho_so.py.git
- cd Sistemas-operacionais
- py Trabalho_so.py

### Comprovação da eficácia e objetivos alcançados
- Cada transferência é uma thread criada e cada thread criada não atrapalha o fluxo das demais threads
- O resultado se deu pela implementação do semáforo, que controla o acesso às threads por parte do programa
- São realizadas 100 transferências simultâneas
- O saldo da conta from é zerado pela conta to
- As contas podem trocar de ordem apenas por mudar a ordem entre conta from e conta to nos parâmetros da função transferencia
