# Igbo Archives Platform

## Overview

Igbo Archives is a Django-based cultural preservation platform dedicated to preserving and celebrating Igbo history, culture, and heritage. The platform serves as a comprehensive digital archive featuring curated artifacts, community-generated insights, book reviews, and educational resources. Built with Django 4.2.17 (downgraded from 5.1 for django-notifications-hq compatibility), the application emphasizes progressive web capabilities, community engagement, and content moderation workflows.

## Recent Changes

**October 27, 2025 - Phase 5 Completion & Grid/List View Fix**

*Phase 5: Account & Secondary UX Polish*
- Dashboard fully functional with all user data tabs (Messages, Insights, Drafts, Book Reviews, Archives, Edit Suggestions, Notifications)
- Full name display standardized across all templates using `get_display_name()` method with profile links
- Delete account relocated to Edit Profile page under "Danger Zone" section
- Password change/reset enabled for both email and Google OAuth users
- Instant logout implemented (removed confirmation page, set ACCOUNT_LOGOUT_ON_GET = True)
- Donate page simplified to single "Support Our Mission" section with ENABLE_DONATIONS guard restored
- Dashboard "My Insights" tab now shows both published AND pending posts using Q filters
- Comment templates updated to display full names with profile links

*Grid/List View Toggle Fix (Phase 2 Audit)*
- Fixed archives list view by removing Bootstrap `.col` wrappers from archive_grid.html partial
- Added proper `.archive-view-list` container styles with flexbox layout in style.css
- Updated pagination to use `grid-column: 1 / -1` for full-width spanning in both grid and list views
- Added `flex-shrink: 0` to images in list view to prevent distortion
- View toggle now properly switches between grid (responsive CSS Grid) and list (horizontal flex cards) layouts

*Django Version Update*
- Downgraded from Django 5.1 to Django 4.2.17 due to django-notifications-hq incompatibility with deprecated `index_together` Meta attribute
- Added 'notifications' app to INSTALLED_APPS in settings.py

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Web Framework & Application Structure

**Django Monolith Architecture**: The application follows a Django apps-based modular structure with distinct functional boundaries:

- **Core App**: Houses shared utilities, static pages (about, contact, legal), context processors, sitemap generation, and IndexNow SEO integration
- **Users App**: Custom user authentication extending Django's AbstractUser, messaging system, notifications management, and admin moderation workflows
- **Archives App**: Media upload and management system supporting images, videos, documents, and audio files with category-based organization
- **Insights App**: Blog-style content creation with rich text editing, collaborative edit suggestions, and approval workflows
- **Books App**: Book review system with ratings, rich content, and publication management
- **Academy App**: Placeholder for future educational content (currently displays coming soon page)
- **API App**: REST-style endpoints for AJAX operations, push notifications, and media browsing

**Rationale**: Django's app-based architecture provides clean separation of concerns while maintaining shared infrastructure (ORM, authentication, admin). This approach balances modularity with simplicity, avoiding microservices complexity while remaining maintainable.

### Authentication & User Management

**Email-First Authentication**: Implemented via django-allauth with username field removed from signup forms. Users authenticate with email and password, with optional Google OAuth integration.

**Custom User Model**: Extends AbstractUser with additional fields (full_name, bio, profile_picture, social_links as JSONField). The USERNAME_FIELD remains 'username' internally but users provide email during signup which auto-generates username.

**ReCAPTCHA Protection**: Conditionally enabled based on environment configuration. When RECAPTCHA keys are absent, forms degrade gracefully without captcha validation.

**Rationale**: Email authentication reduces friction for users who struggle to remember usernames. django-allauth provides battle-tested social auth while maintaining flexibility. Conditional ReCAPTCHA allows local development without external dependencies.

### Content Management & Moderation

**Three-State Publishing Workflow**:
1. **Draft**: User saves progress without submission (is_published=False, pending_approval=False)
2. **Pending**: User submits for review (pending_approval=True, is_approved=False)
3. **Published**: Admin approves (is_published=True, is_approved=True)

