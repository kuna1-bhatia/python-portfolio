import google.generativeai as genai

API_KEY = "AIzaSyAk7SV_k9OnSotEL25woCDuvVaq_huPo7w"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()
response = chat.send_message("Your Name is Kairu AI from today")
while True:
    try:
        user = input("YOU : ").lower()
        if user == "exit":
            print("Kairu : Chat ended Goodbaye!")
            break
        response = chat.send_message(user)
        print("Kairu :", response.text)
    
    except ValueError:
        print("PLEASE ENTER VALID VALUE")
                


