from manager.models import *

country_list = (
    ('US','America'),
    ('Malaysia','Malaysia'),
    ('Ukraine','Ukraine'),
    ('UK','Great Britain and Northern Ireland'),
    ('Kenya','Kenya'),
    ('Netherlands','Netherlands'),
    ('Canada','Canada'),
    ('Austria','Austria'),
    ('Germany','Germany'),
    ('Colombia','Colombia'),
    ('Israel','Israel'),
    ('Brazil','Brazil'),
    ('Indonesia','Indonesia'),
    ('Denmark','Denmark'),
    ('Italy','Italy'),
    ('Australia','Australia'),
    ('Greece','Greece'),
    ('Russia','Russian Federation'),
    ('Pakistan','Pakistan'),
    ('Nigeria','Nigeria'),
    ('China','China'),
    ('Poland','Poland'),
    ('Turkey','Turkey'),
    ('Japan','Japan'),
    ('Mexico','Mexico'),
    ('Sweden','Sweden'),
    ('India','India'),
    ('Philippines','Philippines'),
    ('N Korea',"The Democratic People's Republic of Korea"),
    ('Spain','Spain'),
    ('Ireland','Ireland'),
    ('Egypt','Egypt'),
    ('Argentina','Argentina'),
    ('S Korea','The Republic of Korea'),
    ('Iran','Iran'),
    ('France','French Republic'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Syria','Syria'),
    ('NZ','New Zealand'),
) 

state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming,'
]



one_province_nations = (
    ('Ukraine','Ukraine'),
    ('Kenya','Kenya'),
    ('Netherlands','Netherlands'),
    ('Austria','Austria'),
    ('Colombia','Colombia'),
    ('Israel','Israel'),
    ('Indonesia','Indonesia'),
    ('Denmark','Denmark'),
    ('Italy','Italy'),
    ('Greece','Greece'),
    ('Pakistan','Pakistan'),
    ('Nigeria','Nigeria'),
    ('Poland','Poland'),
    ('Turkey','Turkey'),
    ('Mexico','Mexico'),
    ('Sweden','Sweden'),
    ('Philippines','Philippines'),
    ('N Korea',"The Democratic People's Republic of Korea"),
    ('Spain','Spain'),
    ('Ireland','Ireland'),
    ('Egypt','Egypt'),
    ('Argentina','Argentina'),
    ('S Korea','The Republic of Korea'),
    ('Iran','Iran'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Syria','Syria'),
    ('NZ','New Zealand'),
)

multistate_nations = (
    ('US','America'),
    ('Malaysia','Malaysia'),
    ('UK','Great Britain and Northern Ireland'),
    ('Canada','Canada'),
    ('Germany','Germany'),
    ('Brazil','Brazil'),
    ('Australia','Australia'),
    ('Russia','Russian Federation'),
    ('China','China'),
    ('Japan','Japan'),
    ('India','India'),
    ('France','French Republic'),
)

sector_types = (
    ('Agriculture','Agriculture'),
    ('Automobiles','Automobiles'),
    ('Defense','Defense'),
    ('Financial','Financial'),
    ('Healthcare','Healthcare'),
    ('Manufacturing','Manufacturing'),
    ('Media','Media'),
    ('Mining','Mining'),
    ('Oil and gas','Oil and gas'),
    ('Retail','Retail'),
    ('Technology','Technology'),
)


sector_count = 1

def gen_country():
    i = 1
    for country in country_list:
        s  = f"""{{"model": "manager.country", "pk": {i}, "fields": {{"name": "{country[0]}"}}}}"""
        print(s + ',')
        i += 1

def gen_us_states():
    global sector_count
    i = 1
    for state in state_list:
        s = f"""{{"model": "manager.region", "pk": {i}, "fields": {{"country": 1, "name": "{state}"}}}}"""
        print(s+',')
        for sector_type in sector_types:
            sector_s = f"""{{"model": "manager.sector", "pk": {sector_count}, "fields": {{"type": "{sector_type[0]}", "region": {i}, "corporations": null, "unions": null}}}},"""
            print(sector_s)
            sector_count += 1
        i += 1


def gen_oneprov_states():
    global sector_count
    i = 51
    for nation in one_province_nations:
        country_code = Country.objects.get(name=nation[0])
        country_code = country_code.pk
        s = f"""{{"model": "manager.region", "pk": {i}, "fields": {{"country": {country_code}, "name": "{nation[0]}"}}}}"""
        print(s+',')
        for sector_type in sector_types:
            sector_s = f"""{{"model": "manager.sector", "pk": {sector_count}, "fields": {{"type": "{sector_type[0]}", "region": {i}, "corporations": null, "unions": null}}}},"""
            print(sector_s)
            sector_count += 1
        i += 1
print('[')
gen_country()
gen_us_states()
gen_oneprov_states()
print(']')