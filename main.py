# main.py
# Perfect print-and-play element cards generator

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors as reportlab_colors
import math
import os
from data import (symbols, names, atomic_numbers, atomic_masses, group_types,
                  element_uses, element_descriptions, element_trivia, is_radioactive,
                  element_group_colors)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Oxygen', 'Oxygen-Light.ttf'))
pdfmetrics.registerFont(TTFont('Oxygen-Bold', 'Oxygen-Bold.ttf'))

# ========== CONFIG ==========
PAGE_SIZE = A4
PAGE_W, PAGE_H = PAGE_SIZE

GRID = "4x5"
NUM_COLS, NUM_ROWS = map(int, GRID.split("x"))
NUM_PER_PAGE = NUM_COLS * NUM_ROWS
NUM_CARDS = 118

OUTPUT_PDF = f"element_cards_PERFECT_{NUM_CARDS}_cards_{GRID}.pdf"
ATOMIC_IMAGES_DIR = "atomic_images"

CARD_W = PAGE_W / NUM_COLS
CARD_H = PAGE_H / NUM_ROWS

BORDER_WIDTH = 0.2
BORDER_COLOR = reportlab_colors.black

# Circle (top-left) with atomic number
CIRCLE_RADIUS = 15
CIRCLE_OFFSET_X = 18
CIRCLE_OFFSET_Y = 18
CIRCLE_NUMBER_FONT = ("Oxygen-Bold", 14)
CIRCLE_NUMBER_COLOR = reportlab_colors.black

# Symbol and mass (centered horizontally)
SYMBOL_FONT = ("Oxygen-Bold", 28)
SYMBOL_Y_OFFSET = 48  # distance from top of card to symbol baseline
SYMBOL_RIGHT_MARGIN = 4  # distance from right edge of card to right edge of symbol

MASS_FONT = ("Oxygen", 8)
MASS_Y_OFFSET = 68  # distance from top of card to mass baseline

# Use text (top-center, centered horizontally)
USE_FONT = ("Oxygen", 12)
USE_Y_OFFSET = 15  # distance from top of card to use text baseline

# Name pill (left vertical half-round, centered at half height)
NAME_PILL_WIDTH = 48
NAME_PILL_HEIGHT = CARD_H * 0.6
NAME_PILL_RADIUS = NAME_PILL_WIDTH / 2
NAME_PILL_OFFSET_X = -NAME_PILL_WIDTH / 2
NAME_PILL_OFFSET_Y = (CARD_H - NAME_PILL_HEIGHT) / 2

NAME_FONT = ("Oxygen", 15)
NAME_TEXT_COLOR = reportlab_colors.black

# Atomic image (center)
ATOM_IMAGE_SIZE = min(CARD_W, CARD_H)
ATOM_IMAGE_CENTER_X = CARD_W / 2
ATOM_IMAGE_CENTER_Y = CARD_H / 2

# Nuclear icon (bottom-right)
NUCLEAR_ICON_FILE = os.path.join(ATOMIC_IMAGES_DIR, "nuclear.png")
NUCLEAR_ICON_SIZE = 12
NUCLEAR_ICON_OFFSET_X = 4
NUCLEAR_ICON_OFFSET_Y = 4

# Right-side vertical description (centered at half height)
DESC_RIGHT_FONT = ("Oxygen", 8)
DESC_RIGHT_OFFSET_X = 12
DESC_RIGHT_CENTER_Y = CARD_H / 2

# Bottom trivia (centered)
TRIVIA_FONT = ("Oxygen", 8)
TRIVIA_Y_OFFSET = 5
TRIVIA_MAX_LINES = 3
TRIVIA_MAX_WIDTH = CARD_W - 24
TRIVIA_X_CENTER = True

# Helper: convert hex color to reportlab color
def hex_to_color(hexcolor):
    h = hexcolor.lstrip("#")
    r, g, b = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return reportlab_colors.Color(r / 255.0, g / 255.0, b / 255.0)

# Draw rounded rectangle helper
def draw_rounded_rect(c, x, y, w, h, r, fill_color):
    c.setFillColor(fill_color)
    c.rect(x + r, y, w - 2*r, h, fill=1, stroke=0)
    c.rect(x, y + r, w, h - 2*r, fill=1, stroke=0)
    c.circle(x + r, y + r, r, fill=1, stroke=0)
    c.circle(x + r, y + h - r, r, fill=1, stroke=0)
    c.circle(x + w - r, y + r, r, fill=1, stroke=0)
    c.circle(x + w - r, y + h - r, r, fill=1, stroke=0)

