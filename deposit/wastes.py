# Helper module for waste type information (for all)
# To import, use "from deposit.wastes import *"

WASTES_DICT = {
    "PLASTIK"   : {'name': "Plastik", 'points': 50},
    "KACA"      : {'name': "Kaca / Beling", 'points': 70},
    "KERTAS"    : {'name': "Kertas / Kardus", 'points': 30},
    "ETC"       : {'name': "Organik & Lainnya", 'points': 15}
}

def get_waste_name(key):
    return WASTES_DICT[key]['name']

def get_waste_points(key):
    return WASTES_DICT[key]['points']