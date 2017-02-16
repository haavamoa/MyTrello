def format_cardname(arguments):
    cardname = ""
    for i in range(2, len(arguments)):
        if not i == 2:
            cardname += " " + arguments[i]
        else:
            cardname += arguments[i]
    return cardname
