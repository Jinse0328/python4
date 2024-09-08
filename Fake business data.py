from faker import Faker
from pprint import pprint
import random

fake = Faker()

# Create a list of dictionaries, where each dictionary represents a person
customers = []
for i in range(10):
    person = {
        "customer_id": i + 1,
        "name": fake.name(),
        "address": fake.address(),
        "phone_number": fake.phone_number() if random.choice([True, False]) else None,
        "email": fake.email() if random.choice([True, False]) else None
    }
    customers.append(person)

first_person = list(customers[0].keys())
print("First person keys: ")
print(first_person)

missing_data = [x for x in customers if x["phone_number"] is None or x["email"] is None]
print("Missing data: ")
pprint(missing_data)

missing_data_percentage = (len(missing_data)/len(customers))*100
print(f"{missing_data_percentage}% of customers are missing contact data")