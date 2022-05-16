from urllib.request import urlopen
import json
import pandas as pd
import matplotlib.pyplot as plt

class TrainerDex:
    """
    Welcome to TrainerDex! This is an OOP program to retrieve Pokemon Trainers data
    from online JSON and show you how the trainers compare to each other by
    looking at their level (experience/skill), PokeDex (number of Pokemons "explored"),
    and number of Pokemons owned.
    """
    def __init__(self):
        """
        Gym is a container for individual trainers split up from JSON object
        data_frame is container of pandas type data of multiple values/series
        These are filled in by __retrieve_data method.
        """
        self.__gym = []
        self.__data_frame =  {"Name": [], "Level": [], "PokeDex": [], "Pokemons": []}

    def start_program(self) -> None:
        """
        Accessed by user to get the magic started, AKA controller code
        """
        self.__retrieve_data()
        self.__menu()

    def __retrieve_data(self) -> None:
        """
        Access online JSON file for data then process into this class's container
        """
        url = 'http://ec2-54-83-124-106.compute-1.amazonaws.com:5000/character/?format=json'
        with urlopen(url) as response:
            info = json.load(response)

        for trainer in info:
            self.__gym.append(trainer)
            self.__data_frame["Name"].append(trainer['name'])
            self.__data_frame["Level"].append(trainer['level'])
            self.__data_frame["PokeDex"].append(trainer['pokedex'])
            self.__data_frame["Pokemons"].append(trainer['pokemons'])
        self.__data_frame = pd.DataFrame(self.__data_frame)

    def __menu(self) -> None:
        """
        Menu controller code for user selections, to access series or data frame of pandas style analysis
        """
        print("""\n    Welcome to TrainerDex! See data on all the trainers' progress. 
    Who is catching them all?""")
        choice = -1
        while choice != "0":
            choice = input("\n    Single or multiple data sets?\n    Enter 1 or 2. To quit enter 0: ").strip()
            if choice not in ("0", "1", "2"):
                choice = input("    Enter 0, 1 or 2 please: ")
            elif choice == "1": self.__series_selection()
            elif choice == "2": self.__dataframe_selection()
        print('\nGood bye! Come again!\n')

    def __series_selection(self) -> None:
        """
        Sub-menu for 1-dimensional data selection, activates analysis method.
        """
        input_query = """\n    See trainers' ranked by: 
            1. Level (experience/skill)
            2. PokeDex count
            3. Pokemon count
            0. Exit

            Enter 1, 2, 3, or 0: """
        input_s = -1
        while input_s != "0":
            input_s = input(input_query).strip()
            if input_s in ("1", "2", "3"):
                self.__series_analysis(input_s)
                input_s = -1

    def __series_analysis(self, selection: str) -> None:
        """
        1-dimensional data analysis by showing you data in horizontal bar charts!
        :param selection: picks of data type to display from __series_selection method
        :param type: str
        :return: None
        """
        ref = {"1":"level", "2":"pokedex", "3":"pokemons"}
        pick = ref[selection]
        series_data = {}
        for trainer in self.__gym:
            series_data[trainer['name']] = trainer[pick]
        s_pd = pd.Series(series_data).sort_values(ascending=False)
        
        print(f'\n{s_pd}')
        ax = s_pd.plot.barh()
        ax = ax.invert_yaxis()
        plt.title(f"Trainers Ranked by {pick.capitalize()}")
        plt.show()

    def __dataframe_selection(self) -> None:
        """
        Sub-menu for 2-data type analysis and choices of visual displays!
        Passes in these choices and triggers the dataframe_analysis method.
        """
        pick_query = """\n    Which 2 data sets do you want to look at?
    1. Levels
    2. PokeDex
    3. Pokemons
    0. Quit

    Enter 2 numbers e.g. "1 3", or "0" to quit: """
        method_query = """\n    What method to you want to see?
    1. Scatter diagram
    2. Line chart
    3. Bar chart
    4. Pie chart
    0. Quit
    
    Enter a number 0 to 4: """
        pick = a = b = method = -1
        p_choices = ("1", "2", "3", "0")
        m_choices = ("1", "2", "3", "4", "0")
        while True:    
            print(f'\n{self.__data_frame}')

            while a not in p_choices and b not in p_choices:
                pick = input(pick_query).strip()
                if len(pick) == 3 and ' ' in pick: 
                    a, b = pick.split(' ')
                elif pick == "0": return 

            while method not in m_choices:
                method = input(method_query).strip()
                if method == "0": return
            self.__dataframe_analysis(a, b, method)
            a = b = method = -1
  
    def __dataframe_analysis(self, a: str, b: str, method: str) -> None:
        """
        Here's where we show you the money! Selected 2 data types are displayed in chosen methods
        :param a: one of 3 data types chosen, see p_ref
        :param type: str
        :param b: one of 3 data types chosen, see p_ref
        :param type: str
        :param method: type of display to show relationship between a and b
        :param type: str
        :return: None
        """
        p_ref = {"1": "Level", "2": "PokeDex", "3": "Pokemons"}
        m_ref = {"1": "scatter", "2": "line", "3": "bar", "4": "pie"}
        a = p_ref[a]
        b = p_ref[b]
        method = m_ref[method]

        # Extra sorting needed for line and pie visuals
        temp = None
        if method in ("line", "pie"):
            temp = self.__data_frame
            self.__data_frame = self.__data_frame.groupby(b)[a].sum() 
        self.__data_frame.sort_index().plot(x=a, y=b, kind=method,
            title=f"{a} vs {b} by {method.capitalize()}", legend=True)
        plt.show()
        
        if temp is not None: 
            self.__data_frame, temp = temp, None
    
if __name__ == "__main__":
    t = TrainerDex()
    t.start_program()