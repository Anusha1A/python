def dec_to_binary( decimal_number ):
	if decimal_number==0:
        		return 0
	else:
		return (decimal_number % 2 + 10 *dec_to_binary(int(decimal_number // 2)))
decimal_number =int(input("Enter decimal number:"))
print(dec_to_binary(decimal_number))