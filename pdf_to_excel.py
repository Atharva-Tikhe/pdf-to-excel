import os
import sys
import argparse
import tabula
import pandas as pd


def pdf_to_excel(pdf_file_path, excel_file_path):
    # Read PDF file
    tables = tabula.read_pdf(pdf_file_path, pages='all')

    # Write each table to a separate sheet in the Excel file
    with pd.ExcelWriter(excel_file_path) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f'Sheet{i+1}')


def file_runner(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            file = os.path.join(input_dir, filename)
            print(f"processing {file}")
            pdf_to_excel(file, os.path.join(output_dir, f"{os.path.basename(filename).rsplit('.')[0]}.xlsx")) 


parser = argparse.ArgumentParser(prog='pdf-to-excel', description='This script utilises tabula and pandas to convert pdf tables to excel sheets.')
parser.add_argument('-i', '--input_dir', default='./input_dir')
parser.add_argument('-o', '--output_dir', default='./output_dir')

args = parser.parse_args()

file_runner(args.input_dir, args.output_dir)

