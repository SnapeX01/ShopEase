import base64

def normalize(data):
    # Reverses the string back to correct Base64
    return data[::-1]

def decode_blob(blob):
    try:
        return base64.b64decode(blob).decode()
    except:
        return None