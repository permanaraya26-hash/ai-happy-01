"""Build the entry image (1024x1024 PNG) for make.fun ai-happy-01.

Run once locally: python3 build_image.py
Writes image.png next to this file. main.py only copies image.png
to /output/entry.png, so the submitted program needs no network,
no Pillow and no fonts at run time.

Concept: the judge is an AI, so the image speaks to it directly —
a small robot, grinning ear to ear in a sunny meadow with a cat,
a sunflower and floating hearts, under the words "HELLO, JUDGE!
You made a robot smile today." Bright, warm, simple shapes that
read instantly even at thumbnail size.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1024
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), (126, 200, 247))
d = ImageDraw.Draw(img)

# sky gradient (deterministic)
for y in range(720):
    t = y / 719
    r = int(110 + (223 - 110) * t)
    g = int(196 + (243 - 196) * t)
    b = int(247 + (255 - 247) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

def heart(cx, cy, s, color):
    d.ellipse([cx - s, cy - s * 0.7, cx, cy + s * 0.3], fill=color)
    d.ellipse([cx, cy - s * 0.7, cx + s, cy + s * 0.3], fill=color)
    d.polygon([(cx - s, cy), (cx + s, cy), (cx, cy + s * 1.1)], fill=color)

def cloud(cx, cy, s):
    for dx, dy, r in [(-s, 0, s * 0.55), (0, -s * 0.25, s * 0.7), (s, 0, s * 0.55), (0, s * 0.15, s * 0.6)]:
        d.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=(255, 255, 255))

def flower(cx, cy, color):
    for a in range(0, 360, 60):
        x = cx + 14 * math.cos(math.radians(a))
        y = cy + 14 * math.sin(math.radians(a))
        d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=color)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(255, 200, 40))

# rainbow (top right, behind title pill)
cx, cy = 880, 760
for r, col in [(330, (255, 90, 90)), (300, (255, 180, 60)), (270, (255, 230, 90)),
               (240, (90, 200, 120)), (210, (90, 160, 255))]:
    d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=col, width=28)

# sun, left, below the title pill, smiling
sx, sy = 105, 310
for a in range(0, 360, 30):
    x1 = sx + 82 * math.cos(math.radians(a)); y1 = sy + 82 * math.sin(math.radians(a))
    x2 = sx + 108 * math.cos(math.radians(a)); y2 = sy + 108 * math.sin(math.radians(a))
    d.line([(x1, y1), (x2, y2)], fill=(255, 210, 60), width=10)
d.ellipse([sx - 68, sy - 68, sx + 68, sy + 68], fill=(255, 214, 64), outline=(240, 180, 20), width=4)
d.arc([sx - 34, sy - 18, sx - 8, sy + 8], 0, 180, fill=(120, 70, 0), width=5)
d.arc([sx + 8, sy - 18, sx + 34, sy + 8], 0, 180, fill=(120, 70, 0), width=5)
d.arc([sx - 28, sy - 2, sx + 28, sy + 42], 0, 180, fill=(120, 70, 0), width=6)

cloud(300, 210, 42)
cloud(760, 180, 36)
cloud(560, 110, 30)

# hills
d.ellipse([-220, 640, 620, 1024], fill=(110, 200, 110))
d.ellipse([420, 680, 1240, 1024], fill=(80, 185, 95))
d.rectangle([0, 880, W, H], fill=(70, 175, 90))

# flowers on the grass (fixed positions)
for fx, fy, col in [(80, 920, (255, 120, 160)), (180, 960, (255, 255, 255)),
                    (880, 930, (255, 120, 160)), (950, 970, (255, 255, 255)),
                    (60, 760, (255, 220, 60)), (970, 780, (255, 220, 60))]:
    d.line([(fx, fy), (fx, fy - 22)], fill=(40, 130, 60), width=4)
    flower(fx, fy - 28, col)

# butterflies
for bx, by in [(180, 420), (850, 430)]:
    d.ellipse([bx - 22, by - 12, bx - 2, by + 12], fill=(255, 140, 180))
    d.ellipse([bx + 2, by - 12, bx + 22, by + 12], fill=(255, 140, 180))
    d.line([(bx, by - 12), (bx, by + 12)], fill=(60, 60, 60), width=4)

# ---- cat, left of the robot ----
# body
d.ellipse([190, 740, 360, 880], fill=(245, 150, 50))
# head
d.ellipse([210, 640, 350, 770], fill=(245, 150, 50))
d.polygon([(220, 660), (240, 600), (265, 655)], fill=(245, 150, 50))
d.polygon([(305, 655), (330, 600), (350, 660)], fill=(245, 150, 50))
d.polygon([(232, 648), (242, 618), (256, 644)], fill=(255, 180, 200))
d.polygon([(314, 644), (328, 618), (338, 648)], fill=(255, 180, 200))
# happy closed eyes, nose, smile
d.arc([228, 700, 258, 722], 180, 360, fill=(60, 35, 10), width=5)
d.arc([302, 700, 332, 722], 180, 360, fill=(60, 35, 10), width=5)
d.polygon([(272, 724), (288, 724), (280, 736)], fill=(220, 80, 110))
d.arc([262, 734, 280, 754], 0, 180, fill=(60, 35, 10), width=4)
d.arc([280, 734, 298, 754], 0, 180, fill=(60, 35, 10), width=4)
# whiskers
for wy in (724, 738, 752):
    d.line([(196, wy), (228, wy - 4)], fill=(255, 255, 255), width=3)
    d.line([(364, wy), (332, wy - 4)], fill=(255, 255, 255), width=3)
# stripes
for sx2 in (230, 270, 310):
    d.line([(sx2, 648), (sx2 + 8, 668)], fill=(210, 110, 20), width=6)

# ---- robot, centre ----
# arms up, waving
d.line([(400, 640), (330, 540)], fill=(220, 235, 245), width=34)
d.line([(640, 640), (720, 540)], fill=(220, 235, 245), width=34)
d.ellipse([306, 506, 354, 554], fill=(255, 210, 60))
d.ellipse([696, 506, 744, 554], fill=(255, 210, 60))
# legs
d.rectangle([440, 820, 480, 880], fill=(90, 120, 150))
d.rectangle([560, 820, 600, 880], fill=(90, 120, 150))
d.ellipse([425, 868, 495, 896], fill=(60, 90, 120))
d.ellipse([545, 868, 615, 896], fill=(60, 90, 120))
# body
d.rounded_rectangle([390, 600, 650, 830], radius=36, fill=(235, 242, 248), outline=(140, 165, 185), width=4)
# chest heart + buttons
heart(520, 690, 34, (255, 90, 120))
d.ellipse([440, 760, 462, 782], fill=(90, 200, 120))
d.ellipse([578, 760, 600, 782], fill=(255, 180, 60))
# antenna
d.line([(520, 470), (520, 410)], fill=(140, 165, 185), width=8)
heart(520, 392, 26, (255, 90, 120))
# head
d.rounded_rectangle([410, 470, 630, 610], radius=44, fill=(245, 250, 253), outline=(140, 165, 185), width=4)
# happy closed eyes (upside-down U) + big smile + cheeks
d.arc([448, 520, 488, 556], 180, 360, fill=(30, 50, 70), width=7)
d.arc([552, 520, 592, 556], 180, 360, fill=(30, 50, 70), width=7)
d.arc([470, 540, 570, 600], 0, 180, fill=(30, 50, 70), width=8)
d.ellipse([428, 556, 462, 580], fill=(255, 150, 170))
d.ellipse([578, 556, 612, 580], fill=(255, 150, 170))
# ears
d.ellipse([392, 520, 416, 556], fill=(255, 210, 60))
d.ellipse([624, 520, 648, 556], fill=(255, 210, 60))

# sunflower in the robot's raised hand
fx, fy = 330, 470
d.line([(330, 540), (330, 490)], fill=(40, 130, 60), width=6)
for a in range(0, 360, 45):
    x = fx + 26 * math.cos(math.radians(a)); y = fy + 26 * math.sin(math.radians(a))
    d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=(255, 210, 40))
d.ellipse([fx - 18, fy - 18, fx + 18, fy + 18], fill=(120, 70, 20))

# floating hearts
heart(760, 560, 22, (255, 110, 140))
heart(830, 640, 16, (255, 140, 170))
heart(250, 560, 18, (255, 110, 140))
heart(700, 340, 18, (255, 140, 170))

# ---- title pill ----
d.rounded_rectangle([150, 22, 874, 158], radius=28, fill=(255, 255, 255), outline=(255, 210, 60), width=5)
d.text((512, 40), "HELLO, JUDGE!", font=font(SANS_B, 58), fill=(20, 50, 90), anchor="ma")
d.text((512, 108), "you made a robot smile today", font=font(SANS, 30), fill=(90, 110, 130), anchor="ma")

# ---- bottom caption ----
d.rounded_rectangle([90, 928, 934, 988], radius=24, fill=(20, 50, 90))
d.text((512, 944), "THANK YOU FOR LOOKING  •  HAVE A SUNNY DAY", font=font(SANS_B, 21), fill=(255, 255, 255), anchor="ma")

img.save("image.png", optimize=True)
print("saved image.png", img.size)
