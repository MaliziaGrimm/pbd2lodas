from flask import Flask
from flask import request
import os, webbrowser
from flask import render_template
from shutil import copyfile

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/basisdaten.html', methods=['POST', 'GET'])
def basisdaten():
    if request.method == 'POST':
    #    if os.path.exists("daten/basisdaten.txt"):
        ## Datei öffnen und Daten werden angehangen
    #        fileziel=open("daten/basisdaten.txt","a")
    #    else:
        fileziel=open("daten/basisdaten.txt","w")
        # schreiben in Datei für Basisdaten
        fileziel.write(request.form['form_berater']+"|"+request.form['form_mandant']+"|"+request.form['form_monat']+"|"+request.form['form_jahr'])
        fileziel.close()
    else:
        pass
    return render_template('basisdaten.html')

###############################################
#### Stundenerfassung und Anlage der Daten ####

@app.route('/erfassungstunden.html', methods=['POST', 'GET'])
def stundenerfassung():

## stammdaten lesen - qualitätssicherung fehlt noch 
    if os.path.exists("daten/basisdaten.txt"):
        filequelle=open("daten/basisdaten.txt","r", encoding='utf-8')
        for x in filequelle:
            var_beraternummer,var_mandantenummer,var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        return render_template('basisdaten.html')

    if request.method == 'POST':
        if os.path.exists("daten/abrechnungsdaten.txt"):
        ## Datei öffnen und Daten werden angehangen
            fileziel=open("daten/abrechnungsdaten.txt","a")
        else:
        ## Datei neu öffnen und Kopfdaten schreiben
            fileziel=open("daten/abrechnungsdaten.txt","w")
        # schreiben in Lodas Importdatei
            fileziel.write("[Allgemein]\nZiel=LODAS\nVersion_SST=1.0\nBeraterNr=")
            fileziel.write(var_beraternummer)
            fileziel.write("\nMandantenNr=")
            fileziel.write(var_mandantenummer)
            fileziel.write("\nStringbegrenzer='")
            fileziel.write("\n\n* LEGENDE:\n* Datei erzeugt mit Tool pbd2lodas\n* AP: Andreé Rosenkranz; andree@rosenkranz.one\n\n")
            fileziel.write("* Satzbeschreibungen zur Übergabe von Bewegungsdaten für Mitarbeiter\n\n")
            fileziel.write("\n10;u_lod_bwd_buchung_standard;abrechnung_zeitraum#bwd;pnr#bwd;la_eigene#bwd;bs_nr#bwd;bs_wert_butab#bwd;kostenstelle#bwd;")
            fileziel.write("\n\n")
            fileziel.write("* Stunden und Beträge zur Abrechnung von Mitarbeitern\n\n")
            fileziel.write("[Bewegungsdaten]\n\n")
# Qualitätssicherung auf frontend kommt noch
        if request.form['form_personalnummer'] == "" or request.form['form_lohnart'] == "" or request.form['form_wert'] == "":
            print("Fehler PNR")
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['form_lohnart']+";1;"+request.form['form_wert']+";"+request.form['form_kostenstelle']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl2'] == "" or request.form['fw2'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl2']+";1;"+request.form['fw2']+";"+request.form['fk2']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl3'] == "" or request.form['fw3'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl3']+";1;"+request.form['fw3']+";"+request.form['fk3']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl4'] == "" or request.form['fw4'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl4']+";1;"+request.form['fw4']+";"+request.form['fk4']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl5'] == "" or request.form['fw5'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl5']+";1;"+request.form['fw5']+";"+request.form['fk5']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl6'] == "" or request.form['fw6'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl6']+";1;"+request.form['fw6']+";"+request.form['fk6']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl7'] == "" or request.form['fw7'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl7']+";1;"+request.form['fw7']+";"+request.form['fk7']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl8'] == "" or request.form['fw8'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl8']+";1;"+request.form['fw8']+";"+request.form['fk8']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl9'] == "" or request.form['fw9'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl9']+";1;"+request.form['fw9']+";"+request.form['fk9']+";\n")
        fileziel.close()
    else:
        pass
    
    return render_template('erfassungstunden.html', v_bnr=var_beraternummer, v_mdt=var_mandantenummer, v_monat=var_abrmonat, v_jahr=var_abrjahr)


