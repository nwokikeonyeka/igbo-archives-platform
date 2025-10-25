# Deployment Guide - Render

This guide will help you deploy your Igbo Archives platform to Render for further development and testing.

## Prerequisites

- A GitHub account
- A Render account (free tier available at https://render.com)
- Your code pushed to a GitHub repository

## Deployment Steps

### 1. Push Your Code to GitHub

If you haven't already, push your code to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Create a New Web Service on Render

1. Log in to your Render account
2. Click on "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:

   - **Name**: `igbo-archives` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Choose the closest to your users
   - **Branch**: `main`
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command**: 
     ```
     gunicorn --bind 0.0.0.0:$PORT --reuse-port igbo_archives.wsgi:application
     ```
   - **Plan**: Free (for development)

### 3. Set Environment Variables

In the Render dashboard, add the following environment variables:

#### Required Variables

```
DEBUG=False
SECRET_KEY=<generate-a-strong-random-secret-key>
ALLOWED_HOSTS=<your-render-app-name>.onrender.com
CSRF_TRUSTED_ORIGINS=https://<your-render-app-name>.onrender.com
```

#### Optional Variables (add as needed)

```
# Google OAuth
GOOGLE_CLIENT_ID=<your-google-client-id>
GOOGLE_CLIENT_SECRET=<your-google-client-secret>

# reCAPTCHA
RECAPTCHA_PUBLIC_KEY=<your-recaptcha-site-key>
RECAPTCHA_PRIVATE_KEY=<your-recaptcha-secret-key>

# Google Gemini AI
GEMINI_API_KEY=<your-gemini-api-key>

# Email (Brevo)
BREVO_EMAIL_USER=<your-brevo-email>
BREVO_API_KEY=<your-brevo-api-key>
DEFAULT_FROM_EMAIL=noreply@igboarchives.com

# Firebase Cloud Messaging (Push Notifications)
FCM_SERVER_KEY=<your-fcm-server-key>
VAPID_PUBLIC_KEY=<your-vapid-public-key>
VAPID_PRIVATE_KEY=<your-vapid-private-key>

# Twitter/X API
TWITTER_API_KEY=<your-twitter-api-key>
TWITTER_API_SECRET=<your-twitter-api-secret>
TWITTER_ACCESS_TOKEN=<your-twitter-access-token>
TWITTER_ACCESS_TOKEN_SECRET=<your-twitter-access-token-secret>

# Google AdSense
GOOGLE_ADSENSE_CLIENT_ID=<your-adsense-client-id>
```

### 4. Generate a Secret Key

To generate a strong secret key, run this Python command:

```python
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Copy the output and use it as your `SECRET_KEY`.

### 5. Deploy

1. Click "Create Web Service"
2. Render will automatically deploy your application
3. Wait for the build to complete (first deployment may take 5-10 minutes)
4. Your app will be available at: `https://<your-app-name>.onrender.com`

## Important Notes

### Database

- This deployment uses **SQLite** as requested
- SQLite data is stored on the server's disk
- **Important**: Render's free tier may reset the file system periodically, which means your database could be lost
- For production, you should migrate to PostgreSQL (see below)

### Static Files

- Static files are collected during the build process
- Django serves static files in production (not recommended for high traffic)
- For better performance, consider using a CDN or object storage

### Media Files

- User-uploaded media files are stored on the server's disk
- Like the database, these may be lost on free tier resets
- For production, configure cloud storage (AWS S3, Cloudflare R2, etc.)

## Upgrading to PostgreSQL (Recommended for Production)

When you're ready to move to production:

1. In Render dashboard, create a new PostgreSQL database
2. Copy the database connection string
3. Update your environment variables:
   ```
   DATABASE_URL=<your-postgresql-connection-string>
   ```
4. The app will automatically use PostgreSQL if `DATABASE_URL` is set

## Monitoring

- Check logs in the Render dashboard under "Logs"
- Monitor your application health in the "Events" tab
- Set up health checks in Render settings

## Custom Domain

To use a custom domain (e.g., igboarchives.com.ng):

1. Go to your web service settings
2. Click "Custom Domain"
3. Add your domain
4. Update your DNS records as instructed
5. Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` with your domain

## Troubleshooting

### Build Fails

- Check the build logs for errors
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Application Won't Start

- Check the logs for errors
- Verify all required environment variables are set
- Make sure `SECRET_KEY` is set

### Static Files Not Loading

- Ensure `collectstatic` ran successfully in the build command
- Check `STATIC_ROOT` and `STATIC_URL` in settings.py

### Database Errors

- Verify migrations ran successfully
- Check that database file has write permissions

## Next Steps

After deployment:

1. Test all features thoroughly
2. Set up monitoring and error tracking (e.g., Sentry)
3. Configure email service for notifications
4. Set up regular backups
5. Implement Phase 6 features as planned

## Support

For Render-specific issues, consult:
- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com

For Django-specific issues:
- Django Documentation: https://docs.djangoproject.com
