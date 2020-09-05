from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')

def movies_news_view(request):
    news1="Pooja Hegde expresses her gratitude towards her fans as she crosses 8 million mark on Instagram!"
    news2="Ileana D’Cruz: I don’t know how Anees Bazmee handles so many actors together"
    news3="'Marjaavaan' box office collection day 3: Sidharth Malhotra-Riteish Deshmukh's film collects Rs 9.75 crore, faces tough competition from Ayushmann Khurrana's 'Bala'"
    news4="Nawazuddin Siddiqui and Athiya Shetty's 'Motichoor Chaknachoor' leaked online"
    news5='Salman and Katrina going to marry soon'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'newsapp/mnews.html',my_dict)

def sports_news_view(request):
    news1="Kohli scored double century"
    news2="India vs Bangladesh: Pink ball Test live streaming, start time and broadcast details"
    news3="BCCI Persident Saurav Ganguli confident of new start for cricket board"
    news4="Jemimah Rodrigues, Rekha Yadav top Indians in women's T20I player rankings"
    news5='''Speaking at his 1st press conference after taking over as Tottenham Hotspur manager,
     Jose Mourinho said he is relaxed and motivated to do well in his new managerial stint.'''
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'newsapp/snews.html',my_dict)

def politics_news_view(request):
    news1="Congress Hits out at BPCL Disinvestment Decision, Says Govt 'Selling the Country'"
    news2="Parliament Parleys: Pegasus Tie-Breaker, Kissa Kursi ka and Sonia Gandhi’s SPG Tangle"
    news3="After Owaisi, Mamata Fumes Over Jharkhand Disom Party's 'Efforts' to Boost Tribal Support for BJP in Bengal"
    news4="'Cat & Mouse Living Together': AIADMK's Take on Tie-up Between Kamal Haasan and Rajinikanth"
    news5="Malegaon Blast Accused Pragya Thakur Nominated to 21-MP House Panel on Defence"
    news6="Thakur had defeated former Madhya Pradesh chief minister Congress leader Digvijaya Singh in the Lok Sabha polls earlier this year."
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6}
    return render(request,'newsapp/pnews.html',my_dict)
