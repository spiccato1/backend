from flask import request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Kona")
#
trainer = ChatterBotCorpusTrainer(bot)
trainer = ListTrainer(bot)

trainer.train([
    "Hi",
    "Hello"
])
trainer.train([
    "How are you?",
    "Good."
])

#
trainer.train("chatterbot.corpus.english")


def getChat(request):
	chatMessage = str(request.args.get('chat'))
	botResponse = str(bot.get_response(chatMessage))
	if botResponse:
	    response, code = {"message": botResponse}, 200
	else:
		response, code = {"message": "No Response"}, 400
	return response, code