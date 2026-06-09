from property import Property
from specialized_housing import Apartment, Villa, Penthouse

def generate_market_report(listings):
    print("\n--- MARKET DASHBOARD REPORT ---")
    total_value = 0
    for item in listings:
        item.display_listing()
        total_value += item.price
    print(f"Total Market Value: {total_value:.2f}B VND")

def villa_inspection(listings):
    print("\n--- RUNNING VILLA INSPECTION ---")
    for item in listings:
        if isinstance(item, Villa):
            print(f"--- Inspection Required for Pool at Property {item.prop_id} ---")
        else:
            print(f"--- Property {item.prop_id} does not require pool inspection ---")

if __name__ == "__main__":
    # Initializing Mock Data Array
    market_dashboard = [
        Apartment(201, "Ocean Park, Gia Lam", 3.1, 55, 15),
        Apartment(202, "Times City, Hai Ba Trung", 4.5, 75, 22),
        Villa(301, "Vinhomes Riverside", 35.0, 300, True),
        Villa(302, "Ciputra, Tay Ho", 50.0, 450, False),
        Penthouse(401, "Keangnam Landmark 72", 15.5, 250, True),
        Penthouse(402, "Lotte Center, Ba Dinh", 18.0, 280, False)
    ]

    # Step 4: Market Dashboard Execution
    generate_market_report(market_dashboard)

    # Step 5: Type-Specific Search Execution
    villa_inspection(market_dashboard)

    # Step 6: Dynamic State Modification Execution
    print("\n--- BEFORE RENOVATION ---")
    market_dashboard[3].display_listing()

    print("\n--- CALLING ADD_POOL() ON CIPUTRA VILLA ---")
    market_dashboard[3].add_pool()

    print("\n--- AFTER RENOVATION ---")
    market_dashboard[3].display_listing()