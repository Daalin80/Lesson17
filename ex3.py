def hide_email (email):
    email = '@'.join([email.replace(email[email.find('@') - 3:], '***'),
                      email.replace(email[:len(email) - email.find('@') + 2], '**')])
    return email
print(hide_email('dinay8@gmail.com'))