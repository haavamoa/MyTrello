from trello import TrelloApi
from format_cardname import *
import sys
from trello_settings import TrelloSettings

############
# Arguments
############

if len(sys.argv) != 3:
    print("Wrong number of arguments, expected 2")
    print("Arguments: list name, card name")
    print("Exiting")
    exit(0)
list_name = sys.argv[1]
card_name = format_cardname(arguments=sys.argv)

######################################################
# Get trello settings and convert from json to object
######################################################
trello_settings = TrelloSettings()
trello_settings.convert_from_json_to_trello_settings(list_name)
#######################################
# Add card to list with trello settings
#######################################
trello = TrelloApi(trello_settings.app_key, trello_settings.token)
trello.cards.new(card_name, trello_settings.list_id)


##############
# Print output
##############
output = 'Card({}) ==> {}.todo'.format(card_name, list_name)
print(output)
