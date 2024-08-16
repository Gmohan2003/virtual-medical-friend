from flask import Flask,request
from whatsapp_responses import responses
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/bot", methods=["POST"])

# chatbot logic
def bot():

	# user input
	user_msg = request.values.get('Body', '')

	# creating object of MessagingResponse
	response = MessagingResponse()
    
   
	msg= response.message()
    
	# User Query
	q = user_msg
	bot_response = responses(q)

	# list to store urls


	# searching and storing urls


	# displaying result
	#msg.body(f"--- Result for '{user_msg}' are ---")

	msg.body(bot_response)

	return str(response)


if __name__ == "__main__":
	app.run(debug=True)
