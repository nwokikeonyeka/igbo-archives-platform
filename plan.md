# Igbo Archives: Platform Development Plan (v9 - Version 2.0)

**Project:** Igbo Archives (Web Platform)

**Author:** Onyeka Nwokike 

**Vision:** To build the definitive, "best-in-class" web platform for Igbo cultural preservation and community engagement. This version (v9) represents the Version 2.0 roadmap, focused on UI/UX modernization, enhanced content authoring, robust moderation workflows, and improved community engagement features.

**Core Principle:** 100% free and feasible. Prioritizes user experience, content quality, modern design, and community collaboration.

---

## STATUS: Version 1.0 Completed (Phases 0-5)

The original MVP has been successfully deployed to Render with the following completed phases:
- **Phase 0:** Environment setup, VM provisioning, database setup, WordPress migration
- **Phase 1:** Django foundation, PWA setup, responsive navigation
- **Phase 2:** User authentication, profiles, dashboard, messaging, notifications
- **Phase 3:** Content apps (Archives, Insights, Books), CKEditor, filtering, threaded comments
- **Phase 4:** AI chat service, Twitter automation, legal pages
- **Phase 5:** SEO optimization, admin enhancements, monetization setup, backups

**Current Platform:** Live at Render with core functionality operational.

---

## Version 2.0 Development Plan

Based on comprehensive user feedback and UX analysis, the following phases will transform the platform into a more mature, visually appealing, and functionally robust application.

---

## Phase 1: Experience Shell & Navigation Foundations (5-7 Days)
**Goal:** Establish the new heritage-inspired design system, modernize navigation structure, update footer with dynamic content, and remove unused AI service app while preserving external links.

### Acceptance Criteria
- [ ] Global design tokens applied across base templates and CSS
- [ ] Header/nav/footer variants responsive and accessible
- [ ] Navigation links updated per device (desktop/mobile)
- [ ] ai_service app code, URLs, and settings references removed without regressions
- [ ] New external AI link present in header and footer

### Sub-Steps

**Color Scheme & Design System:**
* Replace current color palette (remove harsh reds, yellows, blues) with heritage-inspired tones
* Develop "old pictures" color palette: sepia tones, aged paper colors, vintage photograph aesthetics
* Create design tokens for consistent use across platform
* Update CSS variables for primary, secondary, accent, text, and background colors
* Ensure design feels sophisticated and appropriate for cultural preservation (not childish)
* Update all UI components to use new color system
* Test color contrast for accessibility (WCAG AA compliance)

**Sticky Header with Shrinking Behavior:**
* Implement sticky header that remains visible on scroll
* Add JavaScript/CSS for header to shrink to 1/3 of original size when scrolling down
* Smooth transition animations for header size changes
* Ensure logo scales proportionally during shrink
* Test sticky behavior across different screen sizes and browsers

**Updated Header Navigation:**
* Add notification bell icon for logged-in users
  - Display unread notification count badge
  - Dropdown showing top 5 notifications with "Mark as read" option
  - "View all notifications" link to dedicated notification page
* Update profile button to show user's profile picture (if available)
  - Fallback to initials in circle if no picture
* Add "Igbo Archives AI" as fifth nav item on desktop
  - Link to external https://ai.igboarchives.com.ng
  - Label as "AI" on mobile navigation
* Rename "Books" to "Recommended Books" on desktop header nav
  - Keep as "Books" on mobile bottom nav

**Footer Enhancements:**
* Scrape social links from igboarchives.com.ng/contact-us
  - Add Facebook, Instagram, Mastodon links
  - Keep existing Twitter/X link
  - Style social icons consistently
* Add conditional logo in "About Igbo Archives" section
  - Show logo-dark.png in light mode
  - Show logo-light.png in dark mode
* Replace static about text with first paragraph from About Us page
  - Include content about "correcting misconceptions" etc.
* Change "AI Assistant" link in footer to "Igbo Archives AI"
  - Link to external https://ai.igboarchives.com.ng

