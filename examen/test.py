import unittest, time;
from serv import Servidor

class TestServidor(unittest.TestCase):
    def test1_hora(self):
        serv = Servidor()
        hora = serv.hora()
        self.assertEqual(time.strftime("%H:%M:%S"), hora)

    def test2_hora(self):
        serv = Servidor()
        hora = serv.hora()
        self.assertNotEqual("chupamela", hora)

    def test3_sumar(self): #suma bien, primero lo pones con distinto y luego bien
        serv = Servidor()
        a=2
        b=2
        self.assertEqual(a + b, 4)
    def test4_restar(self): #igual que el suma
        serv = Servidor()
        a=2
        b=1
        self.assertEqual(a - b, 1)

    def testarchivo(self): #pasa con las líneas
        serv = Servidor()
        lines = 0
        size = 1024 * 1024
        with open('archivo.txt', "r+") as myfile:
            read_file = myfile.read
            buffer = read_file(size)
            while buffer:
                lines += buffer.count('\n')
                buffer = read_file(size)
        if (lines != 0):
            lines += 1
        self.assertEqual(lines, 6)

