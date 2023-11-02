import subprocess

def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print(f"Command executed successfully: {command}")
            print("Output:")
            print(stdout.decode('utf-8'))
        else:
            print(f"Error executing command: {command}")
            print("Error Output:")
            print(stderr.decode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Replace the following path with the desired path to navigate in the terminal
    path_to_backend = "/home/pilli007/Documents/Projects/Angular/Assignment/Node-Backend"
    
    # Command to navigate to the specified path
    cd_command = f"cd {path_to_backend}"

    # Command to run mvn spring-boot:run with sudo
    mvn_command = "npm start"

    # Joining the two commands with the "&&" to execute them in sequence
    full_command = f"{cd_command} && {mvn_command}"

    # Call the function to run the commands
    run_command(full_command)

if __name__ == "__main__":
    main()

