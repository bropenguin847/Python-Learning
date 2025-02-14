"""
Example of using OpenDOSM data and plotting
"""

from request_api import get_post
import matplotlib.pyplot as plt

# Example of Passport Issuances by Immigration Department of Malaysia
passport_url = "https://api.data.gov.my/data-catalogue?id=passports&limit=12"
mypassport = get_post(passport_url)
# Example of Monthly Arrivals by Nationality & Sex
arrival_url = "https://api.data.gov.my/data-catalogue?id=arrivals&limit=12"
myarrival = get_post(arrival_url)

if mypassport and myarrival:
    print("Passport data\n", mypassport)
    print("Monthly Arrival data\n", myarrival)
else:
    print('Failed to get response.')

passports = []
arrivals = []
dates = []
for i in range(12):
    passports.append(mypassport[i]["passports"])
    dates.append(mypassport[i]["date"])
    arrivals.append(myarrival[i]["arrivals"])

plt.subplot(2, 1, 1)
plt.axvline(x=4, ls="--", color="red", label="MCO")
plt.plot(range(1,13), passports, marker="x", color="darkgreen", label="Passports Issuances")
plt.xticks(range(1, 13), dates, rotation=90)
plt.title("Passport Issuances in Malaysia 2020")
plt.legend()

plt.subplot(2, 1, 2)
plt.axvline(x=4, ls="--", color="red", label="MCO")
plt.plot(range(1,13), arrivals, marker="o", color="royalblue", label="Monthly arrivals")
plt.xticks(range(1, 13), dates, rotation=90)
plt.title("Monthly foreign arrivals in Malaysia 2020")
plt.legend()

plt.tight_layout()
plt.show()
