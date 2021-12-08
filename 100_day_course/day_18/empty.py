
def annouce_cat(cat):
    print(cat["color"])
    print(cat["servents"])
    print(cat["favarate food"])

class Cat:
    def __init__(self,color:str,servents:str,favarate_food:str) -> None:
        self.color=color
        self.servents=servents
        self.favarate_food=favarate_food
    
    def announce(self):
        print(self.color)
        print(self.servents)
        print(self.favarate_food)

        


def main():
    molly={"color":"Black and white","servents":"Shayan and Nan","favarate food":"can food"}
    imaginary_cat={"color":"white","servents":"Shayan and Nan","favarate food":"cat food"}

    annouce_cat(molly)
    annouce_cat(imaginary_cat)

    molly=Cat(color="Black and white",servents="Shayan and Nan",favarate_food="can food")
    imaginary_cat=Cat(color="white",servents="Shayan and Nan",favarate_food="cat food")

    molly.announce()
    imaginary_cat.announce()


main()
