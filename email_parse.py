import re
import sys

our_str = str(sys.argv[1])

def email_parse(our_str):
    email_dict = dict.fromkeys(['username', 'domain'])

    if (re.search(r'[@]',our_str)) is None:
        raise ValueError(f'ValueError: wrong email: {our_str}, must be "@"')

    result = (re.split(r'@', our_str))


    if (re.search(r'[.]',result[1])) is None:
        raise ValueError(f'ValueError: wrong email: {our_str}, must be "." in "{result[1]}"')

    email_dict['username'] = result[0]
    email_dict['domain'] = result[1]
    print(email_dict)

email_parse(our_str)