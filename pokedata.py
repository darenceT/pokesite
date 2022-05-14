from urllib.request import urlopen
import json
import pandas as pd


class Trainer:
    def __init__(self, data):
        self.__name = data['name']
        self.__level = data['level']
        self.__pokedex = data['pokedex']
        self.__pokemons = data['pokemons']

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level

    @property
    def pokedex(self):
        return self.__pokedex

    @property
    def pokemons(self):
        return self.__pokemons

    def __str__(self):
        return f"""
Name: {self.__name}
Level: {self.__level}
PokeDex: {self.__pokedex}
Pokemons: {self.__pokemons}"""

class TrainerDex:
    def __init__(self):
        self.__gym = []

    def start_program(self):
        self.__retrieve_data()
        self.__menu()

    def __retrieve_data(self):
        url = 'http://ec2-44-202-93-255.compute-1.amazonaws.com:5000/character/?format=json'
        with urlopen(url) as response:
            info = json.load(response)
        for person in info:
            self.__gym.append(person)
            # self.__gym.append(Trainer(person)) 

    def __menu(self):
        print("""\n    Welcome to TrainerDex! See data on all the trainers' progress. 
    Who is catching them all?""")
        choice = -1
        while choice != "0":
            choice = input("\n    Single or multiple data sets?\n    Enter 1 or 2. To quit enter 0: ").strip()
            if choice not in ("0", "1", "2"):
                choice = input("    Enter 0, 1 or 2 please: ")
            elif choice == "1": self.__series_selection()
            elif choice == "2": self.__df_selection()
            elif choice == "0": break

    def __series_selection(self):
        input_query = """\n    See trainers' ranked by: 
            1. Level (experience/skill)
            2. PokeDex count
            3. Pokemon count
            4. Exit

            Enter 1, 2, 3, or 4: """

        input_s = input(input_query).strip()
        while input_s != "4":
            if input_s in ("1", "2", "3"):
                self.__series_analysis(input_s)
            input_s = input(input_query)

    def __df_selection(self):
        pass

    def __series_analysis(self, selection):
        ref = {"1":"level", "2":"pokedex", "3":"pokemons"}
        pick = ref[selection]
        series_data = {}
        for trainer in self.__gym:
            series_data[trainer['name']] = trainer[pick]
        series_in_pd = pd.Series(series_data)
        print(f'\n\n{series_in_pd.sort_values(ascending=False)}')

if __name__ == "__main__":
    t = TrainerDex()
    t.start_program()