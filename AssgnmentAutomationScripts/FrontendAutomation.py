import os

def run_command(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Replace the following path with the desired path to navigate in the terminal
    path_to_frontend = "/home/pilli007/Documents/Projects/Angular/Assignment/Angular-Frontend"
    
    # Command to navigate to the specified path
    cd_command = f"cd {path_to_frontend}"

    # Command to run 'ng serve'
    ng_serve_command = "npm start"

    # Joining the two commands with the "&&" to execute them in sequence
    full_command = f"{cd_command} && {ng_serve_command}"

    # Call the function to run the commands
    run_command(full_command)

if __name__ == "__main__":
    main()

