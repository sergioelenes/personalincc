from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from bs4 import BeautifulSoup
import time
import re
import urllib3
urllib3.disable_warnings()

r = requests.Session()

provsvdpl = ["A1190*", "A3888*", "A1855*", "A0201*","A3074*", "A6590*", "A0185*", "A3713*", "A0007*", "A0308*", "A3599*", "A0411*", "A3551*", "A2914*","A3004*", "C1002*", "D0099*", "A0739*", "D1178*", "A0176*", "A0465*", "XXX*"]
provsservices = ["D0099"]
provscdg = ["A3004", "D0099"]
links = []
listocs=[]
urlpo = 'https://villas.esasacloud.com/avance/cgi-bin/e-sasa/PO'



def firma2rec(region, proveedores, mesini, mesfin):
    readfile = open('la_linfomana.txt', 'r')
    passw= readfile.read()
    readfile.close()
    login1 = r.post('https://myavance.esasacloud.com/avance/cgi-bin/e-sasa/dos?', "Corp=LORETO&password=NICOLAS&Idioma=1&origen=1&escondido=1&cmdEnviar=Enviar+Datos&basura=1", verify=False)
    login2 = r.post('https://villas.esasacloud.com/avance/cgi-bin/e-sasa/validapassc', "Ancho=1024&parb=XIUIIUAVUINUUVYUU&lstusuario=selenesm&password="+passw+"&lstregion=AOHVDPLOBL&Corp=LORETO&Idioma=1&origen=1&escondido=1&basura=On&cmdEnviar=Enviar+Datos&nombreus=SERGIO+ELENES+MACHADO+-+CONTRALOR+VDP", verify=False)
    datadoc = "INcanaliza=0503&Emp="+region+"&Idioma=1&Mes="+mesfin+"&Ano=2023&Order=*&Cust="+proveedores+"&Item=*&Curr=.&pedpro=*&Inilin=1&Endlin=999&Orderby=01&Status=01&Autor=04&IniDay=1&IniMon="+mesini+"&IniYear=2023&EndDay=31&EndMon="+mesfin+"&EndYear=2023&FlagDate=1&fpago=0&prio=0&cualobs=0&sinlimite=on&VoyI=1&Opcion=3&Reg=LORETOOBLCONSOLID&Voy=1&Num99=0&Num2=0&Usu=LORETOselenesm&Emp=OBLPALMAR&cmdEnviar=Enviar+Datos"
    pagina = r.post(urlpo, datadoc, verify=False, allow_redirects=True)
    pagina = BeautifulSoup(pagina.text,'html.parser')
    ocs = pagina.find_all(text = re.compile("OC-"))
    for oc in ocs:
        listocs.append(oc)    
    ulinks = pagina.find_all("a", href=re.compile(r"POautoriza?"))
    for link in ulinks:
        links.append("https://villas.esasacloud.com/avance/cgi-bin/e-sasa/"+link['href'])
def firmaporoc(oc,mesfin):
    readfile = open('la_linfomana.txt', 'r')
    passw= readfile.read()
    readfile.close()    
    login1 = r.post('https://myavance.esasacloud.com/avance/cgi-bin/e-sasa/dos?', "Corp=LORETO&password=NICOLAS&Idioma=1&origen=1&escondido=1&cmdEnviar=Enviar+Datos&basura=1", verify=False)
    login2 = r.post('https://villas.esasacloud.com/avance/cgi-bin/e-sasa/validapassc', "Ancho=1024&parb=XIUIIUAVUINUUVYUU&lstusuario=selenesm&password="+passw+"&lstregion=AOHVDPLOBL&Corp=LORETO&Idioma=1&origen=1&escondido=1&basura=On&cmdEnviar=Enviar+Datos&nombreus=SERGIO+ELENES+MACHADO+-+CONTRALOR+VDP", verify=False)
    datadoc = "INcanaliza=0503&Emp=TODAS&Idioma=1&Mes="+mesfin+"&Ano=2023&Order=*"+oc+"*&Cust=*&Item=*&Curr=.&pedpro=*&Inilin=1&Endlin=999&Orderby=01&Status=01&Autor=04&IniDay=1&IniMon=1&IniYear=2023&EndDay=31&EndMon="+mesfin+"&EndYear=2023&FlagDate=1&fpago=0&prio=0&cualobs=0&sinlimite=on&VoyI=1&Opcion=3&Reg=LORETOOBLCONSOLID&Voy=1&Num99=0&Num2=0&Usu=LORETOselenesm&Emp=TODAS&cmdEnviar=Enviar+Datos"
    pagina = r.post(urlpo, datadoc, verify=False, allow_redirects=True)
    pagina = BeautifulSoup(pagina.text,'html.parser')
    ocs = pagina.find_all(text = re.compile("OC-"))
    for oc in ocs:
        listocs.append(oc)
    ulinks = pagina.find_all("a", href=re.compile(r"POautoriza?"))
    for link in ulinks:
        links.append("https://villas.esasacloud.com/avance/cgi-bin/e-sasa/"+link['href'])
