number = 155
st = 0
m = 1
while number!=0:
    rem = number%2
    # st = str(rem)+st 
    st = (rem*m)+st
    number//=2
    m*=10

print(st)
    