import csv

def csv_to_vcf(csv_file, vcf_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        with open(vcf_file, 'w', newline='', encoding='utf-8') as vcf:
            for row in csvreader:
                vcf.write('BEGIN:VCARD\n')
                vcf.write('VERSION:3.0\n')
                full_name = f"{row['first_name']} {row['last_name']}"
                vcf.write(f'FN:{full_name}\n')
                vcf.write(f'ORG:{row["company_name"]}\n')
                vcf.write(f'ADR;TYPE=HOME:{row["address"]},{row["city"]},{row["county"]},{row["state"]},{row["zip"]}\n')
                vcf.write(f'TEL;TYPE=WORK,VOICE:{row["phone1"]}\n')
                vcf.write(f'TEL;TYPE=HOME,VOICE:{row["phone"]}\n')
                vcf.write(f'EMAIL;TYPE=INTERNET:{row["email"]}\n')
                vcf.write('END:VCARD\n')

# File paths
csv_file_path = r'C:\Users\MoeketsiR\Documents\contacts.csv' # CSV file path
vcf_file_path = r'C:\Users\MoeketsiR\Documents\contacts.vcf' # Path to save the generated VCF file

# Call the function
csv_to_vcf(csv_file_path, vcf_file_path)