# Text wrap helper
def wrap_text(c, text, max_width, font_name, font_size):
    words = text.split()
    lines = []
    cur = []
    for w in words:
        attempt = " ".join(cur + [w])
        if c.stringWidth(attempt, font_name, font_size) <= max_width:
            cur.append(w)
        else:
            if cur:
                lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines

def create_cards(output_pdf=OUTPUT_PDF, num_cards=NUM_CARDS, grid=f"{NUM_COLS}x{NUM_ROWS}"):
    cols, rows = map(int, grid.split("x"))
    c = canvas.Canvas(output_pdf, pagesize=PAGE_SIZE)

    element_idx = 0
    for page in range(math.ceil(num_cards / (cols * rows))):
        for row in range(rows):
            for col in range(cols):
                if element_idx >= num_cards:
                    break

                card_x = col * CARD_W
                card_y = PAGE_H - (row + 1) * CARD_H

                # Data for this element
                atomic_num = atomic_numbers[element_idx]
                symbol = symbols[element_idx]
                name = names[element_idx]
                use_text = element_uses[element_idx]
                mass_text = str(atomic_masses[element_idx])
                desc_right = element_descriptions[element_idx]
                trivia = element_trivia[element_idx]
                group = group_types[element_idx]
                group_color_hex = element_group_colors.get(group, "#4CAF50")
                group_color = hex_to_color(group_color_hex)

                # --- Draw half-pill first (so border can overlap it) ---
                pill_x = card_x + NAME_PILL_OFFSET_X
                pill_y = card_y + NAME_PILL_OFFSET_Y

                c.saveState()
                path = c.beginPath()
                path.rect(card_x, card_y, CARD_W, CARD_H)
                c.clipPath(path, stroke=0, fill=0)
                draw_rounded_rect(c, pill_x, pill_y, NAME_PILL_WIDTH, NAME_PILL_HEIGHT, NAME_PILL_RADIUS, group_color)
                # Name text rotated (vertical), centered at half height
                c.saveState()
                cx = pill_x + NAME_PILL_WIDTH / 2
                cy = pill_y + NAME_PILL_HEIGHT / 2
                c.translate(cx, cy)
                c.rotate(270)
                c.setFont(NAME_FONT[0], NAME_FONT[1])
                c.setFillColor(NAME_TEXT_COLOR)
                name_w = c.stringWidth(name, NAME_FONT[0], NAME_FONT[1])
                c.drawString(-name_w / 2, -NAME_FONT[1] / 2 + 15, name)
                c.restoreState()
                c.restoreState()

                # --- Draw border after pill so it overlaps ---
                c.setLineWidth(BORDER_WIDTH)
                c.setStrokeColor(BORDER_COLOR)
                c.rect(card_x, card_y, CARD_W, CARD_H, fill=0, stroke=1)

                # 2) top-left circle with atomic number
                circle_cx = card_x + CIRCLE_OFFSET_X
                circle_cy = card_y + CARD_H - CIRCLE_OFFSET_Y
                c.setFillColor(group_color)
                c.circle(circle_cx, circle_cy, CIRCLE_RADIUS, fill=1, stroke=0)
                c.setFillColor(CIRCLE_NUMBER_COLOR)
                c.setFont(CIRCLE_NUMBER_FONT[0], CIRCLE_NUMBER_FONT[1])
                num_txt = str(atomic_num)
                tw = c.stringWidth(num_txt, CIRCLE_NUMBER_FONT[0], CIRCLE_NUMBER_FONT[1])
                c.drawString(circle_cx - tw / 2, circle_cy - (CIRCLE_NUMBER_FONT[1] / 2) + 3, num_txt)

                # 3) TOP CENTER: use text (centered horizontally)
                c.setFillColor(reportlab_colors.black)
                c.setFont(USE_FONT[0], USE_FONT[1])
                u_text = use_text
                u_w = c.stringWidth(u_text, USE_FONT[0], USE_FONT[1])
                if u_w > CARD_W * 0.6:
                    small_size = max(7, int(USE_FONT[1] * (CARD_W * 0.6 / u_w)))
                    c.setFont(USE_FONT[0], small_size)
                    u_w = c.stringWidth(u_text, USE_FONT[0], small_size)
                c.drawString(card_x + CARD_W / 2 - u_w / 2, card_y + CARD_H - USE_Y_OFFSET, u_text)

                # 4) big element symbol (top-right, as before)
                c.setFont(SYMBOL_FONT[0], SYMBOL_FONT[1])
                c.setFillColor(reportlab_colors.black)
                symbol_w = c.stringWidth(symbol, SYMBOL_FONT[0], SYMBOL_FONT[1])
                symbol_x = card_x + CARD_W - SYMBOL_RIGHT_MARGIN - symbol_w  # right edge fixed margin
                symbol_y = card_y + CARD_H - SYMBOL_Y_OFFSET + 25
                c.drawString(symbol_x, symbol_y, symbol)

                # 5) atomic mass right below symbol (same center as symbol)
                c.setFont(MASS_FONT[0], MASS_FONT[1])
                c.setFillColor(reportlab_colors.black)
                # Apply brackets if radioactive
                if is_radioactive[element_idx]:
                    mass_display = f"[{mass_text}]"
                else:
                    mass_display = mass_text
                mass_w = c.stringWidth(mass_display, MASS_FONT[0], MASS_FONT[1])
                mass_x = symbol_x + symbol_w / 2 - mass_w / 2  # center mass under symbol
                mass_y = symbol_y - (MASS_Y_OFFSET - SYMBOL_Y_OFFSET) + 6
                c.drawString(mass_x, mass_y, mass_display)

                # 6) centered atomic image
                img_file = os.path.join(ATOMIC_IMAGES_DIR, f"atom_{atomic_num}_{symbol}.png")
                atom_size = ATOM_IMAGE_SIZE
                atom_x = card_x + (CARD_W / 2) - (atom_size / 2)
                atom_y = card_y + (CARD_H / 2) - (atom_size / 2)
                if os.path.exists(img_file):
                    try:
                        c.drawImage(img_file, atom_x, atom_y, atom_size, atom_size, mask="auto")
                    except Exception:
                        pass

                # 7) nuclear icon if radioactive (bottom-right)
                if is_radioactive[element_idx]:
                    if os.path.exists(NUCLEAR_ICON_FILE):
                        icon_x = card_x + CARD_W - NUCLEAR_ICON_SIZE - NUCLEAR_ICON_OFFSET_X
                        icon_y = card_y + NUCLEAR_ICON_OFFSET_Y
                        try:
                            c.drawImage(NUCLEAR_ICON_FILE, icon_x, icon_y, NUCLEAR_ICON_SIZE, NUCLEAR_ICON_SIZE, mask="auto")
                        except Exception:
                            pass

                # 8) RIGHT-SIDE vertical description (rotated 90°, centered at half height)
                c.saveState()
                tx = card_x + CARD_W - DESC_RIGHT_OFFSET_X
                ty = card_y + DESC_RIGHT_CENTER_Y
                c.translate(tx, ty)
                c.rotate(-90)
                c.setFont(DESC_RIGHT_FONT[0], DESC_RIGHT_FONT[1])
                c.setFillColor(reportlab_colors.black)
                desc_lines = wrap_text(c, desc_right, CARD_H * 0.55, DESC_RIGHT_FONT[0], DESC_RIGHT_FONT[1])
                desc_lines = desc_lines[:2]
                total_height = len(desc_lines) * (DESC_RIGHT_FONT[1] + 1)
                for i, line in enumerate(desc_lines):
                    line_w = c.stringWidth(line, DESC_RIGHT_FONT[0], DESC_RIGHT_FONT[1])
                    x = -line_w / 2
                    y = (len(desc_lines)-i-1) * (DESC_RIGHT_FONT[1] + 1) - total_height/2
                    c.drawString(x, y, line)
                c.restoreState()

                # 9) BOTTOM trivia (centered, up to TRIVIA_MAX_LINES)
                c.setFont(TRIVIA_FONT[0], TRIVIA_FONT[1])
                c.setFillColor(reportlab_colors.black)
                lines = wrap_text(c, trivia, TRIVIA_MAX_WIDTH, TRIVIA_FONT[0], TRIVIA_FONT[1])
                lines = lines[:TRIVIA_MAX_LINES]
                for i, ln in enumerate(reversed(lines)):
                    y_pos = card_y + TRIVIA_Y_OFFSET + i * (TRIVIA_FONT[1] + 2)
                    text_w = c.stringWidth(ln, TRIVIA_FONT[0], TRIVIA_FONT[1])
                    x_pos = card_x + (CARD_W - text_w) / 2 if TRIVIA_X_CENTER else card_x + 12
                    c.drawString(x_pos, y_pos, ln)

                element_idx += 1

        c.showPage()
    c.save()
    print(f"PDF saved -> {output_pdf}")
    return output_pdf

if __name__ == "__main__":
    if not os.path.isdir(ATOMIC_IMAGES_DIR):
        print(f"Warning: '{ATOMIC_IMAGES_DIR}' folder not found. Atomic images will be skipped.")
    if not os.path.exists(NUCLEAR_ICON_FILE):
        print(f"Note: nuclear icon '{NUCLEAR_ICON_FILE}' not found. Radioactive icon will be skipped.")
    print("Generating element cards PDF with exact layout...")
    create_cards()
    print("Done.")
