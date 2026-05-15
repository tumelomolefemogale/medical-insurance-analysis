# Extract medical records from CSV file for analysis

import csv

medical_records = []

with open('insurance.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        medical_records.append(row)

# 1. Average insurance charge across all patients

total_charges = 0

for medical_record in medical_records:
    total_charges += float(medical_record['charges'])

average_charges = total_charges / len(medical_records)

print(f"The average insurance charge across all patients in the U.S is ${round(average_charges, 2)}.")

# 2. Number of unique regions and number of patients in each

regions = []

for medical_record in medical_records:
    regions.append(medical_record['region'])

regions_count = []

for region in regions:
    regions_count.append((region, regions.count(region)))

regions_count_unique = list(set(regions_count))

print(f"There are {len(regions_count_unique)} unique regions - {[region for region, _ in regions_count_unique]}.")

for region, count in regions_count_unique:
    print(f"There are {count} patients in the {region} region.")

# 3. Ages of the oldest and youngest patients

medical_records_sorted = sorted(medical_records, key=lambda x: x['age'])

print(f"The youngest patient is {medical_records_sorted[0]['age']} years old.")
print(f"The oldest patient is {medical_records_sorted[-1]['age']} years old.")

# 4. Average charge for smokers vs non-smokers

medical_records_smokers = []
medical_records_non_smokers = []

for medical_record in medical_records:
    if medical_record['smoker'] == 'yes':
        medical_records_smokers.append(medical_record)
    else:
        medical_records_non_smokers.append(medical_record)

smokers_total_charges = 0
non_smokers_total_charges = 0

for smoker_medical_record in medical_records_smokers:
    smokers_total_charges += float(smoker_medical_record['charges'])

for non_smoker_medical_record in medical_records_non_smokers:
    non_smokers_total_charges += float(non_smoker_medical_record['charges'])

smokers_average_charges = smokers_total_charges / len(medical_records_smokers)
non_smokers_average_charges = non_smokers_total_charges / len(medical_records_non_smokers)

print(f"The average charge for smokers is ${round(smokers_average_charges, 2)}.")
print(f"The average charge for non-smokers is ${round(non_smokers_average_charges, 2)}.")

# 5. Patients sorted by charges (highest to lowest) — who pays the most?

medical_records_charges_sorted = sorted(medical_records, key=lambda x: float(x['charges']), reverse=True)

print(f"This is the highest-paying patiennt's medical insurance information - {medical_records_charges_sorted[0]}")

# 6. Group by region and the average BMI per region

group_by_region = {}

for region in [region for region, _ in regions_count_unique]:
    medical_records_by_region = []
    for medical_record in medical_records:
        if medical_record['region'] == region:
            medical_records_by_region.append(medical_record)
    group_by_region[region] = medical_records_by_region


for key, value in group_by_region.items():
    total_bmi_by_region = 0
    for item in value:
        total_bmi_by_region += float(item['bmi'])

    average_bmi_by_region = total_bmi_by_region / len(value)
    print(f"The average BMI per region in the {key} region is {round(average_bmi_by_region, 2)}")

# 7. Percentage of smoking patients

smokers_percentage = (len(medical_records_smokers) / len(medical_records)) * 100

print(f"Smokers make up {round(smokers_percentage, 2)}% of all patients.")

# 8. Average charges by age group (18–30, 31–45, 46–60, 60+)

age_18_to_30 = []
age_31_to_45 = []
age_46_to_59 = []
age_60_plus = []

for medical_record in medical_records:
    if int(medical_record['age']) <= 30:
        age_18_to_30.append(medical_record)
    elif int(medical_record['age']) <= 45:
        age_31_to_45.append(medical_record)
    elif int(medical_record['age']) <= 59:
        age_46_to_59.append(medical_record)
    else:
        age_60_plus.append(medical_record)

all_ages = {}
all_ages['18 to 30'] = age_18_to_30
all_ages['31 to 45'] = age_31_to_45
all_ages['46 to 59'] = age_46_to_59
all_ages['60+'] = age_60_plus

for age_group, records in all_ages.items():
    total_charges_by_age_group = 0
    for record in records:
        total_charges_by_age_group += float(record['charges'])

    average_charges_by_age_group = total_charges_by_age_group / len(records)
    print(f"The average charges by the age group {age_group} is ${round(average_charges_by_age_group, 2)}")

# 9. Patients who pay more on average — males or females, and if that change when the smoking factor is controlled

male_medical_records = []
female_medical_records = []

for medical_record in medical_records:
    if medical_record['sex'] == 'male':
        male_medical_records.append(medical_record)
    else:
        female_medical_records.append(medical_record)

male_total_charges = 0
for medical_record in male_medical_records:
    male_total_charges += float(medical_record['charges'])

female_total_charges = 0
for medical_record in female_medical_records:
    female_total_charges += float(medical_record['charges'])

if male_total_charges == female_total_charges:
    print("Both male and female patients pay the same amount on average")
elif male_total_charges > female_total_charges:
    print("Male patients pay more on insurance than female patients on average")
else:
    print("Female patients pay more on insurance than male patients on average")

female_smokers = []
male_smokers = []
for medical_record in medical_records_smokers:
    if medical_record['smoker'] == 'yes' and medical_record['sex'] == 'female':
        female_smokers.append(medical_record)
    elif medical_record['smoker'] == 'yes' and medical_record['sex'] == 'male':
        male_smokers.append(medical_record)

female_smoker_total_charges = 0
for medical_record in female_smokers:
    female_smoker_total_charges += float(medical_record['charges'])

female_smoker_average_charges = female_smoker_total_charges / len(female_smokers)

male_smoker_total_charges = 0
for medical_record in male_smokers:
    male_smoker_total_charges += float(medical_record['charges'])

male_smoker_average_charges = male_smoker_total_charges / len(male_smokers)

if male_smoker_average_charges == female_smoker_average_charges:
    print("Both male and female smoking patients pay the same amount on average.")
elif male_smoker_average_charges > female_smoker_average_charges:
    print("Male smoking patients pay more on insurance than female smoking patients.")
else:
    print("Female smoking patients pay more on insurance than male smoking patients.")

female_non_smokers = []
male_non_smokers = []
for medical_record in medical_records_non_smokers:
    if medical_record['smoker'] == 'no' and medical_record['sex'] == 'female':
        female_non_smokers.append(medical_record)
    elif medical_record['smoker'] == 'no' and medical_record['sex'] == 'male':
        male_non_smokers.append(medical_record)

female_non_smoker_total_charges = 0
for medical_record in female_non_smokers:
    female_non_smoker_total_charges += float(medical_record['charges'])

female_non_smoker_average_charges = female_non_smoker_total_charges / len(female_non_smokers)


male_non_smoker_total_charges = 0
for medical_record in male_non_smokers:
    male_non_smoker_total_charges += float(medical_record['charges'])

male_non_smoker_average_charges = male_non_smoker_total_charges / len(male_non_smokers)

if male_non_smoker_average_charges == female_non_smoker_average_charges:
    print("Both male and female non-smoking patients pay the same amount on average.")
elif male_non_smoker_average_charges > female_non_smoker_average_charges:
    print("Male non-smoking patients pay more on insurance than female non-smoking patients.")
else:
    print("Female non-smoking patients pay more on insurance than male non-smoking patients.")
