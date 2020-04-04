def change_string_to_int(string):
    x = [i for i in string.split(' ')]
    y = [i.replace(',', '.') for i in x]
    z = []
    for i in y:
        if not i.isalpha():
            z.append(i)
    output = float(''.join(z))
    return output


def change_string_to_int_2(string):
    a = string.strip()
    b = a.replace('zł', '')
    c = b.replace(',', '.')
    d = c.encode('utf-8')
    e = d.replace(b'\xc2\xa0', b'')
    f = float(e.decode('utf-8'))
    return f


def get_product(price, database):
    for i in database:
        if i['item_price'] == price:
            return i
