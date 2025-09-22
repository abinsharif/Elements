from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors as reportlab_colors
import math
import os
from data import (symbols, names, atomic_numbers, atomic_masses, group_types, 
                 element_uses, element_descriptions, element_trivia, is_radioactive,
                 element_group_colors, orbital_colors)
from atom_generator import generate_atom_image

# GENERATION CONTROL
REGENERATE_ATOMIC_IMAGES = False  # Set to True to force regeneration of all atomic images
NUMBER_OF_CARDS_TO_GENERATE = 118  # Set to any number (1-118) to generate specific amount of cards

# PAGE CONFIGURATION
page_size = A4
page_width, page_height = page_size
grid_size = '4x5'
num_cols, num_rows = map(int, grid_size.split('x'))
num_per_page = num_cols * num_rows

# CARD DIMENSIONS - EXACT measurements from reference
card_width = page_width / num_cols
card_height = page_height / num_rows

# ========== EXACT POSITIONING based on reference image analysis ==========

# 1. Green circle with atomic number (TOP LEFT)
circle_x_offset = 18
circle_y_from_top = 18
circle_radius = 14
circle_color = "#4CAF50"  # Green
number_font_size = 14
number_color = reportlab_colors.white
number_font_name = "Helvetica-Bold"

# 2. Element use text (TOP CENTER - horizontal)
use_x_center = card_width * 0.45
use_y_from_top = 22
use_font_size = 11
use_color = reportlab_colors.black
use_font_name = "Helvetica"

# 3. Large element symbol (TOP RIGHT)
symbol_x_offset = 20  # From right edge
symbol_y_from_top = 12
symbol_font_size = 42  # Very large like reference
symbol_color = reportlab_colors.black
symbol_font_name = "Helvetica-Bold"

# 4. Atomic mass (RIGHT SIDE, below symbol)
mass_x_offset = 20  # From right edge  
mass_y_from_top = 52
mass_font_size = 11
mass_color = reportlab_colors.black
mass_font_name = "Helvetica"

# 5. Green rounded rectangle with element name (LEFT SIDE - vertical)
name_rect_x_offset = 8  # From left edge
name_rect_y_start = card_height * 0.25  # Start position
name_rect_width = 24
name_rect_height = card_height * 0.5  # Half the card height
name_rect_color = "#4CAF50"  # Green background
name_rect_radius = 12  # Rounded corners
name_font_size = 11
name_color = reportlab_colors.white
name_font_name = "Helvetica-Bold"

# 6. Atomic image (CENTER area)
atomic_image_size = 35  # Small like reference
atomic_image_x = card_width * 0.4  # Center-left
atomic_image_y = card_height * 0.45  # Middle

# 7. Description text - VERTICAL on right side (like reference)
desc_right_x_offset = 12  # From right edge
desc_right_y_center = card_height * 0.6  # Center vertically
desc_right_font_size = 8
desc_right_color = reportlab_colors.black
desc_right_font_name = "Helvetica"

# 8. Bottom description text (BOTTOM area)
desc_bottom_x_margin = 12
desc_bottom_y_from_bottom = 25
desc_bottom_font_size = 9
desc_bottom_color = reportlab_colors.black
desc_bottom_font_name = "Helvetica"
desc_bottom_max_width = card_width - (2 * desc_bottom_x_margin)

# Card border
border_width = 2
border_color = reportlab_colors.black

