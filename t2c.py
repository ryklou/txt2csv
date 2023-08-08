import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw()
input_file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])

output_file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

with open(input_file_path, 'r') as input_file:
  stripped = (line.strip() for line in input_file)
  lines = (line.split(",") for line in stripped if line)
  with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(lines)