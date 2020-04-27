from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 12
    paginate_orphans = 4
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

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                # Paginating Search Result
                paginator = Paginator(qs, 12, orphans=4)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                query_str = request.environ.get("QUERY_STRING")

                return render(
                    request,
                    "rooms/search.html",
                    {"form": form, "rooms": rooms, "query_str": query_str,},
                )

        else:
            # empty form without validation
            form = forms.SearchForm()

        # precautionary measure when people modify url queries  without using search bar
        return render(request, "rooms/search.html", {"form": form})


class EditRoomView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Room
    template_name = "rooms/room_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room


class RoomPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Room
    template_name = "rooms/room_photos.html"

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room


@login_required
def delete_photo(request, room_pk, photo_pk):
    user = request.user
    try:
        room = models.Room.objects.get(pk=room_pk)
        if room.host.pk != user.pk:
            messages.error(request, "Cant delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("rooms:photos", kwargs={"pk": room_pk}))
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
