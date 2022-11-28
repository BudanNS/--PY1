import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE) -> list[dict]:
        with open(INPUT_FILE, "r") as in_f:
            dict = []
            for line in in_f:
                line = line.replace("\n", "")
                dict.append(line.split(','))
            for i in range(1, len(dict)):
                dict[i] = dict(zip(dict[0], dict[i]))
        return dict
# TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
