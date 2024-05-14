from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
HARDRADA_BASE_DIR = Path(__file__).resolve().parent.parent

HARDRADA_TEMPLATES = [
    HARDRADA_BASE_DIR  / 'templates'
]

HARDRADA_STATICFILES_DIRS = [
    HARDRADA_BASE_DIR / 'staticfiles'
]
