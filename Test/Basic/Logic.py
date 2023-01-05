# 开发者：Annona
# 开发时间：2022/12/13 18:00
x = int(input('please input an integer'))
if x<0:
    print('x<0')
elif x==0:
    print('x=0')
elif x>0:
    print('x>0')

word = ['China','test','dog']
for w in word:
    print(w,len(w))

capital = {'China':'Beijin','Japan':'Tokyo','American':'Washington'}
capital1=capital.copy().items()
print(capital.items())
print(capital1)

# Strategy:  Iterate over a cop
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user,status in users.copy().items():
    if status =='inactive':
        del users[user]
print(users)

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user,status in users.copy().items():
    if status =='inactive':
        del users[user]
print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
