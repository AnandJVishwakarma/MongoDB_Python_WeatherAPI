import sys
from mongodb_crud import getAllData, getSelectiveData

# =========================================== COMMON FUNCTIONS : START ================================================== #
def printException(func_name: str, error: str) -> None:
    print(f'{func_name}: {error}')
    _, __, exc_tb = sys.exc_info()
    print(f'Line No: {exc_tb.tb_lineno}')
# =========================================== COMMON FUNCTIONS : END ================================================== #

def display_data(data):
    # print("-------------------data------:",data)
    if data and type(data) == dict:
        data = [data]
    if data and type(data) == list:
        for i in data:
            print("----------------------------------------------------------------------------------------")
            for key, value in i.items():
                print(f"{key}: {value}")
            print("----------------------------------------------------------------------------------------")
    else:
        print("Data not found.")


def main():
    while True:
        user_input = input("Enter a query (e.g., {'location': 'Thane'} or * (for all)): ")
        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        elif user_input.lower() == "*":
            fetched_data = getAllData()
            display_data(fetched_data)
        else:
            try:
                query = eval(user_input)
                fetched_data = getSelectiveData(request = query)
                display_data(fetched_data)
            except (Exception) as error:
                printException("main()", error)
                print("Please enter a valid query.")

if __name__ == "__main__":
    print("Welcome to the Weather Data CLI interface!!!")
    print("Enter a MongoDB query to fetch and display data.\nType '*' to fetch all data.\nType 'exit' to exit.")
    main()
