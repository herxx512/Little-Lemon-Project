from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import generics, viewsets, renderers, status
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from .forms import MenuForm, BookingForm
 
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Custom work around for renderer_classes if using TemplateHTMLRender with Concrete Generics. Include a 'template_name' in the class in order for it to work:
class MyTemplateHTMLRender(renderers.TemplateHTMLRenderer):        
    def get_template_context(self, *args, **kwargs):
        context = super().get_template_context(*args, **kwargs)
        if isinstance(context, list):
            context = {'menu':context}
        return context
 
 # 3 Classes below includes custom/override functions to help render and handle requests (via "GET" and "POST") due to limited scope of the front-end in this project:   
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    form_class = MenuForm
        
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'menu.html', {'form':form, 'data': self.list(request, *args, **kwargs).data})
    
    def post(self, request, *args, **kwargs):
        self.create(request,*args,**kwargs)
        return HttpResponseRedirect(reverse('menu'))
        
class SingleMenuItemView(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    form_class = MenuForm

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        form = self.form_class(instance=instance)
        return render(request, 'menu_item.html', {'form': form, 'data': self.retrieve(request, *args, **kwargs).data, 'instance': instance})
    
    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = self.form_class(request.data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('menu'))
        else:
            return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteSingleMenuItemView(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    form_class = MenuForm
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        form = self.form_class(instance=instance)
        return render(request, 'delete_menu_item.html', {'form': form, 'data': self.retrieve(request, *args, **kwargs).data, 'instance': instance}) 
    
    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return HttpResponseRedirect(reverse('menu'))

# Handles all CRUD requests of Booking:
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # Uncomment below to implement Authentication via token
    # permission_classes = [IsAuthenticated]

# Custom functions to handling Booking CRUD requests via "GET" and "POST":
def booking(request):
    booking = Booking.objects.all()
    return render(request, 'booking.html', {'booking': booking})

def bookingDetail(request, pk):
    booking = Booking.objects.get(pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})

def addBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('booking'))
    else:
        form = BookingForm()
    return render(request, 'add_booking.html', {'form': form})

def updateBooking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('booking'))
    else:
        form = BookingForm(instance=booking)

    return render(request, 'update_booking.html', {'form': form, 'booking': booking})

def deleteBooking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        booking.delete()
        return HttpResponseRedirect(reverse('booking'))

    return render(request, 'delete_booking.html', {'booking': booking})