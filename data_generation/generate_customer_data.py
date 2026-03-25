from faker import Faker
import pandas as pd

def generate_data():
    customer_data = []

    for i in range(100):
        fake = Faker()
        name = fake.name()
        age = fake.random_int(min=18, max=80)
        print(f"Name: {name}, Age: {age}")
        customer_data.append({'Name': name, 'Age': age})
    df = pd.DataFrame(customer_data)
    df.to_csv('customer_data.csv', index=False)


generate_data()
