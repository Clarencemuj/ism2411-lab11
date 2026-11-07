#Self Assessment Questions
#1:In exercise 3, the difference between .get() and bracket notation is that .get() allows you to specify a default value if the key does not exist, while bracket notation will raise a KeyError if the key is not found. I would use .get() for any optional data the user will put in and brackets for anything mandatory that must be inputted. A good rule of thumb is if it is necessary, to use brackets. But if it is optional, use .get().
#2: The pattern in part 8 reminds me of a table you would make in excel. Python would be more useful in large databases beacuse python can take large datasets, and easily organize them into organized variables and dictionaries. Python can also perform calculations on the data, and create reports based on the data.

print("--Exercise 1 ---")
customer= {
    "name": "Alice", #Key: value,
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("---Exercise 2 ---")
customer['phone']='555-5555' #Adding a new key-value pair to the dictionary
print(customer)
customer['tier']   ='platinum'
print(customer)
del customer['name'] #Deleting a key-value pair from the dictionary
print(customer)

print(customer.get('ytd_spend',0)) #Using the get() method to retrieve a value from the dictionary

print("---Exercise 3 ---")
print(customer.get("email", "no email on file"))

print("---Exercise 4 ---")
# Exercise 4: Iterate with and without .items()
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating with .items() extracts both keys and values at the same time, allowing for more concise code.
# Iterating without .items() only loops through the keys, requiring bracket notation (customer[key]) to access the corresponding values.
for key in customer:
    print(f"{key}: {customer[key]}")

print("--- Exercise 5---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15,
}

purchase=200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate*100}%")
print(f"Final Price ${final_price:.2f}")


print("---Exercise 6---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 1500},
]
purchase_amount = 300
for record in customers:
    tier = record["tier"]
    rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_amount * rate
    print(f"Name: {record['name']}, Tier: {tier}, Discount: ${discount_amount:.2f}")

print("---Exercise 7---")
catalog={
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name,product_details in catalog.items():
    if product_details["stock"]<20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")

print("---Exercise 8---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region={}
for sale in transactions:
    region=sale["region"]
    amount=sale["amount"]
    sales_by_region[region]= sales_by_region.get(region,0) + amount

print(sales_by_region)
for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")