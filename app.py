import xml.etree.ElementTree as ET

# Get input from user
username = input("Enter username: ")
amt = float(input("Enter loan amount: "))

# Calculate loan interest amount
interest_rate = 0.1  # 10% interest rate
interest_amt = amt * interest_rate

# Create XML element
root = ET.Element("Loan_Details")
user = ET.SubElement(root, "User")
user.text = username
loan_amt = ET.SubElement(root, "Loan_Amount")
loan_amt.text = str(amt)
interest = ET.SubElement(root, "Interest")
interest.text = str(interest_amt)

# Save details in XML file
tree = ET.ElementTree(root)
tree.write("Loan_Details.xml")
