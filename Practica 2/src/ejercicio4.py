def validation_mail ():
    mail = input('Ingrese un email: ')
    valid = True
    if mail.count('@') != 1 or mail.startswith(('@', '.')) or mail.endswith(('.', '@')):
         valid = False
    else:
        user, domain = mail.split('@')
        if len(user) == 0 or domain.startswith('.') or domain.count('.') < 1:
            valid = False
        else:
            extension = domain.split('.')[-1]
            if len(extension) < 2 or not extension.isalpha():
                valid = False
    
    print('El email es válido.' if valid else 'El email no es válido.')