#Jake Hayes
#Case Study 1
def calc_sum(n_list = []):
    tot = 0
    for i in n_list:
        tot += i
    return tot

def calc_avg(n_list = []):
    avg = 0
    div = len(n_list)
    for i in n_list:
        avg += i
    avg = avg / div
    return avg

def calc_stan_dev(n_list = []):
    n = len(n_list)
    avg = calc_avg(n_list)
    j = 0
    for i in n_list:
        j += (i-avg)**2

    return j/n


n = [2, 3, 4, 7, 4, 5, 4, 8, 9, 8]
#print calc_sum(n)
#print calc_avg(n)
#print calc_stan_dev(n)


#Case Study 2
import random
posMessages = [ 'It is certain',
              'It is decidedly so',
              'Without a doubt',
              'Yes definitely',
              'You may rely on it',
              'As I see it, yes',
              'Most likely',
              'Outlook good',
              'Yes',
              'Signs point to yes']
neuMessage = ['Reply hazy try again',
              'Ask again later',
              'Better not tell you now',
              'Cannot predict now',
              'Concentrate and ask again']
negMessage = ['Don\'t count on it',
              'My reply is no',
              'My sources say no',
              'Outlook not so good',
              'Very doubtful' ]

eightMessages = random.sample(posMessages, 4) + random.sample(neuMessage, 2) + random.sample(negMessage, 2)
print random.sample(eightMessages, 1)[0]

