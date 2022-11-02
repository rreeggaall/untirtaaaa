from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodifh(request):
    judul = "S1 Ilmu Hukum",

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fh.html', konteks)

def sejarahfh(request):
    return render(request, 'sejarahfh.html')