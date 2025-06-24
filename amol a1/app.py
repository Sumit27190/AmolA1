import base64
import streamlit as st
from PIL import Image
import os

# ---------- CONFIG ----------
st.set_page_config(page_title="Amol A1 Cement Products", layout="wide")

# ---------- GLOBAL STYLES ----------
st.markdown("""
    <style>
        body {
            background-color: #f2f4f8;
            font-family: 'Segoe UI', sans-serif;
        }
        .nav-bar {
            display: flex;
            justify-content: space-around;
            background-color: #1a202c;
            padding: 12px;
            margin-bottom: 30px;
            border-radius: 10px;
            width: 100%;
        }
        .nav-bar a {
            color: #ffffff;
            text-decoration: none;
            font-size: 17px;
            font-weight: 500;
            flex-grow: 1;
            text-align: center;
        }
        .nav-bar a:hover {
            color: #90cdf4;
        }
        .product-card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 18px;
        }
        .product-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        }
        .section-title {
            font-size: 32px;
            font-weight: 700;
            color: #2d3748;
            border-left: 6px solid #3182ce;
            padding-left: 12px;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            color: #718096;
            font-size: 14px;
            padding-top: 30px;
        }
        .floating-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #25D366;
            color: white;
            padding: 12px 18px;
            border-radius: 50px;
            font-size: 18px;
            text-decoration: none;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: background-color 0.2s;
        }
        .floating-button:hover {
            background-color: #1ebd5a;
        }
        .image-hover {
            transition: transform 0.2s ease-in-out;
            border-radius: 10px;
            object-fit: cover;
            height: 350px;
            width: 100%;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HERO TITLE ----------
st.markdown("""
    <div style='background: linear-gradient(to right, #3182ce, #63b3ed); padding: 30px 10px; border-radius: 12px; text-align: center; margin-bottom: 30px;'>
        <h1 style='color: white; margin-bottom: 10px;'>Amol A1 Group</h1>
        <p style='font-size: 18px; color: white;'>Strong Foundations, Nourishing Livestock, and Fragrant Living – All from One Brand</p>
    </div>
""", unsafe_allow_html=True)

# ---------- NAVIGATION BAR ----------
st.markdown("""
    <div class='nav-bar'>
        <a href="#our-products">Cement Products</a>
        <a href="#shrushti-pashukhadya">Shrushti PashuKhadya</a>
        <a href="#amol-aggarbatti">Amol Aggarbatti</a>
        <a href="#contact-us">Contact</a>
    </div>
""", unsafe_allow_html=True)

# ---------- LOGO ----------
def get_base64_image(path):
    with open(path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_data}"

logo_base64 = get_base64_image("logo.png")

st.markdown(
    f"""
    <div style='text-align: center; margin-bottom: 20px;'>
        <img src="{logo_base64}" width="300" style="border-radius:10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"/>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- IMAGE LIST ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "assets")
image_files = [
    "poles.webp", "pots.jpeg", "doorframe.webp", "pole5.jpg", "pole2.jpg",
    "pole3.jpg", "pole4.jpg", "pole7.jpg", "pole1.jpg", "pole6.jpg"
]

# ---------- PRODUCT IMAGES ----------
st.markdown("<div class='section-title' id='our-products'>🧱 Amol A1 Cement Products</div>", unsafe_allow_html=True)
image_paths = [os.path.join(image_dir, fname) for fname in image_files if os.path.exists(os.path.join(image_dir, fname))]

if not image_paths:
    st.warning("No images found. Please check your 'assets' folder.")
else:
    rows = len(image_paths) // 3 + int(len(image_paths) % 3 > 0)
    for row in range(rows):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            if idx < len(image_paths):
                with cols[col]:
                    st.markdown(f"<img src='data:image/jpeg;base64,{base64.b64encode(open(image_paths[idx], 'rb').read()).decode()}' class='image-hover'>", unsafe_allow_html=True)

