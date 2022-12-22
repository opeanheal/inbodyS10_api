import json

class Patient:

    def __init__(self, name, id = None, bios = None):  # bios -> Array of Bio

        self.name = name
        self.id = id
        self.bios = self.include_bios(bios)

    def include_bios(self, bios):

        array = []

        if len(bios) > 0:
            for item in bios:
                array.append(item)
        else:
            print('You must at least 1 item in array (bios)')

        return array

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
