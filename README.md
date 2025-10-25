# Igbo Archives: Platform Development Plan (v8 - Definitive)

**Project:** Igbo Archives (Web Platform)

**Author:** Onyeka Nwokike 

**Vision:** To build the definitive, "best-in-class" web platform for Igbo cultural preservation and community engagement. This plan (v8) is the final, pragmatic blueprint for launching a feature-rich MVP within 3-5 months, balancing the full vision with achievable scope and maximum stability for a solo developer.

**Core Principle:** 100% free and feasible. Prioritizes core features, modularity, stability, and minimal necessary dependencies. Relies on familiar and manageable technologies.

---

## Phase 0: Pre-Development and Environment Setup (2-3 Days)
**Goal:** Establish the complete development and deployment environment, secure all assets, migrate initial data, and finalize the core technology stack decisions. This foundational phase ensures all prerequisites are met before coding begins, preventing mid-project roadblocks.

### Sub-Steps

**Account & Tool Setup:**
* **Oracle Cloud:** Utilize the existing "Always Free" account.
* **VM Allocation:** Provision two `VM.Standard.A1.Flex` instances as planned: VM1 (AI Server: 2 OCPU, 12GB RAM) and VM2 (Platform Server: 1 OCPU, 6GB RAM). This plan focuses on deploying the platform to VM2. *Rationale: Separates concerns; 6GB RAM is sufficient for this Django platform.*
* **Neon Database:** Create a new, free PostgreSQL project specifically for Igbo Archives within your existing Neon account. Securely save the database connection string. *Rationale: Leverages your familiarity, provides a free managed database, and allows multiple free projects per account.*
* **GitHub Repository:** Create the `igbo-archives-platform` repository. Initialize with a `README`, Python `.gitignore`, and basic project structure ideas. *Rationale: Essential for version control and tracking progress.*
* **API Keys & Credentials:** Securely obtain and prepare to store (using `python-dotenv`) keys/tokens for essential services:
    * **Google AI Studio (Gemini API Key - Free Tier).** *Rationale: Powers the initial AI Chat Service.*
    * **Google Firebase Cloud Messaging (FCM Server Key - Free).** *Rationale: Enables Web Push Notifications.*
    * **Google reCAPTCHA (v2 Site/Secret Keys - Free).** *Rationale: Protects guest comments from spam.*
    * **Brevo (API Key - Free Tier, 300 emails/day).** *Rationale: Handles transactional emails (password reset, etc.) and subscriber notifications.*
    * **Twitter/X API (Developer App Keys/Tokens - Free).** *Rationale: Enables automated posting to X/Twitter.*
    * **Google OAuth 2.0 (Client ID/Secret - Free).** *Rationale: Enables "Sign in with Google".*
    * **Google Colab:** Keep available for running one-off data migration or processing scripts. *Rationale: Free compute for specific tasks.*

**Oracle VM Server (Platform - 6GB) Preparation:**
* SSH into VM2: `ssh -i <key.pem> ubuntu@<VM_IP>`
* Update & Install Baseline Software: `sudo apt update && sudo apt install python3-pip python3-venv nginx -y`. *Rationale: Installs essential tools for running Python web applications and serving traffic.*

**Data Migration (WordPress):**
* Export all content from the WordPress blog to an XML file.
* **Script (Colab):** Write and run a Python script (using `xml.etree.ElementTree`) to parse the XML. Extract posts (title, content, date, author, original URL/slug), image URLs, and categories/tags. Save this structured data into a `migration_data.json` file. *Rationale: Preserves existing content and URL structure, crucial for SEO redirects.*

**Technology Stack & Dependencies Planning:**
* **Core:** Django (latest stable version), Gunicorn (production WSGI server).
* **Database:** PostgreSQL (via Neon in production), SQLite (development). A Python adapter like `psycopg2-binary` will be needed.
* **Frontend:** HTML, CSS (Bootstrap 5.3 via CDN), JavaScript (minimal vanilla JS, potentially HTMX for dynamic interactions).
* **Key Django Packages:** Plan to install packages for: Authentication (`django-allauth`), Rich Text Editing (`django-ckeditor-5`), Threaded Comments (`django-threadedcomments`), In-App Notifications (`django-notifications-hq`), Push Notifications (`django-push-notifications`), PWA (`django-pwa`), SEO Meta Tags (`django-meta`), Form Spam Protection (`django-recaptcha`), Database Backups (`django-dbbackup`), Image Handling (`Pillow`), Environment Variables (`python-dotenv`), and API clients (`google-generativeai`, `tweepy`). *Rationale: Selects stable, well-maintained packages covering essential features while avoiding overly complex or niche dependencies for the MVP. Note: The exact list will be built in `requirements.txt` during development.*

