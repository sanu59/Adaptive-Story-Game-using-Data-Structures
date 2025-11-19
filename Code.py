import tkinter as tk

class StoryGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Adaptive Story Game")

        self.story_data = {
            'start': {
                'text': "You are Skylar, a self-made archaeologist who spends most of their time in examining stuff and researching about artifacts. One day, you come across an abandoned museum, located at the edge of your town. You enter it and to your surprise, you find out that it’s filled with some of the rarest items on Earth. Your eyes catch three of them: a type of bone that you’ve never come across in your years of research, a painting of a horrific ghost that only reveals the image when lifted, and a ring made of some glowing material that looks too high-tech to be kept in a museum. Which one do you pick?",
                'choices': {
                    'Bone': 'choice1',
                    'Painting': 'choice2',
                    'Ring': 'choice3'
                }
            },
            'choice1': {
                'text': "The moment you touch the bone, you are pulled away and you feel yourself shrinking into the thin air.",
                'choices': {
                    'Next': 'Next'
                }
            },
            'Next':{
                'text': "When you gain control over yourself again, you find yourself lost in ancient Egypt. You have no idea how to get back home. You try to seek help from the local people. The people suggest you can do the following:",
                'choices': {
                    'Seek help from the pharaoh': 'help_pharaoh',
                    'Visit the pyramids for answers': 'visit_pyramids',
                    'Stay with the people and start a new life': 'start_life'
                    }
            },
            'help_pharaoh':{
                'text': "The pharaoh guides you with two possible ways:",
                'choices':{
                    'Perform the ritual of Marasavi to seek the help of Almighty':'marasavi',
                    'Visit the pyramids for answers': 'visit_pyramids'
                    }
            },
            'marasavi': {
                'text': "You decide to perform the ritual of Marasavi, which involves burying the bone you found and praying to the Almighty. Upon doing it, you hear the Almighty speaking with you.",
                'choices': {
                    'Return to your timeline':'goodending',
                    'Return to your timeline with a prize amount for performing the ritual':'futurepush'}
            },
            'goodending':{
                'text':"Congratulations! You've successfully completed the game",
                'choices':{}
            },
            'futurepush':{
                'text':"The almighty gets angry because of your greediness and decides to punish you. He pushes you into a void and you shrink into thin air again",
                'choices':{
                    'Next':'future'}
            },
            'visit_pyramids': {
                'text': "You decide to visit the pyramids. As soon as you get close, you hear a mysterious voice. You realize that the pyramids are speaking to you. You tell them that you are lost in time and need to get back home. The pyramids tell that you have two ways to get back home:",
                'choices': {
                    'Perform the ritual of Marasavi to seek the help of Almighty':'marasavi',
                    'Perform the ritual of Ravimasa':'ravimasa'}
            },
            'ravimasa':{
                'text':"You decide to perform the ritual of Ravimasa, which involves burning the object you found that brought you to this place and chant a prayer to the Almighty. You decide to burn the bone you found in the museum. Upon burning it, you find a portal open from the bone. You enter it, hoping to get back home",
                'choices':{}
            },
            'start_life':{
                'text':"You decide to forget about your past life and start a new one in ancient Egypt with the ancient people. Life’s not gonna be easy without having WiFi and mobile phones and to live in a desert surrounded by pyramids!",
                'choices':{
                    'Game Over':'gameover'}
            }
        }

        self.story_label = tk.Label(master, text="Welcome to the Adaptive Story Game!", wraplength="1000", font=("Segoe UI Semibold", "14"))
        self.story_label.place(relx=0.5, rely=0.3, anchor='center')

        self.choice_buttons = []
        for i in range(3):
            button = tk.Button(master, text="", command=lambda i=i: self.make_choice(i + 1), font=("Segoe UI Semibold", "14"), width="20")
            button.place(relx=0.5, rely=0.5 + i * 0.1, anchor='center')
            self.choice_buttons.append(button)

        self.current_state = 'start'
        self.update_story()

    def make_choice(self, choice_number):
        current_choices = list(self.story_data[self.current_state]['choices'].keys())
        if choice_number <= len(current_choices):
            chosen_choice = current_choices[choice_number - 1]
            next_state = self.story_data[self.current_state]['choices'][chosen_choice]
            self.current_state = next_state
            self.update_story()

    def update_story(self):
        story_text = self.story_data[self.current_state]['text']
        self.story_label.config(text=story_text)

        choices = list(self.story_data[self.current_state]['choices'].keys())
        for i in range(len(choices)):
            self.choice_buttons[i].config(text=choices[i])

        # Show/hide buttons based on the number of choices
        for j in range(len(choices), 3):
            self.choice_buttons[j].place_forget()

        if len(choices) == 1:  # If only one choice is available, ensure all buttons are visible
            self.choice_buttons[1].place(relx=0.5, rely=0.6, anchor='center')
            self.choice_buttons[2].place(relx=0.5, rely=0.7, anchor='center')

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGameGUI(root)
    root.mainloop()
