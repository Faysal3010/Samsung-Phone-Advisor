from db_setup import get_db_connection, create_table

def seed_database():
    # 1. Re-create the table
    create_table()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. 30 Premium Samsung Phones Data
    # Format: (Model, Release Date, Display, Battery, Camera, RAM, Storage, Price)
    phones = [
        # --- S24 Series ---
        ("Samsung Galaxy S24 Ultra", "January 2024", "6.8-inch Dynamic LTPO AMOLED 2X", "5000 mAh, 45W", "200MP Main, 50MP Periscope", "12GB", "256GB/512GB/1TB", "$1299"),
        ("Samsung Galaxy S24 Plus", "January 2024", "6.7-inch Dynamic LTPO AMOLED 2X", "4900 mAh, 45W", "50MP Main, 10MP Telephoto", "12GB", "256GB/512GB", "$999"),
        ("Samsung Galaxy S24", "January 2024", "6.2-inch Dynamic LTPO AMOLED 2X", "4000 mAh, 25W", "50MP Main, 10MP Telephoto", "8GB", "128GB/256GB/512GB", "$799"),
        
        # --- Z Fold & Flip 6/5 Series ---
        ("Samsung Galaxy Z Fold 6", "July 2024", "7.6-inch Foldable Dynamic AMOLED 2X", "4400 mAh, 25W", "50MP Main, 10MP Telephoto", "12GB", "256GB/512GB/1TB", "$1899"),
        ("Samsung Galaxy Z Flip 6", "July 2024", "6.7-inch Foldable Dynamic AMOLED 2X", "4000 mAh, 25W", "50MP Main, 12MP Ultrawide", "12GB", "256GB/512GB", "$1099"),
        ("Samsung Galaxy Z Fold 5", "August 2023", "7.6-inch Foldable Dynamic AMOLED 2X", "4400 mAh, 25W", "50MP Main, 10MP Telephoto", "12GB", "256GB/512GB/1TB", "$1799"),
        ("Samsung Galaxy Z Flip 5", "August 2023", "6.7-inch Foldable Dynamic AMOLED 2X", "3700 mAh, 25W", "12MP Main, 12MP Ultrawide", "8GB", "256GB/512GB", "$999"),

        # --- S23 Series ---
        ("Samsung Galaxy S23 Ultra", "February 2023", "6.8-inch Dynamic AMOLED 2X", "5000 mAh, 45W", "200MP Main, 10MP Telephoto", "8GB/12GB", "256GB/512GB/1TB", "$1199"),
        ("Samsung Galaxy S23 Plus", "February 2023", "6.6-inch Dynamic AMOLED 2X", "4700 mAh, 45W", "50MP Main, 10MP Telephoto", "8GB", "256GB/512GB", "$999"),
        ("Samsung Galaxy S23", "February 2023", "6.1-inch Dynamic AMOLED 2X", "3900 mAh, 25W", "50MP Main, 10MP Telephoto", "8GB", "128GB/256GB", "$799"),
        ("Samsung Galaxy S23 FE", "October 2023", "6.4-inch Dynamic AMOLED 2X", "4500 mAh, 25W", "50MP Main, 8MP Telephoto", "8GB", "128GB/256GB", "$599"),

        # --- Z Fold & Flip 4 Series ---
        ("Samsung Galaxy Z Fold 4", "August 2022", "7.6-inch Foldable Dynamic AMOLED 2X", "4400 mAh, 25W", "50MP Main, 10MP Telephoto", "12GB", "256GB/512GB/1TB", "$1499"),
        ("Samsung Galaxy Z Flip 4", "August 2022", "6.7-inch Foldable Dynamic AMOLED 2X", "3700 mAh, 25W", "12MP Main, 12MP Ultrawide", "8GB", "128GB/256GB/512GB", "$899"),

        # --- S22 Series ---
        ("Samsung Galaxy S22 Ultra", "February 2022", "6.8-inch Dynamic AMOLED 2X", "5000 mAh, 45W", "108MP Main, 10MP Periscope", "8GB/12GB", "128GB/256GB/512GB/1TB", "$900"),
        ("Samsung Galaxy S22 Plus", "February 2022", "6.6-inch Dynamic AMOLED 2X", "4500 mAh, 45W", "50MP Main, 10MP Telephoto", "8GB", "128GB/256GB", "$700"),
        ("Samsung Galaxy S22", "February 2022", "6.1-inch Dynamic AMOLED 2X", "3700 mAh, 25W", "50MP Main, 10MP Telephoto", "8GB", "128GB/256GB", "$600"),

        # --- S21 Series ---
        ("Samsung Galaxy S21 Ultra", "January 2021", "6.8-inch Dynamic AMOLED 2X", "5000 mAh, 25W", "108MP Main, 10MP Periscope", "12GB/16GB", "128GB/256GB/512GB", "$800"),
        ("Samsung Galaxy S21 FE", "January 2022", "6.4-inch Dynamic AMOLED 2X", "4500 mAh, 25W", "12MP Main, 8MP Telephoto", "6GB/8GB", "128GB/256GB", "$500"),
        ("Samsung Galaxy S21 Plus", "January 2021", "6.7-inch Dynamic AMOLED 2X", "4800 mAh, 25W", "12MP Main, 64MP Telephoto", "8GB", "128GB/256GB", "$600"),

        # --- Note Series (Legendary) ---
        ("Samsung Galaxy Note 20 Ultra", "August 2020", "6.9-inch Dynamic AMOLED 2X", "4500 mAh, 25W", "108MP Main, 12MP Periscope", "12GB", "256GB/512GB", "$850"),
        
        # --- High-End A Series & Others ---
        ("Samsung Galaxy A55", "March 2024", "6.6-inch Super AMOLED", "5000 mAh, 25W", "50MP Main, 12MP Ultrawide", "8GB/12GB", "128GB/256GB", "$479"),
        ("Samsung Galaxy A54", "March 2023", "6.4-inch Super AMOLED", "5000 mAh, 25W", "50MP Main, 12MP Ultrawide", "6GB/8GB", "128GB/256GB", "$350"),
        ("Samsung Galaxy A35", "March 2024", "6.6-inch Super AMOLED", "5000 mAh, 25W", "50MP Main, 8MP Ultrawide", "6GB/8GB", "128GB/256GB", "$399"),
        ("Samsung Galaxy A73 5G", "March 2022", "6.7-inch Super AMOLED Plus", "5000 mAh, 25W", "108MP Main, 12MP Ultrawide", "6GB/8GB", "128GB/256GB", "$450"),
        ("Samsung Galaxy F55", "May 2024", "6.7-inch Super AMOLED Plus", "5000 mAh, 45W", "50MP Main, 8MP Ultrawide", "8GB/12GB", "128GB/256GB", "$360"),
        ("Samsung Galaxy M55", "March 2024", "6.7-inch Super AMOLED Plus", "5000 mAh, 45W", "50MP Main, 8MP Ultrawide", "8GB/12GB", "128GB/256GB", "$330"),
        ("Samsung Galaxy Quantum 4", "May 2023", "6.4-inch Super AMOLED", "5000 mAh, 25W", "50MP Main, 12MP Ultrawide", "8GB", "128GB", "$450"),
        ("Samsung Galaxy XCover 7", "January 2024", "6.6-inch PLS LCD", "4050 mAh (Removable), 15W", "50MP Main", "6GB", "128GB", "$400"),
        ("Samsung W24", "September 2023", "7.6-inch Foldable AMOLED", "4400 mAh, 25W", "50MP Main, 10MP Telephoto", "16GB", "1TB", "$2200"),
        ("Samsung W24 Flip", "September 2023", "6.7-inch Foldable AMOLED", "3700 mAh, 25W", "12MP Main, 12MP Ultrawide", "12GB", "512GB", "$1300")
    ]
    
    print(f"Inserting {len(phones)} phones into database...")
    
    for p in phones:
        try:
            cursor.execute("""
                INSERT INTO phones (model_name, release_date, display, battery, camera, ram, storage, price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, p)
        except Exception as e:
            print(f"Skipped {p[0]}: {e}")
            
    conn.commit()
    cursor.close()
    conn.close()
    print("All 30 phones inserted successfully!")
