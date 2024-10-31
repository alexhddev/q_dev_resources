# Function that parses emails:
import email

def parse_email(file_path):
    with open(file_path, 'r') as f:
        msg = email.message_from_file(f)

        # access email headers
        print("From:", msg['From'])
        print("To:", msg['To'])
        print("Subject:", msg['Subject'].upper())
        # access email body:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    print("Body:", body)

        
        else:
            body = msg.get_payload(decode=True).decode()
            print("Body:", body)

parse_email('email.eml')