def firmaVDA(mesfin):
    readfile = open('la_linfomana.txt', 'r')
    passw= readfile.read()
    readfile.close()    
    login1 = r.post('https://myavance.esasacloud.com/avance/cgi-bin/e-sasa/dos?', "Corp=LORETO&password=NICOLAS&Idioma=1&origen=1&escondido=1&cmdEnviar=Enviar+Datos&basura=1", verify=False)
    login2 = r.post('https://villas.esasacloud.com/avance/cgi-bin/e-sasa/validapassc', "Ancho=1024&parb=XIUIIUAVUINUUVYUU&lstusuario=selenesm&password="+passw+"&lstregion=AOHVDPLOBL&Corp=LORETO&Idioma=1&origen=1&escondido=1&basura=On&cmdEnviar=Enviar+Datos&nombreus=SERGIO+ELENES+MACHADO+-+CONTRALOR+VDP", verify=False)
    datadoc = "INcanaliza=0503&Emp=VVDANZLOR&Idioma=1&Mes="+mesfin+"&Ano=2023&Order=*&Cust=*&Item=*&Curr=.&pedpro=*&Inilin=1&Endlin=999&Orderby=01&Status=01&Autor=04&IniDay=1&IniMon="+mesfin+"&IniYear=2023&EndDay=31&EndMon="+mesfin+"&EndYear=2023&FlagDate=1&fpago=0&prio=0&cualobs=0&sinlimite=on&VoyI=1&Opcion=3&Reg=LORETORLORVVDANZ&Voy=1&Num99=0&Num2=0&Usu=LORETOselenesm&Emp=VVDANZLOR&cmdEnviar=Enviar+Datos"
    pagina = r.post(urlpo, datadoc, verify=False, allow_redirects=True)
    pagina = BeautifulSoup(pagina.text,'html.parser')
    ocs = pagina.find_all(text = re.compile("OC-"))
    for oc in ocs:
        listocs.append(oc)    
    ulinks = pagina.find_all("a", href=re.compile(r"POautoriza?"))
    for link in ulinks:
        links.append("https://villas.esasacloud.com/avance/cgi-bin/e-sasa/"+link['href'])
def firmaPalmita(mesfin):
    readfile = open('la_linfomana.txt', 'r')
    passw= readfile.read()
    readfile.close()    
    login1 = r.post('https://myavance.esasacloud.com/avance/cgi-bin/e-sasa/dos?', "Corp=LORETO&password=NICOLAS&Idioma=1&origen=1&escondido=1&cmdEnviar=Enviar+Datos&basura=1", verify=False)
    login2 = r.post('https://villas.esasacloud.com/avance/cgi-bin/e-sasa/validapassc', "Ancho=1024&parb=XIUIIUAVUINUUVYUU&lstusuario=selenesm&password="+passw+"&lstregion=AOHVDPLOBL&Corp=LORETO&Idioma=1&origen=1&escondido=1&basura=On&cmdEnviar=Enviar+Datos&nombreus=SERGIO+ELENES+MACHADO+-+CONTRALOR+VDP", verify=False)
    datadoc = "INcanaliza=0503&Emp=OBLMKTPALM&Idioma=1&Mes="+mesfin+"&Ano=2023&Order=*&Cust=*&Item=*&Curr=.&pedpro=*&Inilin=1&Endlin=999&Orderby=01&Status=01&Autor=04&IniDay=1&IniMon="+mesfin+"&IniYear=2023&EndDay=31&EndMon="+mesfin+"&EndYear=2023&FlagDate=1&fpago=0&prio=0&cualobs=0&sinlimite=on&VoyI=1&Opcion=3&Reg=LORETOOBLCONSOLID&Voy=1&Num99=0&Num2=0&Usu=LORETOselenesm&Emp=OBLMKTPALM&cmdEnviar=Enviar+Datos"
    pagina = r.post(urlpo, datadoc, verify=False, allow_redirects=True)
    pagina = BeautifulSoup(pagina.text,'html.parser')
    ocs = pagina.find_all(text = re.compile("CO-"))
    for oc in ocs:
        listocs.append(oc)    
    ulinks = pagina.find_all("a", href=re.compile(r"POautoriza?"))
    for link in ulinks:
        links.append("https://villas.esasacloud.com/avance/cgi-bin/e-sasa/"+link['href'])
