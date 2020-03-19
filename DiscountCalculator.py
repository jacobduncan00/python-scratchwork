# Item Percentage Calculator

original_price = float(input("Enter the item's original price: "))
print('Original Price:', original_price)
discount_percentage = float(input('Enter the discount percentage: '))
discount_percentage = discount_percentage / 100
discount = original_price * discount_percentage
final_price = original_price - discount
print('Discount %:', discount_percentage)
print('Final Price:', final_price)
