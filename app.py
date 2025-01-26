# this will list our sandwich builder and ask user for some ingredients
def build_sandwich(ingredients):
    # Check if the ingredients list is empty
    if not ingredients:
        print("You need to choose some ingredients!")
        return
        
    print("Let's make a sandwich!")
    print("First, we grab some bread...")
    
    # Loop through each ingredient
    for i, ingredient in enumerate(ingredients, 1):
        print(f"Adding {ingredient}...")
    
    print("And top it with bread!")
    # Join all ingredients with " and " between them for a nice final message
    print(f"\nCongrats! You made a {' and '.join(ingredients)} sandwich!")

# Main function that handles user input and error catching
def main():
    try:
        print("Welcome to the Sandwich Maker!")
        # this allows us to separte our ingredients with commas 
        ingredients_input = input("Enter ingredients (separated by commas): ")
        
        # this will remove white space 
        ingredients = [i.strip() for i in ingredients_input.split(",")]
        
    
        build_sandwich(ingredients)
            
    # this will catch any errors
    except Exception as e:
        print("Oops, something went wrong! Let's try again.")
# this will only run the main after all is completed
if __name__ == "__main__":
    main()
  