**Collaborative Edit Suggestions**: Users can suggest edits to published insights. Authors receive notifications and can approve/reject suggestions through their dashboard.

**Content Approval System**: Staff members access moderation dashboard to review pending insights and book reviews, with notification system alerting authors of approval/rejection decisions.

**Rationale**: Moderation prevents spam and maintains content quality. Draft state enables users to work iteratively. Edit suggestions foster community collaboration while preserving author control.

### Rich Text Editing

**Quill.js Implementation**: Selected as the primary rich text editor after evaluating CKEditor 5, Editor.js, and TinyMCE.

**Content Storage**: Dual-field approach with `content_json` (EditorJsJSONField for future migration) and `legacy_content` (TextField for backward compatibility). Currently uses HTML storage with Quill.

**Image Upload Integration**: Custom `/api/upload-image/` endpoint handles inline image uploads during content creation.

**Rationale**: Quill.js chosen for zero-cost, no-API-key operation with WordPress-like UX. Dual storage fields future-proof the application for potential editor migrations while maintaining existing content.

### Media Management

**Type-Specific Upload Validation**: Archives support four media types (image, video, document, audio) with different file size limits and extension validators:
- Images: 2-5MB, JPEG/PNG/WebP
- Videos: max 50MB, MP4/WebM/AVI
- Documents: 2-5MB, PDF/DOCX
- Audio: 2-5MB, MP3/WAV/OGG

**Featured Images**: Video and audio archives can have optional thumbnail images for display purposes.

**Metadata Fields**: Archives include caption, alt_text, location, date_created, and circa_date for detailed historical documentation.

**Rationale**: File size constraints balance quality with storage/bandwidth costs. Type-specific validation prevents inappropriate uploads. Minimum size requirements (2MB) ensure quality submissions while maximum limits prevent abuse.

### Progressive Web App (PWA)

**django-pwa Integration**: Manifest generation, service worker registration, and offline capability scaffolding.

**Install Prompt**: Custom install button appears on beforeinstallprompt event, allowing users to add the platform to their home screens.

**Service Worker Caching**: Basic cache-first strategy for static assets (CSS, JS, logos) with network fallback.

**Rationale**: PWA capabilities enable mobile-first experience with app-like behavior. Offline support improves accessibility in low-connectivity environments. django-pwa handles manifest boilerplate automatically.

### Real-Time Interactivity

**HTMX Integration**: Powers dynamic filtering, sorting, and pagination without full page reloads. Filter changes trigger partial template updates via `hx-get` attributes.

**View/Layout Toggle**: JavaScript-based grid/list view toggle with localStorage persistence across archives, insights, and books sections.

**Push Notifications**: Web Push API integration via django-push-notifications with VAPID keys for authenticated messages (configuration required for production).

**Rationale**: HTMX provides SPA-like interactivity without complex JavaScript frameworks. Server-side rendering maintains SEO benefits. Push notifications enable re-engagement without email dependency.

### Dark Mode Implementation

**CSS Variables + localStorage**: Theme switching implemented via body class toggle with CSS custom properties for color values. User preference persists across sessions.

**Vintage Color Palette**: Heritage-inspired sepia tones, aged parchment colors, and antique cream shades appropriate for cultural preservation context.

**Rationale**: Dark mode reduces eye strain and battery usage. CSS variables enable maintainable theming. Vintage aesthetic aligns with archival/historical content nature.

### SEO & Discoverability

**Django Meta Integration**: Open Graph tags, Twitter Cards, and structured metadata for social sharing.

**XML Sitemaps**: Automated sitemap generation for static pages, archives, insights, books, and user profiles via django.contrib.sitemaps.

**IndexNow API**: Real-time search engine notification when content is published (custom implementation in core/indexnow.py).

