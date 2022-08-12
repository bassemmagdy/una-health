from django.apps import AppConfig
import pandas as pd
from dateutil import parser
import sys

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    
    def ready(self):
        def read_file():
            file_names = ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa','bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb','cccccccc-cccc-cccc-cccc-cccccccccccc')
            if 'runserver' in sys.argv:
                from base.models import Glucose

                if not Glucose.objects.all():
                    for file_name in file_names:
                        skipHeaderDf=pd.read_csv(f"{file_name}.csv", skiprows=[0])
                        records = skipHeaderDf.to_dict('records')
                        
                        instances = [Glucose(
                                gerat=record['Gerät'],
                                user_id=file_name,
                                serien_nummer=record['Seriennummer'],
                                gerate_zeitstempel=parser.parse(record['Gerätezeitstempel']),
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
                        Glucose.objects.bulk_create(instances)

        read_file()