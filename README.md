# Shiv-Shakti-Stone
🪨 Shiv Shakti Stone – Business Website
Live Website: https://shivshaktistonee.co.in�
Deployed on: Render
📌 Project Overview
Shiv Shakti Stone is a production-ready business website built for a stone handicraft company.
The platform showcases products and allows customers to submit inquiries for selected items.
Instead of direct online payments, the system follows a lead generation model where interested customers fill out a contact form and the details are sent directly to the admin via email.
This project was developed as a real freelance client project and deployed to production.
🚀 Features
Dynamic product listing
Category management
Product detail pages
Product image uploads
Custom product extra details / bullet points
Editable hero section
Contact form for customer inquiries
Email notifications via SendGrid (SMTP)
SEO optimization
Fully dynamic admin control panel
Production deployment on Render
🛠️ Tech Stack
Backend
Django 5
Django REST Framework
PostgreSQL
Gunicorn
Whitenoise
Authentication
django-allauth
Email Service
SendGrid (SMTP integration)
Admin UI
Django Jazzmin
Environment & Deployment
Render (Cloud deployment)
Environment variables for secure API key storage
dj-database-url
django-environ
python-dotenv
📧 Email Workflow
When a user clicks on a product and submits the inquiry form:
Form data is validated
Email is sent to admin via SendGrid SMTP
Admin receives full customer details
Admin contacts customer manually
🖥️ Admin Capabilities
The admin can manage everything directly from the Django admin panel:
Add / Edit / Delete products
Manage categories
Upload product images
Add custom extra details
Modify hero section content
Manage website content without developer assistance
🔐 Security & Best Practices
API keys stored in environment variables
No sensitive credentials in source code
Production-ready WSGI server (Gunicorn)
Static file management with Whitenoise
PostgreSQL database integration
📈 SEO Optimization
Clean URLs
Optimized meta titles
SEO-friendly product slugs
Structured product pages
🎯 Project Type
Freelance Client Project
Lead Generation Based Business Website
Production Deployment
👨‍💻 Developer
Mayank Rajoriya
Backend Developer | Django | AI Enthusiast