**robots.txt**: Dynamic generation allowing public content while protecting private routes (admin, user dashboards, API endpoints).

**Rationale**: Comprehensive SEO strategy maximizes organic discovery. IndexNow provides faster indexing than traditional sitemaps. Structured data improves rich snippet eligibility.

### Comments & Community Engagement

**Threaded Comments**: django-threadedcomments enables nested discussion with guest participation support.

**Messaging System**: Private thread-based messaging between users with read/unread status tracking.

**Notification System**: django-notifications-hq for in-app alerts on comments, messages, edit suggestions, and moderation actions. Custom utility functions in core/notifications_utils.py handle email notifications.

**Rationale**: Threaded comments enable nuanced discussions. Private messaging fosters community connections. Multi-channel notifications (in-app + email) ensure users stay informed.

### Tagging & Categorization

**django-taggit**: Provides flexible tagging across archives, insights, and book reviews with comma-separated input.

**Archive Categories**: Hierarchical category system with slug-based URLs and optional descriptions.

**Rationale**: Tags enable organic discovery patterns while categories provide structured navigation. django-taggit handles tag normalization and relationships efficiently.

## External Dependencies

### Database

**PostgreSQL**: Primary data store via psycopg2-binary adapter. Settings configured for Render's managed Postgres service.

**Deployment Note**: Application designed for Postgres but Django ORM abstracts database specifics. SQLite works for local development.

### Cloud Services (Optional/Configurable)

**Google OAuth**: Social authentication via allauth.socialaccount.providers.google (requires client ID/secret configuration).

**Google reCAPTCHA**: Spam protection via django-recaptcha (conditionally loaded when keys present in settings).

**Google Analytics**: GA4 tracking code embedded in base template (G-HNZ18KM0B8, AW-16576124028).

**Google AdSense**: Conditional ad placement when ENABLE_ADSENSE setting is true.

**Google Gemini AI**: Future AI chat integration via google-generativeai library (ai_service app references removed but external link preserved in navigation).

### Third-Party Python Packages

**Authentication & Authorization**:
- django-allauth: Social and email authentication
- PyJWT, cryptography: Token handling for OAuth

**Content Management**:
- django-editorjs-fields: Block-based editor field types (currently unused but installed)
- Pillow: Image processing and validation

**Community Features**:
- django-threadedcomments: Nested comment threading
- django-notifications-hq: In-app notification system
- django-push-notifications: Web push notification backend

**SEO & Discovery**:
- django-meta: Meta tag generation
- django-taggit: Tagging functionality

**Utilities**:
- django-htmx: HTMX integration helpers
- django-pwa: PWA manifest and service worker
- django-recaptcha: reCAPTCHA validation
- django-dbbackup: Database backup management
- python-dotenv: Environment variable loading

**Social Media (Future)**:
- tweepy: Twitter API integration (referenced in settings but not actively used)

### Static Assets & CDN

**Bootstrap 5.3.0**: Frontend framework via CDN
**Font Awesome 6.4.0**: Icon library via CDN
**Google Fonts**: Inter (body), Playfair Display (headings)
**Quill.js**: Rich text editor loaded via CDN

### Hosting & Deployment

**Render**: Configured for deployment with Gunicorn WSGI server. CSRF_TRUSTED_ORIGINS includes Render and Replit domains.

**Static/Media Files**: Django's default storage backend (filesystem). DEBUG=False requires collectstatic for production.

**Environment Variables**: Managed via .env file (python-dotenv) including SECRET_KEY, DEBUG, ALLOWED_HOSTS, database credentials, API keys.

### Future/Planned Dependencies

**AWS S3**: boto3 package installed for potential media storage migration (not currently configured).

**Stripe**: STRIPE_PUBLIC_KEY setting suggests future donation/payment integration (ENABLE_DONATIONS flag in settings).

**Social Automation**: Twitter posting automation logic present in insights/signals.py but requires API credentials and activation.