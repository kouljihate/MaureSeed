import json
import random
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

COUNTRIES = ["morocco", "algeria", "tunisia", "mauritania", "mali"]

# Seed-specific photo URLs (Unsplash photo IDs)
SEED_PHOTOS = {
    "tomato": [
        "https://images.unsplash.com/photo-1546470427-0d4db154ceb8?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1592921870789-04563d55041c?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1558818498-28c1e002b655?w=400&h=300&fit=crop",
    ],
    "pepper": [
        "https://images.unsplash.com/photo-1583119022896-8a8b77c22f5e?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1583119022896-8a8b77c22f5e?w=400&h=300&fit=crop",
    ],
    "eggplant": [
        "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?w=400&h=300&fit=crop",
    ],
    "zucchini": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "cucumber": [
        "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?w=400&h=300&fit=crop",
    ],
    "pumpkin": [
        "https://images.unsplash.com/photo-1509622905150-fa66d3906e09?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1570586437263-ab629fccc818?w=400&h=300&fit=crop",
    ],
    "melon": [
        "https://images.unsplash.com/photo-1571575173700-afb9492e6a50?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1571575173700-afb9492e6a50?w=400&h=300&fit=crop",
    ],
    "watermelon": [
        "https://images.unsplash.com/photo-1563114773-84221bd62daa?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400&h=300&fit=crop",
    ],
    "okra": [
        "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=400&h=300&fit=crop",
    ],
    "carrot": [
        "https://images.unsplash.com/photo-1447175008436-054170c2e979?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=400&h=300&fit=crop",
    ],
    "turnip": [
        "https://images.unsplash.com/photo-1594057687713-5fd14eed1c15?w=400&h=300&fit=crop",
    ],
    "radish": [
        "https://images.unsplash.com/photo-1582284540020-8acbe03f4924?w=400&h=300&fit=crop",
    ],
    "beet": [
        "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?w=400&h=300&fit=crop",
    ],
    "onion": [
        "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?w=400&h=300&fit=crop",
    ],
    "garlic": [
        "https://images.unsplash.com/photo-1615477550926-01f5597a3e8b?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1540148426945-8cf22a8bcb19?w=400&h=300&fit=crop",
    ],
    "leek": [
        "https://images.unsplash.com/photo-1558818498-28c1e002b655?w=400&h=300&fit=crop",
    ],
    "celery": [
        "https://images.unsplash.com/photo-1515586838455-8f8f940d6853?w=400&h=300&fit=crop",
    ],
    "lettuce": [
        "https://images.unsplash.com/photo-1556801712-76c8eb07af38?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1515586838455-8f8f940d6853?w=400&h=300&fit=crop",
    ],
    "spinach": [
        "https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=400&h=300&fit=crop",
    ],
    "chard": [
        "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop",
    ],
    "cabbage": [
        "https://images.unsplash.com/photo-1594282486756-7e4b10782b75?w=400&h=300&fit=crop",
    ],
    "broccoli": [
        "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=400&h=300&fit=crop",
    ],
    "cauliflower": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "artichoke": [
        "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400&h=300&fit=crop",
    ],
    "pea": [
        "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "bean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?w=400&h=300&fit=crop",
    ],
    "corn": [
        "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400&h=300&fit=crop",
    ],
    "squash": [
        "https://images.unsplash.com/photo-1506484381205-f7945b68db56?w=400&h=300&fit=crop",
    ],
    "parsnip": [
        "https://images.unsplash.com/photo-1594057687713-5fd14eed1c15?w=400&h=300&fit=crop",
    ],
    "sweet potato": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "potato": [
        "https://images.unsplash.com/photo-1518977676601-b53f82ber40?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1590868309235-ea34bed7bd7f?w=400&h=300&fit=crop",
    ],
    "mint": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1515586838455-8f8f940d6853?w=400&h=300&fit=crop",
    ],
    "basil": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1515586838455-8f8f940d6853?w=400&h=300&fit=crop",
    ],
    "parsley": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "cilantro": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "dill": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "thyme": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "rosemary": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "oregano": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "sage": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "lavender": [
        "https://images.unsplash.com/photo-1468327768560-75b778cbb551?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1499002238440-d264edd596ec?w=400&h=300&fit=crop",
    ],
    "chamomile": [
        "https://images.unsplash.com/photo-1455659817273-f96807779a8a?w=400&h=300&fit=crop",
    ],
    "lemongrass": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "cumin": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "coriander": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "fenugreek": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    ],
    "anise": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "saffron": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "cardamom": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "turmeric": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "ginger": [
        "https://images.unsplash.com/photo-1596097635121-14b63b7a0c17?w=400&h=300&fit=crop",
    ],
    "rose": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1455659817273-f96807779a8a?w=400&h=300&fit=crop",
    ],
    "jasmine": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "sunflower": [
        "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400&h=300&fit=crop",
    ],
    "marigold": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "poppy": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "zinnia": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "dahlia": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "tulip": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "iris": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "lily": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "carnation": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "peony": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "chrysanthemum": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "cosmos": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "amaranth": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "hollyhock": [
        "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    ],
    "wheat": [
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1530507629858-e4977d30e9e0?w=400&h=300&fit=crop",
    ],
    "barley": [
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
    ],
    "oats": [
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
    ],
    "rice": [
        "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400&h=300&fit=crop",
    ],
    "millet": [
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
    ],
    "sorghum": [
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
    ],
    "rye": [
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
    ],
    "quinoa": [
        "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400&h=300&fit=crop",
    ],
    "buckwheat": [
        "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400&h=300&fit=crop",
    ],
    "lentil": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "chickpea": [
        "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?w=400&h=300&fit=crop",
    ],
    "fava bean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "black bean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "kidney bean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "mung bean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "peanut": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "soybean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "green bean": [
        "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    ],
    "olive": [
        "https://images.unsplash.com/photo-1528821128474-27f963b062bf?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1563281746-48b9dba2c6d2?w=400&h=300&fit=crop",
    ],
    "date palm": [
        "https://images.unsplash.com/photo-1563281746-48b9dba2c6d2?w=400&h=300&fit=crop",
    ],
    "fig": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "pomegranate": [
        "https://images.unsplash.com/photo-1541344999736-13b5c7f63d10?w=400&h=300&fit=crop",
    ],
    "orange": [
        "https://images.unsplash.com/photo-1547514701-42782101795e?w=400&h=300&fit=crop",
    ],
    "lemon": [
        "https://images.unsplash.com/photo-1590502593747-42a996133562?w=400&h=300&fit=crop",
    ],
    "mandarin": [
        "https://images.unsplash.com/photo-1547514701-42782101795e?w=400&h=300&fit=crop",
    ],
    "apricot": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "peach": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "almond": [
        "https://images.unsplash.com/photo-1508061253366-f7da158b6d44?w=400&h=300&fit=crop",
    ],
    "walnut": [
        "https://images.unsplash.com/photo-1508061253366-f7da158b6d44?w=400&h=300&fit=crop",
    ],
    "pistachio": [
        "https://images.unsplash.com/photo-1508061253366-f7da158b6d44?w=400&h=300&fit=crop",
    ],
    "carob": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "prickly pear": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "avocado": [
        "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=400&h=300&fit=crop",
    ],
    "mango": [
        "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400&h=300&fit=crop",
    ],
    "guava": [
        "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400&h=300&fit=crop",
    ],
    "papaya": [
        "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400&h=300&fit=crop",
    ],
    "banana": [
        "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=400&h=300&fit=crop",
    ],
    "coconut": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "mulberry": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
    "jujube": [
        "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
    ],
}

