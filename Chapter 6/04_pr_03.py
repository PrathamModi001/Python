s = input("Enter the article to detect the spam: ")

if(bool(s.count("spam")) or bool(s.count("buy now")) or bool(s.count("make a lot of money")) or bool(s.count("subscribe this")) or bool(s.count("click this"))):
    print("Very SPAMMY text. Please improvise")
else:
    print("Good Job! No spammy texts :)")