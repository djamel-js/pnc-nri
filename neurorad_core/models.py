# Create your models here.
from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    adresse = models.TextField()
    wilaya = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    personne_a_contacter = models.CharField(max_length=255)
    email = models.EmailField()
    numero_secu_sociale = models.CharField(max_length=20)
    
    # Champs pour les options Assuré, Ayant droit, Démuni, Non assuré
    ASSURE = 'Assuré'
    AYANT_DROIT = 'Ayant droit'
    DEMUNI = 'Démuni'
    NON_ASSURE = 'Non assuré'
    AFFILIATION_CHOICES = [
        (ASSURE, 'CNAS'),
        (AYANT_DROIT, 'CASNOS'),
        (DEMUNI, 'Démuni'),
        (NON_ASSURE, 'Non assuré'),
    ]
    affiliation = models.CharField(
        max_length=11,
        choices=AFFILIATION_CHOICES,
        default=ASSURE,
    )

class Antecedent(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    maladies_chroniques = models.TextField()
    allergies_medicamenteuses = models.TextField()
    medicaments_en_cours = models.TextField()

class Chirurgie(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    type_chirurgie = models.TextField()
    resultats_complications = models.TextField()
    dates_details_interventions = models.TextField()
    commentaires = models.TextField()

class TraitementMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    traitement_en_cours = models.TextField()

class AnomalieGenetique(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    anomalie_connue = models.TextField()

class HistoireMaladie(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    symptomes_revelateurs = models.TextField()
    date_debut = models.DateField()
    duree = models.TextField()

class EtatClinique(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    groupe_sanguin = models.CharField(max_length=10)
    taille = models.FloatField()
    poids = models.FloatField()
    imc = models.FloatField()
    ta = models.CharField(max_length=15)
    temperature = models.FloatField()
    respiration = models.CharField(max_length=15)
    fr = models.FloatField()

class EtatNeurologique(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    score_wfns = models.FloatField()

class AutresSignesCliniques(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    description = models.TextField()

class Exploration(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    tdm_cerebrale = models.TextField()
    score_fisher = models.FloatField()
    angio_scanner_cerebral = models.TextField()
    irm_cerebrale = models.TextField()
    angiographie_cerebrale = models.TextField()
    doppler_transcranien = models.TextField()
    autres_explorations = models.TextField()

class Diagnostic(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    maladie = models.TextField()
    code_cim = models.CharField(max_length=10)
    lesion_unique_rompue = models.BooleanField()
    lesion_multiple_non_rompue = models.BooleanField()
    pathologie_associee = models.TextField()
    code_cim_pathologie_associee = models.CharField(max_length=10)

class Traitement(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    traitement_antiepileptique = models.TextField()
    therapie_triple_h = models.TextField()
    drogues_vasoactives = models.TextField()
    vasodilatateurs = models.TextField()

class Microchirurgie(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    type_traitement = models.TextField()
    operation_1 = models.TextField()
    operation_2 = models.TextField()
    operation_3 = models.TextField()

class TraitementEndovasculaire(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    coiling = models.CharField(max_length=255)
    coiling_assiste_balonnet = models.CharField(max_length=255)
    coiling_assiste_stent = models.CharField(max_length=255)
    flow_diverter = models.CharField(max_length=255)
    autres = models.TextField()
    reconstruction = models.TextField()
    quantification_unites = models.IntegerField()
    codification_acte = models.CharField(max_length=255)

class Radiochirurgie(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    diagnostic = models.TextField()
    code_cim = models.CharField(max_length=255)
    embolisation_prealable = models.BooleanField()
    nb_seances_embolisation = models.IntegerField()
    microchirurgie_prealable = models.BooleanField()
    nb_operations_microchirurgie = models.IntegerField()
    codification_acte = models.CharField(max_length=255)

class Complications(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    saignement_siege = models.TextField()
    delais_saignement = models.FloatField()
    decision_thérapeutique_saignement = models.TextField()
    acte_medicochirurgical_saignement = models.CharField(max_length=255)
    resultats_saignement = models.TextField()
    hydrocephalie = models.TextField()
    decision_thérapeutique_hydrocephalie = models.TextField()
    delais_apparition_hydrocephalie = models.FloatField()
    acte_medicochirurgical_hydrocephalie = models.CharField(max_length=255)
    resultats_hydrocephalie = models.TextField()
    vasospasme_localisation = models.TextField()
    deficit_neurologique_vasospasme = models.TextField()
    acte_medical_interventionnel_vasospasme = models.CharField(max_length=255)
    resultats_vasospasme = models.TextField()
    epilepsie_traitement_medical = models.TextField()
    resultats_epilepsie = models.TextField()
    complications_liees_acte = models.TextField()
    acte_medicochirurgical_autres = models.CharField(max_length=255)
    resultats_autres = models.TextField()

class PriseEnCharge(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    traitement_medical = models.TextField()
    reeducation_fonctionnelle = models.TextField()
    traitement_suivi_comorbidites = models.TextField()
    prise_en_charge_psychologique = models.TextField()

class SuiviMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    frequence_consultations_3mois = models.BooleanField()
    frequence_consultations_12mois = models.BooleanField()
    consultation_post_op_demande = models.BooleanField()

class ExamensImagerie(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    angiographie_controle_3_6mois = models.BooleanField()
    angiographie_controle_12mois = models.BooleanField()
    angiographie_controle_24mois = models.BooleanField()
    angio_irm_angioscanner_suivi_tardif = models.BooleanField()

class EvolutionSymptomes(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    nouveaux_symptomes = models.TextField()
    amelioration_symptomes = models.TextField()

class EvaluationPostOp(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    evaluation = models.TextField()

# Ajoutez d'autres modèles pour les sections restantes de la fiche médicale
