import datetime
import Connection


class Marary:
    def __init__(self, idMarary=0, nom=0):
        self._idMarary = idMarary
        self._nom = nom

    def get_idMarary(self):
        return self._idMarary

    def set_idMarary(self, x):
        self._idMarary = x

    def get_nom(self):
        return self._nom

    def set_nom(self, x):
        self._nom = x

    def showallPatient(self):
        con = Connection.conekta().cursor()
        con.execute("select * from marary")
        result = con.fetchall()
        print(result)

    def insertMarary(self, anarana):
        sql = "insert into marary (idMarary,nom) values(concat('Pat00',nextval('patient')),'"+anarana+"')"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        con.commit()
        con.cursor().close()
        con.close()
        print(" Insereo ")
        print(sql, anarana)

    def showAnarana(self):
        anarana =[]
        sql="select nom from marary"
        con = Connection.conekta()
        con1 = con.cursor()
        con1.execute(sql)
        result = con1.fetchall()
        for item in result:
            anarana.append(item)
        return anarana

