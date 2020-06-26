import os

def read_note_to_standard(input_filename):
    global KALIMBA
    with open(input_filename, "r") as the_input:
        buffer = ""
        for line in the_input:
            if line.startswith("#"):
                continue
            data = line.strip()
            buffer = buffer + data + " "
        buffer = buffer.strip()
        if buffer.startswith("("):
            buffer = "['" + buffer[1:]
        if buffer.endswith(")"):
            buffer = buffer[:-1] + "']"
        note_standard = eval("[" + buffer.replace(") (","'],['").replace(" (","',['").replace(") ","'],'").replace(" ","','") + "]")
        return note_standard


def read_all_config():
    global KALIMBA
    for item in os.listdir("config"):
        kalimba_name = item
        KALIMBA[kalimba_name]={
            "notes":[],
            "orders":None
        }
        file_path = os.path.join("config", item)
        with open(file_path, "r") as the_config:
            KALIMBA[kalimba_name]["orders"] = eval(the_config.readline())
            for line in the_config:
                data = line.strip().split()
                KALIMBA[kalimba_name]["notes"].append(data)


def draw_tabs(tabs, song_name, ktype, setting):
    with open(os.path.join("tabs", "_".join([song_name, ktype, str(setting)])), "w") as the_output:
        for line in tabs:
            line[8] = [line[8]]
            the_output.write(str(line) + "\n")


def gen_tabs(notes, song_name, ktype, setting):
    global KALIMBA
    kalimba = KALIMBA[ktype]
    kalimba_notes = []
    tabs = []
    for i in kalimba["notes"]:
        kalimba_notes.append(i[setting])
    for item in notes:
        if type(item) is str:
            line = [0] * 17
            line[kalimba_notes.index(item)] = 1
            tabs.append(line)
        if type(item) is list:
            line = [0] * 17
            for tmp in item:
                line[kalimba_notes.index(tmp)] = 1
            tabs.append(line)
    tabs.reverse()
    draw_tabs(tabs, song_name, ktype, setting)


if __name__ == "__main__":
    KALIMBA = {}
    read_all_config()
    for item in os.listdir("notes"):
        song_name, ktype, setting = item.split("-")
        notes = read_note_to_standard(os.path.join("notes",item))
        gen_tabs(notes, song_name, ktype, int(setting))