**Testing Setup:**
* Plan to use Django's built-in testing framework (unittest or `pytest`). Install `coverage` for monitoring test coverage. *Rationale: Establishes a process for ensuring code quality and reliability.*

**Dependencies:** None.
**Output:** A fully provisioned server, a ready database, an initialized code repository, migrated WordPress data, and a clear plan for the technology stack.
**Testing:** Verify Neon DB connection string works from your local machine. Ensure VM is accessible via SSH.

---

## Phase 1: Foundation & Core Structure (4-6 Days)
**Goal:** Build the core Django project, establish the modular app structure, implement PWA capabilities, and set up the responsive user interface framework with all navigation elements.

### Sub-Steps

**Project Initialization:**
* On your local machine, initialize the Django project: `django-admin startproject igbo_archives .`
* Create the initial modular apps: `core` (for base templates, static files, core utilities), `users` (for user models, auth, profiles), `archives` (for cultural artifact models/views), `insights` (for user-generated post models/views), `books` (for book review models/views), `ai_service` (for the AI chat feature). Add these apps to `INSTALLED_APPS` in `settings.py`. *Rationale: Organizes the project logically from the start.*

**Database Configuration (settings.py):**
* Configure the `DATABASES` setting. Use `python-dotenv` to load the Neon `DATABASE_URL` in production environments, defaulting to a simple SQLite configuration for local development.
* Run initial migrations: `python manage.py makemigrations && python manage.py migrate`. *Rationale: Sets up the database schema based on Django's built-in apps.*

**PWA & UI Framework (core app):**
* Integrate `django-pwa`. Add `pwa` to `INSTALLED_APPS`. Configure necessary `PWA` settings in `settings.py` (App name, icons, theme color, etc.).
* Create `base.html` in `core/templates/`. Link the Bootstrap 5.3 CSS and JS via CDN. Define standard blocks (`{% block content %}`, `{% block scripts %}`).
* **Responsive Navigation:** Implement two distinct navigation bars in `base.html`:
    * **Desktop Header:** A standard Bootstrap navbar (`<nav class="navbar ... d-none d-md-block">`) with text links (Archives, Insights, Books, Notifications Bell, User Menu, AI Service).
    * **Mobile:** A fixed-bottom navbar (`<nav class="... d-md-none">`) with icons for key sections. Include a placeholder link/modal trigger for "Academy (Coming Soon)" like on mobile the app should feel like a mobile app, the default is archives there should be insights, books, Academy, AI like the core sections of the platform, others should be under profile icon drop down at top right.
* **Conditional Sub-Navigation:** Design a placeholder area (e.g., a specific `div`) where context-specific sub-navigation (like archive filters) can be loaded dynamically or included via template inheritance.
* **Mobile Back Button:** Add a simple JS-powered back button (`<button onclick="history.back()">Back</button>`) styled appropriately and displayed only on mobile views (`d-md-none`).
* **Night Mode Toggle:** Implement a JS toggle button that adds/removes a `dark-mode` class on the `<body>` and stores the preference in `localStorage`. Define basic dark mode styles in your CSS.
* Create the `manifest.json` and a basic `serviceworker.js` (for caching static assets) in `core/static/`, linked correctly in `base.html` and configured via `django-pwa`. *Rationale: Establishes the visual foundation, core navigation, and installable app behavior.*

**Sticky PWA Install Button:**
* Add the small, fixed-position button HTML element to `base.html`.
* Write JavaScript to listen for the `beforeinstallprompt` event. When fired, prevent the default prompt, store the event object, and make your custom button visible. Add an event listener to your button that, when clicked, calls `event.prompt()` and then hides the button. *Rationale: Provides a user-friendly way to encourage PWA installation.*

