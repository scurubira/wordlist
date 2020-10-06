from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(1970, 1, 1)
end_date = date.today()
with open('wordlist_datas.txt','w') as f:
    for single_date in daterange(start_date, end_date):
        f.writelines(single_date.strftime("%d%m%Y") + '\n')
