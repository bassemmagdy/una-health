from django.db import models
import uuid

class Glucose(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gerat = models.CharField(max_length=255, blank=True)
    serien_nummer = models.CharField(max_length=255, blank=True)
    gerate_zeitstempel=models.DateTimeField(null=True, blank=True)
    auf_zeichnungstyp =  models.CharField(max_length=255, blank=True)
    glukosewert_verlauf= models.CharField(max_length=255, blank=True)
    glukose_scan= models.CharField(max_length=255, blank=True)
    nicht_numerisches_schnellwirkendes_insulin = models.CharField(max_length=255, blank=True)
    schnellwirkendes_insulin = models.CharField(max_length=255, blank=True)
    nicht_numerische_nahrungsdaten=models.CharField(max_length=255, blank=True)
    kohlenhydrate_gramm = models.CharField(max_length=255, blank=True)
    kohlenhydrate_portionen= models.CharField(max_length=255, blank=True)
    nicht_numerisches_depotinsulin=models.CharField(max_length=255, blank=True)
    depot_insulin_einheiten = models.CharField(max_length=255, blank=True)
    notizen = models.CharField(max_length=255, blank=True)
    glukose_teststreifen= models.CharField(max_length=255, blank=True)
    keton= models.CharField(max_length=255, blank=True)
    mahlzeiteninsulin_einheiten = models.CharField(max_length=255, blank=True)
    korrekturinsulin_einheiten=models.CharField(max_length=255, blank=True)
    insulin_anderung_durch_anwender_einheiten =models.CharField(max_length=255, blank=True)
    user_id = models.CharField(max_length=255, blank=False)
    
