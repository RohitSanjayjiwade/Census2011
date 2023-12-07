from concurrent.futures import ThreadPoolExecutor
from django.core.management.base import BaseCommand
from census.models import State, District, City, Village
import csv

class Command(BaseCommand):
    help = 'Populates State, District, City, and Village models from a CSV file'

    def handle(self, *args, **kwargs):
        print("hello")

        CHUNK_SIZE = 10  # Set the chunk size

        with open(r'/home/vaibhav/Desktop/pincode.csv', mode='r') as file:
            csvFile = csv.DictReader(file)

            # Function to process each row
            def process_row(row):
                statename = row.get('statename', '')
                district = row.get('Districtname', '')
                city = row.get('Taluk', '')
                village = row.get('officename', '')
                pincode = row.get('pincode', '')
                villageType = row.get('officeType', '')
                deliveryStatus = row.get('Deliverystatus', '')
                divisionName = row.get('divisionname', '')
                regionName = row.get('regionname', '')
                circleName = row.get('circlename', '')
                telephone = row.get('Telephone', '')
                relatedSuboffice = row.get('Related Suboffice', '')
                relatedHeadoffice = row.get('Related Headoffice', '')

                state_instance, created = State.objects.get_or_create(name=statename)
                district_instance, created = District.objects.get_or_create(name=district, state=state_instance)
                city_instance, created = City.objects.get_or_create(name=city, district=district_instance,
                                                                    state=state_instance)
                village_instance = Village.objects.create(name=village, pincode=pincode, villageType=villageType,
                                                          deliveryStatus=deliveryStatus, divisionName=divisionName,
                                                          regionName=regionName, circleName=circleName,
                                                          telephone=telephone, relatedSuboffice=relatedSuboffice,
                                                          relatedHeadoffice=relatedHeadoffice, city=city_instance,
                                                          district=district_instance, state=state_instance)

            # Read the CSV file in chunks
            chunk = []
            for row in csvFile:
                chunk.append(row)
                if len(chunk) == CHUNK_SIZE:
                    with ThreadPoolExecutor() as executor:
                        executor.map(process_row, chunk)
                    chunk = []

            # Process any remaining rows
            with ThreadPoolExecutor() as executor:
                executor.map(process_row, chunk)

            print("Processing completed.")
