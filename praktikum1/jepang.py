import random 

def Jepang():
    fn = ["kobayakawa","Hasegawa","Yamaha","Honda","Kiyawisa"]
    ln = ["tatsuo","takeru","yamato","shiba","himeno","hirai"]
    firstname = random.choice(fn)
    lastname = random.choice(ln)
    name = firstname + " " + lastname
    print(name)


def indonesia():
    fn = ["asep","ujang","yanto","oman","usmena","firmena","tajudin","timan"]
    ln = ["suproto","udin","wati","suzuki","jindan","utina","doang","aja"]
    firstname = random.choice(fn)
    lastname = random.choice(ln)
    name = firstname + " " + lastname
    print(name)

indonesia()
