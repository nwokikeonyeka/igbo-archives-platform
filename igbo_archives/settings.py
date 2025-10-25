"""
Django settings for igbo_archives project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-#9&(g6-t9vq8fmhh@l$ipieejrsh^ubecn(advzg$_5i_=n$99')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# CSRF Settings for Replit and Render
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', 'https://*.replit.dev,https://*.repl.co,https://*.onrender.com').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    'django_comments',
    'threadedcomments',
    'taggit',
    'django_htmx',
    'pwa',
    'meta',
    'django_recaptcha',
    'dbbackup',
    'push_notifications',
    'django_ckeditor_5',
    
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
    'archives.apps.ArchivesConfig',
    'insights.apps.InsightsConfig',
    'books.apps.BooksConfig',
    'ai_service.apps.AiServiceConfig',
    'academy.apps.AcademyConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'igbo_archives.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'core.context_processors.pwa_settings',
                'core.context_processors.monetization_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'igbo_archives.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Disable email verification for development
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
    'login': 'users.forms.CustomLoginForm',
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID', ''),
            'secret': os.getenv('GOOGLE_CLIENT_SECRET', ''),
            'key': ''
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}

PWA_APP_NAME = 'Igbo Archives'
PWA_APP_DESCRIPTION = 'Preserving the Past, Inspiring the Future'
PWA_APP_THEME_COLOR = '#3D2817'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/logos/logo-light.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/logos/logo-light.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/logos/logo-light.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY', '')

PUSH_NOTIFICATIONS_SETTINGS = {
    "FCM_API_KEY": os.getenv('FCM_SERVER_KEY', ''),
    "WP_PRIVATE_KEY": os.getenv('WEBPUSH_PRIVATE_KEY', ''),
    "WP_CLAIMS": {"sub": "mailto:contact@igboarchives.com"}
}

DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True,
    'SOFT_DELETE': True
}

COMMENTS_APP = 'threadedcomments'

customColorPalette = [
    {'color': 'hsl(4, 90%, 58%)', 'label': 'Red'},
    {'color': 'hsl(340, 82%, 52%)', 'label': 'Pink'},
    {'color': 'hsl(291, 64%, 42%)', 'label': 'Purple'},
    {'color': 'hsl(262, 52%, 47%)', 'label': 'Deep Purple'},
    {'color': 'hsl(231, 48%, 48%)', 'label': 'Indigo'},
    {'color': 'hsl(207, 90%, 54%)', 'label': 'Blue'},
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'],
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backups'}

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', '')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET', '')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', '')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', '')

# Email Configuration
# Use console backend for development if no credentials are provided
if os.getenv('BREVO_EMAIL_USER') and os.getenv('BREVO_API_KEY'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp-relay.brevo.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv('BREVO_EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.getenv('BREVO_API_KEY')
else:
    # Console backend for development - emails print to console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'noreply@igboarchives.com')

# Push Notifications Configuration
PUSH_NOTIFICATIONS_SETTINGS = {
    'WNS_PACKAGE_SECURITY_ID': os.getenv('WNS_PACKAGE_SECURITY_ID'),
    'WNS_SECRET_KEY': os.getenv('WNS_SECRET_KEY'),
    'GCM_API_KEY': os.getenv('FCM_SERVER_KEY'),  # Firebase Cloud Messaging
    'APNS_CERTIFICATE': os.getenv('APNS_CERTIFICATE'),
    'APNS_TOPIC': os.getenv('APNS_TOPIC'),
    'WP_PRIVATE_KEY': os.getenv('VAPID_PRIVATE_KEY'),
    'WP_CLAIMS': {
        'sub': 'mailto:admin@igboarchives.com'
    }
}

# VAPID Keys for Web Push (set these in environment variables)
VAPID_PUBLIC_KEY = os.getenv('VAPID_PUBLIC_KEY', '')
VAPID_PRIVATE_KEY = os.getenv('VAPID_PRIVATE_KEY', '')

# ============================================
# SEO CONFIGURATION (django-meta)
# ============================================
META_SITE_PROTOCOL = 'https'
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_SCHEMAORG_PROPERTIES = True
META_SITE_TYPE = 'website'
META_SITE_NAME = 'Igbo Archives'
META_DEFAULT_KEYWORDS = ['Igbo culture', 'Nigerian heritage', 'Igbo history', 'cultural preservation', 'Igbo language', 'African culture']
META_INCLUDE_KEYWORDS = ['Igbo', 'archives', 'cultural', 'heritage', 'history']
META_DEFAULT_IMAGE = '/static/images/logos/og-image.png'
META_IMAGE_URL = '/static/images/logos/og-image.png'
META_USE_SITES = True
META_OG_NAMESPACES = ['og', 'fb']

# ============================================
# DATABASE BACKUP CONFIGURATION (django-dbbackup)
# ============================================
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backups'}
DBBACKUP_CLEANUP_KEEP = 10
DBBACKUP_CLEANUP_KEEP_MEDIA = 10
DBBACKUP_DATE_FORMAT = '%Y-%m-%d-%H-%M-%S'
DBBACKUP_FILENAME_TEMPLATE = 'igbo-archives-{datetime}.{extension}'
DBBACKUP_MEDIA_FILENAME_TEMPLATE = 'igbo-archives-media-{datetime}.{extension}'

# ============================================
# MONETIZATION SETTINGS
# ============================================
# Google AdSense
GOOGLE_ADSENSE_CLIENT_ID = os.getenv('GOOGLE_ADSENSE_CLIENT_ID', '')
ENABLE_ADSENSE = bool(GOOGLE_ADSENSE_CLIENT_ID)

# Donation Settings
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
ENABLE_DONATIONS = bool(STRIPE_SECRET_KEY)

# ============================================
# INDEXNOW CONFIGURATION
# ============================================
INDEXNOW_API_KEY = os.getenv('INDEXNOW_API_KEY', '')
