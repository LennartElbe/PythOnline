tage = 365 - (31 - 10) + (365 * 12) + (366 * 5)
wochen = int(tage/7)
zusatz = tage % 7
print("Tage vom 1. Janur 2000 bis zum 10. Dezember 2017: " + str(tage) +
      "\nWochen: " + str(wochen) + "\nZusätzlichen Tagen: " + str(zusatz))