# Default fallback photos by category
DEFAULT_PHOTOS = {
    "vegetables": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop",
    "herbs": "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=400&h=300&fit=crop",
    "flowers": "https://images.unsplash.com/photo-1490750967868-88aa4f44baee?w=400&h=300&fit=crop",
    "cereals": "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=400&h=300&fit=crop",
    "legumes": "https://images.unsplash.com/photo-1563746098251-d35aef196e83?w=400&h=300&fit=crop",
    "fruitiers": "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=400&h=300&fit=crop",
}

CATEGORIES = {
    "vegetables": {
        "en": ["Tomato", "Pepper", "Eggplant", "Zucchini", "Cucumber", "Pumpkin", "Melon",
               "Watermelon", "Okra", "Carrot", "Turnip", "Radish", "Beet", "Onion",
               "Garlic", "Leek", "Celery", "Lettuce", "Spinach", "Chard", "Cabbage",
               "Broccoli", "Cauliflower", "Artichoke", "Pea", "Bean", "Corn", "Squash",
               "Parsnip", "Sweet Potato", "Potato", "Cassava", "Taro", "Arugula",
               "Endive", "Fennel", "Kohlrabi", "Rutabaga", "Shallot", "Scallion"],
        "ar": ["طماطم", "فليفلة", "باذنجان", "كوسا", "خيار", "قرع", "شمام",
               "بطيخ", "بامية", "جزر", "لفت", "فجل", "بنجر", "بصل",
               "ثوم", "كراث", "كرفس", "خس", "سبانخ", "سلق", "ملفوف",
               "بروكلي", "قرنبيط", "ارتيشوك", "بازلاء", "فاصوليا", "ذرة", "قرع",
               "بقدونس حلو", "بطاطا حلوة", "بطاطا", "مانية", "تارو", "جرجير",
               "هندية", "شمر", "قرنبيط أخضر", "لفت أحمر", "كراث أحمر", "بصل أخضر"]
    },
    "herbs": {
        "en": ["Mint", "Basil", "Parsley", "Cilantro", "Dill", "Thyme", "Rosemary",
               "Oregano", "Sage", "Lavender", "Chamomile", "Lemongrass", "Marjoram",
               "Tarragon", "Chives", "Cumin", "Coriander", "Fenugreek", "Anise",
               "Caraway", "Nigella", "Saffron", "Cardamom", "Turmeric", "Ginger",
               "Lemon Balm", "Borage", "Calendula", "Echinacea", "St. John's Wort"],
        "ar": ["نعناع", "ريحان", "بقدونس", "كزبرة", "شبت", "زعتر", "إكليل الجبل",
               "أورغانو", "سالمية", "لافندر", "بابونج", "ليمون عشب", "مردقوش",
               "تراغون", "بصل أخضر", "كمون", "كزبرة", "حلبة", "يانسون",
               "كراوية", "حبة البركة", "زعفران", "هيل", "كركم", "زنجبيل",
               "مليسا", "بوراجي", "قنديل الماء", "إكيناسيا", "نيولورت"]
    },
    "flowers": {
        "en": ["Rose", "Jasmine", "Sunflower", "Marigold", "Poppy", "Zinnia",
               "Dahlia", "Tulip", "Iris", "Lily", "Carnation", "Peony",
               "Chrysanthemum", "Cosmos", "Nasturtium", "Amaranth", "Lavender",
               "Hollyhock", "Morning Glory", "Sweet Pea", "Cornflower",
               "Honeysuckle", "Bougainvillea", "Daisy", "Anemone"],
        "ar": ["وردة", "ياسمين", "عباد الشمس", "كالي", "خشخاش", "زينيا",
               "دالية", "خزامى", "سوسن", "ليلى", "قرنفل", "بيونيا",
               "مومياء", "كوزموس", "نستورتيوم", "amaranth", "لافندر",
               "ختمية", "أزهار الصباح", "بازلاء عطرية", "أزهار الذرة",
               "دفلة", "بوغنوافيليا", "مخ陛", "أنيمون"]
    },
    "cereals": {
        "en": ["Wheat", "Barley", "Oats", "Rice", "Millet", "Sorghum", "Corn",
               "Rye", "Triticale", "Spelt", "Einkorn", "Emmer", "Quinoa",
               "Buckwheat", "Amaranth", "Teff", "Farro", "Kamut", "Freekeh"],
        "ar": ["قمح", "شعير", "شوفان", "أرز", "دوار", "ذرة رفيعة", "ذرة",
               "جاودار", "ترايتيكالي", "سبلت", "أينكورن", "إيمر", "كينوا",
               "قنارية", "amaranth", "تيف", "فارو", "كاموت", "فريكة"]
    },
    "legumes": {
        "en": ["Lentil", "Chickpea", "Fava Bean", "Black Bean", "Kidney Bean",
               "Mung Bean", "Pigeon Pea", "Cowpea", "Peanut", "Soybean",
               "White Bean", "Lima Bean", "Adzuki Bean", "Black-eyed Pea",
               "Green Bean", "Runner Bean", "Broad Bean", "Hyacinth Bean"],
        "ar": ["عدس", "حمص", "فول", "فاصوليا سوداء", "فاصوليا حمراء",
               "عدس أخضر", "حennessee", "لوبيا", "فول سوداني", "فول الصويا",
               "فاصوليا بيضاء", "فاصوليا ليما", "عدس أحمر", "لوبيا-eyed",
               "فاصوليا خضراء", "فاصوليا ركض", "فاصوليا عريضة", "فاصوليا هيلcon"]
    },
    "fruitiers": {
        "en": ["Olive", "Date Palm", "Fig", "Pomegranate", "Orange", "Lemon",
               "Mandarin", "Grapefruit", "Apricot", "Peach", "Almond", "Walnut",
               "Pistachio", "Carob", "Prickly Pear", "Avocado", "Mango",
               "Guava", "Papaya", "Banana", "Coconut", "Dragon Fruit",
               "Passion Fruit", "Mulberry", "Jujube"],
        "ar": ["زيتون", "نخلة التمر", "تين", "رمان", "برتقال", "ليمون",
               "مندرين", "جريب فروت", "مشمش", "خوخ", "لوز", "جوز",
               "فستق", "خروب", "هندية", "أفوكادو", "مانجو",
               "جوافة", "بابايا", "موز", "جوز الهند", "مانجو التنين",
               "فاكهة العاطفة", "توت", "نبق"]
    }
}

