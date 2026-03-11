exports.handler = async (event, context) => {
  // Always return success for now to test
  console.log('=== FUNCTION CALLED ===');
  console.log('HTTP Method:', event.httpMethod);
  console.log('Event:', JSON.stringify(event, null, 2));
  
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify({ 
      success: true,
      message: 'Function is working!',
      method: event.httpMethod,
      redirect: '/quote-thank-you/'
    })
  };
};
