def main():
    # get the actual value of the property from the user
    actual_value = float(input("Enter the actual value of the property: $"))

    # calculate the assessment value (60% of hte actual value)
    assessment_value = 0.6 * actual_value

    # calculate the property tax (.72 for each $100 of the assessment value)
    property_tax = (assessment_value / 100) * 0.72

    # display the assessment value and property tax
    print("\nAssessment Value: $", format(assessment_value, ",.2f"))
    print("Property Tax: $", format(property_tax, ",.2f"))

if __name__ == "__main__":
    main()