VARIETIES = [
    "Early", "Late", "Dwarf", "Giant", "Sweet", "Bitter", "Wild", "Domestic",
    "Heirloom", "Traditional", "Ancient", "Royal", "Golden", "Red", "White",
    "Black", "Green", "Purple", "Yellow", "Striped", "Round", "Long",
    "Flat", "Mini", "Giant", "Improved", "Resistant", "Hybrid", "Open-Pollinated",
    "Creole", "Local", "Mountain", "Desert", "Coastal", "Valley", "Highland",
    "Saharan", "Atlas", "Sahel", "Mediterranean", "Tropical", "Arid"
]

VARIETIES_AR = [
    "مبكر", "متأخر", "قزم", "ضخم", "حلو", "مر", "بري", "منزلي",
    "تراثي", "تقليدي", "قديم", "ملكي", "ذهبي", "أحمر", "أبيض",
    "أسود", "أخضر", "بنفسجي", "أصفر", "مخطط", "دائري", "طويل",
    "مسطح", "صغير", "ضخم", "مُحسّن", "مقاوم", "هجين", "مفتوح التلقيح",
    "كريبول", "محلي", "جبلي", "صحرائي", "ساحلي", "ودي", "مرتفع",
    "صحراوي", "أطلسي", "ساحل", "متوسطي", "استوائي", "جاف"
]

