import smtplib
import email.message


def enviar_email():

    nome = input("Informe o nome do proprietário: ")
    end = input("Informe o email do proprietário: ")
    cnpj = input("Informe o CNPJ do proprietário: ")
    ass = input("Relate os erros ou dúvidas sobre o software: ")

    corpo_email = """
    <p>Nome: {} </p>
    <p>Email: {} </p>
    <p>CNPJ: {} </p>
    <p>Assunto: {} </p>
    """.format(nome, end, cnpj, ass)

    msg = email.message.Message()
    msg['Subject'] = "SUPORTE: GRALHA VISION"
    msg['From'] = 'suporte.gralha@gmail.com'
    msg['To'] = 'visiongralha@gmail.com', 'suporte.gralha@gmail.com'
    password = 'tsxkpujjzchdnszh'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email()
