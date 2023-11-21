import pandas as pd
from faker import Faker

def generate_fake_data_and_save_csv(num_rows, output_file):
    faker = Faker()

    # Generate fake data for multiple columns
    fake_data = {
        'Name': [faker.name() for _ in range(num_rows)],
        'Email': [faker.email() for _ in range(num_rows)],
        'Phone': [faker.phone_number() for _ in range(num_rows)],
        'Address': [faker.address() for _ in range(num_rows)],
        'Job': [faker.job() for _ in range(num_rows)],
        'Company': [faker.company() for _ in range(num_rows)],
        'City': [faker.city() for _ in range(num_rows)],
        'Country': [faker.country() for _ in range(num_rows)],
        'Date of Birth': [faker.date_of_birth() for _ in range(num_rows)],
        'Credit Card Number': [faker.credit_card_number() for _ in range(num_rows)],
        'Color': [faker.color_name() for _ in range(num_rows)],
        'Word': [faker.word() for _ in range(num_rows)],
        'Sentence': [faker.sentence() for _ in range(num_rows)],
        'Paragraph': [faker.paragraph() for _ in range(num_rows)],
        'ISBN': [faker.isbn13() for _ in range(num_rows)],
        'Currency Code': [faker.currency_code() for _ in range(num_rows)],
        'Latitude': [faker.latitude() for _ in range(num_rows)],
        'Longitude': [faker.longitude() for _ in range(num_rows)],
        'Boolean': [faker.boolean() for _ in range(num_rows)],
        'Hex Color': [faker.hex_color() for _ in range(num_rows)],
        'URL': [faker.url() for _ in range(num_rows)],
        'IPv4': [faker.ipv4() for _ in range(num_rows)],
        'Password': [faker.password() for _ in range(num_rows)]
    }

    # Create a Pandas DataFrame from the fake data
    df = pd.DataFrame(fake_data)

    # Save the DataFrame to a CSV file
    return df


def generate_fake_data_and_save_csv1(num_rows, output_file):
    faker = Faker()

    # Generate fake data for multiple columns
    fake_data = {
        'Name': [faker.name() for _ in range(num_rows)],
        'Email': [faker.email() for _ in range(num_rows)],
        'Phone': [faker.phone_number() for _ in range(num_rows)],
    }

    # Create a Pandas DataFrame from the fake data
    df = pd.DataFrame(fake_data)

    # Save the DataFrame to a CSV file
    return df
    
