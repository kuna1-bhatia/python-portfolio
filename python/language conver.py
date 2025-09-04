import google.generativeai as genai

API_KEY = "AIzaSyAk7SV_k9OnSotEL25woCDuvVaq_huPo7w"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

try:
    code = input("Enter your code that wanna convert = ").lower()
    lang = input("Enter language = ").lower()

    response = chat.send_message(f"conver this code {code} into {lang} code")
    print("AM :", response.text)

except ValueError:
    print("Please enter valid code")  
    