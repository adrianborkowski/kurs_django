from django.views.generic import DetailView, FormView
from .models import Message
from .forms import MessageForm


# class MessageDetailView(DetailView):
#     model = Message


class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()     # bo form jest instancja ModelForm, który posiada metodę save()
        return super(MessageAddView, self).form_valid(form)     # odwołanie do klasy pierwotnej

    # def form_invalid(self, form):
