import math
from PIL import Image, ImageDraw
from data import symbols, group_types, element_group_colors, orbital_colors, atomic_masses

# Van der Waals radii (in picometers) for atomic size
VAN_DER_WAALS_RADII = {
    1: 120,   # H
    2: 140,   # He
    3: 182,   # Li
    4: 153,   # Be  (estimated)
    5: 192,   # B   (estimated)
    6: 170,   # C
    7: 155,   # N
    8: 152,   # O
    9: 147,   # F
    10: 154,  # Ne
    11: 227,  # Na
    12: 173,  # Mg
    13: 184,  # Al  (estimated)
    14: 210,  # Si
    15: 180,  # P
    16: 180,  # S
    17: 175,  # Cl
    18: 188,  # Ar
    19: 275,  # K
    20: 231,  # Ca  (estimated)
    21: 215,  # Sc  (estimated)
    22: 211,  # Ti  (estimated)
    23: 207,  # V   (estimated)
    24: 206,  # Cr  (estimated)
    25: 205,  # Mn  (estimated)
    26: 204,  # Fe  (estimated)
    27: 200,  # Co  (estimated)
    28: 197,  # Ni
    29: 196,  # Cu  (estimated)
    30: 201,  # Zn  (estimated)
    31: 187,  # Ga
    32: 211,  # Ge  (estimated)
    33: 185,  # As
    34: 190,  # Se
    35: 185,  # Br
    36: 202,  # Kr
    37: 303,  # Rb  (estimated)
    38: 249,  # Sr
    39: 232,  # Y   (estimated)
    40: 223,  # Zr  (estimated)
    41: 218,  # Nb  (estimated)
    42: 217,  # Mo  (estimated)
    43: 216,  # Tc  (estimated)
    44: 213,  # Ru  (estimated)
    45: 210,  # Rh  (estimated)
    46: 210,  # Pd  (estimated)
    47: 211,  # Ag  (estimated)
    48: 218,  # Cd  (estimated)
    49: 193,  # In
    50: 217,  # Sn
    51: 206,  # Sb  (estimated)
    52: 206,  # Te
    53: 198,  # I
    54: 216,  # Xe
    55: 343,  # Cs
    56: 268,  # Ba  (estimated)
    57: 243,  # La  (estimated)
    58: 242,  # Ce  (estimated)
    59: 240,  # Pr  (estimated)
    60: 239,  # Nd  (estimated)
    61: 238,  # Pm  (estimated)
    62: 236,  # Sm  (estimated)
    63: 235,  # Eu  (estimated)
    64: 234,  # Gd  (estimated)
    65: 233,  # Tb  (estimated)
    66: 231,  # Dy  (estimated)
    67: 230,  # Ho  (estimated)
    68: 229,  # Er  (estimated)
    69: 227,  # Tm  (estimated)
    70: 226,  # Yb  (estimated)
    71: 224,  # Lu  (estimated)
    72: 223,  # Hf  (estimated)
    73: 222,  # Ta  (estimated)
    74: 218,  # W   (estimated)
    75: 216,  # Re  (estimated)
    76: 216,  # Os  (estimated)
    77: 213,  # Ir  (estimated)
    78: 213,  # Pt  (estimated)
    79: 214,  # Au  (estimated)
    80: 223,  # Hg  (estimated)
    81: 196,  # Tl
    82: 202,  # Pb
    83: 207,  # Bi  (estimated)
    84: 197,  # Po  (estimated)
    85: 202,  # At  (estimated)
    86: 220,  # Rn  (estimated)
    87: 348,  # Fr  (estimated)
    88: 283,  # Ra  (estimated)
    89: 247,  # Ac  (estimated)
    90: 245,  # Th  (estimated)
    91: 243,  # Pa  (estimated)
    92: 241,  # U   (estimated)
    93: 239,  # Np  (estimated)
    94: 243,  # Pu  (estimated)
    95: 244,  # Am  (estimated)
    96: 245,  # Cm  (estimated)
    97: 244,  # Bk  (estimated)
    98: 245,  # Cf  (estimated)
    99: 245,  # Es  (estimated)
    100: 245, # Fm  (estimated)
    101: 246, # Md  (estimated)
    102: 246, # No  (estimated)
    103: 246, # Lr  (estimated)
    # Super heavy elements (theoretical estimates based on trends)
    104: 220, # Rf  (estimated)
    105: 210, # Db  (estimated)
    106: 200, # Sg  (estimated)
    107: 190, # Bh  (estimated)
    108: 180, # Hs  (estimated)
    109: 170, # Mt  (estimated)
    110: 160, # Ds  (estimated)
    111: 170, # Rg  (estimated)
    112: 180, # Cn  (estimated)
    113: 190, # Nh  (estimated)
    114: 200, # Fl  (estimated)
    115: 210, # Mc  (estimated)
    116: 220, # Lv  (estimated)
    117: 230, # Ts  (estimated)
    118: 240, # Og  (estimated)
}

