from django.shortcuts import render
import pickle
from django.conf import settings


def selfpredict(sent):
	print(settings.BASE_DIR)
	f = open('mycountvec.txt', 'rb')
	cv = pickle.load(f)
	f.close()

	f = open('my main classifier', 'rb')
	classifier = pickle.load(f)
	f.close()

	f = open('my tfidfvec', 'rb')
	tfidfvec = pickle.load(f)
	f.close()
	
	ctrans = cv.transform([sent])
	tf_trans = tfidfvec.transform(ctrans)
	if classifier.predict(tf_trans)[0]:
		return True
	else:
		return False



# Create your views here.
def ask_user(request):
	return render(request, 'mainpage.html')

def confirm(request):
	if request.method == "POST":
		text = request.POST['mytext']
		if selfpredict(text):
			pic = 1
		else:
			pic = 2
		return render(request, 'show_emotion.html', {"pic": pic, 'review': text})


def thankyou(request):
	if request.method == "POST":
		if request.POST.get("no"):
			print("nanannana")
		elif request.POST.get("yes"):
			print("eyahyeahyayeahyaehayhyaheyaheyahe")
	return render(request, 'thanks.html')