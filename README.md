# GSoCeXract2021

##Procedure
Ensure u have phthon installed
Compile and run f.py file using
"phyton3 f.py"



###First Try
Firstly I tried with normal requests and beautysoup procedure i.e geting html files and searching tags in them (inspecting through Browser developer tools.
But it didn't worked as content on webpage is modified but javascript depending on scroll.
###FINAL
Then somehow when I saw network in developer tools and findout the source from where javascript was extracting data. Response received was in JSON format.
So, I simpliy changed my URL and it worked!
