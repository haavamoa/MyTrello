import json
import os.path


class TrelloSettings:
    @classmethod
    def convert_from_json_to_trello_settings(cls, list_name):
        resource_path = os.path.join(os.path.split(__file__)[0], "resources")

        with open("{}/trello_settings.json".format(resource_path)) as data_file:
            data = json.load(data_file)
            cls.app_key = data['app_key']
            cls.token = data['token']
            cls.list_id = ""
            found_list = False
            available_lists = []
            for list in data['lists']:
                for key, value in list.items():
                    available_lists.append(key)
                    if list_name == key:
                        cls.list_id = value
                        found_list = True
            if not found_list:
                print("List not found, exiting")
                print("Available lists: {}".format(available_lists))
                exit(0)