SUFFIXES_EN = ["II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
               "Special", "Premium", "Elite", "Classic", "Heritage", "Reserve"]

SUFFIXES_AR = ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "مميز", "بريميوم",
               "كلاسيكي", "تراثي", "محفوظ"]

DESCRIPTIONS_EN = [
    "A traditional variety passed down through generations, prized for its exceptional flavor and adaptability to local growing conditions.",
    "Well adapted to arid and semi-arid conditions, this drought-resistant variety thrives where others fail.",
    "Excellent flavor profile, ideal for traditional North African cuisine and Mediterranean cooking.",
    "High yielding variety suitable for both commercial farming and home gardens.",
    "Naturally drought resistant, perfect for dry regions with limited water resources.",
    "Organic and open-pollinated, ideal for seed saving and sustainable farming practices.",
    "Ancient heritage variety from the Maghreb region, preserved by generations of farmers.",
    "Versatile in the kitchen, excellent both fresh and cooked in a variety of dishes.",
    "Rich in essential nutrients and antioxidants, a healthy addition to any diet.",
    "Slow maturing with deep, complex flavor that develops fully in warm climates.",
    "Early maturing variety perfect for short growing seasons and quick harvests.",
    "Heat tolerant and sun-loving, thrives in Mediterranean and Saharan climates.",
    "Disease resistant with reliable production year after year.",
    "Compact growth habit, ideal for container gardening and small urban spaces.",
    "Vigorous grower with heavy yields, a favorite among experienced gardeners.",
]

