import re
from bs4 import BeautifulSoup
import requests


def truecar(brand, model):
    founded =[]
    print('Please wait')
    for i in range(1, 10):
        if i == 1:
            r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/%s/' % (brand, model))
        else:
            r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/%s/?page=%i' % (brand, model, i))
        soup = BeautifulSoup(r.text, 'html.parser')
        cars = soup.find("ul",attrs={"class": "row mb-3 mt-1"})
        founded.extend(cars.find_all('li'))
        print(11 - i, end=', ')
    print(1)
    result = []

    for f in founded:
        try:
            this_car = f.find('div', attrs={"linkable card card-shadow vehicle-card"})
            if this_car != None:
                miles = this_car.find('div', attrs={'class': "mt-2-5 w-full border-t pt-2-5"})
                result.append([this_car['aria-label'], miles.get_text()])

        except:
            continue

    return result


def extract_data(my_list):
    result =[]
    collect_year_brand_model_price_in_item = 'for (\d+) (\w+) ([\w\d]+),.*\$(\d+,\d+)'
    collect_miles = '(\d+),(\d+)'
    for item, miles in my_list:
        year_brand_model_price = re.findall(r'%s' % collect_year_brand_model_price_in_item, item)
        miles_digits = re.findall(r'%s' % collect_miles, miles)
        if miles_digits == []:
            miles = 1000
        else:
            miles = int(''.join(miles_digits[0]))
        try:
            price_digits = year_brand_model_price[0][3].split(',')
            car_price = int(''.join(price_digits))
        except:
            continue

        car_year = int(year_brand_model_price[0][0])
        car_brand = year_brand_model_price[0][1]
        car_model = year_brand_model_price[0][2]
        car_miles = miles
        result.append([car_brand, car_model, car_year, car_miles, car_price])
    return result


def go_to_true_car(brand, model):
    return extract_data(truecar(brand, model))








