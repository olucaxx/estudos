def register_log(error: str, message: str) -> None:
    with open('log.txt', 'a+') as log:
        log.write(f"{error} -> {message}\n")

def error_simulator(option: int) -> bool:
    got_error = False

    if option == 1:
        try:
            nums: list[int] = [1,2,3,4,5]
            index: int = int(input(f'type the index of some item from this list: {nums}\n'))
            print("the item is:", nums[index])

        except IndexError as e:
            got_error = True
            register_log("IndexError", e)

        finally: 
            return got_error
    
    if option == 2:
        try:
            file: str = input("type the name of the text file to see the content: ")

            with open(f"{file}.txt", "r") as text_file:
                for line in text_file.readlines():
                    print(line, end="")

        except FileNotFoundError as e:
            got_error = True
            register_log("FileNotFoundError", e)

        finally:
            return got_error

        
print("ERROR simulator app")
print("1. IndexError")
print("2. FileNotFoundError")

if error_simulator(int(input("select a option: "))):
    print("\nwe got a error! it was added to the log.txt file")
else:
    print("\nwe got no error, everything worked just fine")