
def numOfWays(N):
    totalWays=(1<<N)
    
    notAllowed=notAllowedFunc(N)

    return (totalWays-notAllowed)

def notAllowedFunc(N):
    if N==4:
        return 1
    if N==5:
        return 3
    
    out=2*(2**(N-5))+(N-5)*(2**(N-6))-1         #counting no. of ways with exactly 4 consec As 
    return out+notAllowedFunc(N-1)              #Adding no. of ways wiht more than 4 As


def returnFormat(N):
    a=str(numOfWays(N-1)-(2**(N-5)))            #fixing last day as A and substracting ways with 3 or more As before last day
    b=str(numOfWays(N))
    print(a+'/'+b)

returnFormat(10)
