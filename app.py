from flask import Flask, render_template, request, redirect, url_for, flash
from flask_basicauth import BasicAuth
import requests
from bs4 import BeautifulSoup
import time
import re
import urllib3
urllib3.disable_warnings()
from funciones import firma2rec, firmaPalmita, firmaporoc, firmaVDA, provs, links, listocs, urlpo, passw, r

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
        return render_template('ocs.html')

@app.route("/oblvdpl", methods=['POST'])
def oblvdpl():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        for proveedor in provs:
            firma2rec('OBLPALMAR',proveedor,str(int(mesfin)-1), mesfin)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs))   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocs.html')
        
@app.route("/palmita", methods=['POST'])
def palmita():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        firmaPalmita(mesfin)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs))   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocs.html')
        

@app.route("/vda", methods=['POST'])
def vdata():
    if request.method == 'POST':
        mesfin = request.form['mes_final']
        firmaVDA(mesfin)
        numocs = len(links)
        flash('Se autorizaron '+str(numocs)+' Ordenes de Compras, Se autorizaron: '+str(listocs))   
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocs.html')

@app.route("/poroc", methods=['POST'])
def poroc():
    if request.method == 'POST':
        oc = request.form['numoc']
        mesfin = request.form['mes_final']
        firmaporoc(oc,mesfin)
        flash('Se autorizó la '+str(listocs)+'')
        for link in links:
                requests.get(str(link), verify=False, allow_redirects=True)
                time.sleep(1)
        links.clear()
        listocs.clear()
        return render_template('ocs.html')






if __name__=='__main__':
    app.run(debug=True)