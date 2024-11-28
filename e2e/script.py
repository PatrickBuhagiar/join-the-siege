import subprocess

# List of filenames to classify
filenames = [
    "../files/invoice_1.pdf",
    "../files/invoice_2.pdf",
    "../files/invoice_3.pdf",
    "../files/bank_statement_1.pdf",
    "../files/bank_statement_2.pdf",
    "../files/bank_statement_3.pdf",
    "../files/drivers_license_1.jpg",
    "../files/drivers_licence_2.jpg",
    "../files/drivers_license_3.jpg"
]


# Function to run curl command and print the result
def classify_files(files):
    for filename in files:
        try:
            # Prepare the curl command
            command = [
                "curl", "-X", "POST",
                "-F", f"file=@{filename}",
                "http://127.0.0.1:5000/classify_file"
            ]

            # Execute the command and capture the output
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Print the result of the classification
            if result.returncode == 0:
                print(f"Result for '{filename}':\n{result.stdout}\n")
            else:
                print(f"Error for '{filename}':\n{result.stderr}\n")

        except Exception as e:
            print(f"Exception occurred while processing '{filename}': {str(e)}\n")


# Run the script to classify the files
if __name__ == "__main__":
    classify_files(filenames)
