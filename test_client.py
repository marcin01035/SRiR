import client
import function


class Model_mock:
    def __init__(self, name):
        pass

    def numberoflines(self, filename):
        return function.numberoflines(filename)




class Server_mock:
    def __init__(self):
        self.filename = ''

    def sendmodule(self, name, file):
        self.filename = file

    def module(self, name):
        model = Model_mock(name)

        return model

    def sendfile(self, plikserwer, filesource):
        pass


def test_wysylanie():
    x = client.Rmi()
    x.zmienne('stuff.py', 't.py')
    server = Server_mock()
    res = x.wysylanie(server)
    assert res == 1


def test_function():
    x = client.Rmi()
    server = Server_mock()
    res = x.funkcja(server, 'function.py')
    assert res == 13