**Remove AI Service App:**
* Delete ai_service app directory and all files
* Remove ai_service from INSTALLED_APPS in settings.py
* Remove ai_service URL patterns from main urls.py
* Remove any AI service-related templates
* Remove GEMINI_API_KEY and related AI settings (or keep for future use as comments)
* Ensure no broken links or import errors
* Update any references to point to external AI link

**Dependencies:** None (builds on existing v1.0 foundation)
**Output:** Modernized design system, updated navigation structure, enhanced footer, cleaned codebase
**Testing:** Verify header shrinking behavior, test all navigation links, confirm social links work, verify logo switching in dark mode, ensure no errors from AI app removal

---

## Phase 2: Homepage & Browsing Enhancements (6-8 Days)
**Goal:** Build featured archives carousel, unify list/grid toggle and filter controls across all content sections, implement sticky filters with shrink-on-scroll, and add carousel presentations for filtered results.

### Acceptance Criteria
- [ ] Homepage carousel fed by featured archives via reusable query
- [ ] HTMX/JS filter interactions coexisting with pagination
- [ ] Filter bar sticky behavior consistent desktop/mobile
- [ ] List and grid views functional for Archives and Insights
- [ ] Performance and Lighthouse baselines maintained

### Sub-Steps

**Homepage Museum-Like Carousel:**
* Create beautiful, museum-quality carousel before "Explore Archives" section
* Carousel displays featured archive posts (where is_featured=True)
* Each slide shows:
  - Archive image as background or prominent display
  - Title overlaid or positioned elegantly
  - Description/excerpt text
  - "View Archive" link/button
* Make entire carousel slide clickable to archive detail page
* Implement smooth transitions (fade or slide effects)
* Add navigation arrows and dot indicators
* Auto-play with pause on hover
* Responsive design: adjust layout for mobile
* Style with vintage/heritage aesthetic matching new color scheme

**Unified Filter System:**
* Design single, consistent filter bar for Archives, Insights, and Books
* Place filter as extended header (sticky, shrinks on scroll)
* Filter components:
  - **Archives:** By Category, By Type, Sort (Newest first, Oldest first, Featured), Search box, Grid/List toggle
  - **Insights:** By Tag, Sort (Newest first, Most commented), Search box, Grid/List toggle
  - **Books:** By Rating, By Tag, Sort (Newest first, Highest rated), Search box, Grid view only (no list)
* Use HTMX for dynamic filtering without page reload
* Update URL parameters for shareable filtered views
* Maintain pagination when filtering

**Sticky Filter with Shrink Behavior:**
* Implement sticky positioning for filter bar
* Add JavaScript to shrink filter bar on scroll (similar to header)
* Ensure smooth transitions
* Keep essential controls visible even when shrunk
* Test across different devices and orientations

**Grid and List View Toggle:**
* Implement working toggle for Archives and Insights
* **Grid View:** Cards in responsive grid (3-4 columns desktop, 2 mobile)
* **List View:** Image first, content beside (responsive layout)
* Save user preference in localStorage
* Smooth transition between view modes
* **Books:** Grid view only (no list view option)

**Carousel for Filtered Results:**
* Add carousel section above filtered results
* Carousel shows featured items matching current filter
* Example: If filtering by "Masks" category, carousel shows featured Masks
* Carousel design appropriate for each content type:
  - Archives: Museum-style presentation
  - Insights: Article preview cards
  - Books: Book cover showcase
* Carousel updates dynamically when filters change

**"Why Igbo Archives" Section:**
* Ensure 4 items display on single line on desktop
* Use CSS Grid or Flexbox for responsive layout
* Stack vertically on mobile
* Equal spacing and sizing
* Icons and text well-balanced

**Dependencies:** Phase 1 (design system must be in place)
**Output:** Interactive homepage carousel, unified filtering system, working grid/list views, enhanced browsing UX
**Testing:** Test all filter combinations, verify carousel responsiveness, confirm grid/list toggle works, check pagination with filters

---

