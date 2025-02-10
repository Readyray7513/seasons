from datetime import date
import sys
import inflect

# Function to get the user's birth date
def get_birth_date(user_input=None):
    try:
        if user_input is None:
            user_input = input("(YYYY-MM-DD): ")
        birth_date = date.fromisoformat(user_input)
        return birth_date
    except ValueError:
        sys.exit("Invalid date format")


# Function to calculate the number of minutes since the user's birth date
def calculate_mins(birth_date):
    current_date = date.today()
    diff = current_date - birth_date
    return diff.days * 24 * 60

# Function to convert the number of minutes to words
def convert_to_words(mins):
    p = inflect.engine()
    words = p.number_to_words(mins, andword="") + " minutes"
    return words[0].upper() + words[1:]  # Capitalizes the first letter dynamically

# Main function
def main():
    birth_date = get_birth_date()
    mins = calculate_mins(birth_date)
    print(convert_to_words(mins))

if __name__ == "__main__":
    main()

