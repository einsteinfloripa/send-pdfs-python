import os
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Função para enviar email com anexo
def send_email(to_email, subject, body, attachment_path):

    # Configurações do email
    # O email de onde o email será enviado
    # senha do email de onde o email será enviado. Foi utilizado uma senha gerada para apps
    from_email = 'pedro.rocha@einsteinfloripa.com.br'
    from_password = 'fwdn wygt zefv lenz'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Anexando o arquivo
    attachment = open(attachment_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment_path)}')

    msg.attach(part)

    # Conectando ao servidor SMTP e enviando o email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Caminho para a planilha Excel e a pasta com os PDFs
excel_path = 'alunos_infos_2024 - Respostas ao formulário 1.csv'
pdf_folder_path = 'pdfs'

# Lendo a planilha
df = pd.read_csv(excel_path)
print(len(df))
df['CPF'] = df['CPF'].str.replace(r'[^\d]', '', regex=True)
# Iterando pelas linhas da planilha
alunos_nao_encontrados = 0
alunos_encontrados = 0


# pdf_filename = f'01309638950.pdf'
# pdf_path = os.path.join(pdf_folder_path, pdf_filename)

# if os.path.exists(pdf_path):
#     # Enviando o email
    
#     send_email(
#         to_email='pedro.rocha2609@gmail.com',
#         subject='Seu PDF',
#         body='Por favor, encontre em anexo o seu PDF.',
#         attachment_path=pdf_path
#     )


# for index, row in df.iterrows():
#     cpf = str(row['CPF'])  # Supondo que a coluna do CPF se chama 'CPF'
#     email = row['E-mail']   # Supondo que a coluna do Email se chama 'Email'
#     print(email)
#     # Encontrando o arquivo PDF correspondente ao CPF
#     pdf_filename = f'{cpf}.pdf'
#     pdf_path = os.path.join(pdf_folder_path, pdf_filename)

#     if os.path.exists(pdf_path):
#         # Enviando o email

#         send_email(
#             to_email='pedro.rocha2609@gmail.com',
#             subject='Seu PDF',
#             body='Por favor, encontre em anexo o seu PDF.',
#             attachment_path=pdf_path
#         )
        
#         alunos_encontrados += 1

#     else:
#         alunos_nao_encontrados += 1

print('ALUNOS NAO ENCONTRADOS', alunos_nao_encontrados)
print('ALUNOS ENCONTRADOS', alunos_encontrados)

