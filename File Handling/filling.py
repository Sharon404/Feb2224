try:
    with open("my_file.txt", "w") as file:
        file.write("Hello my name is Aoko\n")
        file.write("I am over 18 years old\n")
        file.write("I love Python\n")

    
    with open("my_file.txt", "a") as file:
        file.write("These are additional lines\n")
        file.write("They are 3 lines\n")
        file.write("Additional lines\n")
    
    with open("my_file.txt","r") as file:
        file_content = file.read()
        print(file_content)
    
except FileNotFoundError:
    print("Error: The specified file does not exist.")

except PermissionError:
    print("Error: Permission denied to access the file.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Execution completed.")