DESCRIPTIONS_AR = [
    "نوع تقليدي يُنقل من جيل إلى آخر، يُقدّم بطعمه الاستثنائي ومظهره الم在当地.",
    "مكيف للظروف الجافة وشبه الجافة، هذا النوع المقاوم للجفاف يزدهر حيث يفشل الآخرون.",
    "ملمس ممتاز، مثالي للمطبخ التقليدي الشمالي أفريقي والمتوسطي.",
    "نوع عالي الإنتاج مناسب للزراعة التجارية والحدائق المنزلية.",
    "مقاوم للجفاف بشكل طبيعي، مثالي للمناطق الجافة ذات الموارد المائية المحدودة.",
    "عضوي ومفتوح التلقيح، مثالي لحفظ البذور والممارسات الزراعية المستدامة.",
    "نوع تراثي قديم من منطقة المغرب العربي، حافظ عليه أجيال من المزارعين.",
    "متعدد الاستخدامات في المطبخ، ممتاز طازجً ومطبوخاً في أطباق مختلفة.",
    "غني بالعناصر الغذائية الأساسية والمغذيات الدقيقة، إضافة صحية لأي نظام غذائي.",
    "ينضج ببطء بطعم عميق ومعقد يتطور بالكامل في المناخات الدافئة.",
    "نوع مبكر مثالي للمواسم القصيرة وال harvestات السريعة.",
    "يتحمل الحرارة ويحب الشمس، يزدهر في المناخات المتوسطية والصحرائية.",
    "مقاوم للأمراض مع إنتاج موثوق عاماً بعد عام.",
    "عادة نمو مدمجة، مثالية للحدائق الجامدة والمساحات الصغيرة.",
    "نبات نشط مع إنتاجات غزيرة، مفضل بين المزارعين ذوي الخبرة.",
]

USAGE_TIPS_EN = {
    "vegetables": [
        "Sow seeds 1-2 cm deep in well-prepared soil after last frost.",
        "Start indoors 6-8 weeks before last frost date.",
        "Direct sow after soil warms to 15°C (60°F).",
        "Provide support for climbing varieties.",
        "Harvest when fruits reach desired size and color.",
    ],
    "herbs": [
        "Sow on surface of moist soil, press lightly, do not cover.",
        "Harvest regularly to encourage bushy growth.",
        "Best harvested in morning after dew dries.",
        "Can be dried, frozen, or used fresh.",
        "Pinch flowers to extend leaf production.",
    ],
    "flowers": [
        "Sow after last frost, cover seeds lightly with soil.",
        "Thin seedlings to recommended spacing.",
        "Deadhead regularly to promote continuous blooming.",
        "Full sun to partial shade depending on variety.",
        "Water at base of plant to prevent fungal diseases.",
    ],
    "cereals": [
        "Sow in rows 15-30 cm apart, 2-3 cm deep.",
        "Requires consistent moisture during germination.",
        "Harvest when grains are hard and dry on the plant.",
        "Dry grains thoroughly before storage.",
        "Can be grown as cover crop to improve soil.",
    ],
    "legumes": [
        "Inoculate seeds with nitrogen-fixing bacteria for better yields.",
        "Sow directly in garden, do not transplant.",
        "Provide trellis for climbing varieties.",
        "Harvest pods when young and tender.",
        "Allow some pods to dry on plant for seed saving.",
    ],
    "fruitiers": [
        "Plant in well-drained soil with full sun exposure.",
        "Water deeply and regularly during first growing season.",
        "Prune annually to maintain shape and productivity.",
        "Mulch around base to retain moisture.",
        "Harvest when fruit is fully colored and slightly soft.",
    ],
}

