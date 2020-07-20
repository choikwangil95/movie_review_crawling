from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Moviedata
from .forms import ReviewSearchForm
from django.db.models import Q
from django.core.paginator import Paginator

class HomeView(ListView, FormView):
    template_name = 'index.html'
    model = Moviedata
    form_class = ReviewSearchForm
    pagenate_by = 5

    # 검색
    def form_valid(self,form): # 값이 전달 됬을 경우
        
        title = '%s' %self.request.POST['title'] # 검색어 
        review_list = Moviedata.objects.filter(
            Q(review__icontains=title) # Q 객체를 사용해서 검색한다. 
                                      # review 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사 
                                      # icontains는 띄어쓰기도 알아서 처리해줌
        ).distinct() #중복을 제거한다.  

        word_list = []

        # 검색된 WordCount
        for data in review_list:
            word_list.append(data.title)

        word_dictionary = {}

        for word in word_list:
            if word in word_dictionary:
                # Increase
                word_dictionary[word] += 1
            else:
                # add to the dictionary
                word_dictionary[word] = 1

        title_list = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)

        context = {
            'review_list' : review_list,
            'word' : title,
            'form' : form,
            'count' : len(review_list),
            'dictionary': word_dictionary.items(),
            'title_list' : title_list,
        }
        
        return render(self.request, self.template_name, context)    # No redirection

    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_list'] = Moviedata.objects.all()           # 모든 objects 가져오기

        word_list2 = []

        # 검색된 WordCount
        for data in object_list:
            word_list2.append(data.title)

        word_dictionary2 = {}

        for word in word_list2:
            if word in word_dictionary2:
                # Increase
                word_dictionary2[word] += 1
            else:
                # add to the dictionary
                word_dictionary2[word] = 1

        title_list2 = sorted(word_dictionary2.items(), key=lambda x: x[1], reverse=True)

        context['dictionary2'] =  word_dictionary2.items()
        context['title_list2'] = title_list2

        return context

    # pagination
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        posts = paginator.get_page(page)
        return context

class ReviewList(ListView):
    model = Moviedata
    template_name = 'review.html'

    #pagination
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ReviewList, self).get_context_data(**kwargs)
        
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        posts = paginator.get_page(page)
        return context