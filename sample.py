# 1
# create a search form in forms.py :
class SearchFrom(forms.Form)
    q = forms.Charfield()
# ===================================================================================
# 2
#  create custom_context_processor.py  and give the search form to template :
def search(request):
    return {'search_form' : SearchForm() }
  
# ===================================================================================
# 3
#  add your context processor to TEMPLATES in settings.py
# ===================================================================================
# 4
# go to your template and use search_form that you initialized as dictionary :
 <form method="get" novalidate>
     {{search_form}}
     <input type="submit" value="q">
 </form>
# ===================================================================================
# 4
# go to your queryset whatever it is and get 'q' key and filter by this keyword
class SongListView(View):

    def get(self,request):
        songs = Song.objects.all()
        
        if request.GET.get('search'):
            q = request.GET.get('search')
            songs = songs.filter(
              Q(title__icontains=q)
             | Q(lyrics__icontains=q) 
             | Q(artist__name__icontains=q))
            
        context = {'songs':songs,'page_title':self.page_title}
        return render(request,self.template_name,context)
