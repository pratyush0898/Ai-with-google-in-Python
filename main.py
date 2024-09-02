from googlesearch import search
import webbrowser

def search_google(query):
    search_results = list(search(query, num=1, stop=1, pause=2))
    return search_results[0] if search_results else None

def main():
    print("Welcome to the Pratyush A.I Assistant!")
    while True:
        user_query = input("Ask me a question (type 'exit' to end): ")
        
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break

        search_result = search_google(user_query)

        if search_result:
            print(f"Here is what I found: {search_result}")
            webbrowser.open(search_result)
        else:
            print("I couldn't find an answer. Please try again.")

if __name__ == "__main__":
    main()