def hex_to_reportlab_color(hex_color):
    """Convert hex color to reportlab Color object"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return reportlab_colors.Color(r/255.0, g/255.0, b/255.0)

def draw_rounded_rect(canvas_obj, x, y, width, height, radius, fill_color):
    """Draw a rounded rectangle"""
    canvas_obj.setFillColor(fill_color)
    # Draw main rectangle
    canvas_obj.rect(x + radius, y, width - 2*radius, height, fill=1, stroke=0)
    canvas_obj.rect(x, y + radius, width, height - 2*radius, fill=1, stroke=0)
    # Draw corner circles
    canvas_obj.circle(x + radius, y + radius, radius, fill=1, stroke=0)
    canvas_obj.circle(x + width - radius, y + radius, radius, fill=1, stroke=0)
    canvas_obj.circle(x + radius, y + height - radius, radius, fill=1, stroke=0)
    canvas_obj.circle(x + width - radius, y + height - radius, radius, fill=1, stroke=0)

def wrap_text(canvas_obj, text, max_width, font_name, font_size):
    """Wrap text to fit within specified width"""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        text_width = canvas_obj.stringWidth(test_line, font_name, font_size)

        if text_width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def check_atomic_images_exist():
    """Check if atomic images already exist"""
    images_dir = "atomic_images"
    if not os.path.exists(images_dir):
        return False

    existing_count = 0
    for i in range(1, min(NUMBER_OF_CARDS_TO_GENERATE + 1, len(symbols) + 1)):
        symbol = symbols[i - 1]
        filename = os.path.join(images_dir, f"atom_{i}_{symbol}.png")
        if os.path.exists(filename):
            existing_count += 1

    expected_count = min(NUMBER_OF_CARDS_TO_GENERATE, len(symbols))
    return existing_count >= (expected_count * 0.8)

def generate_atomic_images_for_elements(max_elements=None, force_regenerate=False):
    """Pre-generate ULTRA HIGH RESOLUTION atomic images"""

    if not force_regenerate and check_atomic_images_exist():
        print("✅ Atomic images already exist, skipping generation.")
        print("   Set REGENERATE_ATOMIC_IMAGES = True to force regeneration.")
        return []

    if max_elements is None:
        max_elements = min(NUMBER_OF_CARDS_TO_GENERATE, len(names))

    print(f"🔬 Generating ULTRA HIGH RES atomic images for {max_elements} elements...")

    images_dir = "atomic_images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    generated_files = []

    for i in range(min(max_elements, len(names))):
        atomic_num = i + 1

        filename = os.path.join(images_dir, f"atom_{atomic_num}_{symbols[i]}.png")

        try:
            # Generate ULTRA HIGH RESOLUTION atomic image (1200px)
            atom_img = generate_atom_image(atomic_num, scale_factor=1.0, image_size=1200)
            atom_img.save(filename)
            generated_files.append(filename)

            if atomic_num % 20 == 0:
                print(f"   Generated {atomic_num} ultra high resolution atomic images...")

        except Exception as e:
            print(f"❌ Error generating image for {symbols[i]} (#{atomic_num}): {e}")

    print(f"✅ Generated {len(generated_files)} ULTRA HIGH RES atomic images in '{images_dir}' directory")
    return generated_files

def create_element_cards_with_atoms(grid_input=grid_size, output_filename=None, 
                                   generate_atoms=True, num_cards=None):
    """Create PDF with EXACT layout matching reference image"""

    if num_cards is None:
        num_cards = NUMBER_OF_CARDS_TO_GENERATE

    # Calculate pages needed
    num_per_page = num_cols * num_rows
    pages_needed = math.ceil(num_cards / num_per_page)

    if output_filename is None:
        output_filename = f"element_cards_PERFECT_{num_cards}_cards_{grid_input}.pdf"

    try:
        cols, rows = map(int, grid_input.lower().split('x'))
        if not (1 <= cols <= 10 and 1 <= rows <= 10):
            raise ValueError("Columns and rows must be between 1 and 10")
    except Exception as e:
        print(f"Invalid input format or range: {e}")
        return

    # Generate atomic images if requested
    if generate_atoms:
        generate_atomic_images_for_elements(max_elements=num_cards, force_regenerate=REGENERATE_ATOMIC_IMAGES)

    # Recalculate dimensions if different grid size
    if grid_input != grid_size:
        global card_width, card_height
        card_width = page_width / cols
        card_height = page_height / rows
        global atomic_image_x, atomic_image_y, desc_bottom_max_width
        atomic_image_x = card_width * 0.4
        atomic_image_y = card_height * 0.45
        desc_bottom_max_width = card_width - (2 * desc_bottom_x_margin)

    c = canvas.Canvas(output_filename, pagesize=page_size)
    images_dir = "atomic_images"

    element_idx = 0
    for page in range(pages_needed):
        for row in range(rows):
            for col in range(cols):
                if element_idx >= num_cards or element_idx >= len(names):
                    continue

                # Calculate card position
                x = col * card_width
                y = page_height - (row + 1) * card_height

                # ========== DRAW ATOMIC IMAGE FIRST (background) ==========
                atomic_num = element_idx + 1
                symbol = symbols[element_idx]
                atom_image_file = os.path.join(images_dir, f"atom_{atomic_num}_{symbol}.png")

                # Position atomic image (center area like reference)
                img_x = x + atomic_image_x - (atomic_image_size / 2)
                img_y = y + atomic_image_y - (atomic_image_size / 2)

                if os.path.exists(atom_image_file):
                    try:
                        c.drawImage(atom_image_file, img_x, img_y, 
                                   atomic_image_size, atomic_image_size,
                                   mask='auto')
                    except Exception as e:
                        print(f"❌ Error embedding image for {symbol}: {e}")

                # ========== EXACT LAYOUT ELEMENTS (pixel perfect) ==========

                # Card border (EXACT like reference)
                c.setStrokeColor(border_color)
                c.setLineWidth(border_width)
                c.rect(x, y, card_width, card_height, fill=0, stroke=1)

                # 1. GREEN CIRCLE with atomic number (TOP LEFT)
                circle_x = x + circle_x_offset
                circle_y = y + card_height - circle_y_from_top
                c.setFillColor(hex_to_reportlab_color(circle_color))
                c.circle(circle_x, circle_y, circle_radius, fill=1, stroke=0)

                # White number inside circle
                c.setFillColor(number_color)
                c.setFont(number_font_name, number_font_size)
                num_text = str(atomic_numbers[element_idx])
                num_width = c.stringWidth(num_text, number_font_name, number_font_size)
                c.drawString(circle_x - num_width/2, circle_y - number_font_size/2 + 3, num_text)

                # 2. Element use text (TOP CENTER - horizontal like reference)
                c.setFillColor(use_color)
                c.setFont(use_font_name, use_font_size)
                use_text = element_uses[element_idx]
                use_width = c.stringWidth(use_text, use_font_name, use_font_size)
                c.drawString(
                    x + use_x_center - use_width/2,
                    y + card_height - use_y_from_top,
                    use_text
                )

                # 3. Large element symbol (TOP RIGHT - EXACT position)
                c.setFillColor(symbol_color)
                c.setFont(symbol_font_name, symbol_font_size)
                symbol_width = c.stringWidth(symbol, symbol_font_name, symbol_font_size)
                c.drawString(
                    x + card_width - symbol_x_offset - symbol_width,
                    y + card_height - symbol_y_from_top - symbol_font_size,
                    symbol
                )

                # 4. Atomic mass (RIGHT SIDE, below symbol - EXACT position)
                c.setFillColor(mass_color)
                c.setFont(mass_font_name, mass_font_size)
                mass_text = f"{atomic_masses[element_idx]}"
                mass_width = c.stringWidth(mass_text, mass_font_name, mass_font_size)
                c.drawString(
                    x + card_width - mass_x_offset - mass_width,
                    y + card_height - mass_y_from_top,
                    mass_text
                )

                # 5. Green rounded rectangle with element name (LEFT SIDE - EXACT like reference)
                element_name = names[element_idx]

                # Draw green rounded rectangle background
                rect_x = x + name_rect_x_offset
                rect_y = y + name_rect_y_start
                draw_rounded_rect(c, rect_x, rect_y, name_rect_width, name_rect_height, 
                                name_rect_radius, hex_to_reportlab_color(name_rect_color))

                # Draw rotated element name in white
                c.setFillColor(name_color)
                c.setFont(name_font_name, name_font_size)
                c.saveState()
                c.translate(rect_x + name_rect_width/2, rect_y + name_rect_height/2 + len(element_name)*3)
                c.rotate(270)  # Rotate 270 degrees (same as -90)
                name_width = c.stringWidth(element_name, name_font_name, name_font_size)
                c.drawString(-name_width/2, 0, element_name)
                c.restoreState()

                # 6. Description text - VERTICAL on right side (like reference)
                desc_text = element_descriptions[element_idx]
                c.setFillColor(desc_right_color)
                c.setFont(desc_right_font_name, desc_right_font_size)
                c.saveState()
                c.translate(x + card_width - desc_right_x_offset, y + desc_right_y_center + len(desc_text)*2)
                c.rotate(270)  # Rotate 270 degrees
                c.drawString(0, 0, desc_text)
                c.restoreState()

                # 7. Bottom description text (BOTTOM area - like reference)
                c.setFillColor(desc_bottom_color)
                c.setFont(desc_bottom_font_name, desc_bottom_font_size)
                # Use trivia for bottom text like in reference
                trivia_text = element_trivia[element_idx]
                description_lines = wrap_text(c, trivia_text, 
                                            desc_bottom_max_width, desc_bottom_font_name, desc_bottom_font_size)

                for i, line in enumerate(description_lines[:2]):  # Max 2 lines
                    c.drawString(
                        x + desc_bottom_x_margin,
                        y + desc_bottom_y_from_bottom - (i * (desc_bottom_font_size + 2)),
                        line
                    )

                element_idx += 1

        c.showPage()
    c.save()
    print(f"🎉 PERFECT LAYOUT element cards PDF created: {output_filename}")
    print(f"📊 Generated {element_idx} cards with EXACT reference layout")
    print(f"📊 Ultra high resolution atomic images included")
    return output_filename

# Example usage:
if __name__ == "__main__":
    print("🧪 Element Cards Generator - PERFECT REFERENCE LAYOUT")
    print("=" * 70)
    print("🎯 PIXEL PERFECT reproduction of reference image")
    print(f"🔄 Regenerate images: {'YES' if REGENERATE_ATOMIC_IMAGES else 'NO (will skip if exist)'}")
    print(f"📊 Number of cards to generate: {NUMBER_OF_CARDS_TO_GENERATE}")
    print("✅ Features: Green circles, rounded rectangles, vertical text, ultra high res atoms")

    # Generate element cards with PERFECT layout
    create_element_cards_with_atoms()
    print("\n🎊 PERFECT layout generation complete!")
