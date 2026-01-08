number = 155
st = 0
m = 1
while number!=0:
    rem = number%8
    # st = str(rem)+st 
    st = (rem*m)+st
    number//=8
    m*=10

print(st)
    