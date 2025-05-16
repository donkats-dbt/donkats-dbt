
import random

def use_randomized_plan(include_fish_on_friday=True):
    breakfast_options = [
        ("Oatmeal w/ fruit", "Quaker", 1.20),
        ("Pancakes", "Aunt Jemima", 1.50),
        ("Scrambled Eggs", "Eggland's Best", 1.40),
        ("Cereal & Milk", "Kellogg's", 1.00)
    ]
    lunch_options = [
        ("Grilled Cheese", "Kraft", 2.30),
        ("Turkey Wrap", "Hillshire Farm", 2.70),
        ("Chicken Salad", "Perdue", 2.90),
        ("Veggie Wrap", "Fresh Express", 2.20)
    ]
    dinner_options = [
        ("Chicken Pasta", "Tyson", 4.80),
        ("Spaghetti", "Barilla", 4.50),
        ("Beef Stir Fry", "Smithfield", 5.00),
        ("Taco Night", "Old El Paso", 4.80),
        ("Baked Chicken", "Tyson", 5.20),
        ("Homemade Pizza", "Pillsbury", 5.50),
    ]
    fish_dinners = [
        ("Fish & Rice", "Gorton's", 5.10),
        ("Grilled Salmon", "SeaBest", 6.00),
        ("Tuna Casserole", "StarKist", 4.70)
    ]

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    meal_data = use_randomized_plan(data.get('include_fish_friday', True))

    for day in weekdays:
        breakfast = random.choice(breakfast_options)
        lunch = random.choice(lunch_options)
        if day == "Friday" and include_fish_on_friday:
            dinner_pool = dinner_options + fish_dinners
        else:
            dinner_pool = dinner_options
        dinner = random.choice(dinner_pool)
        meal_data[day] = [
            ("Breakfast", *breakfast),
            ("Lunch", *lunch),
            ("Dinner", *dinner)
        ]
    return meal_data


from fpdf import FPDF

from datetime import datetime  

# --- Region detection and pricing multiplier setup ---
def get_region_from_zip(zip_code):
    if not zip_code or len(zip_code) < 1:
        return "Southeast"  # default fallback
    zip_prefix = int(str(zip_code).strip()[:1])
    if zip_prefix == 0 or zip_prefix == 1:
        return "Northeast"
    elif zip_prefix == 2:
        return "Mid-Atlantic"
    elif zip_prefix == 3:
        return "Southeast"
    elif zip_prefix == 4 or zip_prefix == 5:
        return "Midwest"
    elif zip_prefix == 6 or zip_prefix == 7:
        return "South Central"
    elif zip_prefix == 8:
        return "Mountain"
    elif zip_prefix == 9:
        return "West"
    else:
        return "Southeast"

REGION_MULTIPLIER = {
    "Northeast": 1.20,
    "Mid-Atlantic": 1.15,
    "Southeast": 1.00,
    "Midwest": 1.10,
    "South Central": 1.05,
    "Mountain": 1.10,
    "West": 1.25,
}

def generate_pdf(data):
    pdf = FPDF(format='letter')  # Use 8.5x11 inch paper
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "DonKats Meal Plan - 7 Day Summary", ln=True, align="C")

    # Add small copyright line
    pdf.set_font("Arial", "", 9)
    pdf.cell(0, 5, "Copyright © 2025 by Donald and Kathy Sallot. All Rights Reserved.", ln=True, align="C")
   
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Budget: ${data.get('budget', 'N/A')}", ln=True)
    zip_code = data.get('zip', '39503')
