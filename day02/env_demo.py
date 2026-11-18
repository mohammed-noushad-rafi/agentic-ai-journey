import os
from dotenv import load_dotenv
load_dotenv
key=os.getenv("MY_TEST_KEY")
if key is None:
    print("Key missing! Check your .env file")
else:
    print(f"Key loaded: {key[:4]}...")