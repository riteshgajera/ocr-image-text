from data import Data

class TestData:

    def get(self):
        data = Data()
        data.set('Filename', 'in.jpg')
        data.set('Extracted text', 'abc xxx def')
        return data