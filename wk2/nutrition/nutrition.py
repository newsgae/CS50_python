def main():
    # define usda dictionary
    # https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish

    fruits_dict = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
}

    fruit = input('Item: ').title().strip()
    if fruit in fruits_dict:
        print(f'Calories: {fruits_dict[fruit]}')


if __name__ == '__main__':
    main()