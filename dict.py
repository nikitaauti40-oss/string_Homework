movies = {}
movies["Dhurandhar"] = ["ranveer singh", "akshay kanna", "sanjay Dutt", "sara Arjun"]
movies["chhaava"] = ["vicky kaushal", "Rashmika mandanna","akshay kanna", "Ajay Devgan"]
movies["Animal"] = ["Tripti Dimri", "Ranveer kapoor", "Rashmika mandanna", "Anil kapoor"]
movies["Tanhaji"] = ["Ajay Devgan", "saif Ali khan", "kajol", "kiran Rathod"]
#print(movies)

for k,v in movies.items():
    for n in v:
        count = 0
        if n == "Rashmika mandanna":
            count = count + 1
            print(k)
            
            
