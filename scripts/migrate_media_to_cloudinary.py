# scripts/migrate_media_to_cloudinary.py
import os
import sys
import django
from pathlib import Path
from django.conf import settings

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "handicraft.settings")
django.setup()

import cloudinary.uploader
from django.core.files.storage import default_storage
from django.db import transaction
from django.apps import apps

MEDIA_ROOT = Path(settings.MEDIA_ROOT)

# Example for Product model (adjust app_label.model_name)
Product = apps.get_model("products", "Product")

def upload_file_to_cloudinary(local_path, public_id=None, folder=None):
    try:
        res = cloudinary.uploader.upload(str(local_path), public_id=public_id, folder=folder)
        return res.get("secure_url")
    except Exception as e:
        print("Upload error:", e)
        return None

def migrate_files():
    # If your DB stores file path in ImageField on Product model:
    with transaction.atomic():
        for p in Product.objects.exclude(image="").iterator():
            file_path = p.image.name  # e.g. 'product/abc.jpg'
            local_file = MEDIA_ROOT / file_path
            if local_file.exists():
                print("Uploading", local_file)
                url = upload_file_to_cloudinary(local_file, public_id=file_path.rsplit(".",1)[0].replace("/", "_"), folder="migrated_media")
                if url:
                    # Option A: set field to cloudinary URL (if you want absolute)
                    # p.image = url  # if your ImageField accepts URL (usually it doesn't)
                    # Option B: keep ImageField but update to cloudinary path format used by your storage
                    # If you use cloudinary_storage as DEFAULT_FILE_STORAGE, re-saving via field will use Cloudinary
                    with open(local_file, "rb") as f:
                        p.image.save(os.path.basename(local_file), f, save=True)
                    print("Saved for", p.pk)
            else:
                print("Local file not found:", local_file)

if __name__ == "__main__":
    migrate_files()
