from django.db import models
import datetime, requests, os, pandas as pd
from django.core.files import File
from hack.settings import BASE_DIR

# Create your models here.

class Data_set(models.Model):

    index = models.IntegerField(null=True, blank = True)
    start = models.CharField(max_length=200, null=True, blank = True)
    STATE = models.CharField(max_length=200, null=True, blank = True)
    LGA = models.CharField(max_length=200, null=True, blank = True)
    Name_of_SEEFOR_FADAMA_Community_Association_SFCA = models.CharField(max_length=200, null=True, blank = True)
    Name_of_SEEFOR_FADAMA_User_Groups_SFUG = models.CharField(max_length=200, null=True, blank = True)
    Type_of_Subproject_Enterprise = models.CharField(max_length=200, null=True, blank = True)
    CROP_PRODUCTION = models.CharField(max_length=200, null=True, blank = True)
    FISHERY = models.CharField(max_length=200, null=True, blank = True)
    LIVESTOCK = models.CharField(max_length=200, null=True, blank = True)
    POULTRY = models.CharField(max_length=200, null=True, blank = True)
    PROCESSING = models.CharField(max_length=200, null=True, blank = True)
    MARKETING = models.CharField(max_length=200, null=True, blank = True)
    RURAL_INFRASTRUCTURE = models.CharField(max_length=200, null=True, blank = True)
    FORESTRY = models.CharField(max_length=200, null=True, blank = True)
    Total_Cost_of_SubProject = models.FloatField(null=True, blank = True)
    IDA_Amount = models.FloatField(null=True, blank = True)
    Beneficiary_Contribution = models.FloatField(null=True, blank = True)
    Total_Amount_Disbursed = models.FloatField(null=True, blank = True)
    Date_of_disbursement = models.CharField(max_length=200, null=True, blank = True)
    Status_of_SubProject = models.CharField(max_length=200, null=True, blank = True)
    Duration_of_SubProject_Implementation = models.CharField(max_length=200, null=True, blank = True)
    Total_Number_of_Service_Providers = models.FloatField(null=True, blank = True)
    Total_number_of_enterprise_beneficiaries = models.FloatField(null=True, blank = True)
    access_to_extension = models.FloatField(null=True, blank = True)
    access_to_project_support_service = models.CharField(max_length=200, null=True, blank = True)
    access_to_capacity_building_services = models.FloatField(null=True, blank = True)
    access_to_advisory_services = models.FloatField(null=True, blank = True)
    access_to_rural_infrastructure_services = models.FloatField(null=True, blank = True)
    access_to_input_support = models.FloatField(null=True, blank = True)
    Number_of_Meetings = models.FloatField(null=True, blank = True)
    Frequency_of_meetings_held_by_Group = models.FloatField(null=True, blank = True)
    Average_Size_of_Each_Members_Household = models.FloatField(null=True, blank = True)
    Number_of_Direct_Beneficiaries_Male = models.FloatField(null=True, blank = True)
    Number_of_Direct_Beneficiaries_Female = models.FloatField(null=True, blank = True)
    Number_of_beneficiaries_under_supported_services_Male = models.FloatField(null=True, blank = True)
    female_beneficiaries_under_support_services = models.FloatField(null=True, blank = True)
    Number_of_Indirect_Beneficiaries_Male = models.FloatField(null=True, blank = True)
    Number_of_Indirect_Beneficiaries_Female = models.FloatField(null=True, blank = True)
    permanently_employed_males = models.FloatField(null=True, blank = True)
    permanently_employed_females = models.FloatField(null=True, blank = True)
    temporarily_employed_males = models.FloatField(null=True, blank = True)
    temporarily_employed_females = models.FloatField(null=True, blank = True)
    Crop_Production_Metric_Tons_per_Hecta = models.FloatField(null=True, blank = True)
    Fishery_Number_of_Kg = models.FloatField(null=True, blank = True)
    Livestock_Number_of_Livestock = models.FloatField(null=True, blank = True)
    Poultry_Number_of_Birds = models.FloatField(null=True, blank = True)
    Poultry_Crate_of_Eggs = models.FloatField(null=True, blank = True)
    Processing_Volume_of_Produce_Processed_Kg = models.FloatField(null=True, blank = True)
    Number_of_Production_Cycle = models.FloatField(null=True, blank = True)
    FUEF_Amount_Saved = models.FloatField(null=True, blank = True)
    Picture_of_Subproject_1 = models.CharField(max_length=200, null=True, blank = True)
    Picture_of_Subproject_2 = models.CharField(max_length=200, null=True, blank = True)
    GPS_Coordinates_of_site = models.CharField(max_length=200, null=True, blank = True)
    _GPS_Coordinates_of_site_latitude = models.FloatField(null=True, blank = True)
    _GPS_Coordinates_of_site_longitude = models.FloatField(null=True, blank = True)
    _GPS_Coordinates_of_site_altitude = models.FloatField(null=True, blank = True)
    _GPS_Coordinates_of_site_precision = models.FloatField(null=True, blank = True)
    Success_Stories_due_to_presence_of_intervention = models.CharField(max_length=200, null=True, blank = True)
    Do_you_have_any_challenges = models.CharField(max_length=200, null=True, blank = True)
    If_yes_what_is_the_challenge = models.CharField(max_length=200, null=True, blank = True)
    Risk_factors = models.CharField(max_length=200, null=True, blank = True)
    Risk_factorsMilitancy = models.FloatField(null=True, blank = True)
    Risk_factorsOil_Spillage = models.FloatField(null=True, blank = True)
    Risk_factorsFlood = models.FloatField(null=True, blank = True)
    Risk_factorsOthers = models.FloatField(null=True, blank = True)
    If_others_specify = models.CharField(max_length=200, null=True, blank = True)
    Name_of_Data_Collector = models.CharField(max_length=200, null=True, blank = True)
    Signature_of_Data_Collector = models.CharField(max_length=200, null=True, blank = True)
    Name_of_SEEFOR_FADAMA_User_Groups_SFUGs = models.FloatField(null=True, blank = True)
    Type_of_enterprise = models.FloatField(null=True, blank = True)
    Total_number_of_membership = models.FloatField(null=True, blank = True)
    Frequency_of_meetings_held = models.FloatField(null=True, blank = True)
    Number_of_Male = models.FloatField(null=True, blank = True)
    Number_of_Female = models.FloatField(null=True, blank = True)
    Frequency_of_meetings_held_by_Groups = models.FloatField(null=True, blank = True)
    Number_of_person_employed_on_permanent_basis_Male1 = models.FloatField(null=True, blank = True)
    Number_of_person_employed_on_permanent_basis_Female1 = models.FloatField(null=True, blank = True)
    Number_of_person_employed_on_temporary_basis_Male1 = models.FloatField(null=True, blank = True)
    Number_of_person_employed_on_temporary_basis_Female1 = models.FloatField(null=True, blank = True)
    access_to_project_support_service1 = models.FloatField(null=True, blank = True)
    Amount_disbursed = models.FloatField(null=True, blank = True)
    Duration_of_SubProject = models.FloatField(null=True, blank = True)
    Total_Number_of_Service_Provider = models.FloatField(null=True, blank = True)
    Picture_of_Site = models.FloatField(null=True, blank = True)
    GIS_Coordinates_of_site = models.FloatField(null=True, blank = True)
    _GIS_Coordinates_of_site_latitude = models.FloatField(null=True, blank = True)
    _GIS_Coordinates_of_site_longitude = models.FloatField(null=True, blank = True)
    _GIS_Coordinates_of_site_altitude = models.FloatField(null=True, blank = True)
    _GIS_Coordinates_of_site_precision = models.FloatField(null=True, blank = True)
    Increase_of_Agricultural_Production_for_SEEFOR_FADAMA = models.FloatField(null=True, blank = True)
    Picture_of_Subproject = models.FloatField(null=True, blank = True)
    calculation = models.FloatField(null=True, blank = True)
    Number_of_Indirect_Beneficiaries_Male_calculation = models.FloatField(null=True, blank = True)
    calculation_001 = models.FloatField(null=True, blank = True)
    Number_of_Indirect_Beneficiaries_Female_calculation_001 = models.FloatField(null=True, blank = True)
    Sustainability_Measures = models.FloatField(null=True, blank = True)
    Picture_of_Subproject_3 = models.FloatField(null=True, blank = True)
    If_yes_specify = models.FloatField(null=True, blank = True)
    _id = models.IntegerField(null=True, blank = True)
    _uuid = models.CharField(max_length=200, null=True, blank = True)
    _submission_time = models.CharField(max_length=200, null=True, blank = True)
    _validation_status = models.FloatField(null=True, blank = True)
    _index = models.IntegerField(null=True, blank = True)

