import requests

def get_nutrition_data(plu_number, api_key):
    base_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": api_key,
        "x-app-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "query": f"{plu_number}"
    }

    response = requests.post(base_url, json=payload, headers=headers)
    data = response.json()

    return data

def display_plu_info(plu_number, api_key):
    try:
        nutrition_data = get_nutrition_data(plu_number, api_key)
        if 'foods' in nutrition_data:
            food_info = nutrition_data['foods'][0]
            food_name = food_info['food_name']
            calories = food_info['nf_calories']
            nutrients = food_info['full_nutrients']

            print(f"Nutritional Information for {food_name} (PLU: {plu_number}):")
            print(f"Calories: {calories} kcal")

            print("Nutrients:")
            for nutrient in nutrients:
                nutrient_name = nutrient['name']
                nutrient_value = nutrient['value']
                nutrient_unit = nutrient['unit']
                print(f"{nutrient_name}: {nutrient_value} {nutrient_unit}")

        else:
            print("No information found for this PLU number.")
    except Exception as e:
        print("Error fetching data. Please check your API key or try again later.")
        print(e)

if __name__ == "__main__":
    api_key = "YOUR_NUTRITIONIX_API_KEY"

    # Assuming the user enters the PLU number
    plu_number = input("Enter the PLU number of the fruit or vegetable: ")
    display_plu_info(plu_number, api_key)

