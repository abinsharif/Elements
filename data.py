# Symbols of elements
symbols = [
    "H", "He",
    "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr",
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
    "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba",
    # Lanthanides
    "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
    "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra",
    # Actinides
    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
    "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

# Names of elements
names = [
    "Hydrogen", "Helium",
    "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
    "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton",
    "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium",
    "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon",
    "Cesium", "Barium",
    # Lanthanides
    "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium",
    "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon",
    "Francium", "Radium",
    # Actinides
    "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium",
    "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
]

# Group types (updated based on user's note: astatine to metalloid, oganesson to noble gas, halogen to nonmetal)
group_types = [
    "nonmetal", "noble gas",
    "alkali metal", "alkaline earth metal", "metalloid", "nonmetal", "nonmetal", "nonmetal", "nonmetal", "noble gas",
    "alkali metal", "alkaline earth metal", "post-transition metal", "metalloid", "nonmetal", "nonmetal", "nonmetal", "noble gas",
    "alkali metal", "alkaline earth metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal",
    "post-transition metal", "metalloid", "metalloid", "nonmetal", "nonmetal", "noble gas",
    "alkali metal", "alkaline earth metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal",
    "post-transition metal", "post-transition metal", "metalloid", "metalloid", "nonmetal", "noble gas",
    "alkali metal", "alkaline earth metal",
    # Lanthanides
    "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide", "lanthanide",
    "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal",
    "post-transition metal", "post-transition metal", "post-transition metal", "post-transition metal", "nonmetal", "noble gas",
    "alkali metal", "alkaline earth metal",
    # Actinides
    "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide", "actinide",
    "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "transition metal", "post-transition metal", "post-transition metal", "post-transition metal", "post-transition metal", "post-transition metal", "noble gas"
]

# Atomic numbers
atomic_numbers = list(range(1, 119))

# Atomic masses (standard atomic weights, approximate)
atomic_masses = [
    1.0080, 4.0026, 7.0, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.18,
    22.99, 24.305, 26.982, 28.085, 30.974, 32.07, 35.45, 39.9,
    39.098, 40.08, 44.956, 47.867, 50.942, 51.996, 54.938, 55.84, 58.933, 58.693, 63.55, 65.4,
    69.723, 72.63, 74.922, 78.97, 79.9, 83.8,
    85.468, 87.62, 88.906, 91.22, 92.906, 95.95, 96.906, 101.1, 102.91, 106.42, 107.868, 112.41,
    114.818, 118.71, 121.76, 127.6, 126.905, 131.29,
    132.91, 137.33,
    138.91, 140.12, 140.91, 144.24, 144.91, 150.4, 151.96, 157.25, 158.93, 162.5, 164.93, 167.26, 168.93, 173.05, 174.97,
    178.49, 180.95, 183.84, 186.21, 190.2, 192.22, 195.08, 196.97, 200.59,
    204.38, 207, 208.98, 208.98, 209.99, 222.02,
    223.02, 226.03,
    227.03, 232.04, 231.04, 238.03, 237.05, 244.06, 243.06, 247.07, 247.07, 251.08, 252.08, 257.1, 258.1, 259.1, 266.12,
    267.12, 268.13, 269.13, 270.13, 269.13, 277.15, 282.17, 282.17, 286.18, 286.18, 290.19, 290.2, 293.21, 294.21, 295.22
]

element_states = [
    "gas", "gas",
    "solid", "solid", "solid", "solid", "gas", "gas", "gas", "gas",
    "solid", "solid", "solid", "solid", "solid", "solid", "gas", "gas",
    "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid",
    "solid", "solid", "solid", "solid", "liquid", "gas",
    "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid",
    "solid", "solid", "solid", "solid", "gas", "gas",
    "solid", "solid",
    # Lanthanides
    "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid",
    "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "liquid",
    "solid", "solid", "solid", "solid", "solid", "gas",
    "solid", "solid",
    # Actinides
    "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid", "solid",
    "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown"
]


# One-word use of each element
element_uses = [
    "Fuel", "Balloons",  # H, He
    "Batteries", "Alloys", "Ceramics", "Steel", "Fertilizer", "Breathing", "Toothpaste", "Lighting",  # Li-Ne
    "Salt", "Flares", "Cans", "Chips", "Matches", "Gunpowder", "Disinfectant", "Inert",  # Na-Ar
    "Soap", "Bones", "Aerospace", "Implants", "Pigments", "Plating", "Electrodes", "Construction", "Glass", "Currency", "Wiring", "Galvanizing",  # K-Zn
    "LEDs", "Transistors", "Preservatives", "Photoconductors", "Antiseptic", "Windows",  # Ga-Kr
    "Clocks", "Fireworks", "Cladding", "Ceramics", "Superalloys", "Lubricants", "Isotope", "Electronics", "Jewelry", "Dentistry", "Photography", "Panels",  # Rb-Cd
    "Displays", "Soldering", "Flame-retardant", "Solar", "Medicine", "Anesthesia",  # In-Xe
    "Timekeeping", "Imaging",  # Cs, Ba
    
    # Lanthanides
    "Lighters", "Polishing", "Engines", "Speakers", "Luminous", "Reactors", "Phosphors", "Contrast", "Green", "Lasers", "Devices", "Fiber", "Sources", "Sensors", "Catalysis",  # La-Lu
    "Cutting", "Capacitors", "Filaments", "Coatings", "Contacts", "Plugs", "Refining", "Bullion", "Switches",  # Hf-Hg
    "Screens", "Radiation", "Cosmetics", "Antistatic", "Therapy", "Tracing",  # Tl-Rn
    "Experiments", "Treatment",  # Fr, Ra
    # Actinides
    "Radiotherapy", "Mantles", "Dating", "Weapons", "Detectors", "Power", "Alarms", "Missions", "Cyclotron", "Starters",  # Ac-Cf
    "Research", "Research", "Research", "Research", "Research",  # Es-Lr
    # Superheavies
    "Research", "Research", "Research", "Research", "Research", "Research", "Research", "Research", "Research", "Research", 
    "Research", "Research", "Research", "Research", "Research", "Research", "Research", "Research", "Research", "Research"
]

# Short descriptions of element uses (about 80 characters)
element_descriptions = [
    "Used as rocket fuel and in hydrogen cars and fusion",  # H
    "Used in balloons and as inert atmosphere for welding",  # He
    "Used in rechargeable batteries and mood stabilizers",  # Li
    "Used in aerospace alloys and nuclear reactors",  # Be
    "Used in ceramics, glass, and as neutron absorber",  # B
    "Essential for all life and used in steel production",  # C
    "Used in fertilizers and as liquid nitrogen coolant",  # N
    "Essential for breathing and used in steel production",  # O
    "Used in toothpaste and water fluoridation",  # F
    "Used in neon signs and as inert gas in lighting",  # Ne
    "Used in table salt and street lighting",  # Na
    "Used in flares, alloys, and as dietary supplement",  # Mg
    "Used in beverage cans, foil, and aircraft parts",  # Al
    "Used in computer chips, glass, and construction",  # Si
    "Used in fertilizers, matches, and DNA structure",  # P
    "Used in rubber vulcanization and gunpowder",  # S
    "Used in pool disinfection and PVC production",  # Cl
    "Used in welding and incandescent light bulbs",  # Ar
    "Used in fertilizers and soap production",  # K
    "Used in concrete production and car batteries",  # Ca
    "Used in aerospace alloys and baseball bats",  # Sc
    "Used in aircraft, medical implants, and paints",  # Ti
    "Used in steel alloys and as catalyst",  # V
    "Used in stainless steel and chrome plating",  # Cr
    "Used in steel production and battery electrodes",  # Mn
    "Used in construction, tools, and magnets",  # Fe
    "Used in magnets, catalysts, and blue glass",  # Co
    "Used in coins, batteries, and stainless steel",  # Ni
    "Used in electrical wiring and plumbing pipes",  # Cu
    "Used in galvanizing steel and brass alloys",  # Zn
    "Used in semiconductors and LEDs",  # Ga
    "Used in fiber optics and transistors",  # Ge
    "Used in wood preservatives and semiconductors",  # As
    "Used in photoconductors and glass coloring",  # Se
    "Used as antiseptic and in flame retardants",  # Br
    "Used in energy-efficient windows and lasers",  # Kr
    "Used in atomic clocks and medical tracers",  # Rb
    "Used in fireworks and flares for red color",  # Sr
    "Used in lasers and as cancer treatment",  # Y
    "Used in nuclear reactors and ceramics",  # Zr
    "Used in jet engines and MRI scanners",  # Nb
    "Used in steel alloys and high-temp lubricants",  # Mo
    "Used in medical imaging and as tracer",  # Tc
    "Used in electrical contacts and hard disks",  # Ru
    "Used in catalytic converters and jewelry",  # Rh
    "Used in catalytic converters and dentistry",  # Pd
    "Used in jewelry, mirrors, and photography",  # Ag
    "Used in batteries, pigments, and solar panels",  # Cd
    "Used in semiconductors and LCD screens",  # In
    "Used in solder, cans, and bronze alloys",  # Sn
    "Used in flame retardants and semiconductors",  # Sb
    "Used in solar panels and rubber vulcanization",  # Te
    "Used as antiseptic and in photography",  # I
    "Used in ion drives and medical anesthesia",  # Xe
    "Used in atomic clocks and oil drilling",  # Cs
    "Used in X-ray imaging and drilling fluids",  # Ba
    # Lanthanides
    "Used in lighter flints and camera lenses",  # La
    "Used in catalysts and glass polishing",  # Ce
    "Used in aircraft engines and magnets",  # Pr
    "Used in powerful permanent magnets",  # Nd
    "Used in nuclear batteries and research",  # Pm
    "Used in magnets and cancer treatment",  # Sm
    "Used in red phosphors for TV screens",  # Eu
    "Used in MRI contrast agents and neutron capture",  # Gd
    "Used in green phosphors and magnets",  # Tb
    "Used in lasers and hard disk drives",  # Dy
    "Used in magnets and medical devices",  # Ho
    "Used in fiber optic amplifiers and lasers",  # Er
    "Used in X-ray sources and portable equipment",  # Tm
    "Used in lasers and stress gauges",  # Yb
    "Used in catalysts and medical imaging",  # Lu
    "Used in tungsten carbide and nuclear reactors",  # Hf
    "Used in electronics and surgical instruments",  # Ta
    "Used in light bulb filaments and X-ray tubes",  # W
    "Used in catalysts and jet engine parts",  # Re
    "Used in fountain pen tips and electrical contacts",  # Os
    "Used in spark plugs and cancer treatment",  # Ir
    "Used in jewelry, catalysts, and electronics",  # Pt
    "Used in jewelry, electronics, and dentistry",  # Au
    "Used in thermometers, dental fillings, and switches",  # Hg
    "Used in electronics and medical imaging",  # Tl
    "Used in car batteries, bullets, and radiation shields",  # Pb
    "Used in medicine and cosmetics",  # Bi
    "Used in antistatic devices and neutron sources",  # Po
    "Used in medicine and scientific research",  # At
    "Used as tracer gas and in dating",  # Rn
    "Used in research and atomic clocks",  # Fr
    "Used in cancer treatment and luminous paints",  # Ra
    # Actinides
    "Used in cancer treatment and neutron sources",  # Ac
    "Used in gas mantles and nuclear fuel",  # Th
    "Used in nuclear research and dating",  # Pa
    "Used in nuclear fuel and weapons",  # U
    "Used in smoke detectors and research",  # Np
    "Used in nuclear weapons and power",  # Pu
    "Used in smoke detectors and neutron sources",  # Am
    "Used in research and space missions",  # Cm
    "Used in research and as electron source",  # Bk
    "Used in research and neutron sources",  # Cf
    "Used in research and medical applications",  # Es
    "Used in research only",  # Fm
    "Used in research only",  # Md
    "Used in research only",  # No
    "Used in research only",  # Lr
    "Used in research only",  # Rf
    "Used in research only",  # Db
    "Used in research only",  # Sg
    "Used in research only",  # Bh
    "Used in research only",  # Hs
    "Used in research only",  # Mt
    "Used in research only",  # Ds
    "Used in research only",  # Rg
    "Used in research only",  # Cn
    "Used in research only",  # Nh
    "Used in research only",  # Fl
    "Used in research only",  # Mc
    "Used in research only",  # Lv
    "Used in research only",  # Ts
    "Used in research only"   # Og
]

# Trivia/facts about each element (85-100 characters with superlatives and comparisons)
element_trivia = [
    "Hydrogen is the lightest element and makes up 73.9% of the universe's visible matter",  # H
    "Helium has the lowest boiling point at 4.22K and becomes superfluid with zero viscosity",  # He
    "Lithium is the lightest metal that can float on water while violently reacting with it",  # Li
    "Beryllium is 6 times stronger than steel but weighs only 25% as much, yet highly toxic",  # Be
    "Boron is the hardest element but essential for plants and harder than most metals when pure",  # B
    "Carbon is highest for 2 hundred million compounds, melting point of 3823K, and over 500 allotropes",  # C
    "Nitrogen makes up 78% of Earth's atmosphere but is completely inert at room temperature",  # N
    "Oxygen is Earth's most abundant element at 46% of crust mass and paramagnetic both gas and liquid",  # O
    "Fluorine is the most reactive element that can corrode glass and concrete on contact",  # F
    "Neon produces the most intense light discharge creating the classic orange-red glow",  # Ne
    "Sodium lamps are so efficient that one can outshine 100 incandescent bulbs combined",  # Na
    "Magnesium burns with 3000K white light so bright it can cause permanent eye damage",  # Mg
    "Aluminum was worth more than gold until 1890s before efficient electrolytic extraction",  # Al
    "Silicon makes up 27% of Earth's crust and enabled the entire computer age revolution",  # Si
    "Phosphorus colored white glows green in darkness but is essential for life despite being toxic",  # P
    "Sulfur is second for forming 30+ allotropes and creates yellow crystals in volcanic regions",  # S
    "Chlorine has the highest electron affinity (349 kJ/mol) and was WWI's first poison gas",  # Cl
    "Argon was Earth's first isolated noble gas and makes up nearly 1% of our atmosphere",  # Ar
    "Potassium is so violently reactive it ignites spontaneously and must be stored in oil",  # K
    "Calcium phosphate comprises 70% of bone mass giving vertebrates their rigid structure",  # Ca
    "Scandium is paradoxically rarer than many 'rare earth' elements despite being lighter",  # Sc
    "Titanium has the highest strength-to-weight ratio of all metals at 45% lighter than steel",  # Ti
    "Vanadium can exist in 5 different oxidation states creating rainbow-colored solutions",  # V
    "Chromium gives rubies red and emeralds green color while being the hardest pure metal",  # Cr
    "Manganese nodules carpet vast ocean floors containing trillions of tons of the element",  # Mn
    "Iron comprises 32.1% of Earth's total mass with most concentrated in the molten core",  # Fe
    "Cobalt blue glass has been prized for 4000 years and retains color at 1000°C heat",  # Co
    "Nickel-62 has the highest binding energy per nucleon at 8.8 MeV, making it the most stable isotope",  # Ni
    "Copper naturally kills bacteria and viruses within hours making it self-sterilizing",  # Cu
    "Zinc deficiency causes loss of taste/smell and affects 2 billion people worldwide",  # Zn
    "Gallium melts at 29.8°C in hand temperature but boils at 2400°C with the widest liquid range",  # Ga
    "Germanium was predicted by Mendeleev 15 years before discovery with exact properties",  # Ge
    "Arsenic has been humanity's poison of choice for over 2000 years earning 'King of Poisons'",  # As
    "Selenium deficiency causes fatal white muscle disease but it is toxic in excess amounts",  # Se
    "Bromine is the only liquid non-metal but it evaporates quickly from 1 mL to 3 liters of toxic gas",  # Br
    "Krypton was used in ultra-bright airport runway lighting systems and old camera flashes",  # Kr
    "Rubidium ignites spontaneously in air and was used in early vacuum tubes for electronics",  # Rb
    "Strontium-90 fallout creates the brilliant red in fireworks but is dangerously radioactive",  # Sr
    "Yttrium with barium carbon oxide or YBCO makes the highest temperature superconductors at 92K",  # Y
    "Zirconium is virtually immune to corrosion up to 1270K and used in nuclear reactors",  # Zr
    "Niobium is superconducting below 9K and was originally called columbium in America",  # Nb
    "Molybdenum has the 6th highest melting point at 2896K and strengthens steel dramatically",  # Mo
    "Technetium was the first artificially created element filling Mendeleev's predicted gap",  # Tc
    "Ruthenium is the scarcest platinum group metal ",  # Ru
    "Rhodium is the most expensive precious metal at about $250 per gram, rarer than gold",  # Rh
    "Palladium can absorb 900 times its volume in hydrogen like a metallic sponge",  # Pd
    "Silver has the highest electrical conductivity of all elements at room temperature",  # Ag
    "Cadmium red paint was banned after causing severe poisoning in artists for decades",  # Cd
    "Indium is softer than lead and can be scratched with a fingernail despite being metal",  # In
    "Tin produces a distinctive 'tin cry' scream when bent due to crystal twinning",  # Sn
    "Antimony makes Fluoroantimonic acid, the strongest, 10 quintillion times stronger than sulfuric acid",  # Sb
    "Tellurium-128 has the longest known half-life at 2.2 septillion years - nearly stable",  # Te
    "Iodine deficiency affects 2 billion people causing goiter and developmental disability",  # I
    "Xenon is the rarest gas with 90 grams per million kilograms of air",  # Xe
    "Caesium is the softest metal and its hydroxide is the strongest base ever discovered",  # Cs
    "Barium compounds create brilliant green fireworks but are lethally toxic if ingested",  # Ba
    # Lanthanides
    "Lanthanum remained undiscovered in 'pure' cerium samples for 83 years of confusion",  # La
    "Cerium is the most abundant rare earth comprising 0.006% of Earth's crust mass",  # Ce
    "Praseodymium means 'green twin' creating emerald-green compounds and yellow metal",  # Pr
    "Neodymium creates the strongest permanent magnets lifting 1000 times their own weight",  # Nd
    "Promethium is the only radioactive rare earth and powers space missions for decades",  # Pm
    "Samarium magnets work at 350°C and have the highest neutron absorption cross-section",  # Sm
    "Europium is the softest rare earth and the most reactive, tarnishing rapidly in air",  # Eu
    "Gadolinium has the highest magnetic moment, capturing thermal neutrons like a magnet",  # Gd
    "Terbium shows strong magnetostrictive strength, changing shape powerfully under magnetic fields",  # Tb
    "Dysprosium becomes strongly magnetic only below -180°C with highest magnetic strength",  # Dy
    "Holmium has the strongest magnetic field at 4.5 Tesla saturation, 90,000 times than Earth's field",  # Ho
    "Erbium amplifies light in fiber optic cables enabling global internet communications",  # Er
    "Thulium is the least abundant rare earth metal and possibly the most useless natural element",  # Tm
    "Ytterbium expands by 26% during its phase transition, a powerful structural change among metals",  # Yb
    "Lutetium is the hardest, densest rare earth and was the last lanthanide discovered",  # Lu
    "Hafnium has nearly identical properties to zirconium due to lanthanide contraction",  # Hf
    "Tantalum is virtually immune to all acids except hydrofluoric at high temperatures",  # Ta
    "Tungsten has the highest melting point at 3695K and tensile strength of all metals",  # W
    "Rhenium has the highest boiling point at 5869K and is the last stable element found",  # Re
    "Osmium is the densest element at 22.6 g/cubic centimeter - a cubic centimeter weighs as a golf ball",  # Os
    "Iridium is the most corrosion-resistant element and 2nd densest element at 22.42 g/cubic centimeter",  # Ir
    "Platinum is 30 times rarer than gold and catalyzes 20% of all chemical processes",  # Pt
    "Gold is so chemically inert it never tarnishes and has been treasured for 6000 years",  # Au
    "Mercury is the only metal liquid at room temperature and expands linearly with heat",  # Hg
    "Thallium is 10 times more toxic than lead and was once sold as rat poison",  # Tl
    "Lead's toxicity may have contributed to the fall of Rome through poisoned water pipes",  # Pb
    "Bismuth forms spectacular rainbow-colored oxide crystals and expands when solidifying",  # Bi
    "Polonium is 250 billion times more toxic than cyanide and the most radioactive natural element",  # Po
    "Astatine is Earth's rarest element with less than 1 gram existing at any time",  # At
    "Radon gas is the only radioactive gas that causes 21,000 lung cancer deaths annually in the US",  # Rn
    "Francium has most reactivity, largest atomic radii, shortest half-life of 22 min at $7 per nanogram",  # Fr
    "Radium was worth more than gold and glowed green due to intense radioactive decay",  # Ra
    # Actinides
    "Actinium glows blue-white in darkness and is 150 times more radioactive than radium",  # Ac
    "Thorium is 3 times more abundant than uranium and could power civilization for millennia",  # Th
    "Protactinium is one of the rarest elements, with only about 125 grams found in nature",  # Pa
    "Uranium-235's 1 gram releases energy equal to burning 3 tons of coal completely",  # U
    "Neptunium was the first transuranium element created and is named after planet Neptune",  # Np
    "Plutonium feels warm due to radioactive decay and is illegal for civilians to possess",  # Pu
    "Americium is the only man-made element available to the public in stores",  # Am
    "Curium glows purple-blue in darkness due to intense radioactivity and rapid decay",  # Cm
    "Berkelium was first synthesized at UC Berkeley using the 60-inch cyclotron in 1949",  # Bk
    "Californium costs $27 million per gram and is used to start nuclear reactors",  # Cf
    "Einsteinium was discovered in hydrogen bomb debris from the first H-bomb test in 1952",  # Es
    "Fermium was found in H-bomb fallout like einsteinium and named after physicist Enrico Fermi",  # Fm
    "Mendelevium was the first element created one atom at a time using particle accelerators",  # Md
    "Nobelium discovery was disputed for decades with Soviet, American, and Swedish claims",  # No
    "Lawrencium completes the actinide series and was synthesized at Berkeley in 1961",  # Lr
    "Rutherfordium was claimed by both Soviet and American teams causing naming disputes",  # Rf
    "Dubnium was named after Dubna, Russia where Soviet scientists first claimed discovery",  # Db
    "Seaborgium honors Glenn Seaborg, the only living person to have an element named for them",  # Sg
    "Bohrium was named after Niels Bohr who developed quantum mechanical model of atoms",  # Bh
    "Hassium was named after Hesse, Germany where GSI laboratory first synthesized it",  # Hs
    "Meitnerium honors Lise Meitner who theorised nuclear fission",  # Mt
    "Darmstadtium was named after Darmstadt, the latest city to receive elemental recognition",  # Ds
    "Roentgenium honors X-ray discoverer Wilhelm Röntgen though it doesn't emit X-rays",  # Rg
    "Copernicium was named after Copernicus who placed the Sun at the solar system's center",  # Cn
    "Nihonium was named after Japan (Nihon) where RIKEN laboratory first synthesized it in 2004",  # Nh
    "Flerovium honors Soviet physicist Flyorov who founded heavy element research in USSR",  # Fl
    "Moscovium was named after Moscow where Russian scientists contributed to superheavy research",  # Mc
    "Livermorium honors Lawrence Livermore Laboratory's contributions to superheavy elements",  # Lv
    "Tennessine was named after Tennessee, discovered most recently in 2010 at Oak Ridge",  # Ts
    "Oganesson is the heaviest and most radioactive element with the shortest 0.7ms half-life"   # Og
]

# Radioactivity status (True = radioactive, False = stable)
is_radioactive = [
    False, False,  # H, He
    False, False, False, False, False, False, False, False,  # Li-Ne
    False, False, False, False, False, False, False, False,  # Na-Ar
    False, False, False, False, False, False, False, False, False, False, False, False,  # K-Zn
    False, False, False, False, False, False,  # Ga-Kr
    False, False, False, False, False, False, True, False, False, False, False, False,  # Rb-Cd
    False, False, False, False, False, False,  # In-Xe
    False, False,  # Cs, Ba
    # Lanthanides
    False, False, False, False, True, False, False, False, False, False, False, False, False, False, False,  # La-Lu
    False, False, False, False, False, False, False, False, False,  # Hf-Hg
    False, False, False, True, True, True,  # Tl-Rn
    True, True,  # Fr, Ra
    # Actinides - all radioactive
    True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,  # Ac-Lr
    True, True, True, True, True, True, True, True, True, True, True, True, True, True, True  # Rf-Og
]

# SMOOTH COLOR DEFINITIONS (Hexadecimal format)
# Element group colors for card headers and nucleus
element_group_colors = {
    "nonmetal": "#90EE90",        # Light green
    "noble gas": "#8A2BE2",       # Blue violet  
    "alkali metal": "#FF6B6B",    # Coral red
    "alkaline earth metal": "#FFA500",  # Orange
    "metalloid": "#20B2AA",       # Light sea green
    "post-transition metal": "#D3D3D3",  # Light gray
    "transition metal": "#87CEEB", # Sky blue
    "lanthanide": "#FFD700",      # Gold
    "actinide": "#CD853F",        # Peru (brown)
}

# Orbital colors for each element group
orbital_colors = {
    "nonmetal": "#32CD32",        # Lime green
    "noble gas": "#9370DB",       # Medium purple
    "alkali metal": "#FF4500",    # Orange red
    "alkaline earth metal": "#FF8C00",  # Dark orange
    "metalloid": "#00CED1",       # Dark turquoise
    "post-transition metal": "#A9A9A9",  # Dark gray
    "transition metal": "#4169E1", # Royal blue
    "lanthanide": "#DAA520",      # Goldenrod
    "actinide": "#A0522D",        # Sienna
}

# Electron color (always white as requested)
electron_color = "#000000"  # Black

# Background and text colors
background_color = "#FFFFFF"  # White
text_color_dark = "#000000"   # Black
text_color_light = "#FFFFFF"  # White for dark backgrounds