# Product Segmentation Django Project

This is a skeleton Django project `productsegmentation` with a simple app `segmentation` that demonstrates dynamic segmentation of products by price and size.

## Setup (recommended - conda)
1. Create environment:
   ```bash
   conda env create -f environment.yml
   conda activate productseg
   ```
2. Install via pip (optional):
   ```bash
   pip install -r requirements.txt
   ```

## Initialize & run
1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Load sample products:
   ```bash
   python manage.py loaddata fixtures/products.json
   ```
3. Run server:
   ```bash
   python manage.py runserver
   ```
4. Visit `http://127.0.0.1:8000/` to see the products and segmentation UI.

## Notes
- Uses SQLite by default for simplicity.
- `fixtures/products.json` contains 30 sample products.
- The `segmentation` app has a simple `Product` model and views showing segmented lists by price and size.
