import random
from time import sleep

BUDDHA = "Buddha"
KANT = "Kant"
SOCRATES = "Socrates"
SIMONE_DE_BEAUVOIR = "Simone De Beauvoir"

BUDDHISM = """ Buddha!

You have a tenderness for the world around you. You acknowledge
the suffering of all beings, and wish well for everything alive on this planet.
You see things as they are. You prefer the "no-frills" mom n' pop restaurant to
the overpriced hipster burger joint.

Advice: Do some yoga this week. Call a friend you've been meaning to catch up with.
"""
KANTIANISM = """ Immanuel Kant!

You believe in absolute moral rules. It is ALWAYS wrong to wear
tennis shoes with a skirt.

Advice: Look up a cause you're passionate about. See if you can volunteer with
them before the start of the new year. """

SOCRATISM = """ Socrates!

You don't mind wearing flip-flops. Perhaps your fashion choices are more
utilitarian than aesthetic. Your idea of an ideal date would be a deep
conversation pondering the nature of the universe and asking the deeper
questions in life like:
Why does milk and cereal go so well together?

Advice:
Stay open-minded, you never know, even those most chance encounter can teach you
something new. """

DE_BEAUVOIRISM = """ Simone De Beauvoir

You have bigger things to worry about than your outfit choices.
Like: What is the meaning of life? Or Is free will even real? Heck, if freewill
isn't real,  maybe neither is your decision to wear crocs.

Advice: Don't wear crocs.

More advice:
Start your memoir this week, who knows it might be interesting... Or just read
someone else's. """


questions = [
	{
		"question": "1. What are your thoughts on vegetarianism?\n",
		"answers": (
			"A. What does it even mean to be vegetarian?\n"
			"B. Everyone should be a vegetarian, meat is murder\n"
			"C. I could care less about vegetarians, let's talk about human rights. \n"
			"D. Vegetarianism is good. After all, animals suffer too!\n"

		)

	},
	{
		"question": "\n2.If someone gives you a gift and you give it back,"
		"whose gift is it now?\n",
		"answers": (
			"A. I don't know, that's a good question.\n"
			"B. You should never give a gift back to someone, no matter how bad it is.\n"
			"C. The gift never really meant anything, it's just a social construct.\n"
			"D. It's their gift, duh.\n "
		)

	},
	{
		"question": "\n3. Your favorite type of movies are:",
		"answers": (
			"A. You question what makes a good movie, you still haven't really figured it out yet.\n "
			"B. Movies with clear-cut morals at the end.\n"
			"C. Slice of life movies\n "
			"D. Cult classics, maybe even something quirky like 'The Big Lebowski'\n"
		)
	},
	{
		"question": "\n4. You're a proud New Yorker. A tourist walks up to you"
		"and asks you how to get to Times Square, you: ",
		"answers": (
			"A. Ask them if they've ever been to Times Square, and then ask them why on earth they'd ever want to.\n"
			"B. Admit that you can't remember and pull out google maps.\n"
			"C. Calmly tell them there is better places to go in NY, then enthusiastically suggest Central Park.\n"
			"D. Gallantly show them the way"
		)
	}

]

def run_the_philosofinder(questions):
	print("Welcome to the Philosofinder!\n")
	print("Have you ever wondered which philosopher you are?")
	print("\nWell it's your lucky day!")
	print("\nTake this quiz and find out!")

	sleep(1)

	print("\nAnswer the following questions by choosing A, B, C, or D \n")

	sleep(1)

	list_of_user_choices = [0, 0, 0, 0]

	for question in questions:
		print(question['question'])
		print(question['answers'])
		user_choice = input("Please choose A, B, C, D\n").lower()
		if user_choice == "a":
			list_of_user_choices[0] += 1
		elif user_choice == "b":
			list_of_user_choices[1] += 1
		elif user_choice == "c":
			list_of_user_choices[2] += 1
		elif user_choice == "d":
			list_of_user_choices[3] += 1

	return list_of_user_choices


def find_most_picked_choice(list_of_user_choices):
	choice_counts = [("a", list_of_user_choices[0]),
					 ("b", list_of_user_choices[1]),
					 ("c", list_of_user_choices[2]),
					 ("d", list_of_user_choices[3])]

	highest_count = 0
	highest_count_choice = None
	# for first thing in tuple and second thing in tuple
	for letter_choice, count in choice_counts:
		if count > highest_count:
			# Store new answer with higher count.
			highest_count = count
			highest_count_choice = letter_choice
		elif count == highest_count and count > 0:
			# Pick randomly between ties if choice has count.
			highest_count_choice = random.choice([highest_count_choice,
												  letter_choice])

	return highest_count_choice


def which_philosopher_are_you_really_tho(highest_count_choice):
	# prints which Philosopher you really are though.
	print('\nBEHOLD, the answer draws nigh. I look into the crystal ball and see that you are....\n')
	sleep(3)
	if highest_count_choice == 'a':
		print(BUDDHISM)
	elif highest_count_choice == 'b':
		print(KANTIANISM)
	elif highest_count_choice == 'c':
		print(SOCRATISM)
	elif highest_count_choice == 'd':
		print(DE_BEAUVOIRISM)





#Answer :
# A = Buddha, B = Kant, C = Socrates, D = Simone De Beauvoir



user_actual_choices = run_the_philosofinder(questions)
highest_picked_choice = find_most_picked_choice(user_actual_choices)
which_philosopher_are_you_really_tho(highest_picked_choice)