## Phase 3: Authoring & Media Governance (8-10 Days)
**Goal:** Evaluate and potentially replace CKEditor5 with WordPress-like block editor, enable archive image/media selection in post forms, enforce comprehensive media metadata, implement auto-featured-image selection, enforce file size limits, and distinguish between "Save Changes" and "Publish (Pending Approval)".

### Acceptance Criteria
- [ ] Editor supports block-style authoring with image reuse from archives
- [ ] Server-side validations for metadata (caption, description, copyright) and file sizes
- [ ] Admin workflow stores pending-approval state correctly
- [ ] First image auto-selected as featured if user doesn't choose
- [ ] Legacy content migrated or safely handles new requirements

### Sub-Steps

**Rich Text Editor Evaluation:**
* Research WordPress-like block editor alternatives for Django:
  - Consider django-wagtail's StreamField
  - Evaluate TipTap with Django integration
  - Check django-gutenberg or similar packages
  - Assess Editor.js integration possibilities
* If suitable alternative found:
  - Install and configure chosen block editor
  - Create migration path from CKEditor content
  - Update InsightPost and BookReview models
  - Update forms and templates
* If keeping CKEditor:
  - Enhance configuration for better block-like experience
  - Ensure image upload and management is smooth
* Ensure editor supports:
  - Block-based content creation
  - Image insertion with metadata fields
  - Media library access
  - Responsive embed support

**Archive Media Selection in Posts:**
* Create archive selector interface for Insights and Books creation
* Implement searchable, filterable archive browser within post editor
* Features:
  - Search archives by title
  - Filter by category and type
  - Thumbnail preview grid
  - Select single or multiple archives
* Insert selected archive images into post content
* Auto-populate caption and description from archive metadata
* Selected archives automatically link to their detail pages
* Support for selecting images, videos, audio, documents based on archive type

**Image Upload Requirements:**
* For any uploaded image in Insights posts:
  - Required fields: Caption, Description
  - Required: Copyright information or image source in caption
  - Validate on form submission
  - Clear error messages for missing metadata
* Create checkbox: "Submit this image as archive" (default: checked)
* If checked, show full archive upload fields:
  - Title, Description, Archive Type, Category
  - Alt text, Date created (or circa date like "c1910")
  - Original author/photographer
  - Tags (optional)
* Admin approval workflow:
  - Admin can approve image as archive during post moderation
  - If approved as archive: image and description link to new archive page
  - If not approved: image remains part of post only, no archive link
  
**File Size Enforcement:**
* Implement server-side file size validators:
  - Images: 2-5MB maximum
  - Videos: 50MB maximum
  - Documents: 2-5MB maximum  
  - Audio: 2-5MB maximum
* Display file size limits in upload forms
* Show clear error messages when limits exceeded
* Consider image compression on upload for efficiency

**Auto Featured Image Selection:**
* If user doesn't explicitly select featured image:
  - Automatically use first image in post content
  - Extract first image from editor content
  - Set as featured_image field
* Allow users to override by ticking "Use as featured image" checkbox
* Clear indication in editor of which image will be featured
* Users can change featured image by editing post

**Archives Post Creation Updates:**
* Archives should NOT have rich text editor (just textarea for description)
* Required fields for Archives:
  - Title, Description
  - Archive Type (image, video, document, audio)
  - Category
  - File upload (image/video/document/audio based on type)
  - Caption (with copyright/source info)
  - Description
  - Alt text (for images)
* Optional fields:
  - Original author (e.g., "Northcote Thomas")
  - Date created (calendar picker OR circa text field like "c1910")
  - Tags
* Featured image handling for non-image archives:
  - Videos: Extract thumbnail or allow upload
  - Documents: No featured image required
  - Audio: No featured image required
* Archives without featured images excluded from carousels

**Save vs Publish Workflow:**
* Replace "Draft" terminology with "Save Changes" or "Save Progress"
* Two action buttons:
  - **"Save Changes"** - Saves work without submitting (is_published=False, is_approved=False)
  - **"Submit for Approval"** - Submits to admin queue (is_published=False, is_approved=False, pending_approval=True)
