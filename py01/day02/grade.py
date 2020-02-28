#!/usr/local/bin/python3
# grades=int(input('Please enter your score:'))
#
# if grades > 100 or grades < 0:
#     print('Please type again,and the range is 0 to 100')
# elif 60 <= grades < 70:
#     print('Pass')
# elif 70 <= grades < 80:
#     print('Good!')
# elif 80 <= grades < 90:
#     print('VeryGood!!')
# elif grades >= 90:
#     print('Excellence!!!')
# else:
#     print('You have to work hard!')

grades=int(input('Please enter your score:'))

if grades >100 or grades < 0:
    print('Please type again,and the range is 0 to 100')
elif grades >= 90:
    print('Excellence!!!')
elif grades >=80:
    print('VeryGood!!')
elif grades >=70:
    print('Good!')
elif grades >=60:
    print('Pass')
else:
    print('You have to work hard!')