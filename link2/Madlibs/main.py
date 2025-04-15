def mad_lib():
    print("Welcome to the Mad Libs game!")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    adj = input("Give me an adjective: ")
    obj = input("Give me an object: ")
    verb = input("Give me a verb: ")
    animal = input("Give me an animal: ")
    number = input("Give me a number: ")

    story = f"Once upon a time, {name} went to {place} to find a {adj} {obj}. While walking, they saw a {animal} " \
            f"that decided to {verb} with them. Together, they went on an adventure and found {number} magical treasures!"

    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    mad_lib()