# ---------- AVAILABLE PRODUCTS ----------
st.markdown("<div class='section-title' id='available-products'>📦 Product Catalog</div>", unsafe_allow_html=True)
product_items = [
    "🥵 Cement Pole",
    "🌿 Cement Kundi",
    "🚪 Cement Frames",
    "🥵 Cement Y Pole",
    "🌿 Cement Vrundavan",
    "🚪 Cement Havakashi"
]

for label in product_items:
    st.markdown(f"<div class='product-card'>{label}</div>", unsafe_allow_html=True)

# ---------- OTHER BUSINESSES ----------
st.markdown("<div class='section-title' id='shrushti-pashukhadya'>🌾 Shrushti PashuKhadya (Cattle Feed)</div>", unsafe_allow_html=True)
st.markdown("""
<div class='product-card'>
    <strong>Shrushti PashuKhadya</strong><br>
    <span style='font-size:16px; color:#555;'>High-quality cattle feed and supplements supporting farmers and dairy producers.</span>
</div>
""", unsafe_allow_html=True)

shrushti_folder = os.path.join(image_dir, "pashu")
if os.path.exists(shrushti_folder):
    shrushti_images = [f for f in os.listdir(shrushti_folder) if os.path.isfile(os.path.join(shrushti_folder, f))]
    for img in shrushti_images:
        img_path = os.path.join(shrushti_folder, img)
        st.image(img_path, use_column_width=True)
else:
    st.warning(f"Shrushti folder not found at {shrushti_folder}")

# ---------- Amol A1 Aggarbatti ----------
st.markdown("<div class='section-title' id='amol-aggarbatti'>🕯️ Amol A1 Incense (Aggarbatti)</div>", unsafe_allow_html=True)
st.markdown("""
<div class='product-card'>
    <strong>Amol A1 Aggarbatti</strong><br>
    <span style='font-size:16px; color:#555;'>Premium incense sticks made with natural ingredients for a long-lasting aroma.</span>
</div>
""", unsafe_allow_html=True)

aggar_folder = os.path.join(image_dir, "aggar")
if os.path.exists(aggar_folder):
    aggar_images = [f for f in os.listdir(aggar_folder) if os.path.isfile(os.path.join(aggar_folder, f))]
    aggar_image_paths = [os.path.join(aggar_folder, fname) for fname in sorted(aggar_images)]
    rows = len(aggar_image_paths) // 3 + int(len(aggar_image_paths) % 3 > 0)
    for row in range(rows):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            if idx < len(aggar_image_paths):
                with cols[col]:
                    st.markdown(f"<img src='data:image/jpeg;base64,{base64.b64encode(open(aggar_image_paths[idx], 'rb').read()).decode()}' class='image-hover'>", unsafe_allow_html=True)
else:
    st.warning(f"Aggar folder not found at {aggar_folder}")

# ---------- CONTACT SECTION ----------
st.markdown("<div class='section-title' id='contact-us'>📞 Contact Us</div>", unsafe_allow_html=True)

contact_cols = st.columns(2)

with contact_cols[0]:
    st.markdown("<div style='font-size:20px;'><strong>🏢 Company:</strong> Amol A1 Cement Products</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:20px;'><strong>📍 Address:</strong> Behind Birsa Munda Putla, Main Road, Vairagad</div>", unsafe_allow_html=True)
    st.markdown("""
        <iframe src="https://www.google.com/maps/embed?..." width="100%" height="300" style="border:0; border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    """, unsafe_allow_html=True)

with contact_cols[1]:
    st.markdown("<div style='font-size:20px;'><strong>📞 Phone:</strong> +91-7020634503</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:20px;'><strong>📧 Email:</strong> Amollanjewar918@gmail.com</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer'>© 2025 Amol A1 Group. All rights reserved.</div>", unsafe_allow_html=True)

# ---------- FLOATING WHATSAPP BUTTON ----------
st.markdown("""
    <a href="https://wa.me/917020634503" class="floating-button" target="_blank">
        💬 WhatsApp
    </a>
""", unsafe_allow_html=True)
