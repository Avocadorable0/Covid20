import datetime
from datetime import date
import Connection
import Marari


class Controle(Marari.Marary):
    def __init__(self, idMarary=0, daty=0, temperature=0, o2=0, ):
        Marari.Marary.__init__(self, idMarary)
        self._daty = daty
        self._temperature = temperature
        self._o2 = o2

    def get_daty(self):
        return self._daty

    def set_daty(self, x):
        self._daty = x

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, x):
        self._temperature = x

    def get_o2(self):
        return self._o2

    def set_o2(self, x):
        self._o2 = x

    def showallControle(self):
        con = Connection.conekta().cursor()
        con.execute("select * from Controle")
        result = con.fetchall()
        print(result)

    def insertControle(self, anarana, andro, temp, oxy):
        sql = "insert into controle (idMarary,Daty,temperature,O2) values((select idmarary from marary where nom='" + anarana + "'),%s,%s,%s)"
        con = Connection.conekta()
        values = (andro, temp, oxy)
        con1 = con.cursor()
        con1.execute(sql, values)
        con.commit()
        con.cursor().close()
        con.close()
        print(" Insereo ")
        print(sql, values)

    def getCoordonnees(self, anarana):
        coordonnees = []
        sql = "select controle.o2 as axygene, controle.temperature as temperature, extract(doy from daty) as jour  " \
              "from " \
              "controle join marary on marary.idMarary=controle.idMarary where marary.nom='" + anarana + "'"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        result = con1.fetchall()
        for elements in result:
            coordonnees.append(elements)
        return coordonnees

    def getX(self, anarana):
        CoordonneeesX = []
        sql = "select controle.o2 as axygene  " \
              "from " \
              "controle join marary on marary.idMarary=controle.idMarary where marary.nom='" + anarana + "'"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        result = con1.fetchall()
        for item in result:
            CoordonneeesX.append(item)
        return CoordonneeesX

    def getY(self, anarana):
        CoordonneesY = []
        sql = "select controle.temperature as temp   " \
              "from " \
              "controle join marary on marary.idMarary=controle.idMarary where marary.nom='" + anarana + "'"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        result = con1.fetchall()
        for item in result:
            CoordonneesY.append(item)
        return CoordonneesY

    def getZ(self, anarana):
        CoordonneesZ = []
        sql = "select extract(doy from daty) as jour  " \
              "from " \
              "controle join marary on marary.idMarary=controle.idMarary where marary.nom='" + anarana + "'"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        result = con1.fetchall()
        for item in result:
            CoordonneesZ.append(item)
        return CoordonneesZ

    def getDaty(self, anarana):
        Daty = []
        sql = "select daty from controle join marary on marary.idMarary=controle.idMarary where marary.nom='" + anarana + "' order by daty DESC limit 1"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        result = con1.fetchall()
        for item in result:
            Daty.append(item)
        return result

    def getDonnees(self):
        sql = "select marary.nom as nom, controle.daty as daty, controle.temperature as temperature, controle.o2 as " \
              "o2 from controle join marary on marary.idMarary=controle.idMarary"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        data = con1.fetchall()
        return data

    def moyenneTemp(self, *anarana):
        sql = "select avg(controle.temperature) from controle join marary on marary.idmarary = controle.idmarary " \
              "where marary.nom in ("
        for i in range(0, len(anarana)):
            sql += "'" + anarana[i] + "'"
            if i < len(anarana) - 1:
                sql += ","
        sql += "')"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        moyenne = con1.fetchone()
        return moyenne



"""
b = Controle()
a = b.getDaty('Jean')

date1 = date(2023, 1, 15)
for i in range(len(a)):
    for j in range(len(a[i])):
        valiny = a[i][j]
print(valiny)
if date1 < valiny:
    print("marina")
else:
    print("diso")
"""
