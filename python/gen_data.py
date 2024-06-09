#!/usr/bin/python

import csv
import random
import datetime

# Parameters
num_rows = 100  # Number of rows of sample data to generate
output_file = "sample_data.csv"

# Sample data generation function
def generate_sample_data(num_rows):
    header = ['id', 'name', 'age', 'email', 'signup_date']
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    domains = ['example.com', 'test.com', 'sample.com']

    data = []
    for i in range(1, num_rows + 1):
        name = random.choice(names)
        age = random.randint(18, 70)
        email = f"{name.lower()}{i}@{random.choice(domains)}"
        signup_date = (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
        data.append([i, name, age, email, signup_date])
    
    return [header] + data

# Write sample data to CSV
def write_to_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Generate and write sample data
sample_data = generate_sample_data(num_rows)
write_to_csv(output_file, sample_data)

print(f"Sample data generated and written to {output_file}")

