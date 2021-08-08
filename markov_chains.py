import PySimpleGUI as sg
import nltk, re, random
from nltk.tokenize import word_tokenize
from collections import defaultdict, deque

sg.change_look_and_feel('TealMono')

layout1 = [[sg.Text("How many songs would you like to use?")],
          [sg.Text("The range is between 1 to 5 songs")],
          [sg.Input()],
          [sg.Button('Ok')]]

window = sg.Window('Lyricify', layout1)

event, values = window.read()

window.close()


if int(values[0]) == 1:
    layout1 = [[sg.Text("Please insert the lyrics of your first song")],
               [sg.Input()],
               [sg.Button('Ok')]]

    window = sg.Window('Lyricify', layout1)

    event, values = window.read()

    window.close()


    def markov_chain():

        class markov_chain:
            def __init__(self):
                self.lookup_dict = defaultdict(list)
                self._seeded = False
                self.seed_me_()

            def seed_me_(self, rand_seed=None):
                if self._seeded is not True:
                    try:
                        if rand_seed is not None:
                            random.seed(rand_seed)
                        else:
                            random.seed()
                        self._seeded = True
                    except NotImplementedError:
                        self._seeded = False

            def add_song_lyrics(self, str):
                preprocessed_lyrics_list = self.preprocess_lyrics(str)
                generate_pairs = self.generate_tuple_keys(preprocessed_lyrics_list)
                for pair in generate_pairs:
                    self.lookup_dict[pair[0]].append(pair[1])

            def preprocess_lyrics(self, str):
                cleaned = re.sub(r'\W+', ' ', str).lower()
                tokenized = word_tokenize(cleaned)
                return tokenized

            def generate_tuple_keys(self, data):
                if len(data) < 1:
                    return

                for i in range(len(data) - 1):
                    yield [data[i], data[i + 1]]

            def generate_lyrics(self, max_length=50):
                context = deque()
                output = []
                if len(self.lookup_dict) > 0:
                    self.seed_me_(rand_seed=len(self.lookup_dict))
                    chained_head = [list(self.lookup_dict)[0]]
                    context.extend(chained_head)

                    while len(output) < (max_length - 1):
                        next_choices = self.lookup_dict[context[-1]]
                        if len(next_choices) > 0:
                            next_word = random.choice(next_choices)
                            context.append(next_word)
                            output.append(context.popleft())
                        else:
                            break
                    output.extend(list(context))
                return " ".join(output)

        my_markov = markov_chain()
        my_markov.add_song_lyrics(str(values[0]))
        generated_text = my_markov.generate_lyrics()

        return generated_text

    name = markov_chain()
    layout2 = [[sg.Text(f"Here are the lyrics to your new song: {name}")],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout2)

    event, values = window.read()

    window.close()



elif int(values[0]) == 2:
    layout1 = [[sg.Text("Please insert the lyrics of your first song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your song song")],
               [sg.Input()],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout1)

    event, values = window.read()

    window.close()


    def markov_chain():

        class markov_chain:
            def __init__(self):
                self.lookup_dict = defaultdict(list)
                self._seeded = False
                self.seed_me_()

            def seed_me_(self, rand_seed=None):
                if self._seeded is not True:
                    try:
                        if rand_seed is not None:
                            random.seed(rand_seed)
                        else:
                            random.seed()
                        self._seeded = True
                    except NotImplementedError:
                        self._seeded = False

            def add_song_lyrics(self, str):
                preprocessed_lyrics_list = self.preprocess_lyrics(str)
                generate_pairs = self.generate_tuple_keys(preprocessed_lyrics_list)
                for pair in generate_pairs:
                    self.lookup_dict[pair[0]].append(pair[1])

            def preprocess_lyrics(self, str):
                cleaned = re.sub(r'\W+', ' ', str).lower()
                tokenized_lyrics = word_tokenize(cleaned)
                return tokenized_lyrics

            def generate_tuple_keys(self, data):
                if len(data) < 1:
                    return

                for i in range(len(data) - 1):
                    yield [data[i], data[i + 1]]

            def generate_lyrics(self, max_length=50):
                context = deque()
                output = []
                if len(self.lookup_dict) > 0:
                    self.seed_me_(rand_seed=len(self.lookup_dict))
                    chained_head = [list(self.lookup_dict)[0]]
                    context.extend(chained_head)

                    while len(output) < (max_length - 1):
                        next_choices = self.lookup_dict[context[-1]]
                        if len(next_choices) > 0:
                            next_word = random.choice(next_choices)
                            context.append(next_word)
                            output.append(context.popleft())
                        else:
                            break
                    output.extend(list(context))
                return " ".join(output)

        my_markov = markov_chain()
        my_markov.add_song_lyrics(str(values[0]))
        my_markov.add_song_lyrics(str(values[1]))
        generated_text = my_markov.generate_lyrics()

        return generated_text


    name = markov_chain()
    layout2 = [[sg.Text(f"Here are the lyrics to your new song: {name}")],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout2)

    event, values = window.read()

    window.close()


