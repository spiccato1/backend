from flask import request

user1 = {
	"id": 1,
	"firstName": "Jonathon",
	"lastName": "Wert",
	"email": "jwert@thecoderschool.com"
}
user2 = {
	"id": 2,
	"firstName": "Thomas",
	"lastName": "Weber",
	"email": "thomas@gmail.com"
}
user3 = {
	"id": 3,
	"firstName": "Ace",
	"lastName": "Ventura",
	"email": "ace@gmail.com"
}

def getUser(request):
	uid = str(request.args.get('uid'))
	if uid in ["1","2","3"]:
		if uid == "1":
			profile = user1
		if uid == "2":
			profile = user2
		if uid == "3":
			profile = user3
		response, code = profile, 201
	else:
		response, code = {"message": "No User"}, 400
	return response, code