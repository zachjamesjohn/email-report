import message.brscraper.brscraper as brscraper

def batter_last_game():

    scraper = brscraper.BRScraper()
    #This is the url that will be used
    #data = scraper.parse_tables("/players/gl.fcgi?id=poseybu01&t=b&year=2020")
    data = scraper.parse_tables("/players/gl.fcgi?id=poseybu01&t=b&year=2019")


    message = "On " + data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["Date"] + " Buster Posey went " +  data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["H"] + " for " + data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["AB"] + " last night against " + data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["Opp"]  +" with"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["HR"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["HR"]
        message += " HR"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["2B"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["2B"]
        message += " 2B"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["3B"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["3B"]
        message += " 3B "

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["RBI"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["RBI"]
        message += " RBI"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["R"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["R"]
        message += " R"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["BB"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["BB"]
        message += " BB"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["SO"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["SO"]
        message += " SO"

    if (((int(data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["SB"]))) > 0):
        message += ", "
        message += data["batting_gamelogs"][(len(data["batting_gamelogs"]) - 1)]["SB"]
        message += " SB"

    #Lastest Slash Numbers are the season stat line
    message += ". This season he's hitting "
    message += data["batting_gamelogs"][(len(data["batting_gamelogs"])) -1]["BA"]
    message += "/"

    message += data["batting_gamelogs"][(len(data["batting_gamelogs"])) -1]["OBP"]
    message += "/"

    message += data["batting_gamelogs"][(len(data["batting_gamelogs"])) -1]["SLG"]
    message += " with a "

    message += data["batting_gamelogs"][(len(data["batting_gamelogs"])) -1]["OPS"]
    message += " OPS."

    return message
