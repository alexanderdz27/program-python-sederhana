import operasi
 
def test_tambah():
    output = operasi.tambah(6,4)
    assert output == 10
    
def test_kurang():
    output = operasi.kurang(4, 3)
    assert output == 5
    
def test_kali():
    output = operasi.kali(3,5)
    assert output == 15
    
def test_bagi():
    output = operasi.bagi(8,4)
    assert output == 2
