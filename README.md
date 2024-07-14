# Repositório

Script para o envio automatizados de PDFs para os e-mails dos alunos do Einstein Floripa.

## Descrição
O projeto foi feito com o objetivo de enviar por e-mail os relatórios em pdf de simulados realizados pelos alunos do Einstein Floripa.


## Primeiros passos

### Dependências
Para instalar as depedencias do projeto, utilize:

```bash
# Instlaando dependências
pip install -r ./requirements/requirements.txt
```

### Execução do Programa

- O arquivo main.py é responsável pela lógica que verificar os PDFs com o CPF do aluno e compara-lo com a planilha que possuirá o e-mail do aluno e o seu CPF.
- É necessário criar uma pasta chamada "pdfs" e anexar os PDFs que serão gerados a partir deste repositório: https://github.com/einsteinfloripa/notas-pdf.
- Além disso, é necessário anexar na raíz do projeto um arquivo CSV responsável por conter os e-mails dos alunos com o respectivo CPF. Repositório para gerar o arquivo CSV : https://github.com/einsteinfloripa/relatorio-provasPDF

## Arquivos Exemplo

### Planilha 
https://docs.google.com/spreadsheets/d/1ztkfY1ilMdg7QzFgD-qhhppGOBhbxihZTqQ5x-F4HUA/edit?usp=sharing

### Como deverá estar o repositório
![image](https://github.com/user-attachments/assets/5beba5a5-be92-430d-8cc1-a2b6c796da11)

## Observações
Para realizar o envio de e-mails pelo Gmail é necessário uma conta real com uma senha customizada, gerada para realizar envios por aplicativos externos como esse script.
Segue abaixo um link que informa melhor sobre:
https://support.google.com/accounts/answer/185833?hl=pt-br

