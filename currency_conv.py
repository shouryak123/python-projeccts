dollar ={"EUR":1.088275,"CAD":0.695746,"INR":0.011503,"USD":1,"GBP":1.29304,"KRO":0.007438}
currencies =tuple(dollar.keys())



conversion_history =[]
while True:
    
    amount =float(input("Enter amount(or 0 to quit):"))

    if(amount==0):
        break
    input_currency =input("Enter input currency (eur,cad,inr,usd,gbp,kro)").upper()
    while input_currency not in currencies:
        print("Invalid option!")
        input_currency =input("Enter input currency (eur,cad,inr,usd,gbp,kro)").upper()
    output_currency =input("Enter output currency  (eur,cad,inr,usd,gbp,kro)").upper()
    while output_currency not in currencies:
        print("Invalid option!")
        output_currency =input("Enter output currency (eur,cad,inr,usd,gbp,kro)").upper()

    def input_to_dollar():
        value_in_dollar =float( dollar[input_currency]*amount)
        return value_in_dollar

    dollar_value =input_to_dollar()

    def dollar_to_output():
        return float(dollar_value/dollar[output_currency])
        

    converted_amt = dollar_to_output()
    conversion_record = f"{amount:.2f}{input_currency}->{converted_amt:.2f}{output_currency}"
    conversion_history.append(conversion_record)

    print(f"\n {amount:.2f} {input_currency} converts to {converted_amt:.2f} {output_currency}")
print("Converion History")
for i in conversion_history:
    print(i)

    
    # for i in currencies:
    #     value_output = float(dollar_value/dollar[i])
    #     print(f"{value_output:.2f}{i}")
    



