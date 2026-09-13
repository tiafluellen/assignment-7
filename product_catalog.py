# Mock product catalog
products = [
    {
        "name": "Eco Water Bottle",
        "tags": ["eco-friendly", "durable", "recyclable"]
    },
    {
        "name": "Trail Backpack",
        "tags": ["durable", "water-resistant", "lightweight"]
    },
    {
        "name": "Vegan Leather Wallet",
        "tags": ["vegan", "stylish", "compact"]
    },
    {
        "name": "Bamboo Toothbrush",
        "tags": ["eco-friendly", "vegan", "biodegradable"]
    },
    {
        "name": "Smartwatch",
        "tags": ["tech", "durable", "stylish"]
    }
]


# Store customer preferences
customer_preferences = []

while True:
    preference = input("Input a preference: ").strip().lower()
    customer_preferences.append(preference)

    another = input("Do you want to add another preference? (Y/N): ").strip().lower()

    if another == "n":
        break


# Convert customer preferences to a set
customer_preferences = set(customer_preferences)


# Convert product tags to sets
for product in products:
    product["tags"] = set(product["tags"])


def count_matches(product_tags, customer_preferences):
    """
    Count how many tags a product shares with the customer's preferences.
    """
    return len(product_tags.intersection(customer_preferences))


def recommend_products(products, customer_preferences):
    """
    Return products that have at least one matching tag,
    sorted from most matches to fewest matches.
    """
    recommendations = []

    for product in products:
        matches = count_matches(product["tags"], customer_preferences)

        if matches > 0:
            recommendations.append({
                "name": product["name"],
                "matches": matches
            })

    recommendations.sort(key=lambda product: product["matches"], reverse=True)

    return recommendations


# Generate recommendations
recommendations = recommend_products(products, customer_preferences)

print("\nRecommended Products:")

if recommendations:
    for product in recommendations:
        print(f"- {product['name']} ({product['matches']} match(es))")
else:
    print("No matching products found.")


