# Updated 5/18/2025 5:54 AM

# --- USDA Tier Budget Mapping ---

TIER_WEEKLY_BUDGET = {
    "Thrifty": 180,
    "Moderate": 250,
    "Liberal": 320
}

def calculate_budget_for_family(tier=None, family_size=4):
    tier = tier or "Liberal"
    base_budget = TIER_WEEKLY_BUDGET.get(tier, 320)
    # Baseline family of 4; add 25% per additional child
    extra_members = max(family_size - 4, 0)
    return base_budget + (extra_members * 0.25 * base_budget)


def infer_tier_from_budget(budget):
    if budget <= 180:
        return "Thrifty"
    elif 180 < budget <= 250:
        return "Moderate"
    else:
        return "Liberal"


# --- Thrifty Substitution Logic ---
thrifty_substitutions = {
    "Salmon fillet": "Canned tuna",
    "Beef strips": "Chicken thighs",
    "Mozzarella cheese": "Blended shredded cheese",
    "Marinara sauce": "Store-brand marinara",
    "Pizza dough": "Homemade dough",
    "Olive oil": "Vegetable oil",
    "Cheddar cheese": "Cheddar blend",
    "Pasta": "Generic pasta",
    "Ground beef": "Ground chicken",
    "Strawberries": "Canned fruit",
    "Eggs": "Store-brand eggs"
}

#def apply_tier_pricing(meal_plan, selected_tier):
#    if selected_tier == "Liberal":
#       new_price = max(price * 1.2, 0.5)
#       return meal_plan
#    if selected_tier != "Thrifty":
#      return meal_plan        
#    substituted_plan = {}
#   for day, meals in meal_plan.items():
#        new_meals = []
#        for meal_type, item, brand, price in meals:
#           if item in thrifty_substitutions:
#                new_item = thrifty_substitutions[item]
#                new_brand = "Generic"
#                new_price = max(price * 0.8, 0.5)  # Estimate 20% savings
#                new_meals.append((meal_type, new_item, new_brand, new_price))
#            else:
#                new_meals.append((meal_type, item, brand, price))
#        substituted_plan[day] = new_meals
#    return substituted_plan

def apply_tier_pricing(meal_plan, selected_tier):
    updated_plan = {}
    substitutions_made = []
    price_adjustments = []

    for day, meals in meal_plan.items():
        new_meals = []

        for meal_type, item, brand, price in meals:
            if selected_tier == "Thrifty":
                if item in thrifty_substitutions:
                    new_item = thrifty_substitutions[item]
                    new_brand = "Generic"
                    new_price = max(price * 0.8, 0.5)
                    new_meals.append((meal_type, new_item, new_brand, new_price))
                    substitutions_made.append(f"{item} ➜ {new_item} at ${new_price:.2f}")
                else:
                    new_price = max(price * 0.8, 0.5)
                    new_meals.append((meal_type, item, brand, new_price))
                    price_adjustments.append(f"{item} price reduced to ${new_price:.2f}")

            elif selected_tier == "Liberal":
                new_price = max(price * 1.2, 0.5)
                new_meals.append((meal_type, item, brand, new_price))
                price_adjustments.append(f"{item} price increased to ${new_price:.2f}")

            else:  # Moderate or default
                new_meals.append((meal_type, item, brand, price))

        updated_plan[day] = new_meals

    return updated_plan

