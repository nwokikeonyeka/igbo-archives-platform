# Igbo Archives Platform Version 2.0

## Project Overview
The Igbo Archives Platform is a comprehensive Django-based digital archive and cultural heritage platform focused on preserving and sharing Igbo history, culture, artifacts, insights, and literature.

## Current Status (October 26, 2025)
**Phases Completed:**
- ✅ Phase 1: Basic setup and configuration
- ✅ Phase 2: List/Grid toggle views with filters
- ✅ Phase 3: WordPress-like rich text editor implementation

## Recent Changes

### Phase 2: List/Grid Toggle Views
- Implemented JavaScript-based toggle between list and grid layouts
- Saves user preference in localStorage
- Applied to Archives, Insights, and Books sections
- CSS classes: `.archive-view-grid` and `.archive-view-list`
- Toggle function: `toggleArchiveView()` in `core/static/js/main.js`

### Phase 3: Rich Text Editor Implementation
**Final Solution: Quill.js**
- Completely free, no API keys required
- WordPress-like editing experience
- Clean, modern toolbar with block formatting
- Supports: headings, bold, italic, lists, quotes, code blocks, links, images
- Image upload integration via `/api/upload-image/` endpoint
- Implemented on:
  - Insights create/edit pages
  - Books create/edit pages
- Archives uses simple forms (no rich editor needed for media uploads)

**Previous Editors Removed:**
- ❌ CKEditor 5 (removed - had dependency issues)
- ❌ Editor.js (removed - CDN loading failures)
- ❌ TinyMCE (removed - requires API key)

## Architecture

### Models
**Archives App:**
- `Archive`: Media files (images, videos, documents, audio) with metadata
- Fields: title, description, archive_type, image/video/document/audio files, caption, alt_text, location, date_created

**Insights App:**
- `Insight`: Blog/article posts with rich content
- Content stored as HTML from Quill editor
- Featured images, tags, publish/draft status

**Books App:**
- `BookReview`: Book reviews with ratings
- Fields: book_title, author, publisher, ISBN, rating, review content
- Cover images (front, back, alternate editions)

### API Endpoints
- `/api/upload-image/` - Handles image uploads from Quill editor
- `/api/archive-media-browser/` - Browse existing archive media (for future implementation)
- `/api/get-categories/` - Fetch available categories

### Key Files
- `core/static/js/main.js` - Contains list/grid toggle function
- `core/static/css/style.css` - Styling for grid/list views
- `insights/templates/insights/create.html` - Insight creation with Quill
- `books/templates/books/create.html` - Book review creation with Quill
- `archives/templates/archives/create.html` - Archive upload (no rich editor)

## Technology Stack
- **Backend**: Django 5.2.7
- **Database**: PostgreSQL (Neon)
- **Rich Text Editor**: Quill.js 1.3.7
- **Frontend**: Bootstrap 5, Font Awesome
- **PWA**: django-pwa

## Environment
- **Platform**: Replit
- **Port**: 5000 (Django development server)
- **Server**: 0.0.0.0:5000

## User Workflow

### Creating Content
1. **Archives**: Upload media files with metadata (no rich text needed)
2. **Insights**: Write articles using Quill editor with formatting and images
3. **Books**: Write book reviews with ratings and Quill editor

### Content Management
- Draft/Publish workflow
- Tag-based organization
- Category filtering
- Search functionality

## Next Steps (Future Phases)
- [ ] Phase 4: Advanced archive browser modal for selecting existing archive images within Quill editor
- [ ] Phase 5: User permissions and roles
- [ ] Phase 6: Advanced search and filtering
- [ ] Phase 7: Social features (comments, likes, shares)

## Development Notes
- Always restart Django server after template changes
- Quill editor saves content as HTML in the database
- CSRF tokens required for all forms and AJAX requests
- Login required for create/edit pages (@login_required decorators)

## User Preferences
- Grid/list view preference stored in browser localStorage
- Persists across sessions for each user

## Known Issues
- None currently identified with Quill implementation

## Credits
- Built with Django, Quill.js, and modern web standards
- Deployed on Replit infrastructure
