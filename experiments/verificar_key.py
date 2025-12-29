from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("DEEPSEEK_API_KEY")
print("KEY existe:", key is not None)
print("LARGO:", len(key) if key else "None")
