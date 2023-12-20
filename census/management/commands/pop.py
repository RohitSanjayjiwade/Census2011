from concurrent.futures import ThreadPoolExecutor
from django.core.management.base import BaseCommand
from census.models import State, District, City, Village, Data, Year
import pandas as pd


class Command(BaseCommand):
    help = 'Populates State, District, City, and Village models from an Excel file'

    def handle(self, *args, **kwargs):
        print("hello")

        # Specify the path to your Excel file
        excel_file_path = '/home/vaibhav/Desktop/pop.xlsx'

        # Specify the number of rows to read (adjust as needed)
        nrows = 10000

        # Read the specified number of rows from the Excel file into a DataFrame
        df = pd.read_excel(excel_file_path, nrows=nrows)

        for _, row in df.iterrows():
            self.process_row(row)

        print("Processing completed.")

    # Function to process each row as a dictionary
    def process_row(self, row):
        # print(row)
        stateCode = row.get('State','')
        districtCode = row.get('District','')
        subDistrictCode = row.get('Subdistt','')
        villageCode = row.get('Town/Village','')
        wardCode = row.get('Ward','')
        enumerationCode = row.get('EB','')
        level = row.get('Level','')
        areaName = row.get('Name','')
        totalRuralUrban = row.get('TRU','')
        noOfHoushold = row.get('No_HH','')
        totalPopuP = row.get('TOT_P','')
        totalPopuM = row.get('TOT_M','')
        totalPopuF = row.get('TOT_F','')
        popuInAgeP = row.get('P_06','')
        popuInAgeM = row.get('M_06','')
        popuInAgeF = row.get('F_06','')
        castePopuP = row.get('P_SC','')
        castePopuM = row.get('M_SC','')
        castePopuF = row.get('F_SC','')
        tribPopuP = row.get('P_ST','')
        tribPopuM = row.get('M_ST','')
        tribPopuF = row.get('F_ST','')
        literatesP = row.get('P_LIT','')
        literatesM = row.get('M_LIT','')
        literatesF = row.get('F_LIT','')
        iliteratesP = row.get('P_ILL','')
        iliteratesM = row.get('M_ILL','')
        iliteratesF = row.get('F_ILL','')
        totalWorkP = row.get('TOT_WORK_P','')
        totalWorkM = row.get('TOT_WORK_M','')
        totalWorkF = row.get('TOT_WORK_F','')
        mainWorkP = row.get('MAINWORK_P','')
        mainWorkM = row.get('MAINWORK_M','')
        mainWorkF = row.get('MAINWORK_F','')
        workCultP = row.get('MAIN_CL_P','')
        workCultM = row.get('MAIN_CL_M','')
        workCultF = row.get('MAIN_CL_F','')
        mainWorkAgriLabP = row.get('MAIN_AL_P','')
        mainWorkAgriLabM = row.get('MAIN_AL_M','')
        mainWorkAgriLabF = row.get('MAIN_AL_F','')
        mainWorkHousIndP = row.get('MAIN_HH_P','')
        mainWorkHousIndM = row.get('MAIN_HH_M','')
        mainWorkHousIndF = row.get('MAIN_HH_F','')
        mainWorkOtherWorkP = row.get('MAIN_OT_P','')
        mainWorkOtherWorkM = row.get('MAIN_OT_M','')
        mainWorkOtherWorkF = row.get('MAIN_OT_F','')
        marginWorkP = row.get('MARGWORK_P','')
        marginWorkM = row.get('MARGWORK_M','')
        marginWorkF = row.get('MARGWORK_F','')
        marginCultP = row.get('MARG_CL_P','')
        marginCultM = row.get('MARG_CL_M','')
        marginCultF = row.get('MARG_CL_F','')
        marginWorkAgriLabP = row.get('MARG_AL_P','')
        marginWorkAgriLabM = row.get('MARG_AL_M','')
        marginWorkAgriLabF = row.get('MARG_AL_F','')
        marginWorkHousIndP = row.get('MARG_HH_P','')
        marginWorkHousIndM = row.get('MARG_HH_M','')
        marginWorkHousIndF = row.get('MARG_HH_F','')
        marginWorkOtherWorkP = row.get('MARG_OT_P','')
        marginWorkOtherWorkM = row.get('MARG_OT_M','')
        marginWorkOtherWorkF = row.get('MARG_OT_F','')
        marginWorkTtoSP = row.get('MARGWORK_3_6_P','')
        marginWorkTtoSM = row.get('MARGWORK_3_6_M','')
        marginWorkTtoSF = row.get('MARGWORK_3_6_F','')
        marginCultiTtoSP = row.get('MARG_CL_3_6_P','')
        marginCultiTtoSM = row.get('MARG_CL_3_6_M','')
        marginCultiTtoSF = row.get('MARG_CL_3_6_F','')
        marginAgriLabP = row.get('MARG_AL_3_6_P','')
        marginAgriLabM = row.get('MARG_AL_3_6_M','')
        marginAgriLabF = row.get('MARG_AL_3_6_F','')
        marginWorkHousTtoSP = row.get('MARG_HH_3_6_P','')
        marginWorkHousTtoSM = row.get('MARG_HH_3_6_M','')
        marginWorkHousTtoSF = row.get('MARG_HH_3_6_F','')
        marginWorkOtherTtoSP = row.get('MARG_OT_3_6_P','')
        marginWorkOtherTtoSM = row.get('MARG_OT_3_6_M','')
        marginWorkOtherTtoSF = row.get('MARG_OT_3_6_F','')
        marginWorkLessTP = row.get('MARGWORK_0_3_P','')
        marginWorkLessTM = row.get('MARGWORK_0_3_M','')
        marginWorkLessTF = row.get('MARGWORK_0_3_F','')
        marginCultiLessTP = row.get('MARG_CL_0_3_P','')
        marginCultiLessTM = row.get('MARG_CL_0_3_M','')
        marginCultiLessTF = row.get('MARG_CL_0_3_F','')
        marginAgriLabLessTP = row.get('MARG_AL_0_3_P','')
        marginAgriLabLessTM = row.get('MARG_AL_0_3_M','')
        marginAgriLabLessTF = row.get('MARG_AL_0_3_F','')
        marginWorkHouseLessTP = row.get('MARG_HH_0_3_P','')
        marginWorkHouseLessTM = row.get('MARG_HH_0_3_M','')
        marginWorkHouseLessTF = row.get('MARG_HH_0_3_F','')
        marginOtherWorkLessTP = row.get('MARG_OT_0_3_P','')
        marginOtherWorkLessTM = row.get('MARG_OT_0_3_M','')
        marginOtherWorkLessTF = row.get('MARG_OT_0_3_F','')
        noWorkP = row.get('NON_WORK_P','')
        noWorkM = row.get('NON_WORK_M','')
        noWorkF = row.get('NON_WORK_F','')
        try:
            data_instance = Data.objects.create(state_code=stateCode, district_code=districtCode, sub_district_code=subDistrictCode,
                                            town_village_code=villageCode, ward_code=wardCode, enumeration_block_code=enumerationCode,
                                            level_of_admin_unit=level, area_name=areaName, total_rural_urban=totalRuralUrban,
                                            no_of_houshold=noOfHoushold, total_popul_persons=totalPopuP, total_popul_males=totalPopuM,
                                            total_popul_females=totalPopuF, popul_in_agePersons=popuInAgeP, popul_in_ageMales=popuInAgeM,
                                            popul_in_ageFemales=popuInAgeF, caste_popul_persons=castePopuP, caste_popul_males=castePopuM,
                                            caste_popul_females=castePopuF, tribe_popul_persons=tribPopuP, tribe_popul_males=tribPopuM,
                                            tribe_popul_females=tribPopuF, literates_persons=literatesP, literates_males=literatesM,
                                            literates_females=literatesF, illiterates_persons=iliteratesP, illiterates_males=iliteratesM,
                                            illiterates_females=iliteratesF, total_workers_persons=totalWorkP, total_workers_males=totalWorkM, total_workers_females=totalWorkF, 
                                            main_workers_persons=mainWorkP, main_workers_males=mainWorkM, main_workers_females=mainWorkF, workers_culti_persons=workCultP, workers_culti_males=workCultM,
                                            workers_culti_females=workCultF, main_workers_agri_labourers_persons=mainWorkAgriLabP,
                                            main_workers_agri_labourers_males=mainWorkAgriLabM, main_workers_agri_labourers_females=mainWorkAgriLabF,
                                            main_workers_household_industries_persons=mainWorkHousIndP, main_workers_household_industries_males=mainWorkHousIndM,
                                            main_workers_household_industries_females=mainWorkHousIndF, main_workers_other_workers_persons=mainWorkOtherWorkP,
                                            main_workers_other_workers_males=mainWorkOtherWorkM, main_workers_other_workers_females=mainWorkOtherWorkF,
                                            marginal_workers_persons=marginWorkP, marginal_workers_males=marginWorkM, marginal_workers_females=marginWorkF,
                                            marginal_cultivators_persons=marginCultP, marginal_cultivators_males=marginCultM, marginal_cultivators_females=marginCultF,
                                            marginal_agri_labourers_persons=marginWorkAgriLabP, marginal_agri_labourers_males=marginWorkAgriLabM,
                                            marginal_agri_labourers_females=marginWorkAgriLabF, marginal_workers_household_industries_persons=marginWorkHousIndP,
                                            marginal_workers_household_industries_males=marginWorkHousIndM, marginal_workers_household_industries_females=marginWorkHousIndF,
                                            marginal_workers_other_workers_persons=marginWorkOtherWorkP, marginal_workers_other_workers_males=marginWorkOtherWorkM,
                                            marginal_workers_other_workers_females=marginWorkOtherWorkF, marginal_workers_3_to_6_months_persons=marginWorkTtoSP,
                                            marginal_workers_3_to_6_months_males=marginWorkTtoSM, marginal_workers_3_to_6_months_females=marginWorkTtoSF,
                                            marginal_cultivators_persons_3_to_6_months=marginCultiTtoSP, marginal_cultivators_males_3_to_6_months=marginCultiTtoSM,
                                            marginal_cultivators_females_3_to_6_months=marginCultiTtoSF, marginal_agri_labourers_persons_3_to_6_months=marginAgriLabP,
                                            marginal_agri_labourers_males_3_to_6_months=marginAgriLabM, marginal_agri_labourers_females_3_to_6_months=marginAgriLabF,
                                            marginal_workers_household_industries_persons_3_to_6_months=marginWorkHousTtoSP, marginal_workers_household_industries_males_3_to_6_months=marginWorkHousTtoSM,
                                            marginal_workers_household_industries_females_3_to_6_months=marginWorkHousTtoSF, marginal_other_workers_persons_3_to_6_months=marginWorkOtherTtoSP,
                                            marginal_other_workers_males_3_to_6_months=marginWorkOtherTtoSM, marginal_other_workers_females_3_to_6_months=marginWorkOtherTtoSF, 
                                            marginal_workers_less_than_3_months_persons=marginWorkLessTP, marginal_workers_less_than_3_months_males=marginWorkLessTM, marginal_workers_less_than_3_months_females=marginWorkLessTF,
                                            marginal_cultivators_persons_less_than_3_months=marginCultiLessTP, marginal_cultivators_males_less_than_3_months=marginCultiLessTM, marginal_cultivators_females_less_than_3_months=marginCultiLessTF,
                                            marginal_agri_labourers_persons_less_than_3_months=marginAgriLabLessTP, marginal_agri_labourers_males_less_than_3_months=marginAgriLabLessTM, 
                                            marginal_agri_labourers_females_less_than_3_months=marginAgriLabLessTF, marginal_workers_household_industries_persons_less_than_3_months=marginWorkHouseLessTP,
                                            marginal_workers_household_industries_males_less_than_3_months=marginWorkHouseLessTM, marginal_workers_household_industries_females_less_than_3_months=marginWorkHouseLessTF,
                                            marginal_other_workers_persons_less_than_3_months=marginOtherWorkLessTP, marginal_other_workers_males_less_than_3_months=marginOtherWorkLessTM,
                                            marginal_other_workers_females_less_than_3_months=marginOtherWorkLessTF, non_workers_persons=noWorkP, non_workers_males=noWorkM, non_workers_females=noWorkF)
        except Exception as e:
            print(f"Error processing row: {row}")
            print(f"Error details: {e}")
            data_instance = None


        if data_instance:
            print("Level " + level)
            print("TRU: " + totalRuralUrban)


            
            if level == "STATE":
                state_instance, created = State.objects.get_or_create(
                    name=areaName,
                    state_code=stateCode
                )

                state_instance.save()
                year_instance, created = Year.objects.get_or_create(year=2011, state=state_instance)

                if totalRuralUrban == "Total":
                    year_instance.data = data_instance
                elif totalRuralUrban == "Rural":
                    year_instance.rural_data = data_instance
                elif totalRuralUrban == "Urban":
                    year_instance.urban_data = data_instance

                year_instance.save()


            elif level == 'DISTRICT':
                state_instance = State.objects.get(state_code=stateCode)
                district_instance, created = District.objects.update_or_create(
                    name=areaName,
                    district_code=districtCode,
                    defaults={'state': state_instance}
                )
                print("saved in district and total")

                district_instance.save()

                year_instance, created = Year.objects.get_or_create(year=2011, district=district_instance)

                if totalRuralUrban == "Total":
                    year_instance.data = data_instance
                elif totalRuralUrban == "Rural":
                    year_instance.rural_data = data_instance
                elif totalRuralUrban == "Urban":
                    year_instance.urban_data = data_instance

                year_instance.save()


            elif level == 'SUB-DISTRICT':
                state_instance = State.objects.get(state_code=stateCode)
                district_instance = District.objects.get(district_code=districtCode)

                city_instance, created = City.objects.update_or_create(
                    name=areaName,
                    city_code=subDistrictCode,
                    defaults={'state': state_instance, 'district': district_instance}
                )
                print("saved in city and total")

                city_instance.save()

                year_instance, created = Year.objects.get_or_create(year=2011, city=city_instance)

                if totalRuralUrban == "Total":
                    year_instance.data = data_instance
                elif totalRuralUrban == "Rural":
                    year_instance.rural_data = data_instance
                elif totalRuralUrban == "Urban":
                    year_instance.urban_data = data_instance

                year_instance.save()



            elif level == 'VILLAGE':
                print("coming here")
                state_instance = State.objects.get(state_code=stateCode)
                district_instance = District.objects.get(district_code=districtCode)
                city_instance = City.objects.get(city_code=subDistrictCode)


                village_instance, created = Village.objects.update_or_create(
                    name=areaName,
                    village_code=villageCode,
                    defaults={
                        'state': state_instance,
                        'district': district_instance,
                        'city': city_instance
                    }
                )
                print("saved in village and total")

                village_instance.save()

                year_instance, created = Year.objects.get_or_create(year=2011, village=village_instance)

                if totalRuralUrban == "Total":
                    year_instance.data = data_instance
                elif totalRuralUrban == "Rural":
                    year_instance.rural_data = data_instance
                elif totalRuralUrban == "Urban":
                    year_instance.urban_data = data_instance

                year_instance.save()


        print("Processing completed.")
