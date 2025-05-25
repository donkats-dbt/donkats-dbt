# Combined logic with calorie support and integrated generate_pdf function
# Please ensure ingredients.py is in the same folder

from fpdf import FPDF
from datetime import datetime
import random
from collections import defaultdict
from ingredients import ingredient_base_prices, ingredient_calories, meal_ingredients

# USDA Budget Mapping
TIER_WEEKLY_BUDGET = {
    "Thrifty": 180,
    "Moderate": 250,
    "Liberal": 320
}

def calculate_budget_for_family(tier=None, family_size=4):
    tier = tier or "Liberal"
    base_budget = TIER_WEEKLY_BUDGET.get(tier, 320)
    extra_members = max(family_size - 4, 0)
    return base_budget + (extra_members * 0.25 * base_budget)

def infer_tier_from_budget(budget):
    if budget <= 180:
        return "Thrifty"
    elif 180 < budget <= 250:
        return "Moderate"
    else:
        return "Liberal"

# Calorie logic
def calculate_meal_calories(meal_name):
    total_kcal = 0
    if meal_name in meal_ingredients:
        for ing in meal_ingredients[meal_name]:
            item = ing["item"]
            qty = ing.get("qty", 1)
            kcal_per_unit = ingredient_calories.get(item, 0)
            total_kcal += kcal_per_unit * qty
    return total_kcal

def add_calories_to_meal_plan(meal_plan):
    enhanced_plan = {}
    for day, meals in meal_plan.items():
        new_meals = []
        for meal_type, item, brand, price in meals:
            kcal = calculate_meal_calories(item)
            new_meals.append((meal_type, item, brand, price, kcal))
        enhanced_plan[day] = new_meals
    return enhanced_plan

# Thrifty substitutions
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

def apply_tier_pricing(meal_plan, selected_tier):
    updated_plan = {}
    for day, meals in meal_plan.items():
        new_meals = []
        for meal_type, item, brand, price in meals:
            if selected_tier == "Thrifty":
                if item in thrifty_substitutions:
                    item = thrifty_substitutions[item]
                    brand = "Generic"
                price = max(price * 0.8, 0.5)
            elif selected_tier == "Liberal":
                price = max(price * 1.2, 0.5)
            new_meals.append((meal_type, item, brand, price))
        updated_plan[day] = new_meals
    return updated_plan

# Region logic
def get_region_from_zip(zip_code):
    zip_prefix = int(str(zip_code).strip()[:1]) if zip_code else 3
    return (
        "Northeast" if zip_prefix in [0,1] else
        "Mid-Atlantic" if zip_prefix == 2 else
        "Southeast" if zip_prefix == 3 else
        "Midwest" if zip_prefix in [4,5] else
        "South Central" if zip_prefix in [6,7] else
        "Mountain" if zip_prefix == 8 else
        "West"
    )

REGION_MULTIPLIER = {
    "Northeast": 1.20,
    "Mid-Atlantic": 1.15,
    "Southeast": 1.00,
    "Midwest": 1.10,
    "South Central": 1.05,
    "Mountain": 1.10,
    "West": 1.25
}

# Sample meal plan generator
def use_randomized_plan(include_fish_on_friday=True):
    breakfast = [("Oatmeal w/ fruit", "Quaker", 1.20), ("Pancakes", "Aunt Jemima", 1.50), ("Scrambled Eggs", "Eggland's Best", 1.40), ("Cereal & Milk", "Kellogg's", 1.00)]
    lunch = [("Grilled Cheese", "Kraft", 2.30), ("Turkey Wrap", "Hillshire Farm", 2.70), ("Chicken Salad", "Perdue", 2.90), ("Veggie Wrap", "Fresh Express", 2.20)]
    dinner = [("Chicken Pasta", "Tyson", 4.80), ("Spaghetti", "Barilla", 4.50), ("Beef Stir Fry", "Smithfield", 5.00), ("Taco Night", "Old El Paso", 4.80), ("Baked Chicken", "Tyson", 5.20), ("Homemade Pizza", "Pillsbury", 5.50)]
    fish = [("Fish & Rice", "Gorton's", 5.10), ("Grilled Salmon", "SeaBest", 6.00), ("Tuna Casserole", "StarKist", 4.70)]
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return {d: [("Breakfast", *random.choice(breakfast)), ("Lunch", *random.choice(lunch)), ("Dinner", *random.choice(dinner + fish if d == "Friday" and include_fish_on_friday else dinner))] for d in days}

