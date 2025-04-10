def rename_file():

    import os

    old_name = input('Enter old file name: ')
    new_name = input("Enter new file name: ")

    try:
        os.rename(old_name, new_name) 
        return(f"{old_name} has been renamed as {new_name} successfully")
    except FileNotFoundError:
        return(f"{old_name} does not exists")
    except FileExistsError:
        return(f"{new_name} already exists")    

if __name__ != "__main__":
    print(rename_file())
else:
    print("This script is meant to be imported and not run directly")    