USAGE_TIPS_AR = {
    "vegetables": [
        "ازرع البذور بعمق 1-2 سم في تربة مُعدّة جيداً بعد آخر صقيع.",
        "ابدأ بالداخل 6-8 أسابيع قبل تاريخ آخر صقيع.",
        "ازرع مباشرة بعد أن تدفئ التربة إلى 15 درجة مئوية.",
        "وفر الدعم للأصناف المتسلقة.",
        "احصد عندما تصل الفاكهة الحجم واللون المطلوب.",
    ],
    "herbs": [
        "ازرع على سطح التربة الرطبة، اضغط برفق، لا تغطِ.",
        "احصد بانتشو لتشجيع النمو الكثيف.",
        "الأفضل حصاده في الصباح بعد جفاف الندى.",
        "يمكن تجفيفه أو تجميده أو استخدامه طازجاً.",
        "قلم الأزهار لإطالة إنتاج الأوراق.",
    ],
    "flowers": [
        "ازرع بعد آخر صقيع، غطِ البذور بطبقة خفيفة من التربة.",
        "نحِّل الشتلات إلى المسافة الموصى بها.",
        "أزل الأزهار الذابلة بانتظام لتعزيز الإزهار المستمر.",
        "شمس كاملة إلى ظل جزئي حسب الصنف.",
        "اسقِ عند قاعدة النبات لمنع أمراض الفطريات.",
    ],
    "cereals": [
        "ازرع في صفوف بمسافة 15-30 سم، بعمق 2-3 سم.",
        "يحتاج رطوبة ثابتة أثناء الإنبات.",
        "احصد عندما تكون الحبوب صلبة وجافة على النبات.",
        "جفف الحبوب جيداً قبل التخزين.",
        "يمكن زراعتها كمحصول غطاء لتحسين التربة.",
    ],
    "legumes": [
        "نقِّع البذور ببكتيريا تثبيت النيتروجين لتحسين الإنتاج.",
        "ازرع مباشرة في الحديقة، لا تنقل.",
        "وفر تعليق للصنف المتسلق.",
        "احصد القرون عندما تكون شابة وطرية.",
        "اترك بعض القرون على النبات لتجف لحفظ البذور.",
    ],
    "fruitiers": [
        "ازرع في تربة جيدة الصرف مع تعريض لأشعة الشمس الكاملة.",
        "اسقِ بعمق وانتظام خلال موسم النمو الأول.",
        "قلّم سنوياً للحفاظ على الشكل والإنتاجية.",
        "افرش حول القاعدة للحفاظ على الرطوبة.",
        "احصد عندما يكون الثمر ملوناً بالكامل وطريلاً قليلاً.",
    ],
}

