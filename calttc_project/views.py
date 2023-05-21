from django.shortcuts import render, redirect
from announcements.models import Announcement
from images.models import CarouselImage
import os
from django.conf import settings

 
def home(request):
    # should just have "Cal Table Tennis" as Title for not 
    # "Home | Cal Table Tennis" for search result optimization and
    page_title = None
    if 'next' in request.GET:
        return redirect(request.GET.get('next'))
    else:    
        all_announcements = Announcement.objects.all()
        home_announcements = Announcement.objects.filter(on_home_page=True)
        all_carousel_images = CarouselImage.objects.order_by('name')
        if all_carousel_images:
            primary_carousel_image = all_carousel_images[0]
            carousel_images = all_carousel_images[1:]
        primary_carousel_image
        return render(request, "home.html",
            {
            'page_title': page_title,
            'primary_carousel_image' : primary_carousel_image,
            'carousel_images': carousel_images,
            'home_announcements': home_announcements,
            'all_announcements': all_announcements,
            }
        )

def graphics(request):
    page_title = "Graphics"
    if settings.PRODUCTION:
        STATIC_ROOT = settings.STATIC_ROOT
    else:
        STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')
    def not_a_file(file):
        return not os.path.isfile(file) and  '.' in file and not '.xml' in file and not '.webmanifest' in file
    # logos
    logos_raw = os.listdir(os.path.join(STATIC_ROOT, "graphics/logos"))
    logos_raw.sort()
    logos = filter(not_a_file, logos_raw)
    # sports club logos
    logos_sports_club_raw = os.listdir(os.path.join(STATIC_ROOT, "graphics/logos_sports_club"))
    logos_sports_club_raw.sort()
    logos_sports_club = filter(not_a_file, logos_sports_club_raw)
    # favicons
    favicon_raw = os.listdir(os.path.join(STATIC_ROOT, "graphics/favicon"))
    favicon_raw.sort()
    favicon = filter(not_a_file, favicon_raw)
    #company icons
    company_icons_raw = os.listdir(os.path.join(STATIC_ROOT, "graphics/company_icons"))
    company_icons_raw.sort()
    company_icons = filter(not_a_file, company_icons_raw)   
    #signs
    signs_raw = os.listdir(os.path.join(STATIC_ROOT, "graphics/signs"))
    signs_raw.sort()
    signs = filter(not_a_file, signs_raw)
    #assets
    assets_raw = os.listdir(os.path.join(STATIC_ROOT, "graphics/assets"))
    assets_raw.sort()
    assets = filter(not_a_file, assets_raw)

    
    return render(request, "graphics.html",
        {
        'page_title': page_title,
        'logos': logos,
        'logos_sports_club': logos_sports_club,
        'favicon': favicon,
        'company_icons': company_icons,
        'signs': signs,
        'assets': assets,
        }
    )
