import csv
import matplotlib.pyplot as plt

periods = []
electricity = []
water = []

with open('monthly_bills.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {row}')
            line_count += 1
        else:
            # print(f'\t{row[0]} - {row[1]} - {row[2]}')
            periods.append(row[0])
            electricity.append(float(row[1]))
            water.append(float(row[2]))
            line_count += 1
        # print(f'Processed {line_count} lines.')

print("Periods:", periods)
print("Electricity:", electricity)
print("Water", water)

plt.plot(periods, electricity, 'r', label="Electricity")
plt.plot(periods, water, 'b', label="Water")
plt.plot(periods, electricity, 'ro')
plt.plot(periods, water, 'bo')
plt.title('Electricity and Water Bills Per Payment Period')
plt.xlabel('Period')
plt.ylabel('Bill (₺)')
plt.ylim(bottom=0)
plt.legend(handlelength=3)

plt.show()
