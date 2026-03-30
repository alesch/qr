#!/usr/bin/env python3
import os
import sys

import cairosvg
import qrcode
import qrcode.image.svg

# Initialize the QR Code object
qr = qrcode.QRCode(
    version=1,  # Controls the size (1 is 21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Approx 7% correction
    box_size=40,  # How many pixels each "box" of the QR code is
    border=4,  # Thickness of the white border (minimum is 4)
)

# Add data
qr.add_data("http://qr.schenkman.info/a")
qr.make(fit=True)

# Create the image with custom colors
# png_img = qr.make_image(fill_color="black", back_color="white")
svg_img = qr.make_image(
    image_factory=qrcode.image.svg.SvgPathFillImage,
    fill_color="black",
    back_color="white",
)

# Save the files
basename = os.path.splitext(sys.argv[1])[0] if len(sys.argv) > 1 else "qr"
# with open(f"{basename}.png", "wb") as f:
#    png_img.save(f)

with open(f"{basename}.svg", "wb") as f:
    svg_img.save(f)

# Convert SVG to EPS using Cairo
cairosvg.svg2ps(url=f"{basename}.svg", write_to=f"{basename}.eps")
cairosvg.svg2png(url=f"{basename}.svg", write_to=f"{basename}.png", scale=4)
