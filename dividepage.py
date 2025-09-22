from reportlab.lib.pagesizes import A4  # type: ignore
from reportlab.pdfgen import canvas  # type: ignore
from reportlab.lib import colors  # type: ignore
import math
from data import (symbols, names, atomic_numbers, atomic_masses, group_types, 
                 element_uses, element_descriptions, element_trivia, is_radioactive)

# PAGE CONFIGURATION
page_size = A4
page_width, page_height = page_size
grid_size = '4x5'
num_cols, num_rows = map(int, grid_size.split('x'))
num_per_page = num_cols * num_rows
num_pages = math.ceil(len(names) / num_per_page)

# CARD DIMENSIONS
card_width = page_width / num_cols
card_height = page_height / num_rows
card_border_width = 1
card_border_color = colors.black

# HEADER SECTION (Colored background with element name)
header_height_ratio = 0.22  # 22% of card height
header_height = card_height * header_height_ratio
header_text_color = colors.white
header_text_color_dark_bg = colors.white
header_text_color_light_bg = colors.black
header_font_name = "Helvetica-Bold"
header_font_size = 16
header_vertical_offset = 8  # Pixels from center

# ATOMIC NUMBER
atomic_number_font_name = "Helvetica"
atomic_number_font_size = 11
atomic_number_color = colors.black
atomic_number_x_offset = 8  # From left edge
atomic_number_y_offset = 15  # From header bottom

# ELEMENT SYMBOL (Large, centered)
symbol_font_name = "Helvetica-Bold"
symbol_font_size = 28
symbol_color = colors.black
symbol_y_offset = 45  # From header bottom

# ATOMIC MASS
atomic_mass_font_name = "Helvetica"
atomic_mass_font_size = 10
atomic_mass_color = colors.darkgrey
atomic_mass_x_offset = 8  # From left edge
atomic_mass_y_offset = 8   # From bottom edge

# RADIOACTIVE INDICATOR
radioactive_indicator_size = 12
radioactive_indicator_color = colors.red
radioactive_symbol = "☢"  # Unicode radioactive symbol
radioactive_x_offset = 8   # From right edge
radioactive_y_offset = 15  # From header bottom

# ELEMENT USE (One word)
use_font_name = "Helvetica-Bold"
use_font_size = 9
use_color = colors.darkblue
use_x_offset = 8  # From right edge
use_y_offset = 8  # From bottom edge

# ELEMENT DESCRIPTION
description_font_name = "Helvetica"
description_font_size = 7
description_color = colors.black
description_x_margin = 8
description_y_position = 85  # From bottom of card
description_max_width = card_width - (2 * description_x_margin)

# ELEMENT TRIVIA
trivia_font_name = "Helvetica-Oblique"
trivia_font_size = 6
trivia_color = colors.darkgreen
trivia_x_margin = 8
trivia_y_position = 60  # From bottom of card
trivia_max_width = card_width - (2 * trivia_x_margin)

# IMAGE SPACE (Reserved area for element image)
image_space_x = card_width * 0.25
image_space_y = 100  # From bottom of card
image_space_width = card_width * 0.5
image_space_height = 40
image_placeholder_color = colors.lightgrey
image_placeholder_text = "IMG"
image_placeholder_font = "Helvetica"
image_placeholder_font_size = 8

# GROUP COLORS (Updated based on user's changes)
GROUP_COLORS = {
    "nonmetal": colors.lightgreen,
    "noble gas": colors.purple,
    "alkali metal": colors.red,
    "alkaline earth metal": colors.orange,
    "metalloid": colors.cadetblue,
    "post-transition metal": colors.lightgrey,
    "transition metal": colors.lightblue,
    "lanthanide": colors.gold,
    "actinide": colors.brown,
}

def get_group_color(group_type):
    """Get color for element group type"""
    return GROUP_COLORS.get(group_type, colors.white)