elif int(values[0]) == 3:
    layout1 = [[sg.Text("Please insert the lyrics of your first song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your second song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your third song")],
               [sg.Input()],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout1)

    event, values = window.read()

    window.close()


    def markov_chain():

        class markov_chain:
            def __init__(self):
                self.lookup_dict = defaultdict(list)
                self._seeded = False
                self.seed_me_()

            def seed_me_(self, rand_seed=None):
                if self._seeded is not True:
                    try:
                        if rand_seed is not None:
                            random.seed(rand_seed)
                        else:
                            random.seed()
                        self._seeded = True
                    except NotImplementedError:
                        self._seeded = False

            def add_song_lyrics(self, str):
                preprocessed_lyrics_list = self.preprocess_lyrics(str)
                generate_pairs = self.generate_tuple_keys(preprocessed_lyrics_list)
                for pair in generate_pairs:
                    self.lookup_dict[pair[0]].append(pair[1])

            def preprocess_lyrics(self, str):
                cleaned = re.sub(r'\W+', ' ', str).lower()
                tokenized_lyrics = word_tokenize(cleaned)
                return tokenized_lyrics

            def generate_tuple_keys(self, data):
                if len(data) < 1:
                    return

                for i in range(len(data) - 1):
                    yield [data[i], data[i + 1]]

            def generate_lyrics(self, max_length=50):
                context = deque()
                output = []
                if len(self.lookup_dict) > 0:
                    self.seed_me_(rand_seed=len(self.lookup_dict))
                    chained_head = [list(self.lookup_dict)[0]]
                    context.extend(chained_head)

                    while len(output) < (max_length - 1):
                        next_choices = self.lookup_dict[context[-1]]
                        if len(next_choices) > 0:
                            next_word = random.choice(next_choices)
                            context.append(next_word)
                            output.append(context.popleft())
                        else:
                            break
                    output.extend(list(context))
                return " ".join(output)

        my_markov = markov_chain()
        my_markov.add_song_lyrics(str(values[0]))
        my_markov.add_song_lyrics(str(values[1]))
        my_markov.add_song_lyrics(str(values[2]))
        generated_text = my_markov.generate_lyrics()

        return generated_text


    name = markov_chain()
    layout2 = [[sg.Text(f"Here are the lyrics to your new song: {name}")],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout2)

    event, values = window.read()

    window.close()


