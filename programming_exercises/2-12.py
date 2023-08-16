# Variables
amountPaidForStock = 0.0    # Amount paid for the stock
purchaseCommission = 0.0    # Commission paid to purchase stock
totalPaid = 0.0             # Total amount paid
stockSoldFor = 0.0          # Amount stock sold for
sellingCommission = 0.0     # Commission paid to sell stock
totalReceived = 0.0         # Total amount received
profitOrLoss = 0.0          # Amount of profit or loss

# Constants
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 32.75

# Calculate the amount that Joe paid for the stock (not including commission)
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE

# Calculate the amount of commission that Joe paid his broker
purchaseCommission = COMMISSION_RATE * amountPaidForStock

# Calculate the total amount that Joe paid (total + commission)
totalPaid = amountPaidForStock + purchaseCommission

# Calculate the total amount that Joe sold the stock for.
stockSoldFor = NUM_SHARES * SELLING_PRICE

# Calculate the amount of commission that Joe paid his broker when he sold.
sellingCommission = COMMISSION_RATE * stockSoldFor

# Calculate the amount of money left over, after Joe paid his broker.
totalReceived = stockSoldFor - sellingCommission

# Calculate the amount of profit or loss.
profitOrLoss = totalReceived - totalPaid

# Print the required data.
print("Amount paid for the stock: $", format(amountPaidForStock, ',.2f'))
print("Commission paid on the purchase: $", format(purchaseCommission, ',.2f'))
print("Amount the stock sold for: $", format(stockSoldFor, ',.2f'))
print("Commission paid on the sale: $", format(sellingCommission, '.2f'))
#print("Profit (or loss if negative): $", format(profitOrLoss, '.2f'))
if profitOrLoss >= 0:
    print("Profit: $", format(profitOrLoss, '.2f'))
else:
    print("Loss $", format(profitOrLoss, ',.2f'))