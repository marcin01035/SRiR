import client


class Server_moc:
    def sendfile(self, plikserwer, filesource):
        pass


def test_wysylanie():
    x = client.Rmi()
    x.zmienne('stuff.py', 't.py')
    server = Server_moc()
    res = x.wysylanie(server)
    assert res == 1
