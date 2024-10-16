import { PutObjectCommand, S3Client, ListObjectsV2Command } from "@aws-sdk/client-s3";

const s3Client = new S3Client()
const messagesBucket = process.env.MESSAGES_BUCKET

async function handler(event, context) {

    try {
        switch (event.httpMethod) {
            case 'GET':
                // get all the files in the bucket
                const listObjectsCommand = new ListObjectsV2Command({ Bucket: messagesBucket });
                const response = await s3Client.send(listObjectsCommand);
    
                return {
                    statusCode: 200,
                    body: JSON.stringify(response.Contents)
                };
            case 'POST':
                if (event.body) {
                    const command = new PutObjectCommand({
                        Bucket: process.env.MESSAGES_BUCKET,
                        Key: `${Date.now()}.json`,
                        Body: event.body
                    });
                    const response = await s3Client.send(command);
                    return {
                        statusCode: 200,
                        body: JSON.stringify({ message: 'File uploaded successfully', response })
                    };
                }
                break;
    
            default:
                return{
                    statusCode: 405,
                    body: JSON.stringify({ message: 'Method Not Allowed' })
                };
        }
    } catch (error) {
        console.error(error);
    }

    return {
        statusCode: 500,
        body: JSON.stringify({ message: 'internal server error' })
    }    
}

export { handler }