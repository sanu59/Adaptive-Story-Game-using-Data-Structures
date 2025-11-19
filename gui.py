import tkinter as tk
from tkinter import PhotoImage
import json

class StoryGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Adaptive Story Game")

        self.background_images = {
            'default': PhotoImage(file=r"C:\Users\sanu\Downloads\pexels-riccardo-69903.png"),
            'Bone': PhotoImage(file=r"C:\Users\sanu\Downloads\Left_femur_of_extinct_elephant,_Alaska,_Ice_Age_Wellcome_L0057714.png"),
            'Painting':PhotoImage(file=r"C:\Users\sanu\Downloads\imageyo.png")
        }

        self.background_label = tk.Label(master, image=self.background_images['default'])
        self.background_label.place(relwidth=1, relheight=1)

        with open(r"C:\Users\sanu\AppData\Roaming\JetBrains\PyCharmCE2023.2\scratches\scratch_13.json", 'r') as file:
            self.story_data = json.load(file)

        self.story_label = tk.Label(master, text="Welcome to the Adaptive Story Game!", wraplength="1000",
                                    font=("Segoe UI Semibold", "14"))
        self.story_label.place(relx=0.5, rely=0.3, anchor='center')

        self.choice_buttons = []
        for i in range(3):
            button = tk.Button(master, text="", command=lambda i=i: self.make_choice(i + 1),
                               font=("Segoe UI Semibold", "14"), width="20", wraplength=200)
            button.place(relx=0.5, rely=0.5 + i * 0.1, anchor='center')
            self.choice_buttons.append(button)

        self.current_state = 'start'

        self.yes_button = tk.Button(self.master, text="Yes", command=self.continue_game,
                                    font=("Segoe UI Semibold", "12"))
        self.yes_button.place(relx=0.4, rely=0.8, anchor='center')

        self.no_button = tk.Button(self.master, text="No", command=self.quit_game, font=("Segoe UI Semibold", "12"))
        self.no_button.place(relx=0.6, rely=0.8, anchor='center')

        self.choice_history = []
        self.score = 0

        # Hide the buttons initially
        self.yes_button.place_forget()
        self.no_button.place_forget()
        self.update_story()

    def make_choice(self, choice_number):
        current_choices = list(self.story_data[self.current_state]['choices'].keys())
        if choice_number <= len(current_choices):
            chosen_choice = current_choices[choice_number - 1]
            self.choice_history.append(self.current_state)

            if chosen_choice == 'Bone':
                self.background_label.configure(image=self.background_images['Bone'])
                self.background_label.image = self.background_images['Bone']

            if chosen_choice == 'Painting':
                self.background_label.configure(image=self.background_images['Painting'])
                self.background_label.image = self.background_images['Painting']


            next_state = self.story_data[self.current_state]['choices'][chosen_choice]
            if next_state == '':
                all_paths = self.find_all_paths()
                longest_path, deviation = self.find_path_with_max_score()
                self.display_score_window(longest_path, deviation)
                self.master.destroy()
            else:
                self.current_state = next_state
                self.update_story()

    def find_all_paths(self):
        def dfs(node, path, total_score):
            path.append(node)

            if 'choices' not in self.story_data[node]:
                return [(path.copy(), total_score)]

            paths = []
            for choice, score in self.story_data[node]['choices'].items():
                if choice and choice in self.story_data:  # Check if the choice exists in the story_data
                    try:
                        next_total_score = total_score + int(score)
                    except ValueError:
                        next_total_score = total_score
                    paths.extend(dfs(choice, path.copy(), next_total_score))

            return paths

        return dfs('start', [], 0)

    def find_path_with_max_score(self):
        def dfs_max_score(node, path, max_score):
            path.append(node)

            if 'choices' not in self.story_data[node]:
                return path, max_score

            current_max_score = max_score
            next_node = None

            for choice, score in self.story_data[node]['choices'].items():
                if choice and choice in self.story_data:
                    try:
                        current_score = int(score)
                    except ValueError:
                        current_score = 0

                    next_score = current_max_score + current_score

                    if next_score > current_max_score:
                        current_max_score = next_score
                        next_node = choice

            if next_node:
                return dfs_max_score(next_node, path, current_max_score)
            else:
                return path, current_max_score

        return dfs_max_score('start', [], 0)

    def display_score_window(self, longest_path, deviation):
        score_window = tk.Toplevel(self.master)

        score_window.title("Score")

        longest_path_score = sum(int(self.story_data[state]['score']) for state in longest_path)

        final_score_label = tk.Label(score_window, text=f"Your Final Score: {self.score}",
                                     font=("Segoe UI Semibold", "14"))
        final_score_label.pack(pady=10)

        longest_path_score_label = tk.Label(score_window, text=f"Score from Longest Path: {longest_path_score}",
                                            font=("Segoe UI", "12"))
        longest_path_score_label.pack(pady=10)

        close_button = tk.Button(score_window, text="Close", command=score_window.destroy,
                                 font=("Segoe UI Semibold", "12"))
        close_button.pack()

        score_window.mainloop()

    def update_story(self):
        story_text = self.story_data[self.current_state]['text']
        self.story_label.config(text=story_text)
        self.score += int(self.story_data[self.current_state]['score'])
        choices = list(self.story_data[self.current_state]['choices'].keys())
        for i in range(len(choices)):
            self.choice_buttons[i].config(text=choices[i], wraplength=200)

        for j in range(len(choices), 3):
            self.choice_buttons[j].place_forget()

        if len(choices) == 1 and 'Next' in choices:
            self.choice_buttons[0].place(relx=0.5, rely=0.6, anchor='center')
            self.choice_buttons[1].place_forget()
            self.choice_buttons[2].place_forget()
        else:
            for k in range(3):
                self.choice_buttons[k].place(relx=0.5, rely=0.5 + k * 0.1, anchor='center')

        for l in range(3):
            if l >= len(choices):
                self.choice_buttons[l].place_forget()

        score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Segoe UI Semibold", "12"))
        score_label.place(relx=0.5, rely=0.9, anchor='center')

    def show_continue_prompt(self):
        continue_label = tk.Label(self.master, text="Do you want to continue?", font=("Segoe UI Semibold", "12"))
        continue_label.place(relx=0.5, rely=0.7, anchor='center')

        self.yes_button.place(relx=0.4, rely=0.8, anchor='center')
        self.no_button.place(relx=0.6, rely=0.8, anchor='center')

    def continue_game(self):
        if self.choice_history:
            self.current_state = self.choice_history.pop()
            self.update_story()
        else:
            self.current_state = 'start'
            self.score = 0
            self.update_story()

            # Game completed, find the path with the maximum score
            max_path, max_score = self.find_path_with_max_score()

            # Display the information
            print("Path with Maximum Score:", ' -> '.join(max_path[0]))
            print("Maximum Score Obtained:", max_path[1])

    def quit_game(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGameGUI(root)
    root.mainloop()
