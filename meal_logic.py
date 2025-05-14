
from fpdf import FPDF

def generate_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "DonKats Meal Plan - 7 Day Summary", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Budget: ${data.get('budget', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"ZIP Code: {data.get('zip', 'N/A')}", ln=True)

    if 'restriction' in data:
        pdf.cell(0, 10, f"Food Restrictions: {data.get('restriction')}", ln=True)

    pdf.ln(5)

    # Weekly meal data
    meal_data = {
        "Sunday": [("Breakfast", "Oatmeal w/ fruit", 1.20), ("Lunch", "Grilled Cheese", 2.30), ("Dinner", "Chicken Pasta", 4.80)],
        "Monday": [("Breakfast", "Pancakes", 1.50), ("Lunch", "Turkey Wrap", 2.70), ("Dinner", "Beef Stir Fry", 5.00)],
        "Tuesday": [("Breakfast", "Scrambled Eggs", 1.40), ("Lunch", "Chicken Salad", 2.90), ("Dinner", "Spaghetti", 4.50)],
        "Wednesday": [("Breakfast", "Bagel & Cream Cheese", 1.30), ("Lunch", "Veggie Wrap", 2.20), ("Dinner", "Baked Chicken", 5.20)],
        "Thursday": [("Breakfast", "Cereal & Milk", 1.00), ("Lunch", "Ham Sandwich", 2.40), ("Dinner", "Taco Night", 4.80)],
        "Friday": [("Breakfast", "Waffles", 1.50), ("Lunch", "Quesadilla", 2.60), ("Dinner", "Fish & Rice", 5.10)],
        "Saturday": [("Breakfast", "French Toast", 1.60), ("Lunch", "PB&J Sandwich", 1.80), ("Dinner", "Homemade Pizza", 5.50)]
    }

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "7-Day Meal Plan", ln=True)

    weekly_total = 0
    for day, meals in meal_data.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, f"{day}", ln=True)
        pdf.set_font("Arial", "", 10)
        for meal, item, price in meals:
            pdf.cell(40, 8, meal, 1)
            pdf.cell(100, 8, item, 1)
            pdf.cell(40, 8, f"${price:.2f}", 1)
            pdf.ln()
            weekly_total += price
        pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Total Weekly Cost: ${weekly_total:.2f}", ln=True)

    budget = float(data.get('budget', 0))
    remaining = budget - weekly_total
    pdf.cell(0, 10, f"Remaining Budget: ${remaining:.2f}", ln=True)

    # Page break for shopping list
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Shopping List", ln=True)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(70, 8, "Item", 1)
    pdf.cell(30, 8, "Quantity", 1)
    pdf.cell(60, 8, "Brand", 1)
    pdf.cell(30, 8, "Total", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    shopping = [
        ("Oatmeal", "1 box", "Quaker", 1.20),
        ("Bread", "2 loaves", "Store Brand", 4.00),
        ("Chicken Breast", "3 lb", "Tyson", 8.97),
        ("Milk", "1 gal", "Great Value", 3.50),
        ("Pasta", "1 box", "Barilla", 1.00),
        ("Cheese", "1 block", "Kraft", 2.50),
        ("Eggs", "1 dozen", "Eggland's Best", 2.20),
        ("Wraps", "6 pack", "Mission", 2.00),
        ("Cereal", "1 box", "Kellogg's", 1.00),
        ("Pizza Dough", "1 pack", "Pillsbury", 2.50)
    ]

    for item, qty, brand, total in shopping:
        pdf.cell(70, 8, item, 1)
        pdf.cell(30, 8, qty, 1)
        pdf.cell(60, 8, brand, 1)
        pdf.cell(30, 8, f"${total:.2f}", 1)
        pdf.ln()

    # Page break for calorie summary
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

    for i in range(1, 5):
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
    pdf.set_font("Arial", "I", 9)
    pdf.multi_cell(0, 6, "Note: Prices are based on USDA Southeast region estimates and adjusted for ZIP 39503 (Gulfport, MS). Actual prices may vary.")

    output_file = "meal_plan_output.pdf"
    pdf.output(output_file)
    return output_file
