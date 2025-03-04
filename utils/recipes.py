food_classes = [
    'apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare', 'beet_salad', 'beignets', 
    'bibimbap', 'bread_pudding', 'breakfast_burrito', 'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad',
    'carrot_cake', 'ceviche', 'cheesecake', 'cheese_plate', 'chicken_curry', 'chicken_quesadilla', 
    'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder', 'club_sandwich', 
    'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 'deviled_eggs', 'donuts', 'dumplings', 'edamame', 
    'eggs_benedict', 'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras', 'french_fries', 
    'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice', 'frozen_yogurt', 'garlic_bread', 'gnocchi', 
    'greek_salad', 'grilled_cheese_sandwich', 'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 
    'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna', 'lobster_bisque', 'lobster_roll_sandwich', 
    'macaroni_and_cheese', 'macarons', 'miso_soup', 'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 'pad_thai', 
    'paella', 'pancakes', 'panna_cotta', 'peking_duck', 'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib', 
    'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto', 'samosa', 'sashimi', 'scallops', 
    'seaweed_salad', 'shrimp_and_grits', 'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 
    'strawberry_shortcake', 'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles'
]

recipe_descriptions = {
    "apple_pie": "Тесто, яблоки, сахар, корица. Выпекать 40 минут при 180°C.",
    "baby_back_ribs": "Ребрышки, маринад BBQ, запекать 3 часа при 150°C.",
    "baklava": "Тесто фило, орехи, мёд. Запекать 25 минут при 180°C.",
    "beef_carpaccio": "Тонко нарезанная говядина, оливковое масло, пармезан.",
    "beef_tartare": "Сырая говядина, каперсы, лук, горчица, яйцо.",
    "beet_salad": "Свекла, козий сыр, орехи, оливковое масло.",
    "beignets": "Французские пончики, обжаренные во фритюре.",
    "bibimbap": "Корейское блюдо: рис, овощи, яйцо, мясо.",
    "pizza": "Тесто, томатный соус, сыр, пепперони. Выпекать 15 минут при 220°C.",
    "sushi": "Рис, нори, рыба, васаби. Завернуть и нарезать.",
    "tiramisu": "Савоярди, маскарпоне, кофе, какао. Охладить 3 часа.",
    "hamburger": "Булочка, котлета, сыр, салат, соус. Собрать и поджарить.",
    "ramen": "Бульон, лапша, мясо, яйцо, зелёный лук. Варить 10 минут.",
    "pancakes": "Мука, яйца, молоко, сахар. Жарить на сковороде.",
    "omelette": "Яйца, молоко, соль, перец. Жарить на сковороде.",
    "lasagna": "Листы пасты, мясной соус, бешамель, сыр. Запекать 40 минут.",
    "macaroni_and_cheese": "Макароны, сырный соус, сливки. Готовить 10 минут.",
    "french_fries": "Картофель, масло, соль. Обжарить во фритюре.",
    "hot_dog": "Булочка, сосиска, кетчуп, горчица, лук.",
    "spaghetti_bolognese": "Спагетти, мясной соус с томатами, чеснок.",
    "spring_rolls": "Рисовая бумага, овощи, креветки. Подавать с соусом.",
    "tacos": "Тортилья, мясо, сыр, овощи, соус.",
    "waffles": "Мука, яйца, молоко, разрыхлитель. Выпекать в вафельнице.",
    "steak": "Говяжий стейк, соль, перец, масло. Жарить по 3-5 минут с каждой стороны.",
    "spaghetti_carbonara": "Спагетти, яйца, бекон, сыр пармезан, перец. Готовить 10 минут.",
    "shrimp_and_grits": "Креветки, кукурузная каша, сыр, масло. Жарить и подавать горячим.",
    "seaweed_salad": "Водоросли, кунжут, соевый соус, уксус. Перемешать и охладить.",
    "sashimi": "Свежая рыба, васаби, соевый соус. Подавать нарезанным.",
    "tuna_tartare": "Тунец, соевый соус, авокадо, лимон. Перемешать и подавать свежим."
}

def get_recipe(prediction):
    dish_name = food_classes[prediction]  # Получаем название блюда по индексу
    recipe = recipe_descriptions.get(dish_name, "Рецепт не найден")  # Ищем рецепт
    
    return dish_name.replace("_", " ").capitalize(), recipe  # Возвращаем название блюда и рецепт
