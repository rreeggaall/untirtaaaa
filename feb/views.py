from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodifeb(request):
    judul = "S1 Managemen", "S1 Akuntansi", "S1 Ilmu Ekonomi Pembangunan", "S1 Ekonomi Syariah", "D3 Akuntansi", "D3 Marketing", "D3 Perpajakan", "D3 Keuangan Perbankan"

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'feb.html', konteks)

def sejarahfeb(request):
    return render(request, 'sejarahfeb.html')
