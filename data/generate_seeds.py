import json
import random
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

COUNTRIES = ["morocco", "algeria", "tunisia", "mauritania", "mali"]

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
               "أورغانو", "سالمية", "لافندر", "بابونج", "лимон عشب", "مردقوش",
               "تراغون", "بصل أخضر", "كمون", "كزبرة", "حلبة", "يانسون",
               "كراوية", "حبة البركة", "زعفران", "هيل", "كركم", "زنجبيل",
               "مليسا", "بوراجي", "قنديل الماء", "إكيناسيا", "朝阳草"]
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
               "عدس أخضر", "بigeon", "لوبيا", "فول سوداني", "فول الصويا",
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
    "Flat", "Mini", "Giant", " Improved", "Resistant", "Hybrid", "Open-Pollinated",
    "Creole", "Local", "Mountain", "Desert", "Coastal", "Valley", "Highland",
    "Saharan", "Atlas", "Sahel", "Mediterranean", "Tropical", "Arid"
]

SUFFIXES_EN = ["II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
               "Special", "Premium", "Elite", "Classic", "Heritage", "Reserve"]

SUFFIXES_AR = ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "مميز", "بريميوم",
               "كلاسيكي", "تراثي", "محفوظ"]

DESCRIPTIONS_EN = [
    "A traditional variety passed down through generations",
    "Well adapted to arid and semi-arid conditions",
    "Excellent flavor, ideal for traditional cuisine",
    "High yielding variety for commercial farming",
    "Drought resistant, perfect for dry regions",
    "Organic and open-pollinated, suitable for seed saving",
    "Ancient heritage variety from the Maghreb",
    "Versatile use in cooking and fresh consumption",
    "Rich in nutrients and antioxidants",
    "Slow maturing, deep flavor profile",
    "Early maturing variety for short seasons",
    "Heat tolerant, thrives in Mediterranean climate",
    "Disease resistant, reliable producer",
    "Compact growth, ideal for small gardens",
    "Vigorous climber, heavy producer"
]

DESCRIPTIONS_AR = [
    "نوع تقليدي يُنقل من جيل إلى آخر",
    "مكيف للظروف الجافة وشبه الجافة",
    "طعم ممتاز، مثالي للمطبخ التقليدي",
    "نوع عالي الإنتاج للزراعة التجارية",
    "مقاوم للجفاف، مثالي للمناطق الجافة",
    "عضوي ومفتوح التلقيح، مناسب لحفظ البذور",
    "نوع تراثي قديم من المغرب العربي",
    "استخدام متعدد في الطبخ والاستهلاك الطازج",
    "غني بالعناصر الغذائية والمغذيات",
    "ينضج ببطء، طعم عميق",
    "نوع مبكر للمواسم القصيرة",
    "يتحمل الحرارة، يزدهر في المناخ المتوسطي",
    "مقاوم للأمراض، منتج موثوق",
    "نمو مدمج، مثالي للحدائق الصغيرة",
    "نبات نشط، منتج غزير"
]


def generate_seed(index):
    category = random.choice(list(CATEGORIES.keys()))
    cat_data = CATEGORIES[category]
    country = random.choice(COUNTRIES)
    variety = random.choice(VARIETIES)

    name_en_base = random.choice(cat_data["en"])
    name_ar_base = random.choice(cat_data["ar"])

    suffix_en = random.choice(SUFFIXES_EN) if random.random() > 0.6 else ""
    suffix_ar = random.choice(SUFFIXES_AR) if random.random() > 0.6 else ""

    name_en = f"{variety} {name_en_base} {suffix_en}".strip()
    name_fr = f"{name_en_base} {variety} {suffix_en}".strip()
    name_ar = f"{name_ar_base} {suffix_ar}".strip()

    desc_en = random.choice(DESCRIPTIONS_EN)
    desc_fr = desc_en
    desc_ar = random.choice(DESCRIPTIONS_AR)

    featured = random.random() > 0.92

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

    # category stats
    cats = {}
    countries = {}
    for s in seeds:
        cats[s["category"]] = cats.get(s["category"], 0) + 1
        countries[s["country"]] = countries.get(s["country"], 0) + 1

    print("\nCategories:")
    for k, v in sorted(cats.items()):
        print(f"  {k}: {v}")

    print("\nCountries:")
    for k, v in sorted(countries.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
