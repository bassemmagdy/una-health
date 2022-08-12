from pyexpat import model
import pandas as pd
import api.models as models
skipHeaderDf=pd.read_csv('a.csv', skiprows=[0])

print(skipHeaderDf.shape)
print(skipHeaderDf.to_dict('records')[0])
records = skipHeaderDf.to_dict('records')
# print(skipHeaderDf.loc[0,'Gerätezeitstempel'])

skipHeaderDf.rename(columns={"Gerätezeitstempel": "a", "B": "c"})
model_instances = [models.Glucose(
    gerat=record['Gerät'],
    serien_nummer=record['Seriennummer'],
    gerate_zeitstempel=record['Gerätezeitstempel'],
    auf_zeichnungstyp=record['Aufzeichnungstyp'],
    glukosewert_verlauf=record['Glukosewert-Verlauf mg/dL'],
    glukose_scan=record['Glukose-Scan mg/dL'],
    nicht_numerisches_schnellwirkendes_insulin=record['Nicht numerisches schnellwirkendes Insulin'],
    schnellwirkendes_insulin=record['Schnellwirkendes Insulin (Einheiten)'],
    nicht_numerische_nahrungsdaten=record['Nicht numerische Nahrungsdaten'],
    kohlenhydrate_gramm=record['Kohlenhydrate (Gramm)'],
    kohlenhydrate_portionen=record['Kohlenhydrate (Portionen)'],
    nicht_numerisches_depotinsulin=record['Nicht numerisches Depotinsulin'],
    depot_insulin_einheiten=record['Depotinsulin (Einheiten)'],
    notizen=record['Notizen'],
    glukose_teststreifen=record['Glukose-Teststreifen mg/dL'],
    keton=record['Keton mmol/L'],
    mahlzeiteninsulin_einheiten=record['Mahlzeiteninsulin (Einheiten)'],
    korrekturinsulin_einheiten=record['Korrekturinsulin (Einheiten)'],
    insulin_anderung_durch_anwender_einheiten=record['Insulin-Änderung durch Anwender (Einheiten)'],
) for record in records]

print (model_instances)