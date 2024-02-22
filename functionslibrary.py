class allworkoutfunctions():
    def subfieldsiai():
        subfields=["sub fields in AI are=","machine learning","neural networks","vision","robotics","speech processing","natural language processing"]
        for y in subfields:
            print(y)
    def oddeven():
        num=int(input("enter a number:"))
        
        if((num%2)==0):
            print(num,"is even number")
            message="even number"
        else:
            print(num,"is odd number")
            message="odd number"
    def eligibilityofmarrige():
        gender=input("your gender=")
        age=int(input("your age="))
        if(gender=="male"):
            if(age>=21):
                print("eligible")
                message="eligible"
            else:
                print("not eligible")
                message="not eligible"
        elif(gender=="female"):
            if(age>=18):
                print("eligible")
                message="eligible"
            else:
                print("not eligible")
                message=" not eligible"
        return message  
    def subjects():
        subject1=int(input("subject1="))
        subject2=int(input("subject2="))
        subject3=int(input("subject3="))
        subject4=int(input("subject4="))
        subject5=int(input("subject5="))
        total=subject1+subject2+subject3+subject4+subject5
        print("total=",total)
        percentage=(total/5)
        print("percentage is=",percentage)
    def triangle():
        height=34
        breadth=32
        print("height=",height)
        print("breadth=",breadth)
        print("area formula=(height*breadth)/2")
        areaoftriangle=(height*breadth)/2
        print("areaoftriangle=",areaoftriangle)
        height1=2
        height2=4
        breadth2=4
        print("height1=",height1)
        print("height2=",height2)
        print("breadth2=",breadth2)
        print("perimeter formula=height1+height2+breadth2")
        perimeteroftriangle=height1+height2+breadth2
        print("perimeteroftriangle=",perimeteroftriangle)