* Add `pending_approval` boolean field to InsightPost and BookReview models
* Users can return to saved work anytime from dashboard
* Clear messaging about approval workflow

**Dependencies:** Phase 2 (UI components in place)
**Output:** Enhanced content creation experience, comprehensive media governance, clear publication workflow
**Testing:** Test archive selection, verify file size limits, confirm metadata validation, test save vs publish workflow, verify auto-featured-image logic

---

## Phase 4: Moderation, Collaboration & Notifications (7-9 Days)
**Goal:** Implement threaded-only comments with reCAPTCHA for guests, create admin approval workflow, centralize notifications with bell dropdown and dedicated page, add edit-suggestion flows, implement previous/next/recommended posts, and set up baseline web push notifications.

### Acceptance Criteria
- [ ] Notification models/services cover approvals, comments, suggestions
- [ ] Bell dropdown and notifications page display unread counts correctly
- [ ] Comments validate reCAPTCHA for guests and render threaded
- [ ] Push notifications delivered via native browser support
- [ ] Moderation dashboard operational for admins
- [ ] Edit suggestion workflow functional
- [ ] Previous/next/recommended post navigation working

### Sub-Steps

**Threaded Comments System:**
* Use ONLY django-threadedcomments for all users
* Remove any separate comment forms
* For guest users:
  - Add reCAPTCHA field to comment form (same as signup/login)
  - Validate reCAPTCHA on submission
  - Required fields: Name, Email, Comment text
* For logged-in users:
  - Auto-populate name from full_name
  - No reCAPTCHA required
* Comment UI redesign:
  - Display in compact boxes
  - Clean, modern styling
  - Clear visual hierarchy for threaded replies
  - Indent nested comments
  - Show commenter full_name (linked to profile if registered user)
  - Show relative timestamps ("2 hours ago")
  - Reply button for each comment
  - Edit/Delete for comment owners

**Messages UI Improvements:**
* Display messages in boxes (similar to comments)
* Inbox view:
  - Message title (or subject)
  - Other party's full_name
  - Last message preview (truncated)
  - Timestamp (e.g., "1/3/2026 3:00 PM")
* Thread view:
  - Messages in speech-bubble style boxes
  - Distinguish sent vs received visually
  - Timestamps for each message
  - Clean, WhatsApp-like aesthetic

**Notification Bell & System:**
* Add notification bell icon to header (logged-in users only)
* Bell shows unread notification count badge
* Clicking bell opens dropdown:
  - Show top 5 recent notifications
  - Each notification has "Mark as read" option
  - "View all notifications" link at bottom
* Create dedicated notifications page (`/notifications/`)
  - Paginated list of all notifications
  - Filter by read/unread
  - Mark all as read button
  - Clear visual distinction between read/unread
* Notification types to track:
  - Post approval/rejection
  - New comment on your post
  - Reply to your comment
  - New message received
  - Edit suggestion on your post
  - Your edit suggestion accepted/rejected

**Determine Email Notifications:**
* Not all notifications need emails - only important ones:
  - **Email required:**
    - Post approved (send email with link)
    - Post rejected (with reason)
    - Edit suggestion on your post
    - New message from another user
    - Password reset
    - Account-related actions
  - **In-app only:**
    - New comment (unless comment is on your post)
    - Reply to comment
    - General activity updates
* Create email templates:
  - Include Igbo Archives logo (conditional for light/dark mode awareness)
  - Professional styling matching site aesthetic
  - Clear call-to-action buttons
  - Unsubscribe options where appropriate

**Post Approval Workflow:**
* Add admin moderation dashboard view
* Show posts pending approval (is_published=False, pending_approval=True)
* For each pending post, admin can:
  - Preview full content
  - Approve (sets is_published=True, is_approved=True)
  - Reject (with reason message)
  - Approve images as archives (if submitted with post)