CONSERVATION_TIPS_EN = {
    "vegetables": [
        "Store seeds in airtight containers in cool, dry place.",
        "Label with variety name and harvest date.",
        "Dry seeds completely before storage (max 8% moisture).",
        "Store at 5-10°C for best longevity.",
        "Viability maintained for 2-5 years depending on species.",
    ],
    "herbs": [
        "Dry stems upside down in bundles in shaded, well-ventilated area.",
        "Store dried herbs in airtight glass jars away from light.",
        "Keep seeds in freezer for long-term storage.",
        "Harvest before flowering for strongest flavor.",
        "Replace dried herbs every 1-2 years for best potency.",
    ],
    "flowers": [
        "Allow seed heads to dry completely on plant before harvesting.",
        "Store in paper envelopes in cool, dry location.",
        "Separate seeds from chaff before storage.",
        "Some seeds require cold stratification before sowing.",
        "Maintain seed viability for 1-4 years with proper storage.",
    ],
    "cereals": [
        "Thresh and winnow grains to remove chaff.",
        "Dry to 12-14% moisture content before storage.",
        "Store in airtight containers with desiccant.",
        "Keep in cool, dark place to prevent insect infestation.",
        "Can be stored for 1-3 years under optimal conditions.",
    ],
    "legumes": [
        "Dry pods completely on plant before harvesting.",
        "Shell and sort seeds, removing damaged ones.",
        "Store in airtight containers with oxygen absorbers.",
        "Freeze for 48 hours to kill any insect eggs.",
        "Maintain viability for 3-5 years when stored properly.",
    ],
    "fruitiers": [
        "Extract seeds from ripe fruit and wash clean.",
        "Dry seeds in shade for 1-2 weeks.",
        "Store in refrigerator in moisture-proof containers.",
        "Some seeds require warm stratification before germination.",
        "Plant within 1-2 years for best germination rates.",
    ],
}

CONSERVATION_TIPS_AR = {
    "vegetables": [
        "خزن البذور في أوعية محكمة الإغلاق في مكان بارد وجاف.",
        "رقّم باسم الصنف وتاريخ الحصاد.",
        "جفف البذور تماماً قبل التخزين (الحد الأقصى 8% رطوبة).",
        "خزن عند 5-10 درجات مئوية لأفضل طول عممر.",
        "تبقى الجودة من 2-5 سنوات حسب النوع.",
    ],
    "herbs": [
        "جفف السيقان مقلوبة رأساً على عقب في حزم في مكان مظلل وجيد التهوية.",
        "خزن الأعشاب الجافة في أوعية زجاجية محكمة بعيداً عن الضوء.",
        "احتفظ بالبذور في المجمّع للتخزين طويل الأمد.",
        "احصد قبل الإزهار لأقوى نكهة.",
        "استبدل الأعشاب الجافة كل 1-2 سنوات لأفضل فعالية.",
    ],
    "flowers": [
        "اترك رؤوس الأزهار تجف تماماً على النبات قبل الحصاد.",
        "خزن في أظرف ورقية في مكان بارد وجاف.",
        "افصل البذور عن القشور قبل التخزين.",
        "بعض البذور تحتاج تبريد قبل الزراعة.",
        "حافظ على جودة البذور 1-4 سنوات مع التخزين الصحيح.",
    ],
    "cereals": [
        "دق الحبوب ونفضها لإزالة القشور.",
        "جفف حتى 12-14% محتوى رطوبة قبل التخزين.",
        "خزن في أوعية محكمة مع مادة مجففة.",
        "احتفظ في مكان بارد ومظلم لمنع الحشرات.",
        "يمكن تخزينها 1-3 سنوات في ظروف مثالية.",
    ],
    "legumes": [
        "جفف القرون تماماً على النبات قبل الحصاد.",
        "قشر وفرز البذور، وأزل التالفة.",
        "خزن في أوعية محكمة مع امتصاص الأكسجين.",
        "جمد لمدة 48 ساعة لقتل بيض الحشرات.",
        "حافظ على الجودة 3-5 سنوات مع التخزين الصحيح.",
    ],
    "fruitiers": [
        "استخرج البذور من الثمر الناضج واغسلها نظيفة.",
        "جفف البذور في الظل لمدة 1-2 أسابيع.",
        "خزن في الثلاجة في أوعية مقاومة للرطوبة.",
        "بعض البذور تحتاج تدفئة قبل الإنبات.",
        "ازرع خلال 1-2 سنوات لأفضل نسب إنبات.",
    ],
}


