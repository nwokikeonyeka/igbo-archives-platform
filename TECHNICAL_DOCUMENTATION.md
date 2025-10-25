# Igbo Archives Platform

## Overview

Igbo Archives is a Django-based web platform dedicated to preserving and celebrating Igbo culture, history, and heritage. The platform serves as a comprehensive digital archive featuring cultural artifacts, community-generated insights, book reviews, and an AI-powered chat assistant. It replaces a previous WordPress site and is designed as a Progressive Web App (PWA) with modern features including dark mode, push notifications, and social authentication.

The platform emphasizes community engagement through threaded comments, user-contributed content, and moderation workflows while maintaining a clean, vintage-inspired aesthetic that reflects heritage photography and modern museum design principles.


## System Architecture

### Web Framework & Core Technology
- **Django 5.1+** as the primary web framework
- **Python 3.x** backend with standard Django project structure
- **Gunicorn** for production WSGI serving
- **Bootstrap 5.3** for responsive UI (CDN-based)
- **HTMX** for dynamic content loading without full page reloads

### Database Architecture
- **PostgreSQL** via Neon (cloud-hosted) for production
- **SQLite** for local development
- Django ORM for all database operations
- Migrations managed through Django's built-in system

### Authentication & User Management
- **django-allauth** for authentication handling
- Email-based signup/login (no username required)
- Google OAuth integration for social authentication
- Custom user model (`CustomUser`) extending Django's `AbstractUser`
- User profiles with bio, profile picture, and social links
- Built-in messaging system with threaded conversations

### Content Management Apps
The platform is organized into modular Django apps:

1. **Archives App**: Cultural artifacts, photos, documents, and historical materials
   - File uploads with validation (images, videos, documents)
   - Category and tag-based organization
   - Featured content support

2. **Insights App**: Community-generated articles and blog posts
   - Rich text editing via CKEditor 5
   - Two-stage publishing workflow (published + approved)
   - Edit suggestions from community members
   - Social media integration tracking

3. **Books App**: Book reviews related to Igbo culture
   - Star rating system (1-5)
   - ISBN tracking
   - Cover image uploads

4. **Academy App**: Educational content (marked as "Coming Soon")
   - Placeholder for future language learning features

5. **AI Service App**: Chat interface powered by Google Gemini
   - Real-time AI conversation about Igbo culture
   - HTMX-based chat interface

6. **Users App**: Profile management and messaging
   - Public user profiles
   - Private messaging with threads
   - Account deletion functionality

### Progressive Web App (PWA) Features
- **django-pwa** for PWA manifest and service worker
- Installable on mobile and desktop
- Offline caching strategy for static assets
- App icons and splash screens

### Push Notifications
- **django-push-notifications** for web push
- WebPush device management
- VAPID key-based authentication
- Subscription management API endpoints

### Comments System
- **django-threadedcomments** for nested discussions
- Guest commenting with reCAPTCHA protection
- Integration across archives, insights, and book reviews

### Rich Text Editing
- **django-ckeditor-5** for WYSIWYG content creation
- Configured for extended formatting options
- Consistent across insights and book reviews

### SEO & Discoverability
- **django-meta** for Open Graph and meta tags
- XML sitemap generation for all content types
- robots.txt with crawl directives
- IndexNow API integration for instant search engine notification

### Tagging System
- **django-taggit** for flexible content tagging
- Shared tags across archives, insights, and book reviews
- Tag-based filtering and discovery

### Security Features
- **django-recaptcha** for spam prevention (configurable)
- CSRF protection with Replit-specific trusted origins
- Environment variable-based configuration via python-dotenv
- Conditional reCAPTCHA (only when keys are configured)

### Backup Strategy
- **django-dbbackup** for automated backups
- Custom management command for scheduled backups
- Database and media file backup support
- Cleanup of old backups

### UI/UX Design
- Vintage-inspired color palette (sepia tones, heritage browns)
- Dark mode with localStorage persistence
- Mobile-first responsive design
- Minimal, museum-style aesthetic
- Custom CSS variables for theming

### Notification System
- **django-notifications-hq** for in-app notifications
- Signal-based notification triggers
- Notifications for messages, edit suggestions, etc.

## External Dependencies

### Third-Party APIs
- **Google Gemini API**: AI chat assistant functionality (free tier)
- **Google OAuth 2.0**: Social authentication ("Sign in with Google")
- **Google Analytics**: Site traffic tracking (gtag.js)
- **Google reCAPTCHA v2**: Spam prevention on forms
- **Firebase Cloud Messaging (FCM)**: Push notification delivery
- **Twitter/X API**: Automated social media posting (via Tweepy)
- **IndexNow API**: Search engine notification service

### Cloud Services
- **Neon Database**: Managed PostgreSQL hosting (free tier)
- **Oracle Cloud**: Infrastructure (planned for production VM)
- **Amazon S3 (boto3)**: Media file storage (configured but optional)

### Email Service
- **Brevo (formerly Sendinblue)**: Transactional email delivery
  - Password resets, account notifications
  - Newsletter to subscribers
  - 300 emails/day free tier

### CDN Resources
- **Bootstrap 5.3**: CSS framework
- **Font Awesome 6.4**: Icon library
- **Google Fonts**: Inter and Playfair Display typefaces
- **CKEditor 5**: Rich text editor assets

### Development Tools
- **python-dotenv**: Environment variable management
- **Pillow**: Image processing and uploads
- **psycopg2-binary**: PostgreSQL adapter
- **PyJWT & cryptography**: Token handling and security

### Key Configuration Notes
- All API keys managed via environment variables
- Graceful degradation when optional services unavailable (e.g., reCAPTCHA, VAPID keys)
- Debug mode configurable via environment
- CSRF trusted origins configured for Replit deployment
- Static files served via Django in development, Nginx planned for production
