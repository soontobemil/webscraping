from bs4 import BeautifulSoup
import requests #requesting information from the real website.
import time

print('put some skills that you are unfamiliar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs): #enumerate function iterate over the index of the jobs list 
        published_date = job.find('span', class_ = 'sim-posted').span.text #if the published date does not have the mathching condition, the function will not execute 
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip() # or replace(' ','')
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href'] # you will receive the value of href within the attribute of "a"
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:#f is a variable #call posts directory to name index.txt (텍스트 파일) 'w=write' is the permission level
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                    #f.write('') #empty line is used to see the divisions between lines
                print (f'Great Job! File Saved:{index} under posts')
   
if __name__ == '__main__':
    while True: 
        find_jobs()      
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)#allows your program to wait certain amount of time argument by second

# general convention of python              
# single underscore _ -> the name is to be treated as private by the programmer
# double underscore = aka dunder -> it's going to make harder for someone to create collision when soemone else extneds the certain class name
# dunder -> __ name mangling to prevent collision // more of a protection from subclasses from changing attributes
# dir -> looking for an attribute of an object