def get_seed_photo(seed_name, category):
    """Get appropriate photo URL for a seed based on its name."""
    name_lower = seed_name.lower()

    # Try exact match first
    if name_lower in SEED_PHOTOS:
        return random.choice(SEED_PHOTOS[name_lower])

    # Try partial match
    for key in SEED_PHOTOS:
        if key in name_lower or name_lower in key:
            return random.choice(SEED_PHOTOS[key])

    # Fallback to category default
    return DEFAULT_PHOTOS.get(category, DEFAULT_PHOTOS["vegetables"])


def generate_seed(index):
    category = random.choice(list(CATEGORIES.keys()))
    cat_data = CATEGORIES[category]
    country = random.choice(COUNTRIES)
    variety_idx = random.randint(0, len(VARIETIES) - 1)

    name_en_base = random.choice(cat_data["en"])
    name_ar_base = random.choice(cat_data["ar"])

    suffix_en = random.choice(SUFFIXES_EN) if random.random() > 0.6 else ""
    suffix_ar = random.choice(SUFFIXES_AR) if random.random() > 0.6 else ""

    name_en = f"{VARIETIES[variety_idx]} {name_en_base} {suffix_en}".strip()
    name_fr = f"{name_en_base} {VARIETIES[variety_idx]} {suffix_en}".strip()
    name_ar = f"{name_ar_base} {VARIETIES_AR[variety_idx]} {suffix_ar}".strip()

    desc_en = random.choice(DESCRIPTIONS_EN)
    desc_fr = desc_en
    desc_ar = random.choice(DESCRIPTIONS_AR)

    usage_en = random.choice(USAGE_TIPS_EN[category])
    usage_fr = usage_en
    usage_ar = random.choice(USAGE_TIPS_AR[category])

    conservation_en = random.choice(CONSERVATION_TIPS_EN[category])
    conservation_fr = conservation_en
    conservation_ar = random.choice(CONSERVATION_TIPS_AR[category])

    photo_url = get_seed_photo(name_en_base, category)

    featured = random.random() > 0.92

    # Price and stock
    price = round(random.uniform(1.5, 15.0), 2)
    stock = random.randint(0, 500)

    return {
        "id": f"seed-{index:05d}",
        "name_en": name_en,
        "name_fr": name_fr,
        "name_ar": name_ar,
        "country": country,
        "category": category,
        "description_en": desc_en,
        "description_fr": desc_fr,
        "description_ar": desc_ar,
        "usage_en": usage_en,
        "usage_fr": usage_fr,
        "usage_ar": usage_ar,
        "conservation_en": conservation_en,
        "conservation_fr": conservation_fr,
        "conservation_ar": conservation_ar,
        "photo": photo_url,
        "price": price,
        "stock": stock,
        "featured": featured,
    }


def main():
    seeds = []
    for i in range(1, 10001):
        seeds.append(generate_seed(i))

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seed_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(seeds, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(seeds)} seeds -> {out_path}")

    cats = {}
    countries = {}
    photos_by_cat = {}
    for s in seeds:
        cats[s["category"]] = cats.get(s["category"], 0) + 1
        countries[s["country"]] = countries.get(s["country"], 0) + 1
        if s["category"] not in photos_by_cat:
            photos_by_cat[s["category"]] = set()
        photos_by_cat[s["category"]].add(s["photo"])

    print("\nCategories:")
    for k, v in sorted(cats.items()):
        print(f"  {k}: {v}")

    print("\nCountries:")
    for k, v in sorted(countries.items()):
        print(f"  {k}: {v}")

    print("\nUnique photos per category:")
    for k, v in sorted(photos_by_cat.items()):
        print(f"  {k}: {len(v)} unique URLs")

    print(f"\nFields per seed: {list(seeds[0].keys())}")


if __name__ == "__main__":
    main()
