

const bucketName = process.env.MESSAGE_BUCKET;

// simple aws lambda handler
async function handler(event, context) {
  console.log(bucketName)
  const response = {
    statusCode: 200,
    body: JSON.stringify('Hello from Lambda!'),
  };
  return response;
}

export { handler };