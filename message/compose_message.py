""" This function call all of the other functions and composes the message body.

if your custom report modules are in the message folder, then the following import syntax will work:
import message.YourFile as YourFile

You can then call your functions inside the create_text_body() function using the syntax:
YourFile.YourFunction()

"""
import message.countdowns as countdowns		#DEMO
import message.game_scores as game_scores	#DEMO
import message.players_last_game as players_last_game
#from

def create_text_body():
	""" Call the functions that compose the email, building up the body
		of the message step by step and then appending these to """
	body_string = ''

	""" this section calls the demo functions and builds up the
		information I want in my email report (be aware these outputs are all strings)
		substitute in your custom report functions here! """
	day_of_the_year = countdowns.day_of_year()	#DEMO
	day_of_my_life = countdowns.time_alive()	#DEMO
	giants_game = game_scores.get_team_result_text('San Francisco Giants')
	jays_game = game_scores.get_team_result_text('Toronto Blue Jays')	#DEMO
	tigers_game = game_scores.get_team_result_text('Detroit Tigers')
	buster_posey = players_last_game.batter_last_game("poseybu01", "Buster Posey")
	hunter_pence = players_last_game.batter_last_game("pencehu01", "Hunter Pence")

	""" this section adds the strings to the message body
		substitute in the strings you generate here! """
	body_string += 'Countdowns:\n'				#DEMO
	body_string += day_of_the_year					#DEMO
	body_string += day_of_my_life					#DEMO
	body_string += '\n\n' #to add some separation	#DEMO

	body_string += giants_game
	body_string += '\n\n' #to add some separation
	body_string += tigers_game
	body_string += '\n\n' #to add some separation
	body_string += jays_game						#DEMO
	body_string += '\n\n' #to add some separation	#DEMO

	body_string += buster_posey
	body_string += '\n\n' #to add some separation	#DEMO
	body_string += hunter_pence

	return body_string #return the string to email_me.py it is then written into the email
