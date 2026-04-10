class food_item:
    def __init__(self, name, calories, protein, carbohydrate, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat
        
def nutrition_data_tracker(food):
   
    total_calories = 0
    total_protein = 0
    total_carbohydrate = 0
    total_fat = 0

    for item in food:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrate += item.carbohydrate
        total_fat += item.fat

    print("Total calories:", total_calories)
    print("Total protein:", total_protein, "g")
    print("Total carbohydrate:", total_carbohydrate, "g")
    print("Total fat:", total_fat, "g")

    if total_calories > 2500:
        print("Warning: excessive calorie consumption.")
    if total_fat > 90:
        print("Warning: excessive fat consumption.")

    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbohydrate": total_carbohydrate,
        "fat": total_fat
    }


# Example 
apple = food_item("Apple", 60, 0.3, 15, 0.5)
rice = food_item("Rice", 300, 6, 65, 1)
chicken = food_item("Chicken Breast", 400, 35, 0, 10)
burger = food_item("Burger", 800, 25, 50, 45)
fries = food_item("Fries", 500, 5, 60, 25)
ice_cream = food_item("Ice Cream", 350, 5, 40, 15)

foods_eaten = [apple, rice, chicken, burger, fries, ice_cream]

nutrition_data_tracker(foods_eaten)