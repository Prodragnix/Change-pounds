print('\nThis is a change calculator!\n')
total=eval(input('\nPlease enter the total cost: £'))
paid=eval(input('Please enter the amount paid: £'))
amount=total-paid

if paid>total:
    amount=amount*-1
    x=1
else:
    pass

po50=amount//50
print('\n£50 notes needed: ',po50)
i=amount%50

po20=i//20
print('\n£20 notes needed: ',po20)
i=i%20

po10=i//10
print('\n£10 notes needed: ',po10)
i=i%10

po5=i//5
print('\n£5 notes needed: ',po5)
i=i%5

po2=i//2
print('\n£2 coins needed: ',po2)
i=i%2

po1=i//1
print('\n£1 coins needed: ',po1)
i=i%1

p50=i//0.5
print('\n50p coins needed: ',int(p50))
i=i%0.5

p20=i//0.2
print('\n20p coins needed: ',int(p20))
i=i%0.2

p10=i//0.1
print('\n10p notes needed: ',int(p10))
i=i%0.1

p5=i//0.05
print('\n5p coins needed: ',int(p5))
i=i%0.05

p2=i//0.02
print('\n2p coins needed: ',int(p2))
i=i%0.02

p1=i//0.01
print('\n1p coins needed: ',int(p1))

amount=round(amount,2)
print('\nThe due amount is: £',amount)
print('\nThank you!BYE!\n')
