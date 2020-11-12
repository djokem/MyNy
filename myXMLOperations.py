from datetime import date
import firmaXMLOperations as fXML
import xml.dom.minidom as dom

class MyXML:
    datum = "dd.mm.yyyy"
    maticni_broj = "12345678"
    redni_broj = "1"
    brojOIZ = "1"
    korisnik = ""
    kontakt = ""

    DOMTree = dom.parse("MY.xml")
    collection = DOMTree.documentElement

    @staticmethod
    def reread_xml():
        MyXML.DOMTree = dom.parse("MY.xml")
        MyXML.collection = MyXML.DOMTree.documentElement

    @staticmethod
    def write_to_xmlfile():
        with open("MY.xml", "w") as xml_file:
            MyXML.DOMTree.writexml(xml_file)
            # xml_file.write(Lokacija.DOMTree.toxml())

    @staticmethod
    def getDatum():
        MyXML.datum = date.today()
        MyXML.datum = MyXML.datum.strftime("%d.%m.%Y")
        return MyXML.datum

    def dodajSlogMY(self):
        lokacije = fXML.Lokacija.sve_lokacije()
        for i in range(len(lokacije)):
            nova_lokacija = MyXML.DOMTree.createElement("StavkaMY")

            lokacija_rbr = MyXML.DOMTree.createElement("RedniBroj")
            lokacija_rbr.appendChild(MyXML.DOMTree.createTextNode(str(i + 1)))

            lokacija_naziv = MyXML.DOMTree.createElement("Naziv")
            lokacija_naziv.appendChild(MyXML.DOMTree.createTextNode(lokacije[i].naziv))

            lokacija_mesto = MyXML.DOMTree.createElement("Mesto")
            lokacija_mesto.appendChild(MyXML.DOMTree.createTextNode(lokacije[i].mesto))

            lokacija_adresa = MyXML.DOMTree.createElement("Adresa")
            lokacija_adresa.appendChild(MyXML.DOMTree.createTextNode(lokacije[i].adresa))

            nova_lokacija.appendChild(lokacija_naziv)
            nova_lokacija.appendChild(lokacija_mesto)
            nova_lokacija.appendChild(lokacija_adresa)

            MyXML.collection.getElementsByTagName("SlogMY")[0].appendChild(nova_lokacija)


    @staticmethod
    def popuniMYObrazac(date, matbr, rbr, broiz, kor, kontkt):
        MyXML.collection.getElementsByTagName("DatumIzvestaja")[0].childNodes[0].data = date
        MyXML.collection.getElementsByTagName("MaticniBroj")[0].childNodes[0].data = matbr
        MyXML.collection.getElementsByTagName("RedniBroj")[0].childNodes[0].data = rbr
        MyXML.collection.getElementsByTagName("BrojOIZ")[0].childNodes[0].data = broiz
        MyXML.collection.getElementsByTagName("PodatkeObradio")[0].childNodes[0].data = kor
        MyXML.collection.getElementsByTagName("Kontakt")[0].childNodes[0].data = kontkt
        MyXML.dodajSlogMY()

        MyXML.write_to_xmlfile()
        MyXML.reread_xml()



