from random import*
import csv
from datetime import datetime

DT = datetime.now().strftime("%d/%m/%Y|%H:%M")

fa=open('Score.csv','r+',newline='')

csv_r=csv.reader(fa)
for row in csv_r:
    if row[0].isdigit():
        SL=int(row[0])
    
csv_w=csv.writer(fa)



toss=['H','T']

#WICKET CHECK
def wkt_check(wkt):
    if type(wkt)==int and (wkt>0):
        return(wkt)
    else:
        if wkt==0:
            print('~~~~~Number of Wicket(s) Cannot be ZERO~~~~~')
            wkt1=int(input('Choose number of wicket(s):'))
            wkt2=wkt_check(wkt1)
            return wkt2
        elif wkt<0 or 0<wkt<1:
            print('~~~~~Number of Wickets must be a NATURAL number~~~~~')
            wkt1=int(input('Choose number of wicket(s):'))
            wkt2=wkt_check(wkt1)
            return wkt2


def bt_bl_check(choice):
    if choice.lower()  in ['bat','ball']:
        return choice
    elif choice.lower() not in ['bat','ball']:
        p_bt_bl=input('Choose batting or balling(bat/ball):')
        choice =bt_bl_check(p_bt_bl)
        return choice 


#SUPER OVER
def super_over():
    Su_Ov=True
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~SUPER OVER~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Make maximum run in 2 Overs (12 balls)')
    c_ball,p_ball=12,12
    co_runs=po_runs=0
    if bt=='p':
        print('~~~~~ First Batting: Computer ~~~~~')
        print('~~~~~ First Balling: You ~~~~~')
        while c_ball > 0:            
            try:            
                c_run=randint(1,6)
                p_run=int(input('Ball: '))
                print('Bat: ',c_run,'\n')
                
                if p_run not in [1,2,3,4,5,6]:
                    print('~~~~~Not a valid Number~~~~~')
                else:
                    if c_run==p_run:
                        print('~~~~~OUT!!!~~~~~')
                        c_ball-=1
                        print('||',c_ball,'more ball(s) left ||')                       
                        
                    else:
                        co_runs+=c_run
                        c_ball-=1
                        print('||',c_ball,'more ball(s) left ||')                        
            except:
                continue

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~Computer made',co_runs,'runs in SUPER OVER~~~~~')
        print('~~~~~You Needed',co_runs+1,'runs to WIN~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\n\n')
        print('='*40);print('='*40);print('='*40)
        print('Second batting: You')
        print('Second balling: Computer')


        while p_ball>0:
            try:
                c_run=randint(1,6)
                p_run=int(input('Bat:  '))
                print('Ball:',c_run,'\n')
                
                if p_run not in [1,2,3,4,5,6]:
                    print('~~~~~Not a valid Number~~~~~')
                else:
                    if c_run==p_run:
                        print('~~~~~OUT!!!~~~~~\n')
                        p_ball-=1
                        print('||',p_ball,'more ball(s) left ||')
                    else:
                        po_runs+=p_run
                        p_ball-=1
                        print('||',p_ball,'more ball(s) left ||')
                    
                if po_runs>co_runs:
                    print('\n')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('~~~~~YOU WON by',po_runs-co_runs,'runs(s)~~~~~')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    W='Player'
                    break
                else:
                    print('||','You need',co_runs+1-po_runs,'more run(s) to win from',p_ball,'ball(s)||\n')
            except:
                continue
            
        if co_runs > po_runs:
            print('\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~COMPUTER WON by',co_runs-po_runs,'run(s)~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            W='Computer'
               
        elif co_runs==po_runs:
            super_over()

    if bt=='c':
        print('~~~~~ First Batting: You ~~~~~')
        print('~~~~~ First Balling: Computer ~~~~~')
        while p_ball > 0:
            try:
                c_run=randint(1,6)
                p_run=int(input('Bat:  '))
                print('Ball:',c_run,'\n')
                
                if p_run not in [1,2,3,4,5,6]:
                    print('~~~~~Not a valid Number~~~~~')
                else:
                    if c_run==p_run:
                        print('~~~~~OUT!!!~~~~~')
                        p_ball-=1
                        print('||',p_ball,'more ball(s) left ||')
                    else:
                        po_runs+=p_run
                        p_ball-=1
                        print('||',p_ball,'more ball(s) left ||')
            except:
                continue

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~You made',po_runs,'runs in SUPER OVER~~~~~')
        print('~~~~~Computer Needed',po_runs+1,'runs to WIN~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\n\n')
        print('='*40);print('='*40);print('='*40)
        print('Second batting: Computer')
        print('Second balling: You')


        while c_ball>0:
            try:
                c_run=randint(1,6)
                p_run=int(input('Ball: '))
                print('Bat :',c_run,'\n')
                
                if p_run not in [1,2,3,4,5,6]:
                    print('~~~~~Not a valid Number~~~~~')
                else:
                    if c_run==p_run:
                        print('~~~~~OUT!!!~~~~~\n')
                        print('||',c_ball,'more ball(s) left ||')
                        c_ball-=1
                    else:
                        co_runs+=c_run
                        print('||',c_ball,'more ball(s) left ||')
                        c_ball-=1

                if co_runs>po_runs:
                    print('\n')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('~~~~~COMPUTER WON by',co_runs-po_runs,'runs(s)~~~~~')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    W='Computer'
                    break
                else:
                    print('||','You need',po_runs+1-co_runs,'more run(s) to win from',c_ball,'ball(s)||\n')

            except:
                continue
        if po_runs > co_runs:
            print('\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~YOU WON by',po_runs-co_runs,'run(s)~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            W='Player'
            
        elif po_runs==co_runs:
            super_over()
    return Su_Ov,po_runs,co_runs,W
#SUPER OVER END    

#Computer Batting
def c_bat(_p_runs,c_wkt):
    c_runs=0
    W=0
    #WICKET CHECK
    while c_wkt>0:
        try:
            c_run=randrange(1,7)
            p_run=int(input('Ball: '))
            print('Bat: ',c_run,'\n')
            
            if p_run not in [1,2,3,4,5,6]:
                print('~~~~~Not a valid Number~~~~~')
            else:
                if c_run==p_run:
                    print('~~~~~OUT!!!~~~~~')
                    c_wkt-=1
                    print('Wickets left:',c_wkt)
                else:
                    c_runs+=c_run
            if _p_runs==0:
                continue
            else:
                #RESULT    
                if c_runs>_p_runs:
                    print('\n')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('~~~~~COMPUTER WON by',c_wkt,'wicket(s)~~~~~')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    W='Computer'
                    break
                    
                else:
                    print('||','Computer need',_p_runs+1-c_runs,'more run(s) to win from',c_wkt,'wicket(s)||\n')
        except:
            continue
    return c_runs,W
#Computer Batting End

#player Batting
def p_bat(_c_runs,p_wkt):
    p_runs=0
    W=0
    #Wicket Check 
    while p_wkt>0:
        try:
            c_run=randint(1,6)
            p_run=int(input('Bat:  '))
            print('Ball:',c_run,'\n')
            
            if p_run not in [1,2,3,4,5,6]:
                print('~~~~~Not a valid Number~~~~~')
            else:
                if c_run==p_run:
                    print('~~~~~OUT!!!~~~~~\n')
                    p_wkt-=1
                    print('Wickets left:',p_wkt)
                else:
                    p_runs+=p_run
            if _c_runs==0:
                continue
            else:
                #RESULT 
                if p_runs>_c_runs:
                    print('\n')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('~~~~~YOU WON by',p_wkt,'wicket(s)~~~~~')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    W='Player'
                    break
                    
                else:
                    print('||','You need',_c_runs+1-p_runs,'more run(s) to win from',p_wkt,'wicket(s)||\n')
        except:
            continue
    return p_runs,W
#Player Batting End


#TOSS
while True:
    p_toss=input('choose for tossing(H/T):')
    tossing=toss[int((randint(0,100)%2))]
    if p_toss.upper() in toss:
        if p_toss.upper()==tossing:
            print('The coin showed:',tossing)
            print('You won the toss')
            toss_w='p'
            break
        else:
            print('The coin showed:',tossing,'')
            print('Computer won the toss')
            toss_w='c'
            break
    else:
        print('~~~~~The coin only has two sides H or T~~~~~')
#TOSS END

#CHOOSING BATTING OR BALLING AND WICKET(S)
if toss_w=='p':
    p_bt_bl=input('Choose batting or balling(bat/ball):')
    p_bt_bl=bt_bl_check(p_bt_bl)
    
        
    
    try:
        wkt1=int(input('Choose number of wicket(s):'))
    except:
        print('~~~~~Number of Wickets must be a NATURAL number~~~~~')
        wkt1=int(input('Choose number of wicket(s):'))
    wkt=wkt_check(wkt1)
elif toss_w=='c':
    bat_ball=['bat','ball']
    c_bt_bl=bat_ball[int((randint(0,100)%2))]
    if c_bt_bl=='bat':
        print('Computer choose Batting')
        p_bt_bl='ball'
    else:
        print('Computer choose Balling')
        p_bt_bl='bat'
    wkt=randint(1,4)
    print('The Number of Wicket(s) is:',wkt)
#END CHOOSING

    
#CURRENT BATTING AND BALLING CHECK
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Current batting:',end=' ')
if p_bt_bl=='bat':
    print('You')
    bt='p'
else:
    print('Computer')
    bt='c'
print('Current balling:',end=' ')

if p_bt_bl=='bat':
    print('Computer')
    bl='c'
else:
    print('You')
    bl='p'
print('Number of wicket(s):',wkt)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
c_wkt=p_wkt=wkt
#END CHECK 

#MAIN PROGRAM 
while True:
    #COMP BATTING 1ST INNINGS
    if bt=='c':
        c_runs,W=c_bat(0,c_wkt)
        
        #DECLERARTION OF FIRST OVER
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~Computer made',c_runs,'runs~~~~~')
        print('~~~~~You Needed',c_runs+1,'runs to WIN~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\n\n')
        print('='*40);print('='*40);print('='*40)
        print('Current batting: You')
        print('Current balling: Computer')
        print('Number of wicket(s):',wkt)
        #CURRENT BATTING AND BALLING

        
        #PLAYER BATTING 2ND INNINGS
        p_runs,W=p_bat(c_runs,p_wkt)
        
        #RESULT
        SU=False
        if c_runs > p_runs:
            print('\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~COMPUTER WON by',c_runs-p_runs,'run(s)~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            W='Computer'
        
        
        #SUPER OVER
        elif c_runs==p_runs:
            SU,PO,CO,W=super_over()
        if SU:
            L=[SL+1,DT,p_runs,c_runs,wkt,'Yes',PO,CO,W]
            print('Record Added')
            csv_w.writerow(L)
            fa.close()
        else:
            L=[SL+1,DT,p_runs,c_runs,wkt,'No','-','-',W]
            print('Record Added')
            csv_w.writerow(L)
            fa.close()
        fa.close()
        break



    #PLAYER BATTING 1ST INNINGS
    elif bt=='p':
        p_runs,W=p_bat(0,p_wkt)
        
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~You made',p_runs,'runs~~~~~')
        print('~~~~~Computer Needed',p_runs+1,'runs to WIN~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\n\n')
        print('='*40);print('='*40);print('='*40)
        print('Current batting: Computer')
        print('Current balling: You')
        print('Number of wicket(s):',wkt)
        
        c_runs,W=c_bat(p_runs,c_wkt)
        SU=False
        #RESULT    
        if p_runs > c_runs:
            print('\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~YOU WON by',p_runs-c_runs,'run(s)~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            W='Player'
            SU=False
            
        #SUPER OVER
        elif p_runs==c_runs:
            SU,PO,CO,W=super_over()
            
        if SU:
            L=[SL+1,DT,p_runs,c_runs,wkt,'Yes',PO,CO,W]
            print('Record Added')
            csv_w.writerow(L)
            fa.close()
        else:
            L=[SL+1,DT,p_runs,c_runs,wkt,'No','-','-',W]
            print('Record Added')
            csv_w.writerow(L)
            fa.close()

        fa.close()
    break
 

