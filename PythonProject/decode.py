import base64

# The Base64 encoded string
encoded_string = "AAMkAGQ0M2FiMDc5LWMxZTItNDZmMC04MDU2LWIyZGQ3MjlmYWJmOABGAAAAAABFFLrbKG50Tp6+QfJSsrTVBwBTq30XwAIYT6r0baa+/eJdAAAAAAEMAABTq30XwAIYT6r0baa+/eJdAAB2hXdNAAA="

# Decode the string
decoded_bytes = base64.b64decode(encoded_string)

# Convert to string if it represents text
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

# Print the decoded string
print(decoded_string)
