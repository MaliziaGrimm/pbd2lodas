# pbd2lodas
Abrechnungsdatenerfassung für DATEV Lodas

Mit diesem Tool können Stunden und Beträge für die DATEV Lohnabrechnung (LODAS) vorerfasst und an die abrechnenden Stelle übergeben werden.

Es wird pro Abrechnungsmonat eine Datei erstellt. 

Im ersten Schritt werden die Grunddaten angelegt, dann können Stunden und Beträge erfasst werden. Optional können Kostenstellen erfasst werden. Sind alle Daten erfasst, dann kann eine Exportdatei erstellt werden. Diese Exportdatei kann im Programm Lodas importiert werden. 

pbd2lodas im Branche master ist die Vollversion. Damit kann das Tool konfiguriert werden und die Vorerfassung kann erfolgen. 
pbd2lodas_stb im Branche stb ist das Modul für den Steuerberater/die Abrechnungsstelle. Mit dem Modul kann nur die Datei basisdaten.txt erstellt werden, in dieser Datei werden Beraternummer und Mandantennummer gespeichert, sowie die 5 Lohnarten für Stunden und die 5 Lohnarten für Beträge. Diese Lohnarten werden im Mandantenmosul fest vorgeschlagen, zusätzlich können je Mitarbeiter 4 freie Lohnarten erfasst werden.
pbd2lodas_mdt im Branche mandant ist das Mandantenmodul, bzw. das Modul für die vorerfassende Stelle. Mit der Datei basisdaten.txt vom Steuerbüro können Stunden und Beträge schnell erfasst werden. Die Datei muss der Steuerberater/die abrechnende Stelle erstellen.

Danke an w3.css - diese Quelle ergibt das Design vom frontend.