class Project(models.Model):
    title      = models.CharField( max_length = 200)
    data_url   = models.CharField( max_length = 200, blank = True, null = True)
    date       = models.DateTimeField(blank = True, null = True)
    data       =  models.FileField(upload_to = 'datasets/',blank=False,null=True)

    # def save_image(self, *args, **kwargs):

    #     super( Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def set_date_added(self):
        self.date = datetime.datetime.now()
        self.save()
    
    def set_data_url(self, url):
        self.data_url = url
        self.save()
    
    def add_data_set(self):


        headers = {'content-type': 'application/json', 'Authorization':'Token bcc979086ef1de7e787427fd1827abff776e1cd3'}
        response = requests.get(f"{self.data_url}.csv", headers = headers)

        selected_title = self.title.replace("\\", "_").replace("/", "_")
        open( file = f'{selected_title}.csv', mode = 'wb').write(response.content)

        data_file = open( file = f'{selected_title}.csv', mode = 'rb')
        self.data = File(data_file)
        self.save()

        data_file.close()


    def get_lga_for_state(self, state = False):
        #for commit
        try:
            data = pd.read_csv(self.data)
            
            for column in data.columns:
                if state.lower() in column.lower():
                    selected_lga = column

            state_data = data[(data["STATE"] == state)]
            state_lga = state_data[selected_lga]

            return state_lga.unique()
            
        except NameError:
            return []

    def get_data_columns(self, state = False):

        try:
            data = pd.read_csv(self.data)
            data = data.drop(["STATE",	"LGABAYELSA",	"LGADELTA",	"LGAEDO",	"LGARIVERS"
], axis = 1)

            return data.columns
            
        except NameError:
            return []

    def compute_columns(self, state = False, lga = False, col1 = False, col2 = False, col3 = False):

        data = pd.read_csv(self.data)

        print(col1, col2, col3)
        try:
            if state and lga == "all": # IF STATE DATA IS SENT AS ALL 
                print('ALL STATE COLUMN PLOT CURRENTLY WORKING \n\n')
                values = self.two_col_plot_all(data, state , col1, col2)

            elif state and lga and col1  and not col2 and not col3: # IF ONLY ONE COLUMN SELECTED
                print('ONE COLUMN PLOT CURRENTLY WORKING \n\n')
                values = self.one_col_plot(data, state , lga , col1)

            elif state and lga and col1  and col2 and not col3: # IF TWO COLUMNS SELECTED
                print('TWO COLUMN PLOT CURRENTLY WORKING \n\n')
                values = self.two_col_plot(data, state , lga , col1, col2)
            
            elif True:
                pass

            return values

        except TypeError:
            return []

    def one_col_plot(self, data, state, lga , col1):

        for column in list(data.columns):

            if state.lower() in column.lower():
                selected_lga = column

        state_data = data[(data["STATE"] == state)]
        state_lga = state_data[state_data[selected_lga] == lga]

        distribution = []
        count   = []
        mean    = []
        minimum = []
        maximum = []


        if "object" in str(data[col1].dtype):

            distribution = state_lga[col1].value_counts().to_json()
            count   = int(state_lga[col1].count())

        else:
            
            count   = int(state_lga[col1].count())
            mean    = int(state_lga[col1].mean())
            minimum = int(state_lga[col1].min())
            maximum = int(state_lga[col1].max())

        return  {"distribution" : distribution , "count" : count, "mean" : mean , "minimum" : minimum, "maximum" : maximum }

    def two_col_plot(self, data, state, lga , col1, col2):

        for column in list(data.columns):

            if state.lower() in column.lower():
                selected_lga = column


        state_data = data[(data["STATE"] == state)]
        state_lga = state_data[state_data[selected_lga] == lga]

        distribution = []
        count   = []
        mean    = []
        minimum = []
        maximum = []


        if "object" in str(data[col1].dtype) and "object" in str(data[col2].dtype):

            stats = pd.crosstab(state_lga[col1], state_lga[col2])

            distribution = stats.to_json()
            count   = int(state_lga[col1].count())
        
        elif "object" in str(data[col1].dtype) and "int" in str(data[col2].dtype):

            stats = pd.groupby(state_lga[col1]).sum()[col2]

            distribution = stats.to_json()
            count   = int(state_lga[col1].count())

        else:
            
            count   = int(state_lga[col1].count())
            mean    = int(state_lga[col1].mean())
            minimum = int(state_lga[col1].min())
            maximum = int(state_lga[col1].max())

        return  {"distribution" : distribution , "count" : count, "mean" : mean , "minimum" : minimum, "maximum" : maximum }

    def two_col_plot_all(self, data, state, col1, col2):

        # if not state == "all":
        #     data = data[data["STATE"] == state]

        distribution = []
        count   = []
        mean    = []
        minimum = []
        maximum = []


        if "object" in str(data[col1].dtype):

            stats = pd.crosstab(data[col1], data[col2])

            distribution = stats.to_json()
            count   = int(data[col1].count())

        elif "object" in str(data[col1].dtype) and "int" in str(data[col2].dtype):

            stats = pd.groupby(data[col1]).sum()[col2]

            distribution = stats.to_json()
            count   = int(data[col1].count())

        else:
            
            count   = int(data[col1].count())
            mean    = int(data[col1].mean())
            minimum = int(data[col1].min())
            maximum = int(data[col1].max())

        return  {"distribution" : distribution , "count" : count, "mean" : mean , "minimum" : minimum, "maximum" : maximum }

    