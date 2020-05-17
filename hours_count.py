# Program to read through the mbox-short.txt and figure out the distribtion by hour of the day for each of the messages.
# You can pull dowm the hour from the 'From ' line and then splitting them up by using the colon.
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
# Go to 'http://www.pythonlearn.com/code/mbox-short.txt' to download the text document.

d = dict()
file = open('mbox-short.txt')
for line in file:
    if line.startswith('From:'):
        continue
    elif line.startswith('From '):
        line = line.strip()
        line = line.split()
        time = line[5]
        time = time.split(':')
        hour = time[0]
        d[hour] = d.get(hour,0)+1
lst = d.items()
tmp = sorted(lst)
for k,v in tmp:
    print(k,v)
quit()
