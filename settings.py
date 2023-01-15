import re

def phone_proof(phone : str):
    result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone)
    return bool(result)

ADMINS = ['legeorg2004@gmail.com', 'ranil2086@bk.ru']