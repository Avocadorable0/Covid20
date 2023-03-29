from datetime import datetime
from sqlite3 import Date

import Connection


class DetailsMarary:
    idmarary = None
    anarana = None
    daty = None
    temperature = 0
    o2 = 0

    def setIdmarary(self, x):
        try:
            x = str(x)
            self.idmarary = x
        except ValueError as e:
            raise str(e)

    def getIdmarary(self):
        return self.idmarary

    def setnom(self, x):
        try:
            x = str(x)
            self.anarana = x
        except ValueError as e:
            raise str(e)

    def getAnarana(self):
        return self.anarana

    def setdaty(self, x):
        try:
            x = str(x)
            self.daty = x
        except ValueError as e:
            raise str(e)

    def getDaty(self):
        return self.daty

    def setTemp(self, x):
        try:
            x = float(x)
            self.temperature = x
        except ValueError as e:
            raise str(e)

    def getTemp(self):
        return self.temperature

    def seto2(self, x):
        try:
            x = float(x)
            self.o2 = x
        except ValueError as e:
            raise str(e)

    def getO2(self):
        return self.o2

    def __init__(self, idmarary, anarana, daty, temperature, o2):
        self.setIdmarary(idmarary)
        self.setnom(anarana)
        self.setdaty(daty)
        self.setTemp(temperature)
        self.seto2(o2)

    @staticmethod
    def getlistDetailsMarary():
        Details = []
        sql = "select * from detailsmarary"
        con = Connection.conekta().cursor()
        con.execute(sql)
        a = con.fetchall()
        for i in a:
            Details.append(DetailsMarary(i[1], i[0], i[2], i[3], i[4]))
        return Details

    @staticmethod
    def getlistDetailsMararyById(idmarary):
        Details = []
        sql = "select * from detailsmarary where idmarary=%s"
        con = Connection.conekta().cursor()
        con.execute(sql, (idmarary,))
        a = con.fetchall()
        for i in a:
            Details.append(DetailsMarary(i[1], i[0], i[2], i[3], i[4]))
        return Details


a = DetailsMarary.getlistDetailsMararyById('Pat0042')
for i in a:
    print(i.getDaty() + " " + str(i.getTemp()) + " " + str(i.getO2()))
