import multiprocessing
import subprocess

def run_python_script(script_path):
    try:
        command = f"python {script_path}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print(f"Script executed successfully: {script_path}")
            print("Output:")
            print(stdout.decode('utf-8'))
        else:
            print(f"Error executing script: {script_path}")
            print("Error Output:")
            print(stderr.decode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Replace the following paths with the paths to your Python scripts
    script_path_1 = "/home/pilli007/Desktop/Proj-Automation/angular-frontend.py"
    script_path_2 = "/home/pilli007/Desktop/Proj-Automation/spring-backend-automation.py"

    # Create two separate processes for eachr script
    process1 = multiprocessing.Process(target=run_python_script, args=(script_path_1,))
    process2 = multiprocessing.Process(target=run_python_script, args=(script_path_2,))

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

if __name__ == "__main__":
    main()





