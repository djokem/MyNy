from xml.dom.minidom import parse
import xml.dom.minidom
from datetime import date

# pyuic5 –x "filename".ui –o "filename".py ....iz designera u py



class Lokacija:

    DOMTree = xml.dom.minidom.parse("FirmaLokacije.xml")
    collection = DOMTree.documentElement
    lokacije = collection.getElementsByTagName("Lokacija")
    string_ids = [lokacija.getAttribute("id") for lokacija in lokacije]  # pravljenje niza od ID-jeva ['1', '2', ... , 'N'] iz XML-a za Lokacije

    def __init__(self, naziv = None, mesto = None, adresa = None):
        if naziv is not None:
            self.id = self.get_next_id()
            self.naziv = naziv
            self.mesto = mesto
            self.adresa = adresa

            Lokacija.dodaj_lokaciju(self)

    def __lt__(self, other):
        return int(self.id) < int(other.id)

    @staticmethod
    def reread_xml():
        Lokacija.DOMTree = xml.dom.minidom.parse("FirmaLokacije.xml")
        Lokacija.collection = Lokacija.DOMTree.documentElement
        Lokacija.lokacije = Lokacija.collection.getElementsByTagName("Lokacija")
        Lokacija.string_ids = [lokacija.getAttribute("id") for lokacija in Lokacija.lokacije]  # pravljenje niza od ID-jeva ['1', '2', ... , 'N'] iz XML-a za Lokacije

    @staticmethod
    def write_to_xmlfile():
        with open("FirmaLokacije.xml", "w") as xml_file:
            Lokacija.DOMTree.writexml(xml_file)
            #xml_file.write(Lokacija.DOMTree.toxml())

    def get_next_id(self):
        if len(Lokacija.string_ids) < 1:
            return "1"
        int_ids = [int(string_id) for string_id in Lokacija.string_ids]  # pretvaranje niza ID-jeva koji su string tipa u niz ID-jeva koji su Int tipa
        return str(max(int_ids) + 1)  # vracanje sledeceg ID-ja


    @staticmethod
    def sve_lokacije():
        all_lok = []
        for location in Lokacija.lokacije:
            lok = Lokacija()
            lok.id = location.getAttribute("id")
            lok.naziv = location.getElementsByTagName('Naziv')[0].childNodes[0].data
            lok.mesto = location.getElementsByTagName('Mesto')[0].childNodes[0].data
            lok.adresa = location.getElementsByTagName('Adresa')[0].childNodes[0].data
            all_lok.append(lok)
        all_lok.sort(reverse=True)
        return all_lok

    @staticmethod
    def dodaj_lokaciju(lok):
        if lok.id in Lokacija.string_ids:
            print("Lokacija sa ID = %s vec postoji!" % lok.id)
        else:
            nova_lokacija = Lokacija.DOMTree.createElement("Lokacija")
            nova_lokacija.setAttribute("id", lok.id)

            lokacija_naziv = Lokacija.DOMTree.createElement("Naziv")
            lokacija_naziv.appendChild(Lokacija.DOMTree.createTextNode(lok.naziv))

            lokacija_mesto = Lokacija.DOMTree.createElement("Mesto")
            lokacija_mesto.appendChild(Lokacija.DOMTree.createTextNode(lok.mesto))

            lokacija_adresa = Lokacija.DOMTree.createElement("Adresa")
            lokacija_adresa.appendChild(Lokacija.DOMTree.createTextNode(lok.adresa))

            nova_lokacija.appendChild(lokacija_naziv)
            nova_lokacija.appendChild(lokacija_mesto)
            nova_lokacija.appendChild(lokacija_adresa)

            Lokacija.collection.getElementsByTagName("Lokacije")[0].appendChild(nova_lokacija)

            Lokacija.write_to_xmlfile()
            Lokacija.reread_xml()    # ponovo ucitaj xml

            return True

    @staticmethod
    def obrisi_lokaciju(id):
        for lokacija in Lokacija.lokacije:
            if id == lokacija.getAttribute("id"):
                Lokacija.collection.getElementsByTagName("Lokacije")[0].removeChild(lokacija)
                Lokacija.write_to_xmlfile()
                Lokacija.reread_xml()
                return True
        return False

    @staticmethod
    def izmeni_lokaciju(lok):
        for lokacija in Lokacija.lokacije:
            if lok.id == lokacija.getAttribute("id"):
                Lokacija.obrisi_lokaciju(lok.id)
                lok.dodaj_lokaciju(lok)
                return True
        return False


def getNazivFirma():
    naziv = Lokacija.collection.getElementsByTagName("FirmaNaziv")
    return naziv[0].childNodes[0].data

def getMatBr():
    mat = Lokacija.collection.getElementsByTagName("MaticniBroj")
    return mat[0].childNodes[0].data
