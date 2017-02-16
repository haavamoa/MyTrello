# MyTrello
A very simple way of adding your own lists in a JSON file and create a new card on that list.

## Requirements:
* trello3 - https://github.com/waynew/trello3

## Usage:
* Rename `resources/trello_settings_template.json` to `trello_settings.json`
* Collect your Trello app-key from [this link](https://trello.com/app-key), save it in `trello_settings.json` as `app_key`
* Collect your Trello token key from [this link](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=1b3d47e13dfe37256a5f0ab4b8d50dd1) , save it in `trello_settings.json` as `token` 
* Collect your desired list id's from [Trello sandbox](https://developers.trello.com/sandbox/). Use their sandbox to get lists on boards. Tip: Board id's can be found in the hyperlink of a board when you open [Trello.com](https://trello.com/) and select a board.
* Add a desired name of the list and its id in `trello_settings.json`
* Run `main.py <list_name> <name__of_card>` to add a card to that list.