def generate_scaled_shopping_list(meal_plan, household_size=1):
    shopping_dict = defaultdict(lambda: {"qty": 0, "unit": "", "brand": ""})
    for day, meals in meal_plan.items():
        for meal in meals:
            meal_type, meal_name, brand, base_price, _ = meal  # ignore kcal
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

# --- generate_pdf() with calorie tracking integrated ---
def generate_pdf(data):
    pdf = FPDF(format='letter')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "DonKats Meal Plan - 7 Day Summary", ln=True, align="C")
    pdf.set_font("Arial", "", 9)
    pdf.cell(0, 5, "Copyright © 2025 by Donald and Kathy Sallot. All Rights Reserved.", ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 8, f"  ", ln=True)

    zip_code = data.get("zip", "N/A")
    zip_info = data.get('zip', 'N/A')
    budget = data.get("budget", "N/A")
    restriction = data.get("restriction", "").strip() or "No restrictions"

    budget = float(data.get("budget", 0) or 0)
    selected_tier = infer_tier_from_budget(budget)
    zip_code = data.get("zip_code", "")
    region = get_region_from_zip(zip_code)
    multiplier = REGION_MULTIPLIER.get(region, 1.0)

    household_size = sum(bool(data.get(f'{role}_name') and data.get(f'{role}_age')) for role in ['adult1', 'adult2'])

    for i in range(1, 5):
        if data.get(f'child{i}_name') and data.get(f'child{i}_age'):
            household_size += 1
    if household_size == 0:
        household_size = 1

    meal_data = use_randomized_plan(data.get("include_fish_friday", True))
    meal_data = apply_tier_pricing(meal_data, selected_tier)
    meal_data = add_calories_to_meal_plan(meal_data)
    
    pdf.cell(50, 10, f"Zip Code: {zip_info}", ln=0)                 
    pdf.cell(50, 10, f"Budget: ${budget.2f}", ln=0) 
    pdf.cell(50, 10, f"Plan Tier: {selected_tier}", ln=1)   
    pdf.cell(50, 10, f"Food Restrictions: {restriction}", ln=True)       

    pdf.cell(0, 10, f"  ", ln=True)

    weekly_total = 0
    weekly_total_kcal = 0
    for day, meals in meal_data.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, f"{day}", ln=True)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(35, 8, "Meal", 1)
        pdf.cell(65, 8, "Item", 1)
        pdf.cell(45, 8, "Brand Option", 1)
        pdf.cell(25, 8, "Cost", 1)
        pdf.cell(20, 8, "Kcal", 1)
        pdf.ln()

        pdf.set_font("Arial", "", 10)
        daily_total_kcal = 0
        for meal, item, brand, price, kcal in meals:
            total_price = price * household_size * multiplier
            pdf.cell(35, 8, meal, 1)
            pdf.cell(65, 8, item, 1)
            pdf.cell(45, 8, brand, 1)
            pdf.cell(25, 8, f"${total_price:.2f}", 1)
            pdf.cell(20, 8, f"{kcal}", 1)
            pdf.ln()
            weekly_total += total_price
            daily_total_kcal += kcal
            weekly_total_kcal += kcal

        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 8, f"Total Calories for {day}: {daily_total_kcal} kcal", ln=True)
        pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Total Weekly Cost: ${weekly_total:.2f}", ln=True)
    pdf.cell(0, 10, f"Total Weekly Calories: {weekly_total_kcal} kcal", ln=True)
    remaining = budget - weekly_total
    pdf.cell(0, 10, f"Remaining Budget: ${remaining:.2f}", ln=True)

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
    for role in ['adult1', 'adult2']:
        if data.get(f'{role}_name') and data.get(f'{role}_age'):
            members.append((data[f'{role}_name'], int(data[f'{role}_age'])))
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

    pdf.ln(5)
    
    pdf.set_font("Arial", "", 10)
    
    current_date = datetime.now().strftime("%B %d, %Y")
    

    footer_note = (
        f"Note: Prices are based on USDA {region} region estimates and adjusted for ZIP {zip_info}.\n"
        f"If budget is <= $180, Thrifty Meal Plan is developed.\n"
        f"If budget is <= $250, Moderate Meal Plan is developed.\n"
        f"If budget is > $251, Liberal Meal Plan is developed.\n"
        f"Generated on {current_date}. Actual prices may vary."
    )
    pdf.multi_cell(0, 6, footer_note)
    output_file = "meal_plan_output.pdf"
    pdf.output(output_file)
    return output_file

    pdf.multi_cell(0, 6, footer_note)
    output_file = "meal_plan_output.pdf"
    pdf.output(output_file)
    return output_file