# --- Base Ingredient Prices (USDA Estimate) ---
ingredient_base_prices = {
    "Milk": 3.50,
    "Eggs": 2.80,
    "Bread": 2.00,
    "Cheddar cheese": 4.00,
    "Mozzarella cheese": 4.50,
    "Spaghetti noodles": 1.20,
    "Pasta": 1.10,
    "Tortillas": 2.50,
    "Ground beef": 4.80,
    "Ground beef": 3.50,
    "Chicken breast": 3.50,
    "Beef strips": 5.00,
    "Salmon fillet": 7.00,
    "Canned tuna": 1.30,
    "Pizza dough": 2.50,
    "Tomato sauce": 1.70,
    "Marinara sauce": 2.00,
    "Rice": 1.00,
    "White rice": 1.10,
    "Oatmeal": 2.40,
    "Pancake mix": 2.20,
    "Maple syrup": 3.60,
    "Bananas": 0.25,
    "Strawberries": 2.50,
    "Lettuce": 1.80,
    "Shredded lettuce": 1.90,
    "Mixed vegetables": 2.20,
    "Hummus": 3.00,
    "Sliced turkey": 4.20,
    "Taco shells": 2.30,
    "Salsa": 2.00,
    "Olive oil": 4.50,
    "Butter": 3.20,
    "Garlic powder": 1.50,
    "Paprika": 1.50,
    "Peas": 1.00,
    "Egg noodles": 1.50,
    "Cream of mushroom soup": 1.40,
    "Mayonnaise": 3.00,
    "Pepperoni": 3.00,
    "Cream sauce": 2.00,
    "Lemon": 0.60,
    "Garlic": 0.50
}


