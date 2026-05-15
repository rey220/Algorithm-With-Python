def binary_search(list,find_item) :
    
    batas_bawah = 0
    batas_atas = len(list) - 1
    
    while batas_bawah <= batas_atas :
        
        """
        # ---> menghasilkan nilai index ke 3 = 6
                V V V V V V V
        """
        nilai_tengah = (batas_bawah + batas_atas) // 2 
        
        """
            # ---> variable yg menampung parameter list dengan index ke 3 yaitu 6
                    V V V V V V V
        """
        nilai_list = list[nilai_tengah] 
        
        """
            # ---> mengecek jika variable yg menampung list index ke 3 yaitu 6 sama dengan item yg dicari contoh 6
                        V V V V V V V
        """
        if nilai_list == find_item : 
            
            """
                # ---> mengembalikan nilai tengah karena nilai tengah tadi menujukkan
                    ---> list index ke 3 yaitu 6 sama dengan item yang dicari
                                V V V V V V V V V
            """
            return nilai_tengah             
        
        """
            # ---> mengecek jika variable yg menampung list index ke 3 yaitu 6 lebih besar dari item yg dicari.
                    ---> contoh index ke 3 yaitu 6 lebih besar dari item yg akan dicari yaitu 7
        """
        if nilai_list > find_item : 
            # 6 > # 7
            """
                mengupdate nilai dari variable batas_bawah yang asalnya 0 menjadi nilai_tengah yaitu 3 + 1 = 4
                my_list = [3,4,5,6,7,8,9]
                          [0,1,2,3,4] = nilai batas_bawah yang menjadi 4
                          [9]
                          [6] = nilai batas_atas tetap 6
                          
                          Sehingga pencarian dimulai dari nilai 7 (batas_bawah yang sudah di update) sampai 9 (batas_atas yang nilainya tetap)
                           
                           
                           nilai awal variable batas_bawah yaitu 3 yang berada di index ke 0
                           di update menjadi 7 yang berada di index ke 4 karena 3 + 1 tadi .
                           
                           7 adalah item yang dicari, sehingga 7 lebih besar dari nilai tengah yaitu 6 dari index ke 3.
                            ---> sehingga nilai yang tersisa itu [8,9] 
                           
                        Jadi nilai variable batas_bawah yang tadinya 0,
                        kemudian update menjadi 3+1 = 4, hasil dari mengambil nilai index nilai_tengah 3 + 1
                        
                        [3,4,5,6,7] = tidak akan dicari, sehingga pencarian dimulai dari 7 index ke 4 hingga 9 index ke 6
                        [0,1,2,3,4] 
                        
                        Kesimpulannya : 
                        
                        variable nilai_bawah diubah menjadi 4, yang artinya akan memasuki kondisi dimana batas_bawah (4) < = batas_atas (6),
                        dimana pencarian untuk variale nilai_bawah dimulai di index ke 4 sampai index ke 6.
                        
            """
            batas_bawah = nilai_tengah + 1
        
        # atau else : 
        if find_item < nilai_tengah : 
            # 4 < # 6
            """
                mengupdate nilai dari variable batas_atas yang asalnya 6 menjadi nilai_tengah yaitu 3 - 1 = 2
                my_list = [3,4,5,6,7,8,9]
                           nilai awal variable batas_atas yaitu 9 yang berada di index ke 6
                           di update menjadi 5 yang berada di index ke 2 karena 3 - 1 tadi .
                           [3,4,5] = 2
                           [0,1,2]
                           
                           4 lebih kecil dari item yang akan dicari yaitu 6. 
                            ---> sehingga nilai yang tersisa itu [3,4,5] 
                                                                 [0,1,2] = 2
                                                                                                                   
                        Karena 4 adalah item yang dicari lebih kecil dari 6 nilai tengah list.
                        sehingga, nilai [6,7,8,9] dibuang. kenapa nilai 6 tsb ikut dibuang?
                        karena 6 saja sudah besar, maka nilai besar berikutnya lebih besar juga.
            """
            batas_atas = nilai_tengah - 1
        

my_list = [3,4,5,6,7,8,9]
print(binary_search(my_list,7))