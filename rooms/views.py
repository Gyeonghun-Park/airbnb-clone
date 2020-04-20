# Using Listview
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#listview-working-with-many-django-objects
# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/

from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        # unbound form: form not given with some data
        # form = forms.SearchForm()

        if country:

            # give form with user's GET request
            # form validates data in Get request
            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                # refer to field lookups for querying and filtering
                # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#field-lookups
                # refer to field lookups for querying and filtering "__lte" stuff
                # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
                filter_args = {}

                if city != "":
                    # adding arguments as {"city__startswith" : city}
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                # Not using primary key, but just use object from database itself
                if room_type is not None:
                    filter_args["room_type"] = room_type

                # filtering with foreignkey relationship -> refer to models.py
                # room_type 0 is entire place
                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                # accessing foreignkey is easy. "pointing fieldname"__"pointed fieldname"
                if superhost is True:
                    filter_args["host__superhost"] = True

                # INSTEAD OF PRIMARY KEYS,
                # Actual amenities and facilities items are retreived in cleaned data
                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                rooms = models.Room.objects.filter(**filter_args)

        else:
            # empty form without validation
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
