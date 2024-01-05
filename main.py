print("Welcome to Your Life in Weeks Calculator")

current_age = input("What's your current age? ")

live_up_to_age = 90 - int(current_age)

days = 365 * live_up_to_age

weeks = 52 * live_up_to_age

years = 12 * live_up_to_age

print(f"You have {days} days, {weeks} weeks, and {years} months left if you're to live up to 90.")

