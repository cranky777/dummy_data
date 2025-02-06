import csv
import pprint
from faker import Factory
from faker.providers.person.ja_JP import Provider as PersonProviderJP

def list_to_tuple(l):
    return tuple(list_to_tuple(e) if isinstance(e, list) else e for e in l)

with open('personal_infomation.csv') as f:
    dict_reader = csv.DictReader(f)
    csv_data = [row for row in dict_reader]

male_names = []
female_names = []

last_names = []

for row in csv_data:
    last_names.append([row['姓'], row['姓（カタカナ）'], row['姓（ローマ字）']])
    if row['性別'] == "男":
        male_names.append([row['名'], row['名（カタカナ）'], row['名（ローマ字）']])
    else:
        female_names.append([row['名'], row['名（カタカナ）'], row['名（ローマ字）']])


fake = Factory.create('ja_JP')
person_provider: PersonProviderJP = list(filter(lambda provider: isinstance(provider, PersonProviderJP), fake.providers))[0]

my_last_name_pairs = list_to_tuple(last_names)
my_first_name_male_pairs = list_to_tuple(male_names)
my_first_name_female_pairs = list_to_tuple(female_names)

print(my_last_name_pairs)

# データセットに追加
person_provider.last_name_pairs = my_last_name_pairs
person_provider.first_name_male_pairs = my_first_name_male_pairs
person_provider.first_name_female_pairs = my_first_name_female_pairs

# 確認
for _ in range(1000):
    result = fake.first_name_male_pair()
    print(str(result))



