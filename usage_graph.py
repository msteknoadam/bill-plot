import csv
import matplotlib.pyplot as plt
import matplotlib

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
            try:
                electricity.append(float(row[1]))
            except:
                # Use last month's value if the current value is not defined etc.
                electricity.append(electricity[-1])
            try:
                water.append(float(row[2]))
            except:
                # Use last month's value if the current value is not defined etc.
                water.append(water[-1])
            line_count += 1
        # print(f'Processed {line_count} lines.')

print("Periods:", periods)
print("Electricity:", electricity)
print("Water", water)

matplotlib.rcParams['figure.figsize'] = (10.0, 7.5)

plt.plot(periods, electricity, 'r', label="Electricity")
plt.plot(periods, water, 'b', label="Water")
plt.plot(periods, electricity, 'ro')
plt.plot(periods, water, 'bo')
plt.xticks(periods, rotation='vertical')
plt.subplots_adjust(bottom=0.15)
plt.title('Electricity and Water Bills Per Payment Period')
plt.xlabel('Period')
plt.ylabel('Bill (₺)')
plt.ylim(bottom=0)
plt.legend(handlelength=3)
plt.savefig('example-plot.png')
plt.show()
