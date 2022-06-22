import unittest,time;
from serv import Servidor

class TestServidor(unittest.TestCase):
    def test1_hora(self):
        serv = Servidor()
        hora= serv.hora()
        self.assertEqual(time.strftime("%H:%M:%S"), hora)

    def test2_hora(self):
        serv = Servidor()
        hora= serv.hora()
        self.assertNotEqual("chupamela", hora)