**Dependencies:** Phase 0.
**Output:** A running Django skeleton application, installable as a PWA, with responsive base templates and navigation structure in place.
**Testing:** Verify the site runs locally. Test PWA installation prompt on a compatible browser/device. Check that desktop and mobile navigation render correctly and responsively.

---

## Phase 2: User System & Core Community Features (7-10 Days)
**Goal:** Implement a secure and functional user system, including authentication (Google/Email), user profiles, dashboards, native private messaging, and essential notification channels (in-app & push).

### Sub-Steps

**Authentication (django-allauth in users app):**
* Integrate `django-allauth` fully. Configure required settings (backends, site ID, email verification, redirect URLs). Add Google provider credentials from `.env`.
* Customize `allauth` templates (`account/login.html`, `account/signup.html`, etc.) to match the site's Bootstrap theme.
* Ensure password reset functionality works via `allauth`'s built-in views.
* Create a custom view/form for authenticated users to delete their account, requiring password confirmation for security. *Rationale: Provides comprehensive and secure authentication.*

**Custom User Model & Profiles (users app):**
* Define the `CustomUser` model extending `AbstractUser`. Include fields like `full_name`, `bio`, `profile_picture` (using `ImageField` with size/type validation), and `social_links` (using `JSONField`).
* Set `AUTH_USER_MODEL = 'users.CustomUser'`. Create and run migrations for the `users` app.
* **Views:**
    * **Public Profile (`/profile/<username>/`):** Create a view and template that displays user details attractively. Include a button using JavaScript (`navigator.clipboard.writeText`) to copy the profile URL.
    * **Private Edit Profile (`/profile/edit/`):** Create a view using `UpdateView` and a `ModelForm` for users to modify their profile information. *Rationale: Establishes user identity and allows personalization.*

**User Dashboard (users app):**
* Create a dashboard view restricted to logged-in users (`@login_required` or `LoginRequiredMixin`).
* Use Bootstrap tabs in the template to create sections for managing user-specific content: "My Insights," "My Drafts," "Edit Suggestions Received," "My Book Reviews," "My Messages," "My Notifications." *Rationale: Provides a central hub for user activity.*

