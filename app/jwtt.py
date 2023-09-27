import jwt

# Replace these values with your actual secret key and algorithm
SECRET_KEY = "Aa1$2Bb3*Cc4Dd5Ee6Ff7Gg8Hh9Ii0JjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" 
ALGORITHM = "HS256"

# Function to encode a JWT token
def encode_jwt(payload):
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Function to decode a JWT token
def decode_jwt(token):
    print("decode token is ", token)
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
 

# Example usage:
if __name__ == "__main__":
    # Example payload
    payload = {
                "sub": 1,
                "exp": "1695780832"
            }

    # Encode the payload into a JWT token
    encoded_token = encode_jwt(payload)
    # print("Encoded Token:", encoded_token)

    # Decode the JWT token
    decoded_payload = decode_jwt(encoded_token)
    print("Decoded Payload:", decoded_payload)
