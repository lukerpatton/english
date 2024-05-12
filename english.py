import random

def main():
    facts = [
        "Python was created by Guido van Rossum and first released in 1991.",
        "Python is named after the British comedy series 'Monty Python’s Flying Circus'.",
        "Python is used by many large companies, including Google, Netflix, and Spotify.",
        "Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
        "Python is an interpreted language, which means that the written code is not actually translated to a computer-readable format at runtime."
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