# --- Ingredient Mapping for Shopping List ---
meal_ingredients = {
    "Baked Chicken": [
        {"item": "Chicken thighs", "qty": 2, "unit": "lb", "brand": "Tyson"},
        {"item": "Olive oil", "qty": 1, "unit": "bottle"},
        {"item": "Garlic powder", "qty": 1, "unit": "jar"},
        {"item": "Paprika", "qty": 1, "unit": "jar"}
    ],
    "Beef Stir Fry": [
        {"item": "Beef strips", "qty": 1, "unit": "lb"},
        {"item": "Mixed stir fry vegetables", "qty": 1, "unit": "bag"},
        {"item": "Soy sauce", "qty": 1, "unit": "bottle"},
        {"item": "Rice", "qty": 1, "unit": "lb"}
    ],
        "Turkey Stir Fry": [
        {"item": "Diced turkey", "qty": 1, "unit": "lb"},
        {"item": "Mixed stir fry vegetables", "qty": 1, "unit": "bag"},
        {"item": "Soy sauce", "qty": 1, "unit": "bottle"},
        {"item": "Rice", "qty": 1, "unit": "lb"}
    ],
    "Cereal & Milk": [
        {"item": "Cereal", "qty": 1, "unit": "box", "brand": "Kellogg's"},
        {"item": "Milk", "qty": 1, "unit": "gal", "brand": "Great Value"}
    ],
    "Chicken Salad": [
        {"item": "Chicken breast", "qty": 1, "unit": "lb", "brand": "Perdue"},
        {"item": "Mayonnaise", "qty": 1, "unit": "jar"},
        {"item": "Lettuce", "qty": 1, "unit": "head"}
    ],
    "Fish & Rice": [
        {"item": "Frozen fish fillets", "qty": 1, "unit": "pack", "brand": "Gorton's"},
        {"item": "White rice", "qty": 1, "unit": "lb"}
    ],
    "Grilled Cheese": [
        {"item": "Bread", "qty": 1, "unit": "loaf"},
        {"item": "Cheddar cheese", "qty": 1, "unit": "lb", "brand": "Kraft"},
        {"item": "Butter", "qty": 1, "unit": "stick"}
    ],
    "Grilled Salmon": [
        {"item": "Salmon fillet", "qty": 1, "unit": "lb", "brand": "SeaBest"},
        {"item": "Lemon", "qty": 2, "unit": "pcs"},
        {"item": "Olive oil", "qty": 1, "unit": "bottle"},
        {"item": "White rice", "qty": 1, "unit": "lb"}
    ],
    "Homemade Pizza": [
        {"item": "Pizza dough", "qty": 1, "unit": "pack", "brand": "Pillsbury"},
        {"item": "Tomato sauce", "qty": 1, "unit": "jar"},
        {"item": "Mozzarella cheese", "qty": 1, "unit": "lb"},
        {"item": "Pepperoni", "qty": 1, "unit": "pack"}
    ],
    "Oatmeal w/ fruit": [
        {"item": "Oatmeal", "qty": 1, "unit": "box", "brand": "Quaker"},
        {"item": "Bananas", "qty": 6, "unit": "pcs"},
        {"item": "Strawberries", "qty": 1, "unit": "lb"}
    ],
    "Pancakes": [
        {"item": "Pancake mix", "qty": 1, "unit": "box", "brand": "Aunt Jemima"},
        {"item": "Maple syrup", "qty": 1, "unit": "bottle"},
        {"item": "Eggs", "qty": 1, "unit": "dozen"}
    ],
    "Scrambled Eggs": [
        {"item": "Eggs", "qty": 1, "unit": "dozen"},
        {"item": "Milk", "qty": 0.5, "unit": "gal"},
        {"item": "Salt", "qty": 1, "unit": "shaker"}
    ],
    "Taco Night": [
        {"item": "Taco shells", "qty": 1, "unit": "pack", "brand": "Old El Paso"},
        {"item": "Ground beef", "qty": 1, "unit": "lb"},
        {"item": "Shredded lettuce", "qty": 1, "unit": "head"},
        {"item": "Cheddar cheese", "qty": 0.5, "unit": "lb"},
        {"item": "Salsa", "qty": 1, "unit": "jar", "brand": "Pace"}
    ],
    "Turkey Taco Night": [
        {"item": "Taco shells", "qty": 1, "unit": "pack", "brand": "Old El Paso"},
        {"item": "Ground turkey", "qty": 1, "unit": "lb"},
        {"item": "Shredded lettuce", "qty": 1, "unit": "head"},
        {"item": "Cheddar cheese", "qty": 0.5, "unit": "lb"},
        {"item": "Salsa", "qty": 1, "unit": "jar", "brand": "Pace"}
    ],
    "Tuna Casserole": [
        {"item": "Canned tuna", "qty": 2, "unit": "cans", "brand": "StarKist"},
        {"item": "Egg noodles", "qty": 1, "unit": "lb"},
        {"item": "Cream of mushroom soup", "qty": 1, "unit": "can"},
        {"item": "Peas", "qty": 1, "unit": "bag"}
    ],
    "Turkey Wrap": [
        {"item": "Tortillas", "qty": 1, "unit": "pack"},
        {"item": "Sliced turkey", "qty": 1, "unit": "lb", "brand": "Hillshire Farm"},
        {"item": "Lettuce", "qty": 1, "unit": "head"},
        {"item": "Cheddar cheese", "qty": 0.5, "unit": "lb"}
    ],
    "Veggie Wrap": [
        {"item": "Tortillas", "qty": 1, "unit": "pack"},
        {"item": "Mixed vegetables", "qty": 1, "unit": "bag", "brand": "Fresh Express"},
        {"item": "Hummus", "qty": 1, "unit": "container"}
    ]
}

# --- Enhanced Shopping List Generator ---
from collections import defaultdict

def generate_scaled_shopping_list(meal_plan, household_size=1):
    shopping_dict = defaultdict(lambda: {"qty": 0, "unit": "", "brand": ""})
    for day, meals in meal_plan.items():
        for meal in meals:
            meal_type, meal_name, brand, base_price = meal
            if meal_name in meal_ingredients:
                for ing in meal_ingredients[meal_name]:
                    item = ing["item"]
                    qty = ing.get("qty", 1) * household_size
                    unit = ing.get("unit", "")
                    brand = ing.get("brand", "")
                    if shopping_dict[item]["qty"] == 0:
                        shopping_dict[item]["unit"] = unit
                        shopping_dict[item]["brand"] = brand
                    shopping_dict[item]["qty"] += qty
    shopping_list = []
    for item, details in shopping_dict.items():
        shopping_list.append((item, f"{details['qty']:.2f} {details['unit']}", details["brand"]))
    return shopping_list



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
    meal_data = {}

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
    from fpdf import FPDF
    pdf = FPDF(format='letter')  # Use 8.5x11 inch paper
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "DonKats Meal Plan - 7 Day Summary", ln=True, align="C")
    pdf.set_font("Arial", "", 12)

    # Add small copyright line
    pdf.set_font("Arial", "", 9)
    pdf.cell(0, 5, "Copyright © 2025 by Donald and Kathy Sallot. All Rights Reserved.", ln=True, align="C")
    
    pdf.set_font("Arial", "", 10)
    
    pdf.cell(0, 10, f"  ", ln=True)
 
