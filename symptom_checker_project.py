!pip install openai

import openai #

openai.api_key = " " #add your own api key

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

#after chat bot is trained
def symptomChecker():
  status = input("Are you a patient or a doctor?") 
  while (status.lower() != "patient" and status.lower() != "doctor"):
    status = input("Are you a patient or a doctor?")
  if status.lower()=="doctor":
    symptoms = input("What symptoms are prominent in the patient? Please be specific and separate the list with commas.")
    answer = chatbot("I am a doctor. Give me a diagnosis for a patient suffering from "+symptoms+". Do not tell me anything else other than a diagnosis.")
    print(answer)
    answer = chatbot("What is the best way to treat the patient in the hospital?")
    print(answer)

  else:
    print("Warning: This is not professional medical advice.")
    symptoms = input("What are your abnormal symptoms today? Please be specific and separate your list with commas.")
    answer = chatbot("Give me only the name of the single most likely illness that "+symptoms+" suggest. If there is more than one possibility, only give 3 possibilties, or I will be very sad.")
    print(answer)
    answer = chatbot("Give me 3 of the best at-home treatment options for "+answer+"as well as a recommendation to see a healthcare official.")
    print(answer)

symptomChecker()
