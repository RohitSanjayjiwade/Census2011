from django.db import models
from django.utils.text import slugify

# Create your models here.

class Data(models.Model):
    state_code = models.CharField(max_length=10, default='')
    district_code = models.CharField(max_length=10,default='')
    sub_district_code = models.CharField(max_length=20, default='')  # Adjust the max_length as needed
    town_village_code = models.CharField(max_length=20, default='')
    ward_code = models.CharField(max_length=50, default='')
    enumeration_block_code = models.CharField(max_length=50, default='')
    level_of_admin_unit = models.CharField(max_length=50, default='')
    area_name = models.CharField(max_length=50,default='')
    total_rural_urban = models.CharField(max_length=50, default='')
    no_of_houshold = models.IntegerField(null=True)

    total_popul_persons = models.IntegerField(null=True)
    total_popul_males = models.IntegerField(null=True)
    total_popul_females = models.IntegerField(null=True)

    popul_in_agePersons = models.IntegerField(null=True)
    popul_in_ageMales = models.IntegerField(null=True)
    popul_in_ageFemales = models.IntegerField(null=True)

    caste_popul_persons = models.IntegerField(null=True)
    caste_popul_males = models.IntegerField(null=True)
    caste_popul_females = models.IntegerField(null=True)

    tribe_popul_persons = models.IntegerField(null=True)
    tribe_popul_males = models.IntegerField(null=True)
    tribe_popul_females = models.IntegerField(null=True)

    literates_persons = models.IntegerField(null=True)
    literates_males = models.IntegerField(null=True)
    literates_females = models.IntegerField(null=True)

    illiterates_persons = models.IntegerField(null=True)
    illiterates_males = models.IntegerField(null=True)
    illiterates_females = models.IntegerField(null=True)

    total_workers_persons = models.IntegerField(null=True)
    total_workers_males = models.IntegerField(null=True)
    total_workers_females = models.IntegerField(null=True, blank=True)

    main_workers_persons = models.IntegerField(null=True)
    main_workers_males = models.IntegerField(null=True)
    main_workers_females = models.IntegerField(null=True)

    workers_culti_persons = models.IntegerField(null=True)
    workers_culti_males = models.IntegerField(null=True)
    workers_culti_females = models.IntegerField(null=True)

    # Main Workers - Agricultural Labourers
    main_workers_agri_labourers_persons = models.IntegerField(null=True)
    main_workers_agri_labourers_males = models.IntegerField(null=True)
    main_workers_agri_labourers_females = models.IntegerField(null=True)

    # Main Workers - Workers in Household Industries
    main_workers_household_industries_persons = models.IntegerField(null=True)
    main_workers_household_industries_males = models.IntegerField(null=True)
    main_workers_household_industries_females = models.IntegerField(null=True)

    # Main Workers - Other Workers
    main_workers_other_workers_persons = models.IntegerField(null=True)
    main_workers_other_workers_males = models.IntegerField(null=True)
    main_workers_other_workers_females = models.IntegerField(null=True)

    # Marginal Workers
    marginal_workers_persons = models.IntegerField(null=True)
    marginal_workers_males = models.IntegerField(null=True)
    marginal_workers_females = models.IntegerField(null=True)

    # Marginal Workers - Cultivators
    marginal_cultivators_persons = models.IntegerField(null=True)
    marginal_cultivators_males = models.IntegerField(null=True)
    marginal_cultivators_females = models.IntegerField(null=True)

    # Marginal Workers - Agricultural Labourers
    marginal_agri_labourers_persons = models.IntegerField(null=True)
    marginal_agri_labourers_males = models.IntegerField(null=True)
    marginal_agri_labourers_females = models.IntegerField(null=True)

    # Marginal Workers - Workers in Household Industries
    marginal_workers_household_industries_persons = models.IntegerField(null=True)
    marginal_workers_household_industries_males = models.IntegerField(null=True)
    marginal_workers_household_industries_females = models.IntegerField(null=True)

    # Marginal Workers - Other Workers
    marginal_workers_other_workers_persons = models.IntegerField(null=True)
    marginal_workers_other_workers_males = models.IntegerField(null=True)
    marginal_workers_other_workers_females = models.IntegerField(null=True)

    # Marginal Workers - Those worked for 3 months or more and less than 6 months
    marginal_workers_3_to_6_months_persons = models.IntegerField(null=True)
    marginal_workers_3_to_6_months_males = models.IntegerField(null=True)
    marginal_workers_3_to_6_months_females = models.IntegerField(null=True)

     # Marginal Workers - Cultivators
    marginal_cultivators_persons_3_to_6_months = models.IntegerField(null=True)
    marginal_cultivators_males_3_to_6_months = models.IntegerField(null=True)
    marginal_cultivators_females_3_to_6_months = models.IntegerField(null=True)

    # Marginal Workers - Agricultural Labourers
    marginal_agri_labourers_persons_3_to_6_months = models.IntegerField(null=True)
    marginal_agri_labourers_males_3_to_6_months = models.IntegerField(null=True)
    marginal_agri_labourers_females_3_to_6_months = models.IntegerField(null=True)

    # Marginal Workers - Workers in Household Industries
    marginal_workers_household_industries_persons_3_to_6_months = models.IntegerField(null=True)
    marginal_workers_household_industries_males_3_to_6_months = models.IntegerField(null=True)
    marginal_workers_household_industries_females_3_to_6_months = models.IntegerField(null=True)

    # Marginal Workers - Other Workers
    marginal_other_workers_persons_3_to_6_months = models.IntegerField(null=True)
    marginal_other_workers_males_3_to_6_months = models.IntegerField(null=True)
    marginal_other_workers_females_3_to_6_months = models.IntegerField(null=True)

    # Marginal Workers - Those worked for less than 3 months
    marginal_workers_less_than_3_months_persons = models.IntegerField(null=True)
    marginal_workers_less_than_3_months_males = models.IntegerField(null=True)
    marginal_workers_less_than_3_months_females = models.IntegerField(null=True)

    # Marginal Workers - Cultivators
    marginal_cultivators_persons_less_than_3_months = models.IntegerField(null=True)
    marginal_cultivators_males_less_than_3_months = models.IntegerField(null=True)
    marginal_cultivators_females_less_than_3_months = models.IntegerField(null=True)

    # Marginal Workers - Agricultural Labourers
    marginal_agri_labourers_persons_less_than_3_months = models.IntegerField(null=True)
    marginal_agri_labourers_males_less_than_3_months = models.IntegerField(null=True)
    marginal_agri_labourers_females_less_than_3_months = models.IntegerField(null=True)

    # Marginal Workers - Workers in Household Industries
    marginal_workers_household_industries_persons_less_than_3_months = models.IntegerField(null=True)
    marginal_workers_household_industries_males_less_than_3_months = models.IntegerField(null=True)
    marginal_workers_household_industries_females_less_than_3_months = models.IntegerField(null=True)

    # Marginal Workers - Other Workers
    marginal_other_workers_persons_less_than_3_months = models.IntegerField(null=True)
    marginal_other_workers_males_less_than_3_months = models.IntegerField(null=True)
    marginal_other_workers_females_less_than_3_months = models.IntegerField(null=True)

    # Non-Workers
    non_workers_persons = models.IntegerField(null=True)
    non_workers_males = models.IntegerField(null=True)
    non_workers_females = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.area_name} - {self.total_rural_urban}"


