import csv

# Input and output filename
filename = 'input_file.vcf'

# Open the file and process it
with open(filename, 'r') as infile:
    # Create a CSV writer with the same filename, but with a .csv extension
    with open(filename.replace('.vcf', '.csv'), 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        for line in infile:
            # Skip metadata lines
            if line.startswith('##'):
                continue
            # Handle the header
            elif line.startswith('#CHROM'):
                # Split the header into columns and write to CSV
                headers = line.strip().split('\t')
                csv_writer.writerow(headers)
            else:
                # Write the rest of the lines as rows
                row = line.strip().split('\t')
                csv_writer.writerow(row)

print("File has been converted to CSV successfully.")
