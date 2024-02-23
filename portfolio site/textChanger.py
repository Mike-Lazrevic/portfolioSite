def change_char():
    with open("sourceM.txt", "r") as source_mario:
        mario_char = source_mario.readline().strip()

    with open("sourceE.txt", "r") as source_empty:
        empty_char = source_empty.readline().strip()

    with open("sourceT.txt", "r") as source_treasure:
        treasure_char = source_treasure.readline().strip()

    with open("InputData.txt", "r+") as input_data:
        lines = input_data.readlines()
        lines[5] = " " + treasure_char + " " + '\n'
        lines[6] = " " + mario_char + " " + '\n'
        lines[4] = " " + empty_char + " " + '\n'

        input_data.seek(0)
        input_data.writelines(lines)
        input_data.truncate()

change_char()