# Accurate electron configurations by shell [K, L, M, N, O, P, Q]
ELECTRON_SHELLS_DATA = {
    1: [1], 2: [2], 3: [2, 1], 4: [2, 2], 5: [2, 3], 6: [2, 4], 7: [2, 5], 8: [2, 6], 9: [2, 7], 10: [2, 8],
    11: [2, 8, 1], 12: [2, 8, 2], 13: [2, 8, 3], 14: [2, 8, 4], 15: [2, 8, 5], 16: [2, 8, 6], 17: [2, 8, 7], 18: [2, 8, 8],
    19: [2, 8, 8, 1], 20: [2, 8, 8, 2], 21: [2, 8, 9, 2], 22: [2, 8, 10, 2], 23: [2, 8, 11, 2], 24: [2, 8, 13, 1], 25: [2, 8, 13, 2], 
    26: [2, 8, 14, 2], 27: [2, 8, 15, 2], 28: [2, 8, 16, 2], 29: [2, 8, 18, 1], 30: [2, 8, 18, 2],
    31: [2, 8, 18, 3], 32: [2, 8, 18, 4], 33: [2, 8, 18, 5], 34: [2, 8, 18, 6], 35: [2, 8, 18, 7], 36: [2, 8, 18, 8],
    37: [2, 8, 18, 8, 1], 38: [2, 8, 18, 8, 2], 39: [2, 8, 18, 9, 2], 40: [2, 8, 18, 10, 2], 41: [2, 8, 18, 12, 1], 
    42: [2, 8, 18, 13, 1], 43: [2, 8, 18, 13, 2], 44: [2, 8, 18, 15, 1], 45: [2, 8, 18, 16, 1], 46: [2, 8, 18, 18], 
    47: [2, 8, 18, 18, 1], 48: [2, 8, 18, 18, 2], 49: [2, 8, 18, 18, 3], 50: [2, 8, 18, 18, 4], 51: [2, 8, 18, 18, 5], 
    52: [2, 8, 18, 18, 6], 53: [2, 8, 18, 18, 7], 54: [2, 8, 18, 18, 8],
    55: [2, 8, 18, 18, 8, 1], 56: [2, 8, 18, 18, 8, 2],
    # Lanthanides (4f orbital filling)
    57: [2, 8, 18, 18, 9, 2], 58: [2, 8, 18, 19, 9, 2], 59: [2, 8, 18, 21, 8, 2], 60: [2, 8, 18, 22, 8, 2], 61: [2, 8, 18, 23, 8, 2], 
    62: [2, 8, 18, 24, 8, 2], 63: [2, 8, 18, 25, 8, 2], 64: [2, 8, 18, 25, 9, 2], 65: [2, 8, 18, 27, 8, 2], 66: [2, 8, 18, 28, 8, 2], 
    67: [2, 8, 18, 29, 8, 2], 68: [2, 8, 18, 30, 8, 2], 69: [2, 8, 18, 31, 8, 2], 70: [2, 8, 18, 32, 8, 2], 71: [2, 8, 18, 32, 9, 2],
    72: [2, 8, 18, 32, 10, 2], 73: [2, 8, 18, 32, 11, 2], 74: [2, 8, 18, 32, 12, 2], 75: [2, 8, 18, 32, 13, 2], 76: [2, 8, 18, 32, 14, 2], 
    77: [2, 8, 18, 32, 15, 2], 78: [2, 8, 18, 32, 17, 1], 79: [2, 8, 18, 32, 18, 1], 80: [2, 8, 18, 32, 18, 2],
    81: [2, 8, 18, 32, 18, 3], 82: [2, 8, 18, 32, 18, 4], 83: [2, 8, 18, 32, 18, 5], 84: [2, 8, 18, 32, 18, 6], 85: [2, 8, 18, 32, 18, 7], 86: [2, 8, 18, 32, 18, 8],
    87: [2, 8, 18, 32, 18, 8, 1], 88: [2, 8, 18, 32, 18, 8, 2],
    # Actinides (5f orbital filling) - simplified configurations
    89: [2, 8, 18, 32, 18, 9, 2], 90: [2, 8, 18, 32, 18, 10, 2], 91: [2, 8, 18, 32, 20, 9, 2], 92: [2, 8, 18, 32, 21, 9, 2], 93: [2, 8, 18, 32, 22, 9, 2], 
    94: [2, 8, 18, 32, 24, 8, 2], 95: [2, 8, 18, 32, 25, 8, 2], 96: [2, 8, 18, 32, 25, 9, 2], 97: [2, 8, 18, 32, 27, 8, 2], 98: [2, 8, 18, 32, 28, 8, 2], 
    99: [2, 8, 18, 32, 29, 8, 2], 100: [2, 8, 18, 32, 30, 8, 2], 101: [2, 8, 18, 32, 31, 8, 2], 102: [2, 8, 18, 32, 32, 8, 2], 103: [2, 8, 18, 32, 32, 9, 2],
    # Super heavy elements (predicted configurations)
    104: [2, 8, 18, 32, 32, 10, 2], 105: [2, 8, 18, 32, 32, 11, 2], 106: [2, 8, 18, 32, 32, 12, 2], 107: [2, 8, 18, 32, 32, 13, 2], 
    108: [2, 8, 18, 32, 32, 14, 2], 109: [2, 8, 18, 32, 32, 15, 2], 110: [2, 8, 18, 32, 32, 16, 2], 111: [2, 8, 18, 32, 32, 17, 2], 
    112: [2, 8, 18, 32, 32, 18, 2], 113: [2, 8, 18, 32, 32, 18, 3], 114: [2, 8, 18, 32, 32, 18, 4], 115: [2, 8, 18, 32, 32, 18, 5], 
    116: [2, 8, 18, 32, 32, 18, 6], 117: [2, 8, 18, 32, 32, 18, 7], 118: [2, 8, 18, 32, 32, 18, 8]
}

