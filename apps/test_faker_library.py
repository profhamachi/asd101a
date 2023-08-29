from faker import Faker
fake = Faker()

for i in range(3):
    print(fake.name())
    print(fake.job())
    print(fake.address())
    print(fake.email())
    print(fake.phone_number())
    print()
