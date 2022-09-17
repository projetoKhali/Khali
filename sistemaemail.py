import win32com.client as win32

# Função envio de  e-mail Líder do Grupo e Fake Client
def enviaremail(nome, email1):
    outlook = win32.Dispatch('outlook.application')  # Criar interação com outlook
    email = outlook.CreateItem(0)  # Criar um e-mail

    # Configurar as informações do e-mail
    email.To = email1
    email.Subject = 'E-mail automático - Senha cadastrada para Avaliação 360°'
    email.HTMLBody = f"""
    <p>Olá, {nome}!</p>

    <p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
    <p>SENHA:</p>
    <p>E-MAIL CADASTRADO: {email1}</p>

    <p><b>Sua senha é intrasferível, não compartilhe com ninguém.</b></p>

    <p>Não responda a este e-mail.</p>
    """

    if str(object='@') in email1:
        email.Send()
        print(f'E-mail enviado para {nome}')
    else:
        print(f'Não existe e-mail cadastrado para {nome}')

enviaremail()
