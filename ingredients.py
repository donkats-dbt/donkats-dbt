# ingredients.py

# Base prices per item (for shopping list estimates)
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
    "Garlic": 0.50,
    "Salt": 0.20,
    "Cereal": 3.50,
    "Frozen fish fillets": 5.10,
    "Diced turkey": 4.00,
    "Mixed stir fry vegetables": 2.50,
    "Soy sauce": 2.00,
    "Ground turkey": 4.30
}

# Estimated calorie values per ingredient
ingredient_calories = {
    "Bananas": 90,
    "Beef strips": 250,
    "Blended shredded cheese": 100,
    "Bread": 80,
    "Butter": 102,
    "Canned tuna": 100,
    "Cereal": 110,
    "Cheddar cheese": 113,
    "Chicken breast": 165,
    "Chicken thighs": 209,
    "Cream of mushroom soup": 100,
    "Cream sauce": 100,
    "Diced turkey": 140,
    "Egg noodles": 221,
    "Eggs": 78,
    "Frozen fish fillets": 180,
    "Garlic powder": 8,
    "Garlic": 4,
    "Generic pasta": 200,
    "Generic": 100,
    "Ground beef": 250,
    "Ground chicken": 170,
    "Ground turkey": 140,
    "Homemade dough": 250,
    "Hummus": 70,
    "Lemon": 17,
    "Lettuce": 5,
    "Maple syrup": 52,
    "Marinara sauce": 70,
    "Mayonnaise": 90,
    "Milk": 150,
    "Mixed stir fry vegetables": 50,
    "Mixed vegetables": 60,
    "Mozzarella cheese": 85,
    "Oatmeal": 150,
    "Olive oil": 120,
    "Pancake mix": 200,
    "Paprika": 6,
    "Pasta": 200,
    "Peas": 62,
    "Pepperoni": 140,
    "Pizza dough": 250,
    "Rice": 206,
    "Salmon fillet": 208,
    "Salsa": 15,
    "Salt": 0,
    "Shredded lettuce": 5,
    "Sliced turkey": 120,
    "Soy sauce": 10,
    "Spaghetti noodles": 200,
    "Store-brand eggs": 78,
    "Store-brand marinara": 60,
    "Strawberries": 50,
    "Taco shells": 140,
    "Tomato sauce": 80,
    "Tortillas": 140,
    "White rice": 206
}

# Ingredient mapping per meal
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
    ],
    "Chicken Pasta": [
        {"item": "Ground chicken", "qty": 2, "unit": "lb", "brand": "Tyson"},
		{"item": "Spaghetti noodles", "qty": 1, "unit": "lb", "brand": "Barilla"},
        {"item": "Olive oil", "qty": 1, "unit": "bottle"},
        {"item": "Garlic powder", "qty": 1, "unit": "jar"},
        {"item": "Paprika", "qty": 1, "unit": "jar"}
    ],
    "Spaghetti": [
        {"item": "Ground beef", "qty": 2, "unit": "lb"},
		{"item": "Spaghetti noodles", "qty": 1, "unit": "lb", "brand": "Barilla"},
        {"item": "Olive oil", "qty": 1, "unit": "bottle"},
        {"item": "Garlic powder", "qty": 1, "unit": "jar"},
        {"item": "Paprika", "qty": 1, "unit": "jar"}
    ]    
}