def get_van_der_waals_radius(atomic_num):
    """Get van der Waals radius for element"""
    return VAN_DER_WAALS_RADII.get(atomic_num, 200)  # Default fallback

def get_nucleus_radius_from_mass(atomic_num):
    """Calculate nucleus radius based on atomic mass (proportional to mass)"""
    if atomic_num < 1 or atomic_num > len(atomic_masses):
        return 8  # Default

    mass = atomic_masses[atomic_num - 1]
    # Nuclear radius proportional to cube root of mass number (realistic nuclear physics)
    base_radius = 6 + (mass ** (1/3)) * 1.8
    return max(4, min(int(base_radius), 25))  # Clamp between 4-25 pixels

def get_electron_shells(atomic_num):
    """Get accurate electron configuration by shells"""
    if atomic_num in ELECTRON_SHELLS_DATA:
        return ELECTRON_SHELLS_DATA[atomic_num]
    else:
        # Fallback for any missing elements
        shells = []
        remaining = atomic_num
        shell_capacity = [2, 8, 18, 32, 32, 18, 8]

        for capacity in shell_capacity:
            if remaining <= 0:
                break
            electrons_in_shell = min(remaining, capacity)
            shells.append(electrons_in_shell)
            remaining -= electrons_in_shell

        return shells

def calculate_orbit_spacing(atomic_num, nucleus_radius, num_shells):
    """Calculate spacing between electron orbits based on atomic size"""

    # Use van der Waals radius to determine overall atomic size
    vdw_radius = get_van_der_waals_radius(atomic_num)

    # Calculate spacing to fit within atomic boundary
    if num_shells <= 1:
        return 20

    # Available space for electron orbits
    available_space = (vdw_radius / 30) * 0.6  # Scale down for image
    orbit_space_per_shell = available_space / num_shells

    return max(12, min(int(orbit_space_per_shell), 25))

