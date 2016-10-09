from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.
from models import Album,Song

def listview(request):

    lists=Album.objects.all()

    template='music/list.html'

    context={
        'lists':lists ,
    }

    return render(request,template,context)


def detailview(request,album_id):


    try:
        details=Album.objects.get(id=album_id)

    except Album.DoesNotExist:
        template='music/error.html'
        data={
            'info':'Doesnot exitst'
        }
        return render(request,template,data)

    return render(request,'music/detail.html',{'details':details})

def favourite(request,album_id):
    details=get_object_or_404(Album,pk=album_id)
    try:
        select_song=details.song_set.get(pk=request.POST['song'])


    except(KeyError,Song.DoesNotExist):

        return render(request,'music/detail.html',{
            'details': details,
             'error_message':'Errror Exixts',
        })
    else:
        select_song.is_favourite = True
        select_song.save()


        return render(request, 'music/detail.html', {
            'details': details,

        })

