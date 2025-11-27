from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import io, textwrap

app = Flask(__name__)
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# ... (نفس دوال autosize/prepare_text_lines/find_max_font_size كما في نسخةي السابقة)
# من أجل الإختصار: الصق نفس server.py الكامل الذي أعطيتك سابقًا
# تأكد أن الملف متطابق بدون أخطاء عند اللصق
