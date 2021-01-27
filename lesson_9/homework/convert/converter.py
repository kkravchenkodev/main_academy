def open_dataset(filename):
    import csv
    rows = []
    with open(filename, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return fields, rows


def convert_1(filename):
    for row in open_dataset(filename)[1]:
        print(f'{row[0]}: {row[2]}')


def convert_2(filename):
    for row in open_dataset(filename)[1]:
        print(f'{row[1]} (email: {row[2]})')


def convert_3(filename):
    dct = {}
    for row in open_dataset(filename)[1]:
        dct.setdefault(row[2].split('@')[1], [])
        dct[row[2].split('@')[1]].append(row[0])
    for k, v in dct.items():
        print(f"{k} ==> {', '.join(v)}")


def convert_4(filename):
    from random import sample
    fields, rows = open_dataset(filename)
    fields.append("Password")
    for row in rows:
        row.append(''.join(map(str, sample(range(10), 4))))
    print(*fields, sep=';')
    print(*[';'.join(row) for row in rows], sep='\n')



