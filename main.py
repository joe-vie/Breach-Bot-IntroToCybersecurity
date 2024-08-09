#Breach Bot Starter Code
breachYear = 2014

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts day of data breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("\nWow! That means it has been " + str(timePassed) + " years since the Yahoo data breach occurred!")

#Introduces breach
print("Would you like to learn about the 2014 Yahoo Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Yahoo breach
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) Breach Details, (b) Yahoo's Response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("\nState-sponsored hackers sent from a foreign government collected data from over 500 million Yahoo accounts. While the data breach occurred in 2014, it was not disclosed to the public until 2016. Data such as emails, names, passwords, DOBs, phone numbers were collected during the breach.\n")
  
  elif topic.lower() == "b":
    print("\nYahoo was generally unresponsive when the actual data breach happened. However, 2 years later when the data breach was known to the public, they were quick to get federal agents and their experts to investigate how the data breach occurred. In addition, they informed the public to change their passwords to avoid any future damage to any other account they may have. They did encounter issues with Verizon considering Verizon bought Yahoo over the summer, causing Verizon’s shock that their deal was made the same week of the breach.\n")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")

#Shares my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains my prespective
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) Relation to the CIA Triad, (b) My Reaction, (c) My Advice, (d) none")
  topic = input()

  if topic.lower() == "a":
    print("\nYahoo’s failure to disclose its data breach to Verizon, a recent purchaser of Yahoo, until the contractual agreement began is a lack of integrity, showing that the company is not a trustworthy option to purchase.\n")

  elif topic.lower() == "b":
    print("\nI have mixed feelings regarding the incident. While it was appropriate for Yahoo to speak to the public regarding the data breach such as encouraging the public to change their passwords to avoid the risks of having any other information stolen, some of the actions Yahoo took weren’t the best. Yahoo took an insanely long time, 2 whole years, to figure out when 500 million of their users had their data stolen which I find to be disappointing. If they were a lot quicker with detecting the breach, many people would be informed quicker and prevent the breach of so many users.\n")

  elif topic.lower() == "c":
    print("\nI would convince victims to take action by informing all of their family members or friends if they also had an account within this company to encourage them to check too. I would give them tips such as to check on Have I Been Pwned and see what actions they could take from there. I would also encourage them to regularly change their passwords to prevent any consistency in their online activity.\n")
    
  elif topic.lower() == "d":
    break
  
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")