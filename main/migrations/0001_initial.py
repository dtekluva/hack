# Generated by Django 3.0.3 on 2020-02-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('start', models.CharField(blank=True, max_length=200, null=True)),
                ('STATE', models.CharField(blank=True, max_length=200, null=True)),
                ('LGA', models.CharField(blank=True, max_length=200, null=True)),
                ('Name_of_SEEFOR_FADAMA_Community_Association_SFCA', models.CharField(blank=True, max_length=200, null=True)),
                ('Name_of_SEEFOR_FADAMA_User_Groups_SFUG', models.CharField(blank=True, max_length=200, null=True)),
                ('Type_of_Subproject_Enterprise', models.CharField(blank=True, max_length=200, null=True)),
                ('CROP_PRODUCTION', models.CharField(blank=True, max_length=200, null=True)),
                ('FISHERY', models.CharField(blank=True, max_length=200, null=True)),
                ('LIVESTOCK', models.CharField(blank=True, max_length=200, null=True)),
                ('POULTRY', models.CharField(blank=True, max_length=200, null=True)),
                ('PROCESSING', models.CharField(blank=True, max_length=200, null=True)),
                ('MARKETING', models.CharField(blank=True, max_length=200, null=True)),
                ('RURAL_INFRASTRUCTURE', models.CharField(blank=True, max_length=200, null=True)),
                ('FORESTRY', models.CharField(blank=True, max_length=200, null=True)),
                ('Total_Cost_of_SubProject', models.FloatField(blank=True, null=True)),
                ('IDA_Amount', models.FloatField(blank=True, null=True)),
                ('Beneficiary_Contribution', models.FloatField(blank=True, null=True)),
                ('Total_Amount_Disbursed', models.FloatField(blank=True, null=True)),
                ('Date_of_disbursement', models.CharField(blank=True, max_length=200, null=True)),
                ('Status_of_SubProject', models.CharField(blank=True, max_length=200, null=True)),
                ('Duration_of_SubProject_Implementation', models.CharField(blank=True, max_length=200, null=True)),
                ('Total_Number_of_Service_Providers', models.FloatField(blank=True, null=True)),
                ('Total_number_of_enterprise_beneficiaries', models.FloatField(blank=True, null=True)),
                ('access_to_extension', models.FloatField(blank=True, null=True)),
                ('access_to_project_support_service', models.CharField(blank=True, max_length=200, null=True)),
                ('access_to_capacity_building_services', models.FloatField(blank=True, null=True)),
                ('access_to_advisory_services', models.FloatField(blank=True, null=True)),
                ('access_to_rural_infrastructure_services', models.FloatField(blank=True, null=True)),
                ('access_to_input_support', models.FloatField(blank=True, null=True)),
                ('Number_of_Meetings', models.FloatField(blank=True, null=True)),
                ('Frequency_of_meetings_held_by_Group', models.FloatField(blank=True, null=True)),
                ('Average_Size_of_Each_Members_Household', models.FloatField(blank=True, null=True)),
                ('Number_of_Direct_Beneficiaries_Male', models.FloatField(blank=True, null=True)),
                ('Number_of_Direct_Beneficiaries_Female', models.FloatField(blank=True, null=True)),
                ('Number_of_beneficiaries_under_supported_services_Male', models.FloatField(blank=True, null=True)),
                ('female_beneficiaries_under_support_services', models.FloatField(blank=True, null=True)),
                ('Number_of_Indirect_Beneficiaries_Male', models.FloatField(blank=True, null=True)),
                ('Number_of_Indirect_Beneficiaries_Female', models.FloatField(blank=True, null=True)),
                ('permanently_employed_males', models.FloatField(blank=True, null=True)),
                ('permanently_employed_females', models.FloatField(blank=True, null=True)),
                ('temporarily_employed_males', models.FloatField(blank=True, null=True)),
                ('temporarily_employed_females', models.FloatField(blank=True, null=True)),
                ('Crop_Production_Metric_Tons_per_Hecta', models.FloatField(blank=True, null=True)),
                ('Fishery_Number_of_Kg', models.FloatField(blank=True, null=True)),
                ('Livestock_Number_of_Livestock', models.FloatField(blank=True, null=True)),
                ('Poultry_Number_of_Birds', models.FloatField(blank=True, null=True)),
                ('Poultry_Crate_of_Eggs', models.FloatField(blank=True, null=True)),
                ('Processing_Volume_of_Produce_Processed_Kg', models.FloatField(blank=True, null=True)),
                ('Number_of_Production_Cycle', models.FloatField(blank=True, null=True)),
                ('FUEF_Amount_Saved', models.FloatField(blank=True, null=True)),
                ('Picture_of_Subproject_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Picture_of_Subproject_2', models.CharField(blank=True, max_length=200, null=True)),
                ('GPS_Coordinates_of_site', models.CharField(blank=True, max_length=200, null=True)),
                ('_GPS_Coordinates_of_site_latitude', models.FloatField(blank=True, null=True)),
                ('_GPS_Coordinates_of_site_longitude', models.FloatField(blank=True, null=True)),
                ('_GPS_Coordinates_of_site_altitude', models.FloatField(blank=True, null=True)),
                ('_GPS_Coordinates_of_site_precision', models.FloatField(blank=True, null=True)),
                ('Success_Stories_due_to_presence_of_intervention', models.CharField(blank=True, max_length=200, null=True)),
                ('Do_you_have_any_challenges', models.CharField(blank=True, max_length=200, null=True)),
                ('If_yes_what_is_the_challenge', models.CharField(blank=True, max_length=200, null=True)),
                ('Risk_factors', models.CharField(blank=True, max_length=200, null=True)),
                ('Risk_factorsMilitancy', models.FloatField(blank=True, null=True)),
                ('Risk_factorsOil_Spillage', models.FloatField(blank=True, null=True)),
                ('Risk_factorsFlood', models.FloatField(blank=True, null=True)),
                ('Risk_factorsOthers', models.FloatField(blank=True, null=True)),
                ('If_others_specify', models.CharField(blank=True, max_length=200, null=True)),
                ('Name_of_Data_Collector', models.CharField(blank=True, max_length=200, null=True)),
                ('Signature_of_Data_Collector', models.CharField(blank=True, max_length=200, null=True)),
                ('Name_of_SEEFOR_FADAMA_User_Groups_SFUGs', models.FloatField(blank=True, null=True)),
                ('Type_of_enterprise', models.FloatField(blank=True, null=True)),
                ('Total_number_of_membership', models.FloatField(blank=True, null=True)),
                ('Frequency_of_meetings_held', models.FloatField(blank=True, null=True)),
                ('Number_of_Male', models.FloatField(blank=True, null=True)),
                ('Number_of_Female', models.FloatField(blank=True, null=True)),
                ('Frequency_of_meetings_held_by_Groups', models.FloatField(blank=True, null=True)),
                ('Number_of_person_employed_on_permanent_basis_Male1', models.FloatField(blank=True, null=True)),
                ('Number_of_person_employed_on_permanent_basis_Female1', models.FloatField(blank=True, null=True)),
                ('Number_of_person_employed_on_temporary_basis_Male1', models.FloatField(blank=True, null=True)),
                ('Number_of_person_employed_on_temporary_basis_Female1', models.FloatField(blank=True, null=True)),
                ('access_to_project_support_service1', models.FloatField(blank=True, null=True)),
                ('Amount_disbursed', models.FloatField(blank=True, null=True)),
                ('Duration_of_SubProject', models.FloatField(blank=True, null=True)),
                ('Total_Number_of_Service_Provider', models.FloatField(blank=True, null=True)),
                ('Picture_of_Site', models.FloatField(blank=True, null=True)),
                ('GIS_Coordinates_of_site', models.FloatField(blank=True, null=True)),
                ('_GIS_Coordinates_of_site_latitude', models.FloatField(blank=True, null=True)),
                ('_GIS_Coordinates_of_site_longitude', models.FloatField(blank=True, null=True)),
                ('_GIS_Coordinates_of_site_altitude', models.FloatField(blank=True, null=True)),
                ('_GIS_Coordinates_of_site_precision', models.FloatField(blank=True, null=True)),
                ('Increase_of_Agricultural_Production_for_SEEFOR_FADAMA', models.FloatField(blank=True, null=True)),
                ('Picture_of_Subproject', models.FloatField(blank=True, null=True)),
                ('calculation', models.FloatField(blank=True, null=True)),
                ('Number_of_Indirect_Beneficiaries_Male_calculation', models.FloatField(blank=True, null=True)),
                ('calculation_001', models.FloatField(blank=True, null=True)),
                ('Number_of_Indirect_Beneficiaries_Female_calculation_001', models.FloatField(blank=True, null=True)),
                ('Sustainability_Measures', models.FloatField(blank=True, null=True)),
                ('Picture_of_Subproject_3', models.FloatField(blank=True, null=True)),
                ('If_yes_specify', models.FloatField(blank=True, null=True)),
                ('_id', models.IntegerField(blank=True, null=True)),
                ('_uuid', models.CharField(blank=True, max_length=200, null=True)),
                ('_submission_time', models.CharField(blank=True, max_length=200, null=True)),
                ('_validation_status', models.FloatField(blank=True, null=True)),
                ('_index', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
