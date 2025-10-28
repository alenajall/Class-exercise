# Create a dictionary with 3 countries and their capitals
countries = {
    "Sierra Leone": "Freetown",
    "Ghana": "Accra",
    "Nigeria": "Abuja"
}

# Add one more country
countries["Kenya"] = "Nairobi"

# Update one capital
countries["Ghana"] = "Kumasi"

# Remove one country
del countries["Nigeria"]

# Print all keys and values
print("Countries and Capitals:")
for country, capital in countries.items():
    print(f"{country}: {capital}")
