import csv
import random
from datetime import datetime, timedelta

# Function to generate random datetime within a range
def random_datetime(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

# Generate 500 lines of fictitious data
data = []
start_date = datetime(2023, 1, 1, 8, 0, 0)
end_date = datetime(2023, 12, 31, 17, 0, 0)

for i in range(500):
    product_number = 1000 + i
    quantity = random.randint(50, 200)
    defective_products = random.randint(0, 10)
    product_cost = round(random.uniform(10.0, 100.0), 2)
    
    # Entry into the warehouse with 5 to 15 days difference from manufacturing start time
    manufacturing_start_time = random_datetime(start_date, end_date)
    entry_into_warehouse = manufacturing_start_time - timedelta(days=random.randint(5, 15))
    
    # Manufacturing end time with at least 10 more days difference from manufacturing start time
    manufacturing_end_time = manufacturing_start_time + timedelta(days=random.randint(10, 20))
    
    delivery_date = manufacturing_end_time + timedelta(days=random.randint(5, 15))
    
    factory_time = (manufacturing_end_time - manufacturing_start_time).total_seconds() / 3600

    row = [
        product_number,
        quantity,
        entry_into_warehouse.strftime("%Y-%m-%d %H:%M:%S"),
        manufacturing_start_time.strftime("%Y-%m-%d %H:%M:%S"),
        manufacturing_end_time.strftime("%Y-%m-%d %H:%M:%S"),
        defective_products,
        product_cost,
        delivery_date.strftime("%Y-%m-%d %H:%M:%S"),
        factory_time,
    ]

    data.append(row)

# Write data to CSV file
with open("fictitious_database.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([
        "ProductNumber",
        "Quantity",
        "EntryIntoWarehouse",
        "ManufacturingStartTime",
        "ManufacturingEndTime",
        "DefectiveProducts",
        "ProductCost",
        "DeliveryDate",
        "FactoryTimeHours",
    ])
    csvwriter.writerows(data)