* Notifications:
  - Send push notification to admin when new post submitted
  - Send email to admin (configurable)
  - Send push notification + email to author when approved
  - Send email with reason when rejected
* Update dashboard to show:
  - Posts pending approval (for admins)
  - User's submitted posts status (for authors)

**Edit Request/Collaboration System:**
* Add "Suggest Edit" or "Contribute" button on all posts
* When clicked, open modal/form:
  - Text field for edit suggestion or contribution
  - Submit button
* Create EditSuggestion model (already exists, enhance if needed)
* Original post author gets notification:
  - In-app notification
  - Email notification
  - Can view edit in dashboard
  - Approve or Reject options
* If approved:
  - Suggester gets notification
  - Can now edit the post
  - Changes go through approval again
* If rejected:
  - Suggester gets notification with optional message

**Previous/Next & Recommended Posts:**
* After post content, before comments section:
* **Previous/Next Navigation:**
  - Links to chronologically previous/next post
  - Show title and thumbnail
  - Consistent styling across all post types
* **Recommended Posts:**
  - Section title: "You May Also Like" or "Related Content"
  - Show slider with 3 visible posts, 9 total to slide through
  - Recommendations based on:
    - Same category/tag
    - Same author (for diversity)
    - Similar topics (if possible)
  - Carousel/slider with arrows
  - Responsive on mobile
* Implement for Archives, Insights, and Books

**Web Push Notifications:**
* Use native browser Push API (no external dependencies)
* Request permission on first visit (for logged-in users)
* Store push subscription in database
* Send push notifications for:
  - Post approved
  - New comment on your post
  - New message
  - Edit suggestion received
* Skip iOS implementation (known limitations)
* Focus on Chrome, Firefox, Edge on desktop and Android
* Graceful degradation if push not supported

**Dependencies:** Phase 3 (post creation workflow must be solid)
**Output:** Complete moderation system, centralized notifications, enhanced comments, collaboration features
**Testing:** Test comment threading for guests and users, verify reCAPTCHA, test notification creation and delivery, verify email templates, test push notifications, confirm previous/next/recommended logic

---

## Phase 5: Account & Secondary UX Polish (5-7 Days)
**Goal:** Fix dashboard data display, show book reviews on profiles, replace username with full_name everywhere, relocate delete account control, enable password reset for all users, remove logout confirmation, simplify Donate page.

### Acceptance Criteria
- [ ] Dashboard correctly displays user's messages and posts
- [ ] Book reviews appear on user profiles
- [ ] All author/user references use full_name (with profile links)
- [ ] Delete account option in edit profile page only
- [ ] Password reset works for email and Google OAuth users
- [ ] Logout is instant (no confirmation page)
- [ ] Donate page simplified with single support option
- [ ] Automated tests updated for auth changes

### Sub-Steps

**Dashboard Fixes:**
* Debug and fix dashboard tabs:
  - **My Messages:** Show user's message threads correctly
  - **My Insights:** Show user's insights (published and pending)
  - **My Drafts:** Show saved progress posts (is_published=False, pending_approval=False)
  - **My Book Reviews:** Show user's book reviews
  - **My Archives:** Show user's uploaded archives
  - **Edit Suggestions Received:** Show suggestions on user's posts
  - **My Notifications:** Show recent notifications (or link to notifications page)
* Verify queries for each tab
* Ensure proper filtering by current user
* Add empty state messages for each tab
* Test data display and pagination

**Profile Page Updates:**
* Add Book Reviews section to user profiles
* Currently shows Archives and Insights, add Books
* Tabs or sections for:
  - Archives uploaded by user
  - Insights written by user
  - Book Reviews written by user
* Each section shows grid/list of items
* Consistent styling across all sections
* Show appropriate message if section is empty

**Full Name Display Everywhere:**
* Replace all instances of username display with full_name
* Update templates:
  - Post author bylines ("by [Full Name]")
  - Comment author names
  - Profile page headers
  - Dashboard references
  - Message sender/receiver display
  - Search results
  - Admin interface where appropriate
