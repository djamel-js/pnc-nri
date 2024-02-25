from django.contrib import admin
from .models import Patient, Antecedent, Chirurgie, TraitementMedical, AnomalieGenetique, HistoireMaladie, EtatClinique, EtatNeurologique, AutresSignesCliniques, Exploration, Diagnostic, Traitement, Microchirurgie, TraitementEndovasculaire, Radiochirurgie, Complications, PriseEnCharge, SuiviMedical, ExamensImagerie, EvolutionSymptomes, EvaluationPostOp  # Ajoutez d'autres modèles ici

admin.site.register(Patient)
admin.site.register(Antecedent)
admin.site.register(Chirurgie)
admin.site.register(TraitementMedical)
admin.site.register(AnomalieGenetique)
admin.site.register(HistoireMaladie)
admin.site.register(EtatClinique)
admin.site.register(EtatNeurologique)
admin.site.register(AutresSignesCliniques)
admin.site.register(Exploration)
admin.site.register(Diagnostic)
admin.site.register(Traitement)
admin.site.register(Microchirurgie)
admin.site.register(TraitementEndovasculaire)
admin.site.register(Radiochirurgie)
admin.site.register(Complications)
admin.site.register(PriseEnCharge)
admin.site.register(SuiviMedical)
admin.site.register(ExamensImagerie)
admin.site.register(EvolutionSymptomes)
admin.site.register(EvaluationPostOp)  # Ajoutez d'autres modèles ici