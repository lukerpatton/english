import random

def main():
    facts = [
        "Python is taught at Seven Lakes High School in Computer Science class",
        "The current version of Python is 3",
        "NASA uses Python for some of its programming tasks, including running a space probe!",
        "Python is great for automating repetitive tasks that save time and reduce the chance of errors.",
        "You don't need to declare the type of a variable in Python, unlike many other programming languages.",
        "One of the world's most popular social media platforms, Instagram, uses Python on its backend.",
        "Python programs can run on any operating system, such as Windows, macOS, Linux, and even Raspberry Pi.",
        "Python is open-source, which means it's free to use and distribute, even for commercial purposes.",
        "Python was created by Guido van Rossum over the Christmas holiday in 1989",
        "Python was first released in 1991",
        "Python is not named after the snake, it is named after the British comedy series 'Monty Python's Flying Circus'.",
        "Python is used by many large companies, including Google, Netflix, and Spotify.",
        "Python's design philosophy emphasizes code readability."
    ]
    
    while True:
        fact = random.choice(facts)
        print("Random Python Fact:")
        print(fact)
        
        user_response = input("\nWould you like to see another random fact? (y/n) ").strip().lower()
        if user_response != "y":
            break

if __name__ == "__main__":
    main()