gekochteStuks = int(input())
kostprijs = float(input())
barcodes = int(input())
mijlen = int(input())

amount = gekochteStuks * kostprijs
coupons = gekochteStuks // barcodes
miles = coupons * mijlen

print(f"Phillips spendeerde ${amount} voor {miles} frequent flyer mijlen.")

