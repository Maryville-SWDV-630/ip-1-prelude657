class Teams:
    def __init__(self,members):
        self.__myTeam=members
    #initiates the team

    def __len__(self):
        return len(self.__myTeam)
     #returns the number of member on the team   

    def __contains__(self, member):
    #returns members of the team contained
        return member in self.__myTeam

    def __iter__(self):
    #print("Iterator")
        return iter(self.__myTeam)

def main():
    classmates=Teams(['John','Steve','Tim'])
    
    print (len(classmates))
    print('Tim' in classmates)
    print('Sam' in classmates)
    
    iterator=iter(classmates) #iterator

    for member in iterator:
        print(member,end=" ")
        
main()
