nami = 0
chopper = 0
null_vote = 0

for i in range(5):
    vote = eval(input())

    if vote == 1:
        nami = nami + 1
    elif vote == 2:
        chopper = chopper + 1
    else:
        null_vote = null_vote + 1

    print('Total votes of No.1: Nami =  %d' %(nami))
    print('Total votes of No.2: Chopper =  %d' %(chopper))
    print('Total null votes =  %d' %(null_vote))

if nami > chopper:
    print("=> No.1 Nami won the election.")
elif chopper > nami:
    print("=> No.2 Chopper won the election.")
else:    
    print("=> No one won the election.")