#    pdf.cell(0, 10, f"ZIP Code: {zip_code}", ln=True)

    if 'restriction' in data:
        pdf.cell(0, 10, f"Food Restrictions: {data.get('restriction')}", ln=True)

    pdf.ln(5)

    # Household size calculation
    household_size = 0
    if data.get('adult1_name') or data.get('adult1_age'):
        household_size += 1
    if data.get('adult2_name') or data.get('adult2_age'):
        household_size += 1
    for i in range(1, 7):
        if data.get(f'child{i}_name') or data.get(f'child{i}_age'):
            household_size += 1
    if household_size == 0:
        household_size = 1

    # Region pricing logic
    region = get_region_from_zip(zip_code)
    multiplier = REGION_MULTIPLIER.get(region, 1.00)

    # Meal plan
    meal_data = {
        "Sunday": [
            ("Breakfast", "Oatmeal w/ fruit", "Quaker", 1.20),
            ("Lunch", "Grilled Cheese", "Kraft", 2.30),
            ("Dinner", "Chicken Pasta", "Tyson", 4.80)
        ],
        "Monday": [
            ("Breakfast", "Pancakes", "Aunt Jemima", 1.50),
            ("Lunch", "Turkey Wrap", "Hillshire Farm", 2.70),
            ("Dinner", "Beef Stir Fry", "Smithfield", 5.00)
        ],
        "Tuesday": [
            ("Breakfast", "Scrambled Eggs", "Eggland's Best", 1.40),
            ("Lunch", "Chicken Salad", "Perdue", 2.90),
            ("Dinner", "Spaghetti", "Barilla", 4.50)
        ],
        "Wednesday": [
            ("Breakfast", "Bagel & Cream Cheese", "Philadelphia", 1.30),
            ("Lunch", "Veggie Wrap", "Fresh Express", 2.20),
            ("Dinner", "Baked Chicken", "Tyson", 5.20)
        ],
        "Thursday": [
            ("Breakfast", "Cereal & Milk", "Kellogg's", 1.00),
            ("Lunch", "Ham Sandwich", "Oscar Mayer", 2.40),
            ("Dinner", "Taco Night", "Old El Paso", 4.80)
        ],
        "Friday": [
            ("Breakfast", "Waffles", "Eggo", 1.50),
            ("Lunch", "Quesadilla", "Sargento", 2.60),
            ("Dinner", "Fish & Rice", "Gorton's", 5.10)
        ],
        "Saturday": [
            ("Breakfast", "French Toast", "Pepperidge Farm", 1.60),
            ("Lunch", "PB&J Sandwich", "Jif & Smucker's", 1.80),
            ("Dinner", "Homemade Pizza", "Pillsbury", 5.50)
        ]
    }

    weekly_total = 0
    for day, meals in meal_data.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, f"{day}", ln=True)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(35, 8, "Meal", 1)
        pdf.cell(75, 8, "Item", 1)
        pdf.cell(50, 8, "Brand Option", 1)
        pdf.cell(30, 8, "Cost", 1)
        pdf.ln()

        pdf.set_font("Arial", "", 10)
        for meal, item, brand, price in meals:
            total_price = price * household_size * multiplier
            pdf.cell(35, 8, meal, 1)
            pdf.cell(75, 8, item, 1)
            pdf.cell(50, 8, brand, 1)
            pdf.cell(30, 8, f"${total_price:.2f}", 1)
            pdf.ln()
            weekly_total += total_price

        pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Total Weekly Cost: ${weekly_total:.2f}", ln=True)
    budget = float(data.get('budget', 0) or 0)
    remaining = budget - weekly_total
    pdf.cell(0, 10, f"Remaining Budget: ${remaining:.2f}", ln=True)

    # Shopping list
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Shopping List", ln=True)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(70, 8, "Item", 1)
    pdf.cell(30, 8, "Quantity", 1)
    pdf.cell(60, 8, "Brand Option", 1)
    pdf.cell(30, 8, "Total", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    shopping = [
        ("Oatmeal", 1, "box", "Quaker", 1.20),
        ("Bread", 2, "loaves", "Store Brand", 4.00),
        ("Chicken Breast", 3, "lb", "Tyson", 8.97),
        ("Milk", 1, "gal", "Great Value", 3.50),
        ("Pasta", 1, "box", "Barilla", 1.00),
        ("Cheese", 1, "block", "Kraft", 2.50),
        ("Eggs", 1, "dozen", "Eggland's Best", 2.20),
        ("Wraps", 1, "pack", "Mission", 2.00),
        ("Cereal", 1, "box", "Kellogg's", 1.00),
        ("Pizza Dough", 1, "pack", "Pillsbury", 2.50)
    ]

    for item, qty, unit, brand, price in shopping:
        total_qty = qty * household_size
        total_price = price * household_size * multiplier
        pdf.cell(70, 8, item, 1)
        pdf.cell(30, 8, f"{total_qty} {unit}", 1)
        pdf.cell(60, 8, brand, 1)
        pdf.cell(30, 8, f"${total_price:.2f}", 1)
        pdf.ln()

    # Calorie Summary
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Calorie Summary", ln=True)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(60, 8, "Name", 1)
    pdf.cell(20, 8, "Age", 1)
    pdf.cell(50, 8, "Daily Cal.", 1)
    pdf.cell(50, 8, "Weekly Total", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    members = []
    
    if data.get('adult1_name') and data.get('adult1_age'):
        members.append((data['adult1_name'], int(data['adult1_age'])))
    if data.get('adult2_name') and data.get('adult2_age'):
        members.append((data['adult2_name'], int(data['adult2_age'])))

    for i in range(1, 7):
        name = data.get(f'child{i}_name')
        age = data.get(f'child{i}_age')
        if name and age:
            members.append((name, int(age)))

    for name, age in members:
        if age >= 18:
            daily = 2200 if age > 40 else 2000
        elif age >= 13:
            daily = 2000
        elif age >= 10:
            daily = 1800
        elif age >= 7:
            daily = 1600
        else:
            daily = 1400
        weekly = daily * 7
        pdf.cell(60, 8, name, 1)
        pdf.cell(20, 8, str(age), 1)
        pdf.cell(50, 8, f"{daily} kcal", 1)
        pdf.cell(50, 8, f"{weekly} kcal", 1)
        pdf.ln()

    # ✅ Footer and file generation start here (outdented)
    pdf.ln(5)
    pdf.set_font("Arial", "I", 9)

    from datetime import datetime
    current_date = datetime.now().strftime("%B %d, %Y")

    footer_note = (
        f"Note: Prices are based on USDA {region} region estimates and adjusted for ZIP {zip_code}.\n"
        f"Generated on {current_date}. Actual prices may vary."
    )

    pdf.multi_cell(0, 6, footer_note)

    # Save and return the file
    output_file = "meal_plan_output.pdf"
    pdf.output(output_file)
    return output_file
