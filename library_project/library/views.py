import openpyxl
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowForm

class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'
    paginate_by = 8

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

class BorrowListView(ListView):
    model = BorrowRecord
    template_name = 'library/borrow_list.html'
    context_object_name = 'records'
    paginate_by = 5

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/form.html'
    success_url = reverse_lazy('author-list')

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/form.html'
    success_url = reverse_lazy('book-list')

class BorrowCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowForm
    template_name = 'library/form.html'
    success_url = reverse_lazy('borrow-list')

class ExportExcelView(View):
    def get(self, request):
        wb = openpyxl.Workbook()
        
        #..... Authors
        ws1 = wb.active
        ws1.title = "Authors"
        ws1.append(['ID', 'Name', 'Email'])
        for a in Author.objects.all():
            ws1.append([a.id, a.name, a.email])

        # ......Books
        ws2 = wb.create_sheet("Books")
        ws2.append(['ID', 'Title', 'Author'])
        for b in Book.objects.all():
            ws2.append([b.id, b.title, b.author.name])

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="library_data.xlsx"'
        wb.save(response)
        return response