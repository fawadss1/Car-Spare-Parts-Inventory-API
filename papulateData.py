import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()
from inventory.models import SparePart

fake = Faker()

CAR_MODELS = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Nissan", "Audi", "Chevrolet", "Hyundai", "Kia"]

def populate_spare_parts(num_records=500):
    print(f"Seeding {num_records} spare parts...")

    for _ in range(num_records):
        SparePart.objects.create(
            name=fake.word().capitalize() + " " + fake.random_element(elements=["Filter", "Belt", "Brake", "Battery", "Light", "Mirror"]),
            price=round(random.uniform(20.0, 500.0), 2),
            compatible_models=", ".join(fake.random_choices(elements=CAR_MODELS, length=random.randint(1, 3))),
            quantity=random.randint(1, 50),
            description=fake.sentence(),
        )

    print("Seeding complete!")

if __name__ == "__main__":
    populate_spare_parts(500)
