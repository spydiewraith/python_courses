print("Welcome ot the tip calculator!")
bill = float(input("What was the total bill?: "))
tip = int(input("What percentage tip would you like to give? 10, 12, 15%?: "))
people = int(input("How many people split the bill?: "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
tip_per_person = total_tip_amount / people
without_tip = bill / people
print(f"Each person should pay: {final_amount} and everyone will tip {tip_per_person}, without tipping everyone will pay {without_tip} each.")


