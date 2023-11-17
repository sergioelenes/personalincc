from flask import Flask, render_template, request, redirect, url_for, flash
from flask_basicauth import BasicAuth
import requests
from bs4 import BeautifulSoup
import time
import re
import urllib3
urllib3.disable_warnings()
from funciones import firma2rec, firmaPalmita, firmaporoc, firmaVDA, oblservices, ocs_cdgolf, provsservices, provscdg, links, listocs, urlpo, r

provsvdpl = ["A1190*", "A3888*", "A1855*", "A0201*","A3074*", "A6590*", "A0185*", "A3713*", "A0007*", "A0308*", "A3599*", "A0411*", "A3551*", "A2914*","A3004*", "C1002*", "D0099*", "A0739*", "D1178*", "A0176*", "A0465*", "XXX*"]

app = Flask(__name__)
app.secret_key = "Macarenas"
app.config['BASIC_AUTH_USERNAME'] = 'elenes'
app.config['BASIC_AUTH_PASSWORD'] = 'sElenes2020'
basic_auth = BasicAuth(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
@basic_auth.required
def loginroute():
        return render_template('ocss.html')

@app.route("/oblvdpl", methods=['POST'])
def oblvdpl():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        for proveedor in provsvdpl:
            firma2rec('OBLPALMAR',proveedor,str(int(mesfin)-1), mesfin)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs),'ocs')   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocss.html')
        
@app.route("/palmita", methods=['POST'])
def palmita():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        firmaPalmita(mesfin)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs),'ocs')   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocss.html')
        

@app.route("/vda", methods=['POST'])
def vdata():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        firmaVDA(mesfin)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs),'ocs')   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocss.html')

@app.route("/poroc", methods=['POST'])
def poroc():
    if request.method == 'POST':
        oc = request.form['numoc']
        mesfin = request.form['mes_final']
        firmaporoc(oc,mesfin)
        flash('Se autorizó la '+str(listocs)+'','ocs')
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocss.html')

@app.route("/oblservices", methods=['POST'])
def oblservicess():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        for proveedor in provsservices:
            oblservices(mesfin, proveedor)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs),'ocs')   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocss.html')
    
@app.route("/cdgolf", methods=['POST'])
def cdgolf():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        for proveedor in provscdg:
            ocs_cdgolf(mesfin, proveedor)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs),'ocs')   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocss.html')

@app.route("/cambiacontra", methods=['GET','POST'])
@basic_auth.required
def cambiacontra():
        if request.method == 'POST':
                passwnew = request.form['nwpass']
                if passwnew == '':
                        passwd_confirmation = open('la_linfomana.txt', 'r')
                        passw = passwd_confirmation.read()
                        passwd_confirmation.close()
                        flash(f' el password actual es "  {passw}  "','contra')
                else:
                        with open('la_linfomana.txt', 'w') as f:
                                f.write(passwnew)
                        passwd_confirmation = open('la_linfomana.txt', 'r')
                        passw = passwd_confirmation.read()
                        passwd_confirmation.close()
                        flash(f' el password se a modificado correctamente a "  {passw}  "','contra')
                return render_template('ocss.html')

@app.route("/addprovs", methods=['GET','POST'])
@basic_auth.required
def addprovs():
        if request.method == 'POST':
                if request.form['newprov'] == "":
                        pass
                elif request.form['newprov'] != "":
                        provsvdpl.append(request.form['newprov'])
                
                flash(f' listado de proveedores:  {provsvdpl}','provs')
                return render_template('ocss.html')

@app.route("/remprovs", methods=['GET','POST'])
@basic_auth.required
def remprovs():
        if request.method == 'POST':
                if request.form['remprovs'] == "":
                        pass
                elif request.form['remprovs'] != "":
                        provsvdpl.remove(request.form['remprovs'])
                
                flash(f' listado de proveedores:  {provsvdpl}','provs')
                return render_template('ocss.html')
        






if __name__=='__main__':
    app.run(debug=True)