def is_light_color(color):
    """Determine if a color is light (for text contrast)"""
    light_colors = [colors.white, colors.lightgrey, colors.lightgreen, 
                   colors.lightblue, colors.yellow, colors.orange, colors.gold]
    return color in light_colors

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
                lines.append(word)  # Word too long, add anyway

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def create_element_cards(grid_input=grid_size, output_filename=None, pages=num_pages):
    """Create PDF with element cards based on data.py information"""

    if output_filename is None:
        output_filename = f"element_cards_{grid_input}.pdf"

    try:
        cols, rows = map(int, grid_input.lower().split('x'))
        if not (1 <= cols <= 10 and 1 <= rows <= 10):
            raise ValueError("Columns and rows must be between 1 and 10")
    except Exception as e:
        print(f"Invalid input format or range: {e}")
        return

    # Recalculate dimensions if different grid size
    if grid_input != grid_size:
        global card_width, card_height, header_height
        card_width = page_width / cols
        card_height = page_height / rows
        header_height = card_height * header_height_ratio

    c = canvas.Canvas(output_filename, pagesize=page_size)

    element_idx = 0
    for page in range(pages):
        for row in range(rows):
            for col in range(cols):
                if element_idx >= len(names):
                    continue

                # Calculate card position
                x = col * card_width
                y = page_height - (row + 1) * card_height

                # Draw card border
                c.setStrokeColor(card_border_color)
                c.setLineWidth(card_border_width)
                c.rect(x, y, card_width, card_height, fill=0, stroke=1)

                # Draw colored header bar
                group_type = group_types[element_idx]
                fill_color = get_group_color(group_type)
                c.setFillColor(fill_color)
                c.rect(x, y + card_height - header_height, card_width, header_height, fill=1, stroke=0)

                # Determine text color based on background
                text_color = header_text_color_light_bg if is_light_color(fill_color) else header_text_color_dark_bg

                # Draw element name in header
                c.setFillColor(text_color)
                c.setFont(header_font_name, header_font_size)
                name_text = names[element_idx]
                name_width = c.stringWidth(name_text, header_font_name, header_font_size)
                c.drawString(
                    x + (card_width - name_width) / 2,
                    y + card_height - header_height/2 - header_vertical_offset,
                    name_text
                )

                # Draw atomic number (top left, below header)
                c.setFillColor(atomic_number_color)
                c.setFont(atomic_number_font_name, atomic_number_font_size)
                c.drawString(
                    x + atomic_number_x_offset,
                    y + card_height - header_height - atomic_number_y_offset,
                    str(atomic_numbers[element_idx])
                )

                # Draw radioactive indicator if radioactive
                if is_radioactive[element_idx]:
                    c.setFillColor(radioactive_indicator_color)
                    c.setFont("Helvetica", radioactive_indicator_size)
                    radioactive_width = c.stringWidth(radioactive_symbol, "Helvetica", radioactive_indicator_size)
                    c.drawString(
                        x + card_width - radioactive_x_offset - radioactive_width,
                        y + card_height - header_height - radioactive_y_offset,
                        radioactive_symbol
                    )

                # Draw element symbol (large, centered)
                c.setFillColor(symbol_color)
                c.setFont(symbol_font_name, symbol_font_size)
                symbol = symbols[element_idx]
                symbol_width = c.stringWidth(symbol, symbol_font_name, symbol_font_size)
                c.drawString(
                    x + (card_width - symbol_width) / 2,
                    y + card_height - header_height - symbol_y_offset,
                    symbol
                )

                # Draw atomic mass (bottom left)
                c.setFillColor(atomic_mass_color)
                c.setFont(atomic_mass_font_name, atomic_mass_font_size)
                mass_text = f"{atomic_masses[element_idx]}"
                c.drawString(
                    x + atomic_mass_x_offset,
                    y + atomic_mass_y_offset,
                    mass_text
                )

                # Draw element use (bottom right)
                c.setFillColor(use_color)
                c.setFont(use_font_name, use_font_size)
                use_text = element_uses[element_idx]
                use_width = c.stringWidth(use_text, use_font_name, use_font_size)
                c.drawString(
                    x + card_width - use_x_offset - use_width,
                    y + use_y_offset,
                    use_text
                )

                # Draw element description (wrapped text)
                c.setFillColor(description_color)
                c.setFont(description_font_name, description_font_size)
                description_lines = wrap_text(c, element_descriptions[element_idx], 
                                            description_max_width, description_font_name, description_font_size)

                for i, line in enumerate(description_lines[:2]):  # Max 2 lines
                    c.drawString(
                        x + description_x_margin,
                        y + description_y_position - (i * (description_font_size + 2)),
                        line
                    )

                # Draw element trivia (wrapped text)
                c.setFillColor(trivia_color)
                c.setFont(trivia_font_name, trivia_font_size)
                trivia_lines = wrap_text(c, element_trivia[element_idx], 
                                       trivia_max_width, trivia_font_name, trivia_font_size)

                for i, line in enumerate(trivia_lines[:3]):  # Max 3 lines
                    c.drawString(
                        x + trivia_x_margin,
                        y + trivia_y_position - (i * (trivia_font_size + 1)),
                        line
                    )

                # Draw image placeholder
                c.setStrokeColor(image_placeholder_color)
                c.setFillColor(image_placeholder_color)
                c.rect(x + image_space_x, y + image_space_y, 
                      image_space_width, image_space_height, fill=1, stroke=1)

                # Add "IMG" text in placeholder
                c.setFillColor(colors.darkgrey)
                c.setFont(image_placeholder_font, image_placeholder_font_size)
                img_text_width = c.stringWidth(image_placeholder_text, image_placeholder_font, image_placeholder_font_size)
                c.drawString(
                    x + image_space_x + (image_space_width - img_text_width) / 2,
                    y + image_space_y + (image_space_height - image_placeholder_font_size) / 2,
                    image_placeholder_text
                )

                element_idx += 1

        c.showPage()
    c.save()
    print(f"Element cards PDF created: {output_filename} with {pages} pages.")
    return output_filename

# Example usage:
if __name__ == "__main__":
    create_element_cards()