# Replaced by Kathy 
#   pdf.cell(0, 10, f"Zip Code: {data.get('zip_code', '')}", ln=True)
#
    pdf.cell(0, 10, f"Zip Code: {data.get('zip', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Budget: ${data.get('budget', 'N/A')}", ln=True)
    if 'restriction' in data:
        pdf.cell(0, 10, f"Food Restrictions: {data.get('restriction')}", ln=True)

    # Tier selection
    budget = float(data.get("budget", 0) or 0)
    selected_tier = infer_tier_from_budget(budget)
    
    # Get zip_code
    zip_code = data.get("zip_code", "")
    zip_code_save = (zip_code)
    region = get_region_from_zip(zip_code)
    multiplier = REGION_MULTIPLIER.get(region, 1.0)
   
    # Household Size Calculation
    household_size = 0
    if data.get('adult1_name') and data.get('adult1_age'):
        household_size += 1
    if data.get('adult2_name') and data.get('adult2_age'):
        household_size += 1
    for i in range(1, 5):
        if data.get(f'child{i}_name') and data.get(f'child{i}_age'):
            household_size += 1
    if household_size == 0:
        household_size = 1

    # Meal plan and tier adjustment
    meal_data = use_randomized_plan(data.get("include_fish_friday", True))
    meal_data = apply_tier_pricing(meal_data, selected_tier)

    pdf.cell(0, 10, f"Plan Tier: {selected_tier}", ln=True)

    pdf.cell(0, 10, f"  ", ln=True)

    # Generate meal plan and apply tier-specific substitutions
    meal_data = use_randomized_plan(data.get("include_fish_friday", True))
    meal_data = apply_tier_pricing(meal_data, selected_tier)

 ##   pdf.cell(0, 10, f"Plan Tier: {selected_tier}", ln=True)
 ##   meal_data = apply_tier_pricing(meal_data, selected_tier)

    # Meal plan
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
    pdf.cell(30, 8, "Est. Cost", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    shopping = generate_scaled_shopping_list(meal_data, household_size)


    for item, quantity, brand in shopping:
        price_per_unit = ingredient_base_prices.get(item, 1.00)
        qty_value = float(quantity.split()[0])
        est_price = price_per_unit * qty_value * multiplier
        pdf.cell(70, 8, item, 1)
        pdf.cell(30, 8, quantity, 1)
        pdf.cell(60, 8, brand, 1)
        pdf.cell(30, 8, f"${est_price:.2f}", 1)
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

    # Footer and file generation start here (outdented)
    pdf.ln(5)
    pdf.set_font("Arial", "", 10)

    from datetime import datetime
    current_date = datetime.now().strftime("%B %d, %Y")
    
    Zip_Code = {data.get('zip')}

    footer_note = (
        f"Note: Prices are based on USDA {region} region estimates and adjusted for ZIP {Zip_Code}.\n"
        f"   If budget is <= $ 180.00 then Thrifty Meal Plan is developed.\n"
        f"   If budget is <= $ 250.00 then Moderate Meal Plan is developed.\n"
        f"   If budget is >  $ 251.00 then Liberal Meal Plan is developed.\n"
        f"Generated on {current_date}. Actual prices may vary."
    )

   

    pdf.multi_cell(0, 6, footer_note)

    # Save and return the file
    output_file = "meal_plan_output.pdf"
    pdf.output(output_file)
    return output_file
