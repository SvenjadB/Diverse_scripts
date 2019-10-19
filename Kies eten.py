from random import choice

soep = [
    "Groentensoep",
    "Maissoep",
    "Kippensoep",
    "Paprikasoep",
    "Minestrone",
]

opwarmbaar = [
    "Caribische rijst",
    "Ovenschotel met sperziebonen en aardappels",
    "Risoto",
    "Mexicaanse ovenschotel",
]

snel_v_1x = [
    "Spaghetti met spinazie en feta",
    "Broodje kip",
    "Mac & Cheese",
    "Hamburgers met brood",
    "Curry met rijst",
]

lang_recept = [
    "Hele kip uit de oven",
    "Gebraden lam",
    "Rundvlees met pruimen",
    "Pastei",
]


def maak_weekplan():
    """Kies recepten voor de hele week"""
    maandag = choice(soep)
    dinsdag = choice(opwarmbaar)
    woensdag = choice(snel_v_1x)
    donderdag = "Aardappels, vlees, groente"
    vrijdag = f"restjes van {dinsdag}."
    zaterdag = choice(snel_v_1x)
    while woensdag == zaterdag:
        zaterdag = choice(snel_v_1x)
    zondag = choice(lang_recept)
    weekplan = f"Maandag eten we {maandag}\n" \
               f"Dinsdag eten we {dinsdag}\n" \
               f"Woensdag eten we {woensdag}\n" \
               f"Donderdag eten we {donderdag}\n" \
               f"Vrijdag eten we {vrijdag}\n" \
               f"Zaterdag eten we {zaterdag}\n" \
               f"Zondag eten we {zondag}\n"
    print(weekplan)


maak_weekplan()
