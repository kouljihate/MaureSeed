import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Reuse the data structures (photos, categories, varieties, etc.) from the
# existing generator so photos always match the seed name.
from data.generate_seeds import (
    CATEGORIES,
    COUNTRIES,
    VARIETIES,
    VARIETIES_AR,
    SUFFIXES_EN,
    SUFFIXES_AR,
    DESCRIPTIONS_EN,
    DESCRIPTIONS_AR,
    USAGE_TIPS_EN,
    USAGE_TIPS_AR,
    CONSERVATION_TIPS_EN,
    CONSERVATION_TIPS_AR,
    get_seed_photo,
)

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seed_data_test.json")

# ---------------------------------------------------------------------------
# Seed ID format: S-CCCXXYYZZWW
#   CCC : Country Code     (3 alpha, e.g. MAR)
#   XX  : Category          (2 digits, e.g. 01)
#   YY  : Type              (2 digits, e.g. 01)
#   ZZ  : Variety           (2 digits, e.g. 01)
#   WW  : Sequence          (2 digits, 01-99)
# ---------------------------------------------------------------------------

COUNTRY_IDS = {
    "morocco": "MAR",
    "algeria": "DZA",
    "tunisia": "TUN",
    "mauritania": "MRT",
    "mali": "MLI",
}

CATEGORY_IDS = {
    "vegetables": "01",
    "herbs": "02",
    "flowers": "03",
    "cereals": "04",
    "legumes": "05",
    "fruitiers": "06",
}

TYPE_IDS = {
    "tomato": "01", "pepper": "02", "eggplant": "03", "zucchini": "04",
    "cucumber": "05", "pumpkin": "06", "melon": "07", "watermelon": "08",
    "okra": "09", "carrot": "10", "turnip": "11", "radish": "12",
    "beet": "13", "onion": "14", "garlic": "15", "leek": "16",
    "celery": "17", "lettuce": "18", "spinach": "19", "chard": "20",
    "cabbage": "21", "broccoli": "22", "cauliflower": "23", "artichoke": "24",
    "pea": "25", "bean": "26", "corn": "27", "squash": "28",
    "parsnip": "29", "sweet potato": "30", "potato": "31", "cassava": "32",
    "taro": "33", "arugula": "34", "endive": "35", "fennel": "36",
    "kohlrabi": "37", "rutabaga": "38", "shallot": "39", "scallion": "40",
    # Herbs
    "mint": "01", "basil": "02", "parsley": "03", "cilantro": "04",
    "dill": "05", "thyme": "06", "rosemary": "07", "oregano": "08",
    "sage": "09", "lavender": "10", "chamomile": "11", "lemongrass": "12",
    "marjoram": "13", "tarragon": "14", "chives": "15", "cumin": "16",
    "coriander": "17", "fenugreek": "18", "anise": "19", "caraway": "20",
    "nigella": "21", "saffron": "22", "cardamom": "23", "turmeric": "24",
    "ginger": "25", "lemon balm": "26", "borage": "27", "calendula": "28",
    "echinacea": "29", "st. john's wort": "30",
    # Flowers
    "rose": "01", "jasmine": "02", "sunflower": "03", "marigold": "04",
    "poppy": "05", "zinnia": "06", "dahlia": "07", "tulip": "08",
    "iris": "09", "lily": "10", "carnation": "11", "peony": "12",
    "chrysanthemum": "13", "cosmos": "14", "nasturtium": "15", "amaranth": "16",
    "lavender": "17", "hollyhock": "18", "morning glory": "19", "sweet pea": "20",
    "cornflower": "21", "honeysuckle": "22", "bougainvillea": "23", "daisy": "24",
    "anemone": "25",
    # Cereals
    "wheat": "01", "barley": "02", "oats": "03", "rice": "04",
    "millet": "05", "sorghum": "06", "corn": "07", "rye": "08",
    "triticale": "09", "spelt": "10", "einkorn": "11", "emmer": "12",
    "quinoa": "13", "buckwheat": "14", "amaranth": "15", "teff": "16",
    "farro": "17", "kamut": "18", "freekeh": "19",
    # Legumes
    "lentil": "01", "chickpea": "02", "fava bean": "03", "black bean": "04",
    "kidney bean": "05", "mung bean": "06", "pigeon pea": "07", "cowpea": "08",
    "peanut": "09", "soybean": "10", "white bean": "11", "lima bean": "12",
    "adzuki bean": "13", "black-eyed pea": "14", "green bean": "15",
    "runner bean": "16", "broad bean": "17", "hyacinth bean": "18",
    # Fruitiers
    "olive": "01", "date palm": "02", "fig": "03", "pomegranate": "04",
    "orange": "05", "lemon": "06", "mandarin": "07", "grapefruit": "08",
    "apricot": "09", "peach": "10", "almond": "11", "walnut": "12",
    "pistachio": "13", "carob": "14", "prickly pear": "15", "avocado": "16",
    "mango": "17", "guava": "18", "papaya": "19", "banana": "20",
    "coconut": "21", "dragon fruit": "22", "passion fruit": "23",
    "mulberry": "24", "jujube": "25",
}