def oblservices(mesfin, proveedores):
    readfile = open('la_linfomana.txt', 'r')
    passw= readfile.read()
    readfile.close()    
    login1 = r.post('https://myavance.esasacloud.com/avance/cgi-bin/e-sasa/dos?', "Corp=LORETO&password=NICOLAS&Idioma=1&origen=1&escondido=1&cmdEnviar=Enviar+Datos&basura=1", verify=False)
    login2 = r.post('https://villas.esasacloud.com/avance/cgi-bin/e-sasa/validapassc', "Ancho=1024&parb=XIUIIUAVUINUUVYUU&lstusuario=selenesm&password="+passw+"&lstregion=AOHVDPLOBL&Corp=LORETO&Idioma=1&origen=1&escondido=1&basura=On&cmdEnviar=Enviar+Datos&nombreus=SERGIO+ELENES+MACHADO+-+CONTRALOR+VDP", verify=False)
    datadoc = "INcanaliza=0503&Emp=OBLSERVICE&Idioma=1&Mes="+mesfin+"&Ano=2023&Order=*&Cust="+proveedores+"&Item=*&Curr=.&pedpro=*&Inilin=1&Endlin=999&Orderby=01&Status=01&Autor=04&IniDay=1&IniMon="+mesfin+"&IniYear=2023&EndDay=31&EndMon="+mesfin+"&EndYear=2023&FlagDate=1&fpago=0&prio=0&cualobs=0&sinlimite=on&VoyI=1&Opcion=3&Reg=LORETOOBLCONSOLID&Voy=1&Num99=0&Num2=0&Usu=LORETOselenesm&Emp=OBLMKTPALM&cmdEnviar=Enviar+Datos"
    pagina = r.post(urlpo, datadoc, verify=False, allow_redirects=True)
    pagina = BeautifulSoup(pagina.text,'html.parser')
    ocs = pagina.find_all(text = re.compile("OC-"))
    for oc in ocs:
        listocs.append(oc)    
    ulinks = pagina.find_all("a", href=re.compile(r"POautoriza?"))
    for link in ulinks:
        links.append("https://villas.esasacloud.com/avance/cgi-bin/e-sasa/"+link['href'])

def ocs_cdgolf(mesfin, proveedores):
    readfile = open('la_linfomana.txt', 'r')
    passw= readfile.read()
    readfile.close()    
    login1 = r.post('https://myavance.esasacloud.com/avance/cgi-bin/e-sasa/dos?', "Corp=LORETO&password=NICOLAS&Idioma=1&origen=1&escondido=1&cmdEnviar=Enviar+Datos&basura=1", verify=False)
    login2 = r.post('https://villas.esasacloud.com/avance/cgi-bin/e-sasa/validapassc', "Ancho=1024&parb=XIUIIUAVUINUUVYUU&lstusuario=selenesm&password="+passw+"&lstregion=AOHVDPLOBL&Corp=LORETO&Idioma=1&origen=1&escondido=1&basura=On&cmdEnviar=Enviar+Datos&nombreus=SERGIO+ELENES+MACHADO+-+CONTRALOR+VDP", verify=False)
    datadoc = "INcanaliza=0503&Emp=OBLCAMGLOR&Idioma=1&Mes="+mesfin+"&Ano=2023&Order=*&Cust="+proveedores+"&Item=*&Curr=.&pedpro=*&Inilin=1&Endlin=999&Orderby=01&Status=01&Autor=04&IniDay=1&IniMon="+mesfin+"&IniYear=2023&EndDay=31&EndMon="+mesfin+"&EndYear=2023&FlagDate=1&fpago=0&prio=0&cualobs=0&sinlimite=on&VoyI=1&Opcion=3&Reg=LORETOOBLCONSOLID&Voy=1&Num99=0&Num2=0&Usu=LORETOselenesm&Emp=OBLMKTPALM&cmdEnviar=Enviar+Datos"
    pagina = r.post(urlpo, datadoc, verify=False, allow_redirects=True)
    pagina = BeautifulSoup(pagina.text,'html.parser')
    ocs = pagina.find_all(text = re.compile("OC-"))
    for oc in ocs:
        listocs.append(oc)    
    ulinks = pagina.find_all("a", href=re.compile(r"POautoriza?"))
    for link in ulinks:
        links.append("https://villas.esasacloud.com/avance/cgi-bin/e-sasa/"+link['href'])
#commit the link