* Link all author names to profile pages:
  - `<a href="/profile/{{ user.username }}/">{{ user.full_name }}</a>`
* Ensure full_name is required on signup
* Fallback to username only if full_name is empty (shouldn't happen)

**Delete Account Relocation:**
* Remove "Delete Account" from profile dropdown menu
* Move to Edit Profile page:
  - Place at bottom of edit form
  - Under "Danger Zone" or "Account Management" section
  - Clear warning about permanent deletion
  - Requires password confirmation
* Or create separate "Account Settings" page accessible from Edit Profile
* Ensure delete functionality still works (password verification required)

**Password Reset for All Users:**
* Enable password reset even for Google OAuth users
* Add "Change Password" or "Reset Password" in Edit Profile
* For email users:
  - Standard password change form (old password + new password)
* For Google OAuth users:
  - Allow setting password (enables email login as backup)
  - Clear messaging about adding password for additional security
* Send password reset emails using configured email backend
* Test email templates for password reset

**Remove Logout Confirmation:**
* Update logout flow to be immediate
* When user clicks "Logout":
  - Log them out instantly
  - Redirect to homepage
  - Show success message (toast/banner)
  - Skip the "Are you sure you want to log out?" page
* Update allauth configuration if needed to bypass confirmation

**Simplify Donate Page:**
* Remove "One-time" and "Monthly" support options
* Single, clear "Support Us" section
* Compelling text about mission and impact
* Single prominent donation button/link
* Can integrate with PayPal, Buy Me a Coffee, or Ko-fi
* Optional: Show supporter recognition (if implemented)
* Clean, focused design matching new aesthetic

**Make Clickable Boxes:**
* For Archives, Insights, and Books list/grid views:
  - Remove "Read More" or "Read Review" buttons
  - Make entire card/box clickable
  - Link entire box to post detail page
  - Add hover effects for better UX
  - Ensure accessibility (proper aria labels)
  - Keep consistent across all sections

**Testing & Quality Assurance:**
* Run full test suite
* Update tests for authentication changes
* Test all user flows end-to-end
* Cross-browser testing
* Mobile responsiveness check
* Performance audit (Lighthouse)
* Accessibility audit (WCAG AA)
* Security review

**Dependencies:** Phase 4 (notifications and moderation must be working)
**Output:** Polished user experience, fixed dashboard and profiles, simplified account management, refined UI elements
**Testing:** Comprehensive QA across all features, test account flows, verify password reset, confirm dashboard data accuracy

---

## Phase 6: Future Enhancements (User-Defined)
**Goal:** Reserved for future feature development as defined by project owner.

*This phase is reserved for future planning and will be defined by the project owner after Version 2.0 is completed.*

Potential areas for consideration:
* Igbo Academy development
* Advanced AI integration
* Multi-language support
* Mobile native apps
* Advanced analytics
* Community moderation tools
* Social features expansion
* Content recommendation engine
* API development for third-party integrations

---

## Development Guidelines

**General Principles:**
* Maintain backwards compatibility where possible
* Write comprehensive tests for new features
* Document all significant changes
* Follow Django best practices
* Prioritize performance and accessibility
* Keep design consistent and cohesive

**Code Quality:**
* Use type hints where applicable
* Write descriptive commit messages
* Keep functions/methods focused and small
* Add docstrings to complex logic
* Regular code reviews (even solo: review own code)

**Testing Strategy:**
* Unit tests for models and utilities
* Integration tests for views and workflows
* E2E tests for critical user journeys
* Manual testing for UI/UX
* Cross-browser and device testing

**Deployment:**
* Test thoroughly in development
* Stage on test environment if available
* Deploy during low-traffic periods
* Monitor logs and performance post-deploy
* Have rollback plan ready
* Communicate changes to users

---

**Version:** 9.0  
**Last Updated:** October 26, 2025  
**Status:** Active Development - Version 2.0  
**Platform:** Django 5.1+, Python 3.11+, PostgreSQL  
**Deployment:** Replit (Development), Render (Production)