VARIETY_IDS = {
    "Early": "01", "Late": "02", "Dwarf": "03", "Giant": "04",
    "Sweet": "05", "Bitter": "06", "Wild": "07", "Domestic": "08",
    "Heirloom": "09", "Traditional": "10", "Ancient": "11", "Royal": "12",
    "Golden": "13", "Red": "14", "White": "15", "Black": "16",
    "Green": "17", "Purple": "18", "Yellow": "19", "Striped": "20",
    "Round": "21", "Long": "22", "Flat": "23", "Mini": "24",
    "Improved": "25", "Resistant": "26", "Hybrid": "27", "Open-Pollinated": "28",
    "Creole": "29", "Local": "30", "Mountain": "31", "Desert": "32",
    "Coastal": "33", "Valley": "34", "Highland": "35",
    "Saharan": "36", "Atlas": "37", "Sahel": "38", "Mediterranean": "39",
    "Tropical": "40", "Arid": "41",
}


def get_type_id(name_base):
    return TYPE_IDS.get(name_base.lower().strip(), "00")


def get_variety_id(variety_name):
    return VARIETY_IDS.get(variety_name, "00")


def generate_seed_id(country, category, name_base, variety_name, sequence):
    country_id = COUNTRY_IDS.get(country, "XXX")
    cat_id = CATEGORY_IDS.get(category, "00")
    type_id = get_type_id(name_base)
    var_id = get_variety_id(variety_name)
    seq = f"{sequence:02d}"
    return f"S-{country_id}{cat_id}{type_id}{var_id}{seq}"


# Track sequences per country/category/type/variety so each ID stays unique.
SEQUENCE_COUNTERS = {}


def generate_seed():
    category = random.choice(list(CATEGORIES.keys()))
    cat_data = CATEGORIES[category]
    country = random.choice(COUNTRIES)
    variety_idx = random.randint(0, len(VARIETIES) - 1)

    name_en_base = random.choice(cat_data["en"])
    name_ar_base = random.choice(cat_data["ar"])
    variety_name = VARIETIES[variety_idx]

    suffix_en = random.choice(SUFFIXES_EN) if random.random() > 0.6 else ""
    suffix_ar = random.choice(SUFFIXES_AR) if random.random() > 0.6 else ""

    name_en = f"{variety_name} {name_en_base} {suffix_en}".strip()
    name_fr = f"{name_en_base} {variety_name} {suffix_en}".strip()
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

    # Photo matched to the actual seed/plant name.
    photo_url = get_seed_photo(name_en_base, category)

    featured = random.random() > 0.92
    cost_price = round(random.uniform(1.0, 10.0), 2)
    sell_price = round(cost_price * random.uniform(1.5, 3.0), 2)
    stock = random.randint(0, 500)

    type_id = get_type_id(name_en_base)
    var_id = get_variety_id(variety_name)
    key = f"{country}_{category}_{type_id}_{var_id}"
    SEQUENCE_COUNTERS[key] = SEQUENCE_COUNTERS.get(key, 0) + 1
    sequence = SEQUENCE_COUNTERS[key]
    seed_id = generate_seed_id(country, category, name_en_base, variety_name, sequence)

    return {
        "id": seed_id,
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
        "cost_price": cost_price,
        "sell_price": sell_price,
        "currency": "MAD",
        "stock": stock,
        "featured": featured,
    }


def main():
    total = 20000
    seeds = [generate_seed() for _ in range(total)]

    ids = [s["id"] for s in seeds]
    unique_ids = len(set(ids))
    print(f"Generated {len(seeds)} seeds")
    print(f"Unique IDs: {unique_ids}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(seeds, f, ensure_ascii=False, indent=2)

    print(f"Written to: {OUTPUT_FILE}")

    cats = {}
    for s in seeds:
        cats[s["category"]] = cats.get(s["category"], 0) + 1

    print("\nCategories:")
    for k, v in sorted(cats.items()):
        print(f"  {k}: {v}")

    print("\nSample IDs:")
    for s in seeds[:5]:
        print(f"  {s['id']}  ->  {s['name_en']}")


if __name__ == "__main__":
    main()
