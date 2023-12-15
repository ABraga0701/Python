import csv
import random
from datetime import datetime, timedelta

# Function to generate random datetime within a range
def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

# Generate 100 rows of fictitious data
data = []
start_date = datetime(2023, 1, 1, 8, 0, 0)
end_date = datetime(2023, 12, 31, 17, 0, 0)

for i in range(100):
    product_number = 1000 + i
    manufacturing_start_time = random_date(start_date, end_date)
    manufacturing_end_time = manufacturing_start_time + timedelta(hours=random.randint(1, 8))
    defective_products = random.randint(0, 10)
    product_cost = round(random.uniform(10.0, 100.0), 2)
    factory_time = (manufacturing_end_time - manufacturing_start_time).total_seconds() / 3600

    row = [
        product_number,
        manufacturing_start_time.strftime("%Y-%m-%d %H:%M:%S"),
        manufacturing_end_time.strftime("%Y-%m-%d %H:%M:%S"),
        defective_products,
        product_cost,
        factory_time,
    ]

    data.append(row)

# Write data to CSV file
with open("fictitious_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ProductNumber", "ManufacturingStartTime", "ManufacturingEndTime", "DefectiveProducts", "ProductCost", "FactoryTimeHours"])
    csvwriter.writerows(data)
