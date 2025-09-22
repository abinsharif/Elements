# Element Cards with Atomic Images - Usage Guide

## Required Dependencies

Install the following Python packages:

```bash
pip install reportlab pillow watchdog
```

## File Structure

- `main.py` - Main program to generate element cards with atomic images
- `atom_generator.py` - Generates atomic structure images based on atomic number
- `data.py` - Contains all element data (symbols, names, properties, uses, trivia, etc.)

## How to Use

### 1. Generate All Element Cards

```bash
python main.py
```

This will:
- Generate atomic images for all elements (saved in `atomic_images/` folder)
- Create `element_cards_with_atoms_4x5.pdf` with all elements
- Each card includes: name, symbol, atomic number, mass, use, description, trivia, and atomic structure image


### 4. Generate Individual Atomic Images

```python
from atom_generator import save_atom_image

# Generate hydrogen atom image
save_atom_image(1, scale_factor=1.2)

# Generate carbon atom image with custom scale
save_atom_image(6, scale_factor=1.0, filename="carbon_atom.png")
```

## Customization

### Card Layout (main.py)
- `header_font_size` - Size of element name in header
- `symbol_font_size` - Size of element symbol
- `atomic_image_width/height` - Size of atomic structure image
- `GROUP_COLORS` - Colors for each element type

### Atomic Images (atom_generator.py)
- `ATOMIC_SCALE_FACTORS` - Different magnification for each element type
- `GROUP_COLORS` - Nucleus colors matching card colors
- `image_size` - Size of generated atomic images

### Test Card (card_tester.py)
- `TEST_ATOMIC_NUMBER` - Which element to test (1-118)
- Card design mirrors main.py settings

## Features

✅ **Comprehensive Element Data**: Uses, descriptions, trivia, radioactivity status
✅ **Atomic Structure Visualization**: Electrons, nucleus, orbital shells
✅ **Color-Coded by Element Type**: Matching nucleus and header colors  
✅ **Radioactive Indicators**: ☢ symbol for radioactive elements
✅ **Auto-scaling**: Different magnifications for different element types
✅ **Interactive Testing**: Live reload when testing individual cards
✅ **Professional Layout**: Clean, readable card design

## Example Output

Each card contains:
- **Header**: Element name on colored background
- **Atomic number** (top-left)
- **Radioactive symbol** ☢ (if applicable)  
- **Element symbol** (large, centered)
- **Atomic mass** (bottom-left)
- **Element use** (bottom-right)
- **Atomic structure image** (center)
- **Description** (wrapped text)
- **Trivia/facts** (wrapped text, italics)

The atomic images show:
- Nucleus colored by element type
- Electron shells at proper distances
- Small blue electrons orbiting the nucleus
- Scaled according to atomic radius and element type