def generate_atom_image(atomic_num, scale_factor=1.0, image_size=1200):
    """
    Generate HIGH RESOLUTION atomic structure image with black electrons and nucleus size based on mass

    Args:
        atomic_num: Atomic number of element
        scale_factor: Overall scaling factor
        image_size: Size of output image (square) - INCREASED for better quality

    Returns:
        PIL Image object
    """
    if atomic_num < 1 or atomic_num > len(symbols):
        raise ValueError("Invalid atomic number")

    # Get element properties
    group_type = group_types[atomic_num - 1]
    nucleus_color = element_group_colors.get(group_type, "#FFFFFF")
    orbit_color = orbital_colors.get(group_type, "#808080")

    # Create image with transparent background - HIGHER RESOLUTION
    img = Image.new('RGBA', (image_size, image_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    center_x = center_y = image_size // 2

    # NUCLEUS SIZE based on atomic mass
    nucleus_radius = get_nucleus_radius_from_mass(atomic_num)
    nucleus_radius = int(nucleus_radius * scale_factor * (image_size / 400))  # Scale with image size

    # Get electron configuration
    electron_shells = get_electron_shells(atomic_num)

    # Calculate orbit spacing based on atomic size
    shell_spacing = calculate_orbit_spacing(atomic_num, nucleus_radius, len(electron_shells))
    shell_spacing = int(shell_spacing * scale_factor * (image_size / 400))  # Scale with image size

    # Ensure the entire atom fits within the image
    max_distance = nucleus_radius + (len(electron_shells) * shell_spacing) + 20
    if max_distance * 2 > image_size * 0.8:  # Leave 20% margin
        scaling_factor = (image_size * 0.4) / max_distance
        nucleus_radius = max(int(6 * image_size / 400), int(nucleus_radius * scaling_factor))
        shell_spacing = max(int(8 * image_size / 400), int(shell_spacing * scaling_factor))

    # Draw electron orbits with colored rings
    shell_distances = []
    orbit_width = 4  # Scale line width

    for i, electrons in enumerate(electron_shells):
        if electrons > 0:
            distance = nucleus_radius + int(15 * image_size / 400) + (i * shell_spacing)
            shell_distances.append(distance)

            # Draw colored orbital path
            draw.ellipse([center_x - distance, center_y - distance,
                         center_x + distance, center_y + distance],
                        outline=orbit_color, width=orbit_width)

    # Draw BLACK electrons with FIXED size relative to image
    electron_radius = 10  # Scale electron size with image

    for shell_idx, (electrons, distance) in enumerate(zip(electron_shells, shell_distances)):
        if electrons <= 0:
            continue

        angle_step = 2 * math.pi / electrons

        # Add slight offset for each shell for visual appeal
        shell_offset = shell_idx * 0.1

        for electron_idx in range(electrons):
            angle = (electron_idx * angle_step) + shell_offset

            # Add very slight randomness for more natural look (but keep stable)
            angle += math.sin(electron_idx * 2 + shell_idx) * 0.02

            electron_x = center_x + distance * math.cos(angle)
            electron_y = center_y + distance * math.sin(angle)

            # Draw electron as BLACK circle
            draw.ellipse([electron_x - electron_radius, electron_y - electron_radius,
                         electron_x + electron_radius, electron_y + electron_radius],
                        fill="#000000")  # BLACK electrons

    # Draw nucleus with element group color (NO outline)
    draw.ellipse([center_x - nucleus_radius, center_y - nucleus_radius,
                 center_x + nucleus_radius, center_y + nucleus_radius],
                fill=nucleus_color)

    return img

def save_atom_image(atomic_num, scale_factor=1.0, filename=None, image_size=800):
    """Save HIGH RESOLUTION atomic image to file"""
    if filename is None:
        symbol = symbols[atomic_num - 1]
        filename = f"atom_{atomic_num}_{symbol}.png"

    img = generate_atom_image(atomic_num, scale_factor, image_size)
    img.save(filename)
    return filename

def generate_all_atom_images(max_atomic_num=118, base_scale=1.0):
    """Generate HIGH RESOLUTION images for all elements"""

    for atomic_num in range(1, min(max_atomic_num + 1, len(symbols) + 1)):
        try:
            # Generate high resolution images
            filename = save_atom_image(atomic_num, base_scale, image_size=800)
        except Exception as e:
            print(f"Error generating image for atomic number {atomic_num}: {e}")

if __name__ == "__main__":
    print("🔬 Generating HIGH RESOLUTION atomic images...")
    print("✅ Features: BLACK electrons, nucleus size from mass, better quality")

    # Test a few representative elements
    test_elements = [1, 2, 6, 11, 18, 36]
    for atomic_num in test_elements:
        try:
            mass = atomic_masses[atomic_num - 1]
            nucleus_r = get_nucleus_radius_from_mass(atomic_num)
            vdw_radius = get_van_der_waals_radius(atomic_num)
            filename = save_atom_image(atomic_num, scale_factor=1.0, image_size=800)
            print(f"✅ Generated atom {atomic_num} ({symbols[atomic_num-1]}): mass={mass:.3f}u, nucleus={nucleus_r}px, vdW={vdw_radius}pm -> {filename}")
        except Exception as e:
            print(f"❌ Error with atom {atomic_num}: {e}")

    print("🎉 HIGH RESOLUTION generation completed!")
