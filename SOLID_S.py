class Prepare:
    def __init__(self, raw_data):
        self.data = raw_data

    def extract_data(self):
        result = ''
        for item in self.raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result


class Write_file:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, rawdata):
        with open(self.filename, 'w', encoding='UTF8') as f:
            f.write(rawdata)


data = [
    {
        'name': 'Sherlock',
        'surname': 'Holmes',
        'occupation': 'private detective'
    },
    {
        'name': 'John',
        'surname': 'Watson',
        'occupation': 'doctor'
    }
]

exporter = Prepare(data)
exporter.write_file('out.csv')