@app.route('/erfassungbetrag.html', methods=['POST', 'GET'])
def betragerfassung():
    
    if os.path.exists("daten/basisdaten.txt"):
        filequelle=open("daten/basisdaten.txt","r", encoding='utf-8')
        for x in filequelle:
            var_beraternummer,var_mandantenummer,var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        return render_template('basisdaten.html')
    
    if request.method == 'POST':
## stammdaten lesen - qualitätssicherung fehlt noch 
        if os.path.exists("daten/abrechnungsdaten.txt"):
        ## Datei öffnen und Daten werden angehangen
            fileziel=open("daten/abrechnungsdaten.txt","a")
        else:
        ## Datei neu öffnen und Kopfdaten schreiben
            fileziel=open("daten/abrechnungsdaten.txt","w")
        # schreiben in Lodas Importdatei
            fileziel.write("[Allgemein]\nZiel=LODAS\nVersion_SST=1.0\nBeraterNr=")
            fileziel.write(var_beraternummer)
            fileziel.write("\nMandantenNr=")
            fileziel.write(var_mandantenummer)
            fileziel.write("\nStringbegrenzer='")
            fileziel.write("\n\n* LEGENDE:\n* Datei erzeugt mit Tool pbd2lodas\n* AP: Andreé Rosenkranz; andree@rosenkranz.one\n\n")
            fileziel.write("* Satzbeschreibungen zur Übergabe von Bewegungsdaten für Mitarbeiter\n\n")
            fileziel.write("\n10;u_lod_bwd_buchung_standard;abrechnung_zeitraum#bwd;pnr#bwd;la_eigene#bwd;bs_nr#bwd;bs_wert_butab#bwd;kostenstelle#bwd;")
            fileziel.write("\n\n")
            fileziel.write("* Stunden und Beträge zur Abrechnung von Mitarbeitern\n\n")
            fileziel.write("[Bewegungsdaten]\n\n")

        if request.form['form_personalnummer'] == "" or request.form['form_lohnart'] == "" or request.form['form_wert'] == "":
## pflichtfelder noch im frontend einbauen
            print("Fehler")
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['form_lohnart']+";2;"+request.form['form_wert']+";"+request.form['form_kostenstelle']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl2'] == "" or request.form['fw2'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl2']+";2;"+request.form['fw2']+";"+request.form['fk2']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl3'] == "" or request.form['fw3'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl3']+";2;"+request.form['fw3']+";"+request.form['fk3']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl4'] == "" or request.form['fw4'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl4']+";2;"+request.form['fw4']+";"+request.form['fk4']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl5'] == "" or request.form['fw5'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl5']+";2;"+request.form['fw5']+";"+request.form['fk5']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl6'] == "" or request.form['fw6'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl6']+";2;"+request.form['fw6']+";"+request.form['fk6']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl7'] == "" or request.form['fw7'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl7']+";2;"+request.form['fw7']+";"+request.form['fk7']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl8'] == "" or request.form['fw8'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl8']+";2;"+request.form['fw8']+";"+request.form['fk8']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fl9'] == "" or request.form['fw9'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+request.form['fl9']+";2;"+request.form['fw9']+";"+request.form['fk9']+";\n")
        fileziel.close()
    else:
        pass
    return render_template('erfassungbetrag.html', v_bnr=var_beraternummer, v_mdt=var_mandantenummer, v_monat=var_abrmonat, v_jahr=var_abrjahr)

@app.route('/konvertierung.html', methods=['POST', 'GET'])
def konvert():
    if os.path.exists("daten/basisdaten.txt"):
        filequelle=open("daten/basisdaten.txt","r", encoding='utf-8')
        for x in filequelle:
            var_beraternummer,var_mandantenummer,var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        print("Es gibt keine Basisdaten, also auch nichts zum kovertieren!")

    if os.path.exists("daten/abrechnungsdaten.txt"):
        copyfile('daten/abrechnungsdaten.txt', 'daten/'+var_abrjahr+var_abrmonat+'_'+var_mandantenummer+'_'+var_beraternummer+'_lodas.txt') 
        os.remove('daten/basisdaten.txt')
        os.remove('daten/abrechnungsdaten.txt')
        print("Zieldatei für Lodas wurde angelegt, Quellen gelöscht!")
    else:
        print("Es konnte keine Zieldatei erzeugt werden")

    return render_template('index.html')

webbrowser.open('http://localhost:1701')

if __name__ =='__main__':
    app.run(port=1701, debug=False)