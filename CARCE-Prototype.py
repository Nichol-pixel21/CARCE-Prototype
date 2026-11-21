
def run_carce() :
   print("WELCOME TO CARCE !!")
   print("Here we will explore your hobbies, interests and strengths together.")

   def get_name():
      name = input("So what should we call you young explorer? :")
      while name == "":
         print("You did not enter your name.")
         name = input("Bro, just ell your name man.")
      return name 

   name = get_name()
   country = input("Which country are you from ?")

   def get_age():
      age = int(input("How many days have you spent on planet earth?:"))
      while age < 0 :
         print = ("Age cannot be negative my dear, try again.")
         age = int(input("How many days have yo u spent on planet earth?"))
      return age

   age = get_age()
   if age >= 18:
      print(f"Welome {name}, So let us start by asking a few questions.")
      
   elif age <= 17:
      print(f"Welcome {name} !!!SO let's start by asking a few fun questions about yourself ! ")

   else:
      print(f"We need an age to work with, kindly fill it up !")

   print("IMP : Do NOT think much or contemplate evry answer that comes to your min when you answer th following questions.")

   questions = ("What was your first career that you considered?",
                "What was your childhood hobby?",
                "What are your faourite subjects ?",
                "What have you always struggle with ?",
                "What kind of lifestyle would suit you?") 
      
   options = (("A.Designing, Arts, Ceative", "B.Tech\ programming\ AI ", "C.Manageent\ Business\ Finance", "D. Social\ Research\ Contribution"),
              ("A. Playing mind games\ solving problems\ studies", "B. Sports\ Arts\ Music, C. Organizing\ Groupgames\ , Leader", "D. Helping others\ Volunteering\ beneficial"),
              ("A. Maths\ Science\ IT", "B. Hitory\ Geography\ Political science", "C. Commerce\ Management\ Finance", "D. Arts\ Music\ Others"),
              ("A. Problem-Solving", "B. creativity", "C. Planning", "D. Deep curiousity"),
              ("A. Fast \ Busy\ Hustle", "B.Slow, peaceful, soft" , "C. Balanced"))

   for question in questions:
      print("--------------------")
      print(questions)

      for option in options[question_num] :
          print(option)
         
          question_num += 1 
      
   answer = input("Enter(A, B, C, D)").upper()

   if answer == "a" :
      score += 5 
   elif answer == "B":
      score += 4
   elif answer == "C" :
     score += 3 
   else:
      score += 2
      print("You are done with the mini - quiz!!")


      print("---------------")
      print("FINAL SCORE IS {}")
   
   stress = input("On a scale of 1-10, what is your current stess level?:")
   stress = int(stress)

   if stress > 5 :
      print("You really need to lower that down human!")

   elif stress < 5 :
      print("You a chil guy, keep it up")


   print("Do you have a clear path for it?")
   print("how much do you know about the feild so far ?")
   print("What e your strenggths?")

   print ("THANK YOU FOR USING CARCE !!")
   print (" ********Stick along!*****")

   while True:
      run_carce()

      again = input("Do you anna try CARCE again ? (y/n)")
      if again != "y":
         print("Thank you for exploring WITH cace tAKE CARE BRO.")

      break 

