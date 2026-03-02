# Automated Quote Email Setup Instructions

This guide will help you set up automated emails with custom pricing based on lawn size.

## Setup Steps

### 1. Create a SendGrid Account (Free)
1. Go to https://sendgrid.com/
2. Sign up for a free account (100 emails/day free forever)
3. Verify your email address

### 2. Get Your SendGrid API Key
1. Log into SendGrid dashboard
2. Go to Settings → API Keys
3. Click "Create API Key"
4. Name it "Boxer Lawn Website"
5. Select "Full Access" or "Mail Send" permissions
6. Click "Create & View"
7. **IMPORTANT:** Copy the API key immediately (you can't see it again!)

### 3. Verify Sender Email
1. In SendGrid, go to Settings → Sender Authentication
2. Click "Verify a Single Sender"
3. Enter your business email (e.g., info@boxerlawnandlandscape.com)
4. Fill out the form with your business details
5. Check your email and click the verification link

### 4. Configure Netlify Environment Variables
1. Log into your Netlify dashboard
2. Go to your site → Site settings → Environment variables
3. Add these variables:
   - Variable: `SENDGRID_API_KEY`
     Value: [paste your SendGrid API key]
   - Variable: `BUSINESS_EMAIL`
     Value: info@boxerlawnandlandscape.com (or your preferred email)
4. Click "Save"

### 5. Install Dependencies Locally
Run this in your terminal:
```bash
cd netlify/functions
npm install
cd ../..
```

### 6. Deploy to Netlify
```bash
git add .
git commit -m "Add automated quote emails"
git push
```

Netlify will automatically:
- Install the dependencies
- Deploy the serverless function
- Make it available at `/.netlify/functions/submit-quote`

### 7. Test the System
1. Go to your live website
2. Fill out the instant quote form
3. Submit it
4. Check the customer's email inbox (including spam folder)
5. Check your business email inbox

## Email Templates

The system automatically sends personalized pricing emails based on lawn size:

- **Small Lawn (up to 5.5k sqft)**: $55 per application
- **Medium Lawn (5.5k - 10k sqft)**: $88 per application
- **Large Lawn (10k - 15k sqft)**: $135 per application
- **Extra Large Lawn (15k - 25k sqft)**: $175 per application

Each customer receives a personalized email that begins with their name and includes the specific price for their selected lawn size.

## Customizing Email Templates

To change the pricing or email content:
1. Edit `netlify/functions/submit-quote.js`
2. Find the `emailTemplates` object
3. Update the pricing or text for each lawn size
4. Save and redeploy

## Troubleshooting

**Emails not sending?**
- Check that SENDGRID_API_KEY is set in Netlify
- Verify that BUSINESS_EMAIL is set correctly
- Make sure your sender email is verified in SendGrid
- Check Netlify Function logs: Site → Functions → submit-quote

**Form not

 submitting?**
- Check browser console for errors
- Verify Netlify functions are deployed
- Check that the form action is `/.netlify/functions/submit-quote`

**Customer not receiving emails?**
- Check spam folder
- Verify email address was entered correctly
- Check SendGrid activity log

## Cost
- **SendGrid Free Tier**: 100 emails/day forever (50 customer + 50 business notifications)
- **If you need more**: SendGrid paid plans start at $15/month for 40,000 emails

## Support
- SendGrid Docs: https://docs.sendgrid.com/
- Netlify Functions Docs: https://docs.netlify.com/functions/overview/
