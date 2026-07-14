"""
OptiCrop Utilities Module
Provides agricultural insights, crop recommendations advice, and PDF reporting formatting.
"""

def get_agricultural_tips(crop_label):
    """
    Returns high-fidelity agricultural advice and tips for the selected crop.
    """
    tips = {
        "rice": {
            "watering": "Requires standing water; keep depth of 5-10 cm during vegetative phase.",
            "fertilization": "Apply urea split doses at active tillering and panicle initiation phases.",
            "disease_mgmt": "Monitor for Rice Blast; use copper fungicides or resistant cultivars.",
            "harvesting": "Harvest when 80-85% of the grains turn straw-coloured."
        },
        "maize": {
            "watering": "Highly sensitive to water stress during silking and tasseling phases.",
            "fertilization": "Heavy Nitrogen feeder. Ensure split applications at knee-high and tasseling stages.",
            "disease_mgmt": "Watch out for Stem Borers; apply organic Neem seed kernel extract.",
            "harvesting": "Harvest when moisture level drops to 15-20% and black layer is visible."
        },
        "chickpea": {
            "watering": "Requires low water; avoid waterlogged soils as it causes wilt disease.",
            "fertilization": "Nitrogen fixer. Focus on Rhizobium inoculation rather than high urea.",
            "disease_mgmt": "Prevent Fusarium Wilt; treat seeds with Trichoderma viride.",
            "harvesting": "Harvest when leaves turn yellow and pods mature to a light brown."
        },
        "banana": {
            "watering": "High moisture requirement; maintain deep, frequent watering but ensure good drainage.",
            "fertilization": "Extremely high Potassium demand. Apply wood ash or muriate of potash monthly.",
            "disease_mgmt": "Look out for Panama Wilt; maintain optimal pH and destroy infected pseudo-stems.",
            "harvesting": "Harvest bunches when angles on fruits turn rounded and skin becomes light green."
        }
    }

    # Fallback/Default tips
    default_tips = {
        "watering": "Maintain optimum moisture levels, ensuring soil doesn't suffer extreme saturation or drying.",
        "fertilization": "Perform routine soil tests to determine exact N-P-K deficiency before top dressing.",
        "disease_mgmt": "Adopt integrated pest management (IPM) practices, crop rotation, and clean cultivation.",
        "harvesting": "Harvest during cool morning hours to maintain maximum crop turgidity and shelf-life."
    }

    return tips.get(crop_label.lower(), default_tips)
