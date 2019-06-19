from flask import Flask
from flask import request
import os, webbrowser
from flask import render_template
from shutil import copyfile

app = Flask(__name__)

@app.route('/')
def homepage():
    var_text="Fehlerhinweise stehen hier! Jetzt ist alles ok!"
    return render_template('index.html', v_text=var_text)

@app.route('/index.html', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        fileziel=open("daten/abrechnungszeitraum.txt","w")
        fileziel.write(request.form['form_monat']+"|"+request.form['form_jahr'])
        fileziel.close()
        var_text="Fehlerhinweise stehen hier! Jetzt ist alles ok!"
    else:
        var_text="Fehlerhinweise stehen hier! Jetzt ist alles ok!"
        pass
    return render_template('index.html', v_text=var_text)

@app.route('/basisdaten.html', methods=['POST', 'GET'])
def basisdaten():
##############################################################
### Anlage der Stammdaten für die Erfassung
### Beraternummer, Mandant und Lohnarten mit Text = 5 für Stunden, 5 für Betrag
##############################################################

    if request.method == 'POST':
        fileziel=open("daten/basisdaten.txt","w")
        # schreiben in Datei für Basisdaten
        fileziel.write(request.form['form_berater']+"|"+request.form['form_mandant']+"|")
        if (request.form['loa_ns1'] != "" and request.form['loa_ts1'] != "") and (request.form['loa_ns1'] != "Nummer") :
            fileziel.write(request.form['loa_ns1']+"|"+request.form['loa_ts1']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns2'] != "" and request.form['loa_ts2'] != "") and (request.form['loa_ns2'] != "Nummer"):
            fileziel.write(request.form['loa_ns2']+"|"+request.form['loa_ts2']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns3'] != "" and request.form['loa_ts3'] != "" ) and (request.form['loa_ns3'] != "Nummer"):
            fileziel.write(request.form['loa_ns3']+"|"+request.form['loa_ts3']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns4'] != "" and request.form['loa_ts4'] != "") and (request.form['loa_ns4'] != "Nummer"):
            fileziel.write(request.form['loa_ns4']+"|"+request.form['loa_ts4']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns5'] != "" and request.form['loa_ts5'] != "") and (request.form['loa_ns5'] != "Nummer"):
            fileziel.write(request.form['loa_ns5']+"|"+request.form['loa_ts5']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb1'] != "" and request.form['loa_tb1'] != "") and (request.form['loa_nb1'] != "Nummer"):
            fileziel.write(request.form['loa_nb1']+"|"+request.form['loa_tb1']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb2'] != "" and request.form['loa_tb2'] != "") and (request.form['loa_nb2'] != "Nummer"):
            fileziel.write(request.form['loa_nb2']+"|"+request.form['loa_tb2']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb3'] != "" and request.form['loa_tb3'] != "") and (request.form['loa_nb3'] != "Nummer"):
            fileziel.write(request.form['loa_nb3']+"|"+request.form['loa_tb3']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb4'] != "" and request.form['loa_tb4'] != "") and (request.form['loa_nb4'] != "Nummer"):
            fileziel.write(request.form['loa_nb4']+"|"+request.form['loa_tb4']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb5'] != "" and request.form['loa_tb5'] != "") and (request.form['loa_nb5'] != "Nummer"):
            fileziel.write(request.form['loa_nb5']+"|"+request.form['loa_tb5'])
        else:
            fileziel.write("nicht|buchen")
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
        filequelle=open("daten/basisdaten.txt","r")
        for x in filequelle:
            var_beraternummer,var_mandantenummer,var_3,var_4,var_5,var_6,var_7,var_8,var_9,var_10,var_11,var_12,var_13,var_14,var_15,var_16,var_17,var_18,var_19,var_20,var_21,var_22=x.split("|")
            break
        filequelle.close()
    else:
        return render_template('basisdaten.html')
    if os.path.exists("daten/abrechnungszeitraum.txt"):
        filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
        for x in filequelle:
            var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        var_text="Fehler: **** Du hast noch keinen Abrechnungszeitraum angelegt!"
        return render_template('index.html', v_text=var_text)

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
            fileziel.write("* Satzbeschreibungen zur Übergabe von Bewegungsdaten für Mitarbeiter\n[Satzbeschreibung]\n")
            fileziel.write("\n10;u_lod_bwd_buchung_standard;abrechnung_zeitraum#bwd;pnr#bwd;la_eigene#bwd;bs_nr#bwd;bs_wert_butab#bwd;kostenstelle#bwd;")
            fileziel.write("\n\n")
            fileziel.write("* Stunden und Beträge zur Abrechnung von Mitarbeitern\n\n")
            fileziel.write("[Bewegungsdaten]\n\n")

        if request.form['form_personalnummer'] == "" or request.form['form_wert'] == "":
            print("Fehler PNR")
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_3+";1;"+request.form['form_wert']+";"+request.form['form_kostenstelle']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw2'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_5+";1;"+request.form['fw2']+";"+request.form['fk2']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw3'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_7+";1;"+request.form['fw3']+";"+request.form['fk3']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw4'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_9+";1;"+request.form['fw4']+";"+request.form['fk4']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw5'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_11+";1;"+request.form['fw5']+";"+request.form['fk5']+";\n")
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
    
    return render_template('erfassungstunden.html', v_bnr=var_beraternummer, v_mdt=var_mandantenummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_sn1=var_3,v_st1=var_4,v_sn2=var_5,v_st2=var_6,
    v_sn3=var_7,v_st3=var_8,v_sn4=var_9,v_st4=var_10,v_sn5=var_11,v_st5=var_12,v_bn1=var_13,v_bt1=var_14,v_bn2=var_15,v_bt2=var_16,v_bn3=var_17,v_bt3=var_18,v_bn4=var_19,v_bt4=var_20,v_bn5=var_21,
    v_bt5=var_22)


@app.route('/erfassungbetrag.html', methods=['POST', 'GET'])
def betragerfassung():
    
    if os.path.exists("daten/basisdaten.txt"):
        filequelle=open("daten/basisdaten.txt","r")
        for x in filequelle:
            var_beraternummer,var_mandantenummer,var_3,var_4,var_5,var_6,var_7,var_8,var_9,var_10,var_11,var_12,var_13,var_14,var_15,var_16,var_17,var_18,var_19,var_20,var_21,var_22=x.split("|")
            break
        filequelle.close()
    else:
        return render_template('basisdaten.html')
    if os.path.exists("daten/abrechnungszeitraum.txt"):
        filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
        for x in filequelle:
            var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        var_text="Fehler: **** Du hast noch keinen Abrechnungszeitraum angelegt!"
        return render_template('index.html', v_text=var_text)
    
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
            fileziel.write("* Satzbeschreibungen zur Übergabe von Bewegungsdaten für Mitarbeiter\n[Satzbeschreibung]\n")
            fileziel.write("\n10;u_lod_bwd_buchung_standard;abrechnung_zeitraum#bwd;pnr#bwd;la_eigene#bwd;bs_nr#bwd;bs_wert_butab#bwd;kostenstelle#bwd;")
            fileziel.write("\n\n")
            fileziel.write("* Stunden und Beträge zur Abrechnung von Mitarbeitern\n\n")
            fileziel.write("[Bewegungsdaten]\n\n")

        if request.form['form_personalnummer'] == "" or request.form['form_wert'] == "":
            print("Fehler im backend - kann aber nicht sein!")
## pflichtfelder noch im frontend einbauen
    
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_13+";2;"+request.form['form_wert']+";"+request.form['form_kostenstelle']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw2'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_15+";2;"+request.form['fw2']+";"+request.form['fk2']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw3'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_17+";2;"+request.form['fw3']+";"+request.form['fk3']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw4'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_19+";2;"+request.form['fw4']+";"+request.form['fk4']+";\n")
        if request.form['form_personalnummer'] == "" or request.form['fw5'] == "":
            pass
        else:
            fileziel.write("10;01/"+var_abrmonat+"/"+var_abrjahr+";"+request.form['form_personalnummer']+";"+var_21+";2;"+request.form['fw5']+";"+request.form['fk5']+";\n")
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
    return render_template('erfassungbetrag.html', v_bnr=var_beraternummer, v_mdt=var_mandantenummer, v_monat=var_abrmonat, v_jahr=var_abrjahr,v_sn1=var_3,v_st1=var_4,v_sn2=var_5,v_st2=var_6,
    v_sn3=var_7,v_st3=var_8,v_sn4=var_9,v_st4=var_10,v_sn5=var_11,v_st5=var_12,v_bn1=var_13,v_bt1=var_14,v_bn2=var_15,v_bt2=var_16,v_bn3=var_17,v_bt3=var_18,v_bn4=var_19,v_bt4=var_20,v_bn5=var_21,
    v_bt5=var_22)

@app.route('/konvertierung.html', methods=['POST', 'GET'])
def konvert():
    if os.path.exists("daten/abrechnungszeitraum.txt"):
        filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
        for x in filequelle:
            var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        var_text="Fehler: **** Es gibt keinen Abrechnungszeitraum, bitte Abrechnungszeitraum anlegen! ****"
    
    if os.path.exists("daten/basisdaten.txt"):
        filequelle=open("daten/basisdaten.txt","r")
        for x in filequelle:
            var_beraternummer,var_mandantenummer,var_3,var_4,var_5,var_6,var_7,var_8,var_9,var_10,var_11,var_12,var_13,var_14,var_15,var_16,var_17,var_18,var_19,var_20,var_21,var_22=x.split("|")
            break
        filequelle.close()
    else:
        var_text=("Es gibt keine Basisdaten, bitte Basisdaten (BNR/Mandant) anlegen!")


    if os.path.exists("daten/abrechnungsdaten.txt"):
        copyfile('daten/abrechnungsdaten.txt', 'daten/'+var_abrjahr+var_abrmonat+'_'+var_mandantenummer+'_'+var_beraternummer+'_lodas.txt') 
        os.remove('daten/abrechnungszeitraum.txt')
        os.remove('daten/abrechnungsdaten.txt')
        var_text="Die Datei "+var_abrjahr+var_abrmonat+"_"+var_mandantenummer+"_"+var_beraternummer+"_lodas.txt wurde im Verzeichniss /daten erstellt. Stelle diese Datei deinem Steuerberater zur Verfügung"
    else:
        var_text="Fehler: **** Es gibt keine Datei mit Abrechnungsdaten, es konnte keine Datei konvertiert werden. ****"

    return render_template('index.html', v_text=var_text)

webbrowser.open('http://localhost:1701')

if __name__ =='__main__':
    app.run(port=1701, debug=False)