**Private Messaging (Native users app):**
* Implement the `Thread` and `Message` models within the `users` app as previously designed (linking participants, tracking updates, storing message content).
* Create views for: displaying the inbox (list of threads), viewing a specific thread (messages), and composing a new message (potentially initiated from a user's profile page). Use Django forms for message composition. *Rationale: Builds essential community interaction features natively.*

**In-App Notifications (django-notifications-hq):**
* Integrate the package. Run its migrations.
* Identify key events (new comment, post approval, new message) and implement signal receivers (`@receiver`) that call `notify.send(...)` with appropriate actors, recipients, verbs, and targets.
* Add the necessary template tags/includes from the package to `base.html` to display the notification count and dropdown list. *Rationale: Provides immediate on-site feedback.*

**Web Push Notifications (django-push-notifications):**
* Configure the package with FCM credentials from `.env`. Run its migrations.
* **Frontend Logic:** Write JavaScript to: check for service worker support, request notification permission from the user, register the service worker, get the push subscription object, and send this subscription data to a dedicated Django backend view.
* **Backend Logic:** Create a view to receive the subscription data and create/update `GCMDevice` or `WebPushDevice` records associated with the logged-in user.
* **Sending Logic:** Enhance the signal receivers from the previous step. After calling `notify.send(...)`, query for active push devices linked to the recipient user and use `devices.send_message(...)` to dispatch the push notification. *Rationale: Enables real-time engagement even when the user is offline.*

**Dependencies:** Phase 1.
**Output:** A fully functional user system: signup, login (Google/Email), profile viewing/editing, dashboard, private messaging, and working in-app and push notifications.
**Testing:** Test all authentication flows (signup, login, password reset, Google sign-in, account deletion). Verify profile updates. Send and receive private messages. Trigger events that should create in-app and push notifications and confirm they are received.

---

## Phase 3: Core Content & Interaction Apps (10-14 Days)
**Goal:** Build the main content sections (Archives, Insights, Books) using the chosen editor, implement dynamic filtering and views, enable threaded discussions with guest participation, and add collaborative editing features.

### Sub-Steps

**Content Models (Refinement):**
* Finalize the `Archive`, `InsightPost`, and `BookReview` models in their respective apps. Ensure all necessary fields are present (including required metadata like `alt_text`, image constraints via validators like `FileExtensionValidator` and custom size validators). Use `ForeignKey` for categories and integrate a tagging solution like `django-taggit` by adding `TaggableManager()` to relevant models. *Rationale: Defines the structure for all primary content.*

**Rich Text Editor (django-ckeditor-5):**
* Integrate `django-ckeditor-5`. Add `ckeditor_5` to `INSTALLED_APPS`.
* Configure `CKEDITOR_5_CONFIGS` in `settings.py` to customize the toolbar and potentially enable image uploading features (requires `django-ckeditor-5[uploader]` and further configuration for handling uploads, including capturing alt text).
* Replace standard `TextField` with `CKEditor5Field` in your `InsightPost` and `BookReview` models and corresponding forms. *Rationale: Provides a stable and familiar rich text editing experience.*

**Views & UI (archives, insights, books apps):**
* **Archives List View (Home):** Implement the view. Use Django's ORM to fetch featured items for the Bootstrap Carousel. Fetch paginated items for the main grid display below. Add context variables for categories/tags/types to populate filter controls.
* **Filtering/Sorting:** Implement `django-htmx`. Create dedicated views that accept filter parameters (e.g., `?category=masks&type=image`), query the database accordingly, and return only the HTML fragment for the updated content grid (`render_to_string` with a partial template). Use `hx-get`, `hx-target`, `hx-push-url="true"` (to update browser history) attributes on filter links/buttons.
* **Grid/List Toggle:** Implement simple JavaScript functions triggered by buttons to add/remove CSS classes (e.g., `grid-view`, `list-view`) on the main content container, with corresponding CSS rules to change the layout.
* **Detail Views:** Create standard Django `DetailViews` for each content type.
* **Create/Update Views:** Use Django's `CreateView` and `UpdateView`. Ensure forms correctly handle the CKEditor field and any associated image uploads with required metadata.

**"Tiny Buttons" Implementation:**
* **"Write Post with This":** Add the link in the `archive_detail.html` template. Modify the `InsightCreateView`'s `get_initial` method to check for `self.request.GET.get('archive_id')` and pre-populate relevant form fields or context.
* **"Suggest Edit":** Add the button/modal trigger in `insight_detail.html`. Create a simple Django form (`SuggestionForm`) and a view that handles the `POST` request from the modal, creating an `EditSuggestion` object linked to the post and the (optional) suggesting user. Notify the post author (via in-app/push notification). Add a section in the author's dashboard to view and approve/reject suggestions. *Rationale: Builds the core content display and creation workflows with requested interactive elements.*

**Threaded Discussions (django-threadedcomments):**
* Integrate `django-threadedcomments` by adding the necessary apps (`threadedcomments`, `django_comments`) to `INSTALLED_APPS`. Run migrations.
* Attach the generic relation for comments to your `InsightPost`, `Archive`, and `BookReview` models.
* Include the required template tags (`render_comment_list`, `get_comment_form`) in the detail templates for these models. *Rationale: Enables nested conversations under content.*

**Guest Comments with Spam Protection:**
* Integrate `django-recaptcha`. Add `captcha` to `INSTALLED_APPS` and configure keys in `settings.py`.
* Create a `GuestThreadedCommentForm` inheriting from the default `ThreadedCommentForm` and adding a `ReCaptchaField`.
* Modify the template context or view logic to pass this `GuestThreadedCommentForm` when `request.user.is_anonymous`, otherwise pass the standard form. *Rationale: Allows broader participation while managing spam.*

**Draft Auto-Delete (insights app):**
* Create the `delete_old_drafts` management command as specified previously.
* **Automation (Cron Job):** Schedule this command to run daily on the Oracle VM using `cron`. *Rationale: Automates database cleanup.*

**Dependencies:** Phase 2.
**Output:** Functional content sections (Archives, Insights, Books) with rich text editing, dynamic filtering, threaded comments (including guests), and edit suggestion workflow.
**Testing:** Thoroughly test creating/editing posts, ensuring editor features and image uploads (with metadata) work. Verify comment threading and guest commenting with reCAPTCHA. Test archive filtering/sorting via HTMX. Confirm draft auto-deletion works.

---

## Phase 4: AI & Automation (5-7 Days)
**Goal:** Integrate the Gemini AI chat service and automate content distribution to X/Twitter and email subscribers.

### Sub-Steps

**AI Chat Service (ai_service app):**
* Develop the Django view to handle `POST` requests from the chat interface.
* **Frontend:** Create the HTML template for the chat UI. Use `django-htmx` attributes on the input form (`hx-post`, `hx-target="#chat-log"`, `hx-swap="beforeend"`).
* **Backend:** The view receives the user's message, calls the Gemini API using the `google-generativeai` library, potentially adds context or system prompts, receives the response, and renders a partial template containing both the user message and the AI response to be swapped into the chat log by HTMX. Implement basic error handling for API calls. *Rationale: Provides the initial AI assistant feature.*

**Auto-Post to X/Twitter:**
* Create the `post_to_twitter` management command.
* **Logic:** Query for approved `InsightPost` instances not yet posted (`posted_to_social=False`). For each post, use the `tweepy` library (authenticating with keys from `.env`) to upload the featured image (if present) and create a tweet containing the title, a short description/excerpt, relevant hashtags (#Igbo, #IgboArchives), and the post's absolute URL. Handle potential errors (e.g., image too large, API limits). Update the `posted_to_social` flag on success.
* **Automation (Cron Job):** Schedule this command to run periodically (e.g., hourly or daily) on the Oracle VM. *Rationale: Automates content promotion on a key social platform.*

**Subscriber Emails (core app):**
* Create the `Subscriber` model and a simple signup form (e.g., in the footer).
* Implement the `post_save` signal receiver for `InsightPost`. On approval (`instance.is_approved` becomes `True`), the receiver should:
    * Query all active `Subscriber` email addresses.
    * Construct the email content (e.g., using Django templates, including post title, excerpt, link).
    * Iterate through subscribers in batches (e.g., 50-100). For each batch, use `django.core.mail.send_mass_mail` or loop and use `send_mail`, configured to use Brevo's SMTP credentials (from `.env`). Include error handling and possibly `time.sleep` to respect Brevo's rate limits if needed (though 300/day allows for bursts). *Rationale: Engages registered subscribers with new content.*

**Dependencies:** Phase 3.
**Output:** A functional AI chat assistant, automated posting to X/Twitter, and email notifications for new content subscribers.
**Testing:** Interact with the AI chat. Approve a new post and verify it appears on the configured X/Twitter account and that subscriber emails are sent correctly (use test email addresses).

---

## Phase 5: Admin, SEO, Monetization, & Backups (4-6 Days)
**Goal:** Enhance admin usability, optimize for search engines and social sharing, implement monetization options, and ensure robust data backup procedures.

### Sub-Steps

**SEO (django-meta) & Sitemaps:**
* Integrate `django-meta`. Add `meta` to `INSTALLED_APPS`.
* Define `get_meta()` methods on key models (`InsightPost`, `Archive`, `CustomUser`, `BookReview`) to return dictionaries specifying title, description, image (URL), and potentially keywords for `<meta>` tags and Open Graph (OG) tags.
* Configure Django's sitemaps framework. Create `Sitemap` classes for all relevant content types (including user profiles and threaded comment pages if desired for indexing). Register the sitemap URL in `urls.py`. *Rationale: Improves discoverability on search engines and controls social media link previews.*

**Admin Stats Integration:**
* Create a custom Django admin view (e.g., linked from the main admin index).
* **Backend Logic:** In this view, use the `google-analytics-data-api` library. Authenticate using a service account JSON key (stored securely, path in `.env`). Make API calls to fetch desired GA4 metrics (e.g., `runReport` for sessions, users by country, traffic sources over the last 7/30 days).
* **Template:** Display the fetched data clearly using simple tables or potentially integrating a basic charting library (like Chart.js via CDN) if desired. *Rationale: Provides essential site performance insights directly within the admin interface.*

**Monetization (Adsense & Donations):**
* **Adsense:** Obtain your Google Adsense code snippets. Strategically place the auto-ads script in `base.html` and specific ad unit tags within content templates (e.g., sidebars, between paragraphs in `insight_detail.html`).
* **Donations:** Add a "Support Us / Donate" link in the site footer. This link should go to a simple static page (`core` app) explaining the project's goals and embedding a donation button/link from PayPal, Buy Me a Coffee, or similar platform. *Rationale: Introduces planned revenue streams.*

**Backups (django-dbbackup):**
* Install `django-dbbackup` and add `dbbackup` to `INSTALLED_APPS`.
* Configure `settings.py` for `DBBACKUP_STORAGE` to use Oracle Cloud Infrastructure Object Storage. This requires installing `boto3` and configuring `DBBACKUP_STORAGE_OPTIONS` with OCI credentials (access key, secret key, bucket name, endpoint URL) loaded from the `.env` file.
* **Automation (Cron Job):** Schedule the `python manage.py dbbackup --clean` command to run weekly on the Oracle VM. *Rationale: Automates secure, off-site database backups.*

**Dependencies:** Phase 4.
**Output:** An SEO-optimized platform with admin analytics, integrated monetization options, and automated backups configured.
**Testing:** Use online tools (like Facebook Debugger, Twitter Card Validator) to check OG tags on various pages. Verify GA data appears in the custom admin view. Confirm backup files are created in the OCI bucket.

---

## Phase 6: Future Enhancements (Post-MVP)
**Goal:** Outline the strategic next steps for expanding the platform's capabilities, particularly focusing on deeper AI integration and content growth.

* **Igbo Academy:** Develop the dedicated `academy` app with models for courses, lessons, and quizzes. Integrate the Igbo Archives AI (running on VM1) via API calls. Use the AI for generating personalized learning paths based on user progress/interests, creating interactive exercises (e.g., pronunciation checks, fill-in-the-blanks), and potentially assessing quiz answers. Use Gemini as a fallback for generating basic lesson content.
* **Data Expansion (Ethical Scraping):** Develop targeted scraping scripts (e.g., using `requests` and `BeautifulSoup4`, or `Scrapy`) for identified sources (museums like MMA, Pitt, British Museum). Crucially: Only target sections explicitly licensed under Creative Commons (or similar permissive licenses). Respect `robots.txt`. Extract metadata meticulously. Implement a review stage before programmatically creating new `Archive` objects. Requires careful planning and adherence to legal/ethical guidelines.
* **Full AI Integration:** Transition the `ai_service` chat to primarily use the Igbo Archives AI for Igbo-related queries, using Gemini only as a fallback or for general knowledge questions. Explore using the AI for backend tasks like suggesting tags for new `InsightPost` submissions or flagging potentially problematic comments.
* **Gamification & Referrals:** Implement `django-badgify` and `django-referral-system` (deferred from MVP) to enhance community engagement and growth. Link rewards to Academy access or other site privileges.
* **Full Social Automation:** Add support for posting to Facebook, Instagram, and Mastodon to the `post_to_social` command, carefully handling each platform's API requirements and limitations.
* **Editor Upgrade:** If `django-ckeditor-5` proves insufficient, plan a migration to `django-tiptap` for the full block-based editing experience.
* **Asynchronous Tasks (Celery):** If site traffic and background task volume increase significantly, implement Celery with a free Redis provider to handle email sending, social posting, and potentially AI tasks asynchronously, improving web request performance.

*Rationale: Provides a clear roadmap for evolving the platform beyond the initial launch, focusing on the unique value propositions (custom AI, expanded archive).*

---

## Phase 7: Launch & Maintenance (2-3 Days)
**Goal:** Deploy the completed MVP to the production environment, ensure a seamless transition for existing content/SEO, and establish ongoing maintenance procedures.

### Sub-Steps

**WordPress Redirects (Nginx):**
* Using `migration_data.json`, generate a list of nginx 301 redirect rules (e.g., `rewrite ^/old-wp-slug/$ /insights/new-django-slug/ permanent;`). Add these rules to the nginx server block configuration file (`/etc/nginx/sites-available/igboarchives`) on the VM. Test thoroughly. *Rationale: Preserves SEO value and avoids broken links.*

**Static Pages & Footer (core app):**
* Create `TemplateViews` and simple HTML templates for essential static pages: "Privacy Policy," "Terms of Service," "About User Content," "Contact Us."
* Update the site footer (`base.html`) with links to these pages, plus "Feedback," "Support Us / Donate," and links to official social media profiles. *Rationale: Fulfills legal requirements and provides essential user information.*

**Deployment (Gunicorn + Nginx + Systemd):**
* **Code:** Pull the final code from the GitHub `main` branch onto the VM.
* **Environment:** Set up the virtual environment (`venv`). Install production requirements (`pip install -r requirements.txt`). Create the `.env` file containing all production secrets (DB URL with wallet path, `SECRET_KEY`, API keys). Ensure file permissions are secure.
* **Collect Static & Media:** Run `python manage.py collectstatic`. Configure `settings.py` for `MEDIA_ROOT` and `MEDIA_URL`.
* **Gunicorn Service:** Create a `systemd` service file (`/etc/systemd/system/igboarchives.service`) to manage Gunicorn, binding it to a Unix socket (e.g., `/run/igboarchives.sock`). Configure user, group, working directory, and environment file path. Enable and start the service.
* **Nginx Configuration:** Configure the Nginx server block (`/etc/nginx/sites-available/igboarchives`) to: listen on port `80` (and ideally `443` for HTTPS), set the `server_name` to your domain, serve static files (`/static/`) and media files (`/media/`) directly using `alias` directives, and proxy all other requests to the Gunicorn socket using `proxy_pass http://unix:/run/igboarchives.sock;`. Set appropriate proxy headers. Enable the site configuration and restart Nginx.
* **HTTPS:** Install Certbot (`sudo apt install certbot python3-certbot-nginx`) and use it to obtain a free Let's Encrypt SSL certificate for your domain and automatically configure Nginx for HTTPS. *Rationale: Provides a secure, performant, and auto-restarting production environment.*

**Launch & Monitor:**
* Point your domain's DNS records (A record for the domain, CNAME for `www`) to the Oracle VM's public IP address.
* Announce the launch.
* **Continuously monitor:** Google Analytics (real-time traffic), Google Search Console (indexing status, errors), server logs (Nginx, Gunicorn, cron jobs), database performance (Neon dashboard), and application error reporting (configure Django logging or use a service like Sentry's free tier). Check resource usage (CPU, RAM) on the VM. *Rationale: Ensures a smooth launch and allows for quick identification and resolution of any issues.*

---

*This v8 plan is the most detailed and balanced approach, incorporating your feedback and prioritizing a feasible yet comprehensive MVP launch within months.*

---

## 🎓 Academy Coming Soon

The **Igbo Academy** is currently under development! This feature will provide:

### What to Expect:
- **Language Learning**: Master Igbo with structured lessons from beginner to advanced
- **Cultural Traditions**: Explore customs, ceremonies, and festivals
- **Folktales & Stories**: Discover timeless wisdom through storytelling
- **History & Heritage**: Learn about ancient kingdoms and modern achievements
- **Spiritual Practices**: Understand traditional beliefs and worldviews
- **Arts & Crafts**: Explore pottery, weaving, carving, and contemporary art
- **Music & Dance**: Experience traditional instruments and dances
- **Social Structure**: Learn about family dynamics and community governance
- **Cuisine & Food**: Discover traditional dishes and their cultural significance

### Features:
- 📹 Interactive video lessons with native speakers
- 🎮 Gamified learning with badges and progress tracking
- 👥 Community learning and conversation practice
- ✅ Expert-curated content reviewed by cultural historians
- 📱 Mobile-first progressive web app design

Visit `/academy/` to see the full coming soon page and sign up for early access!

---

## Development Status

**Phase 1 & 2: COMPLETE ✅**
- ✅ Django foundation with all apps
- ✅ PWA integration (verified working)
- ✅ User authentication (allauth + Google OAuth)
- ✅ User profiles and dashboard
- ✅ Private messaging system
- ✅ Push notifications (full backend + frontend)
- ✅ Responsive UI with dark mode
- ✅ Academy coming soon page

**Next: Phase 3**
- Content detail views and creation forms
- HTMX filtering and pagination
- Comments integration
- Edit suggestions workflow

