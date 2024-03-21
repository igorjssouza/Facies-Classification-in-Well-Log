import csv

def clean_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if '-9999' not in row:
                writer.writerow(row)

# Example usage:
input_file = 'combined_data_20240130_213815.csv'
output_file = 'output.csv'
clean_csv(input_file, output_file)
print("CSV cleaned successfully.")
