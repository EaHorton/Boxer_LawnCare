const sgMail = require('@sendgrid/mail');

exports.handler = async (event, context) => {
  console.log('=== Function invoked ===');
  console.log('Method:', event.httpMethod);
  console.log('Path:', event.path);
  console.log('Body:', event.body);
  
  // Handle CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
      },
      body: ''
    };
  }

  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    console.error('Method not allowed:', event.httpMethod);
    return {
      statusCode: 405,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        error: 'Method Not Allowed',
        received: event.httpMethod,
        expected: 'POST'
      })
    };
  }

  try {
    // Parse form data
    const params = new URLSearchParams(event.body);
    const formData = {
      name: params.get('name'),
      email: params.get('email'),
      phone: params.get('phone'),
      address: params.get('address'),
      lawn_size: params.get('lawn_size')
    };
    
    console.log('Parsed form data:', JSON.stringify(formData));

    // Validate required fields
    if (!formData.name || !formData.email || !formData.phone || !formData.address || !formData.lawn_size) {
      return {
        statusCode: 400,
        headers: { 'Access-Control-Allow-Origin': '*' },
        body: JSON.stringify({ error: 'Missing required fields' })
      };
    }

    // Initialize SendGrid
    const SENDGRID_API_KEY = process.env.SENDGRID_API_KEY;
    const BUSINESS_EMAIL = process.env.BUSINESS_EMAIL || 'nash.jaysona@gmail.com';
    
    if (!SENDGRID_API_KEY) {
      console.error('SendGrid API key not configured');
      return {
        statusCode: 500,
        headers: { 'Access-Control-Allow-Origin': '*' },
        body: JSON.stringify({ error: 'Email service not configured' })
      };
    }

    sgMail.setApiKey(SENDGRID_API_KEY);

    // Email templates
    const prices = {
      small: '$55',
      medium: '$88',
      large: '$135',
      xlarge: '$175'
    };
    
    const price = prices[formData.lawn_size] || prices.medium;
    const emailContent = `Hi ${formData.name},

Thank you for reaching out for a weed control & fertilization quote! The price for your property would be ${price} per application, at 8 applications a year. This would include weed control & fertilization, but I also offer fire ant prevention, flea and tick prevention, grub and army worm control, and aeration at an additional cost. Please let me know if you have any questions and I look forward to working with you.

Thank you!`;

    // Email to customer
    const customerEmail = {
      to: formData.email,
      from: BUSINESS_EMAIL,
      subject: template.subject,
      text: emailContent,
      html: emailContent.replace(/\n/g, '<br>')
    };
JSON.stringify(formData)
    // Email to business owner
    const businessEmail = {
      to: BUSINESS_EMAIL,
      from: BUSINESS_EMAIL,
      subject: `New Instant Quote Request - ${formData.name}`,
      text: `New instant quote request received:

Name: ${formData.name}
Email: ${formData.email}
Phone: ${formData.phone}
Address: ${formData.address}
Lawn Size: ${formData.lawn_size}

Estimated Quote Sent: ${price} per application`,
      html: `<h2>New Instant Quote Request</h2>
<p><strong>Name:</strong> ${formData.name}</p>
<p><strong>Email:</strong> ${formData.email}</p>
<p><strong>Phone:</strong> ${formData.phone}</p>
<p><strong>Address:</strong> ${formData.address}</p>
<p><strong>Lawn Size:</strong> ${formData.lawn_size}</p>
<p><strong>Estimated Quote Sent:</strong> ${price} per application</p>`
    };

    // Send both emails
    console.log('Sending emails...');
    await Promise.all([
      sgMail.send(customerEmail),
      sgMail.send(businessEmail)
    ]);
    
    console.log('Emails sent successfully');

    // Return success response with redirect
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({ success: true, redirect: '/quote-thank-you/' })
    };

  } catch (error) {
    console.error('Error processing form:', error);
    
    return {
      statusCode: 500,
      headers: { 'Access-Control-Allow-Origin': '*' },
      body: JSON.stringify({ 
        error: 'Failed to process form submission',
        details: error.message 
      })
    };
  }
};