class State(models.Model):
    name = models.CharField(max_length=30, unique=True)
    state_code = models.CharField(max_length=30, default='')
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='state_data')
    rural_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='state_rural_data')
    urban_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='state_urban_data')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district_code = models.CharField(max_length=30, default='')
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='district_data')
    rural_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='district_rural_data')
    urban_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='district_urban_data')
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.id}-{self.name}")
        super(District, self).save(*args, **kwargs)

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city_code = models.CharField(max_length=30, default="")
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='city_data')
    rural_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='city_rural_data')
    urban_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='city_urban_data')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.id}-{self.name}")
        super(City, self).save(*args, **kwargs)

class Village(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    village_code = models.CharField(max_length=30, default="")
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='village_data')
    rural_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='village_rural_data')
    urban_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name='village_urban_data')
    # slug = models.SlugField(unique=True, blank=True)
    pincode = models.CharField(max_length=6)
    villageType = models.CharField(max_length=6, null=True)
    deliveryStatus = models.TextField(null=True)
    divisionName = models.CharField(max_length=30, null=True)
    regionName = models.CharField(max_length=30, null=True)
    circleName = models.CharField(max_length=30, null=True)
    telephone = models.CharField(max_length=12, null=True)
    relatedSuboffice = models.CharField(max_length=30, null=True)
    relatedHeadoffice = models.CharField(max_length=30, null=True)

    def __str__(self):
        # return f"{self.name}{self.pincode}{self.villageType}{self.deliveryStatus}{self.divisionName}{self.regionName}{self.circleName}{self.telephone}{self.relatedSuboffice}{self.relatedHeadoffice}"
        return f"{self.name}"

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(f"{self.id}-{self.name}")
    #     super(Village, self).save(*args, **kwargs)

