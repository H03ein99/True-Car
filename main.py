import D_B
import M_L
import TrueCar


brand = input('brand(like BMW): ').lower()
model = input('model(like Z4): ').lower()
year_creation = int(input('year(like 2022): '))
miles = int(input('how many miles(like 10000): '))
D_B.update_data(TrueCar.go_to_true_car(brand, model))
data = D_B.read_data()
price = M_L.my_learner(data, [[year_creation, miles]])
print(f"I think this car might costs \"{price[0]}\" dollars")





