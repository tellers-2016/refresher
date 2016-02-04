class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = "a string"
        self.valid = True

        print (self.card_number)
        self.determine_card_type()

# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        print("RUNNING")
        print(self.card_number[0:2])
        if self.card_number[0]== "4":
            self.card_type = "Visa"
            self.check_length()
        elif self.card_number[0:2] in ["51", "52", "53", "54", "55"]:
            self.card_type = "Mastercard"
            self.check_length()
        elif self.card_number[0:2] in ["34", "37"]:
            self.card_type = "American Express"
            self.check_length()
        elif self.card_number[0:4] == "6011":
            self.card_type = "Discover"
            self.check_length()
        else:
            print("INSIDE ELSE")
            self.card_type="INVALID"
            self.valid = False



# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        #print("AT LENGTH")

        if len(self.card_number) == 15 or len(self.card_number) == 16:
            #print ("MADE it PASS IF")
            self.validate()
        else:
            #print ("AT ELSE")
            self.card_type="INVALID"
            self.valid = False




# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        #print ("AT NUMBERS")
        numbers = list(self.card_number)
        new_numbers=[]
        double_num_list = []
        reverse_double = []
        
        for num in numbers:
            new_numbers.append(int(num)) #change from string to int
        print(new_numbers)
        for index in range(len(new_numbers)-2,-1,-2): #selects every other number starting from last index and stores in new numbers
            #print(new_numbers[index])
            double_num_list.append(new_numbers[index] + new_numbers[index])
        
        y = reversed(double_num_list) #change the order of the list
        for eachit in y:
            reverse_double.append(eachit)
        print(reverse_double)
        
        #for index in range(len(new_numbers)-2,-1,-2):
           # remove(new_numbers[index])
        
        
        
            
            
           # print (double_value)
           # double_numbers.append(index)+
           # print(double_numbers[index])
            
        #print(new_numbers)


        #print(numbers)
        pass


# do not modify assert statements

cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