elif int(values[0]) == 4:
    layout1 = [[sg.Text("Please insert the lyrics of your first song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your second song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your third song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your fourth song")],
               [sg.Input()],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout1)

    event, values = window.read()

    window.close()


    def markov_chain():

        class markov_chain:
            def __init__(self):
                self.lookup_dict = defaultdict(list)
                self._seeded = False
                self.seed_me_()

            def seed_me_(self, rand_seed=None):
                if self._seeded is not True:
                    try:
                        if rand_seed is not None:
                            random.seed(rand_seed)
                        else:
                            random.seed()
                        self._seeded = True
                    except NotImplementedError:
                        self._seeded = False

            def add_song_lyrics(self, str):
                preprocessed_lyrics_list = self.preprocess_lyrics(str)
                generate_pairs = self.generate_tuple_keys(preprocessed_lyrics_list)
                for pair in generate_pairs:
                    self.lookup_dict[pair[0]].append(pair[1])

            def preprocess_lyrics(self, str):
                cleaned = re.sub(r'\W+', ' ', str).lower()
                tokenized_lyrics = word_tokenize(cleaned)
                return tokenized_lyrics

            def generate_tuple_keys(self, data):
                if len(data) < 1:
                    return

                for i in range(len(data) - 1):
                    yield [data[i], data[i + 1]]

            def generate_lyrics(self, max_length=50):
                context = deque()
                output = []
                if len(self.lookup_dict) > 0:
                    self.seed_me_(rand_seed=len(self.lookup_dict))
                    chained_head = [list(self.lookup_dict)[0]]
                    context.extend(chained_head)

                    while len(output) < (max_length - 1):
                        next_choices = self.lookup_dict[context[-1]]
                        if len(next_choices) > 0:
                            next_word = random.choice(next_choices)
                            context.append(next_word)
                            output.append(context.popleft())
                        else:
                            break
                    output.extend(list(context))
                return " ".join(output)

        my_markov = markov_chain()
        my_markov.add_song_lyrics(str(values[0]))
        my_markov.add_song_lyrics(str(values[1]))
        my_markov.add_song_lyrics(str(values[2]))
        my_markov.add_song_lyrics(str(values[3]))
        generated_text = my_markov.generate_lyrics()

        return generated_text


    name = markov_chain()
    layout2 = [[sg.Text(f"Here are the lyrics to your new song: {name}")],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout2)

    event, values = window.read()

    window.close()


elif int(values[0]) == 5:
    layout1 = [[sg.Text("Please insert the lyrics of your first song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your second song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your third song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your fourth song")],
               [sg.Input()],
               [sg.Text("Please insert the lyrics of your fifth song")],
               [sg.Input()],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout1)

    event, values = window.read()

    window.close()

    def markov_chain():

        class markov_chain:
            def __init__(self):
                self.lookup_dict = defaultdict(list)
                self._seeded = False
                self.seed_me_()

            def seed_me_(self, rand_seed=None):
                if self._seeded is not True:
                    try:
                        if rand_seed is not None:
                            random.seed(rand_seed)
                        else:
                            random.seed()
                        self._seeded = True
                    except NotImplementedError:
                        self._seeded = False

            def add_song_lyrics(self, str):
                preprocessed_lyrics_list = self.preprocess_lyrics(str)
                generate_pairs = self.generate_tuple_keys(preprocessed_lyrics_list)
                for pair in generate_pairs:
                    self.lookup_dict[pair[0]].append(pair[1])

            def preprocess_lyrics(self, str):
                cleaned = re.sub(r'\W+', ' ', str).lower()
                tokenized_lyrics = word_tokenize(cleaned)
                return tokenized_lyrics

            def generate_tuple_keys(self, data):
                if len(data) < 1:
                    return

                for i in range(len(data) - 1):
                    yield [data[i], data[i + 1]]

            def generate_lyrics(self, max_length=50):
                context = deque()
                output = []
                if len(self.lookup_dict) > 0:
                    self.seed_me_(rand_seed=len(self.lookup_dict))
                    chained_head = [list(self.lookup_dict)[0]]
                    context.extend(chained_head)

                    while len(output) < (max_length - 1):
                        next_choices = self.lookup_dict[context[-1]]
                        if len(next_choices) > 0:
                            next_word = random.choice(next_choices)
                            context.append(next_word)
                            output.append(context.popleft())
                        else:
                            break
                    output.extend(list(context))
                return " ".join(output)

        my_markov = markov_chain()
        my_markov.add_song_lyrics(str(values[0]))
        my_markov.add_song_lyrics(str(values[1]))
        my_markov.add_song_lyrics(str(values[2]))
        my_markov.add_song_lyrics(str(values[3]))
        my_markov.add_song_lyrics(str(values[4]))
        generated_text = my_markov.generate_lyrics()

        return generated_text


    name = markov_chain()
    layout2 = [[sg.Text(f"Here are the lyrics to your new song: {name}")],
               [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout2)

    event, values = window.read()

    window.close()


else:
    layout = [[sg.Text("Please insert a valid number of songs")],
    [sg.Button('Ok')]]
    window = sg.Window('Lyricify', layout)

    event, values = window.read()

    window.close()


