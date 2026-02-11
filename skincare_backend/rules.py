ESSENTIAL_CATEGORIES = {
    "cleanser": None, # Any cleanser can be used, no specific active ingredient requirement
    "sunscreen": None, # Any sunscreen can be used, no specific active ingredient requirement
    "moisturizer": None, # Any moisturizer can be used, no specific active ingredient requirement
} # Every skin type should have at least one product from each of these categories and must use every day.

ALIAS_MAP = {

    # --- AHA ---
    "aha": "aha",
    "glycolic_acid": "aha",
    "lactic_acid": "aha",
    "mandelic_acid": "aha",
    "citric_acid": "aha",
    "fruit_acids": "aha",

    # --- BHA grubu ---
    "bha": "bha",
    "salicylic_acid": "bha",
    "beta_hydroxy_acid": "bha",

    # --- Retinoidler ---
    "retinol": "retinol",
    "retinal": "retinol",
    "retinaldehyde": "retinol",
    "retinyl_palmitate": "retinol",

    # --- Vitamin C ---
    "vitamin_c": "vitamin_c",
    "ascorbic_acid": "vitamin_c",
    "l_ascorbic_acid": "vitamin_c",
    "ethyl_ascorbic_acid": "vitamin_c",
    "ascorbyl_glucoside": "vitamin_c",
    "magnesium_ascorbyl_phosphate": "vitamin_c",

    # --- Niacinamide ---
    "niacinamide": "niacinamide",
    "nicotinamide": "niacinamide",

    # --- Azelaic ---
    "azelaic_acid": "azelaic_acid",

    # --- Nemlendirici / bariyer ---
    "hyaluronic_acid": "hydrator",
    "sodium_hyaluronate": "hydrator",
    "glycerin": "hydrator",
    "ceramide": "hydrator",
    "ceramides": "hydrator",
    "panthenol": "hydrator",
    "beta_glucan": "hydrator",
} # Maps various ingredient names and synonyms to their standardized active ingredient categories for consistent rule application.


ACTIVE_INGREDIENTS = {

    "vitamin_c": {
        "time": "am",
        "conflicts": {"retinol", "aha", "bha"},
        "requires": {"sunscreen"},
        "min_age": 18,
        "notes": "Must be used with sunscreen.",
    },

    "retinol": {
        "time": "pm",
        "conflicts": {"vitamin_c", "aha", "bha"},
        "requires": set(),
        "min_age": 20,
        "notes": "Not recommended under 20.",
    },

    "aha": {
        "time": "pm",
        "conflicts": {"vitamin_c", "retinol", "bha"},
        "requires": set(),
        "min_age": 18,
    },

    "bha": {
        "time": "pm",
        "conflicts": {"vitamin_c", "retinol", "aha"},
        "requires": set(),
        "min_age": 18,
    },

    "niacinamide": {
        "time": "am_pm",
        "conflicts": set(),
        "requires": set(),
        "min_age": 0,
    },

    "azelaic_acid": {
        "time": "am_pm",
        "conflicts": set(),
        "requires": set(),
        "min_age": 0,
    }, 
} # System recommend active ingredients based on skin type and concerns. Each ingredient has specific rules regarding when to use, what it conflicts with, and any age restrictions.

CATEGORY_WEIGHTS = {
#essential categories, user must use every day
    "cleanser": 0,
    "sunscreen": 0,
    "moisturizer": 0,
#active categories
    "tonic": 0.5,
    "essence": 0.7,
    "serum": 1,
    "cream": 0.7,
# high-impact / occasional categories
    "mask": 1.5,
    "peel": 2.0
} # Each product category is assigned a weight that reflects its importance and impact on the overall skincare routine. Essential categories have a weight of 0, while high-impact categories have higher weights to emphasize their significance in the routine.

WEEKLY_BUDGET = {
    "retinol": 2,
    "aha": 2,
    "bha": 2.5,
    "vitamin_c": 7,
    "niacinamide": 10,
    "azelaic_acid": 4,
    "hydrator": 14,

} # Each active ingredient has a recommended maximum weekly usage to prevent overuse and potential skin irritation.
