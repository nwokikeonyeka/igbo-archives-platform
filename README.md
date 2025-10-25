# Igbo Archives Platform

**Preserving the Past, Inspiring the Future**

A comprehensive Django-based web platform for preserving and celebrating Igbo culture, history, and heritage. This platform replaces the previous WordPress site at [igboarchives.com.ng](https://igboarchives.com.ng) with a modern, feature-rich Django application.

## 🌟 Overview

Igbo Archives is a dedicated platform for preserving and celebrating the history and culture of the Igbo people. Our mission is to correct misconceptions and foster a deeper understanding of Igbo heritage, ensuring it is passed on to future generations.

## ✨ Key Features

### Core Functionality
- **Cultural Archives**: Curated collection of Igbo artifacts, photographs, documents, and historical materials
- **Insights**: Community-generated articles exploring various aspects of Igbo culture
- **Book Reviews**: Reviews and discussions of literature related to Igbo history and culture
- **AI Chat Assistant**: Powered by Google Gemini for exploring Igbo heritage
- **Academy** (Coming Soon): Educational resources for learning Igbo language and traditions

### Technical Features
- **Progressive Web App (PWA)**: Installable on mobile and desktop devices
- **Email-Based Authentication**: Secure signup/login with email and password (no username required)
- **Social Authentication**: Google OAuth integration for easy signup
- **ReCAPTCHA Protection**: Spam prevention on signup and login forms (configurable)
- **Push Notifications**: Web push notifications for user engagement
- **Threaded Comments**: Rich discussions with guest participation
- **Rich Text Editor**: CKEditor 5 for content creation
- **Dynamic Filtering**: HTMX-powered content filtering and sorting
- **SEO Optimized**: Meta tags, Open Graph, and XML sitemaps
- **Dark Mode**: User-toggleable dark/light theme
- **Responsive Design**: Mobile-first design with Bootstrap 5

## 📋 Project Structure

```
igbo-archives-platform/
├── academy/                    # Academy app (Coming Soon)
│   ├── templates/
│   ├── apps.py
│   ├── urls.py
│   └── views.py
│
├── ai_service/                 # AI Chat Service
│   ├── templates/ai_service/
│   │   └── chat.html
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── api/                        # API endpoints
│   ├── urls.py
│   └── views.py
│
├── archives/                   # Cultural Archives app
│   ├── migrations/
│   ├── templates/archives/
│   │   ├── partials/
│   │   │   ├── archive_grid.html
│   │   │   └── guest_comment_form.html
│   │   ├── create.html
│   │   ├── detail.html
│   │   ├── edit.html
│   │   └── list.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── books/                      # Book Reviews app
│   ├── migrations/
│   ├── templates/books/
│   │   ├── partials/
│   │   │   └── guest_comment_form.html
│   │   ├── create.html
│   │   ├── detail.html
│   │   ├── edit.html
│   │   └── list.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── core/                       # Core app with base templates
│   ├── management/
│   │   └── commands/
│   │       ├── backup_database.py
│   │       └── send_subscriber_emails.py
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   └── push-notifications.js
│   │   └── serviceworker.js
│   ├── templates/
│   │   ├── account/           # Django-allauth templates
│   │   │   ├── login.html
│   │   │   └── signup.html
│   │   ├── core/
│   │   │   ├── pages/
│   │   │   │   ├── about.html
│   │   │   │   ├── contact.html
│   │   │   │   ├── copyright.html
│   │   │   │   ├── privacy.html
│   │   │   │   └── terms.html
│   │   │   ├── donate.html
│   │   │   └── home.html
│   │   ├── base.html
│   │   └── robots.txt
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── indexnow.py
│   ├── models.py
│   ├── sitemaps.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── igbo_archives/              # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── insights/                   # User Insights app
│   ├── management/
│   │   └── commands/
│   │       ├── delete_old_drafts.py
│   │       └── post_to_twitter.py
│   ├── migrations/
│   ├── templates/insights/
│   │   ├── partials/
│   │   │   ├── guest_comment_form.html
│   │   │   └── insight_grid.html
│   │   ├── create.html
│   │   ├── detail.html
│   │   ├── edit.html
│   │   └── list.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── users/                      # User management app
│   ├── migrations/
│   ├── templates/users/
│   │   ├── compose.html
│   │   ├── dashboard.html
│   │   ├── delete_account.html
│   │   ├── inbox.html
│   │   ├── profile.html
│   │   ├── profile_edit.html
│   │   └── thread.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── backups/                    # Database backup storage
├── media/                      # User-uploaded media files
├── static/                     # Static assets (images, logos)
│   └── images/
│       └── logos/
│           ├── logo-dark.png
│           └── logo-light.png
├── staticfiles/                # Collected static files
│
├── db.sqlite3                  # SQLite database (development)
├── manage.py                   # Django management script
├── plan.md                     # Detailed development plan
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd igbo-archives-platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   # Django Settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   
   # Google OAuth (optional)
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   
   # reCAPTCHA (optional - works without keys in development)
   RECAPTCHA_PUBLIC_KEY=your-recaptcha-site-key
   RECAPTCHA_PRIVATE_KEY=your-recaptcha-secret-key
   
   # Google Gemini AI
   GEMINI_API_KEY=your-gemini-api-key
   
   # Firebase Cloud Messaging (for push notifications)
   FCM_SERVER_KEY=your-fcm-server-key
   VAPID_PUBLIC_KEY=your-vapid-public-key
   VAPID_PRIVATE_KEY=your-vapid-private-key
   
   # Email Settings (Brevo)
   BREVO_EMAIL_USER=your-brevo-email
   BREVO_API_KEY=your-brevo-api-key
   DEFAULT_FROM_EMAIL=noreply@igboarchives.com
   
   # Twitter/X API
   TWITTER_API_KEY=your-twitter-api-key
   TWITTER_API_SECRET=your-twitter-api-secret
   TWITTER_ACCESS_TOKEN=your-twitter-access-token
   TWITTER_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret
   
   # Google AdSense (optional)
   GOOGLE_ADSENSE_CLIENT_ID=your-adsense-client-id
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

8. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - Admin panel: `http://localhost:5000/admin`

## 🔧 Configuration

### Database

By default, the project uses SQLite for development. For production, configure PostgreSQL:

```python
# In settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

### Authentication

The platform uses email-based authentication:
- **Username field**: Hidden from users, auto-generated from email
- **Full name field**: Required during signup
- **Terms acceptance**: Users must agree to Terms of Service and Privacy Policy
- **reCAPTCHA**: Optional protection (works without keys in development)

### PWA Settings

Progressive Web App settings are configured in `settings.py`:
- App name, description, and theme colors
- Icons and splash screens
- Offline capabilities via service worker

## 📝 Key Models

### CustomUser (users/models.py)
- `full_name`: User's display name
- `bio`: User biography
- `profile_picture`: Profile image
- `social_links`: JSON field for social media links

### Archive (archives/models.py)
- Cultural artifacts with metadata
- Categories, tags, and image fields
- SEO-optimized with meta descriptions

### InsightPost (insights/models.py)
- User-generated articles
- Draft/published status
- Auto-deletion of old drafts
- Social media integration

### BookReview (books/models.py)
- Book reviews and discussions
- Rating system
- Author and publication details

## 🛠️ Management Commands

### Backup Database
```bash
python manage.py backup_database
```

### Delete Old Drafts (30+ days)
```bash
python manage.py delete_old_drafts
```

### Post to Twitter/X
```bash
python manage.py post_to_twitter
```

## 🔒 Security Features

- CSRF protection with trusted origins
- Password validation (minimum length, complexity)
- Secure session management
- reCAPTCHA on forms (configurable)
- Content Security Policy headers
- SQL injection protection via Django ORM

## 📱 Mobile Features

- Responsive design with mobile-first approach
- Fixed bottom navigation on mobile
- Mobile back button
- Touch-friendly interface
- PWA installation prompt

## 🎨 Theming

The platform supports dark/light mode toggle:
- User preference stored in localStorage
- Smooth transitions between themes
- Consistent color palette

## 🔍 SEO & Social

- XML sitemaps for all content types
- Open Graph tags for social sharing
- Twitter Card support
- Structured data with Schema.org
- robots.txt configuration
- IndexNow integration

## 📦 Dependencies

See `requirements.txt` for the complete list. Key dependencies:
- **Django 5.1+**: Web framework
- **django-allauth**: Authentication
- **django-ckeditor-5**: Rich text editor
- **django-htmx**: Dynamic interactions
- **django-pwa**: Progressive Web App
- **google-generativeai**: AI chat service
- **Pillow**: Image processing
- **boto3**: Cloud storage (backups)

## 🚢 Deployment

### Production Checklist

1. Set `DEBUG=False` in environment variables
2. Update `ALLOWED_HOSTS` with your domain
3. Configure `CSRF_TRUSTED_ORIGINS`
4. Set up PostgreSQL database
5. Configure static file serving (nginx/whitenoise)
6. Set up SSL certificate
7. Configure email backend (Brevo/SendGrid)
8. Set strong `SECRET_KEY`
9. Configure backup storage (Oracle Cloud/AWS S3)
10. Set up monitoring and logging

### Deployment Command
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port igbo_archives.wsgi:application
```

## 📄 License

See LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For inquiries, suggestions, or contributions:
- Website: [igboarchives.com.ng](https://igboarchives.com.ng)
- Email: contact@igboarchives.com

## 🙏 Acknowledgments

- All contributors to Igbo cultural preservation
- Museum collections providing historical photographs
- The Igbo community for their support and engagement

---

**Thank you for being a part of Igbo Archives. Together, we can ensure that the history and culture of the Igbo people are never forgotten.**
