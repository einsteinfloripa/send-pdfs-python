import os
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Função para enviar email com anexo
def send_email(to_email, subject, body, attachment_path):

    # O email de onde o email será enviado
    # A senha utilizada deve ser criada na conta de email, na aba de "Senhas de App".
    # Essas senhas são específicas para envio de e-mails a partir de programas externos como esse script.
    from_email = 'pedro.rocha@einsteinfloripa.com.br'
    from_password = 'fwdn wygt zefv lenz'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

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

# Caminho para a planilha CSV e a pasta com os PDFs
csv_path = 'alunos_infos_2024 - Respostas ao formulário 1.csv'
pdf_folder_path = 'pdfs'

# Lendo a planilha
df = pd.read_csv(csv_path)
df['CPF'] = df['CPF'].str.replace(r'[^\d]', '', regex=True)

alunos_nao_encontrados = 0
alunos_encontrados = 0

# Iterando pelas linhas da planilha
for index, row in df.iterrows():
    cpf = str(row['CPF']) 
    email = row['E-mail']   
 
    nome_completo = row['Nome Completo']
    nome_dividido = nome_completo.split()

    # Pegue a primeira palavra da lista
    primeiro_nome = nome_dividido[0]

    # Encontrando o arquivo PDF correspondente ao CPF
    pdf_filename = f'{cpf}.pdf'
    pdf_path = os.path.join(pdf_folder_path, pdf_filename)

    if os.path.exists(pdf_path):
        
        # Abaixo é necessário costumizar a mensagem que será enviada no corpo do E-mail.
        # Subject é o Assunto do E-mail.

        html_message = f"""
                <html>
                <body>
                    <h2 style="font-size:16px; color: black;">Olá, <strong>{primeiro_nome}</strong>! Espero que esteja tudo bem por aí!</h2>
                    <p style="color: black;">O seu relatório do Simulinho 2024 está pronto!</p>
                    <p style="margin-bottom: 28px; color: black;">Qualquer problema encontrado, entrar em contato com o vale.</p>
                    <p style="color: black;">Atenciosamente,</p>
                    <p style="color: black;">EinsteinFloripa</p>
                </body>
                </html>
        """

        send_email(
                to_email=email,
                subject='Relatório Simulinho 2024 - EinsteinFloripa',
                body=html_message,
                attachment_path=pdf_path
        )



        alunos_encontrados += 1

    else:
        alunos_nao_encontrados += 1

