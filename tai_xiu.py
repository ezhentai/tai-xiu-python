# cho modun random and time
import random
import time
print("""  
████████╗ █████╗ ██╗    ██╗  ██╗██╗██╗   ██╗    ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
╚══██╔══╝██╔══██╗██║    ╚██╗██╔╝██║██║   ██║    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
   ██║   ███████║██║     ╚███╔╝ ██║██║   ██║    ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
   ██║   ██╔══██║██║     ██╔██╗ ██║██║   ██║    ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
   ██║   ██║  ██║██║    ██╔╝ ██╗██║╚██████╔╝    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                  GAME BY LẬP TRÌNH LỎ NHƯ ĐĂNG
                                                                                                     """)
print ("TÀI XỈU PYTHON")
while True:
    try:
        kachion=['tài','xỉu']
        player=input('bạn cược "tài" hay "xỉu": ')
        money=input('bạn cược bao nhiêu tiền: ')
        com=random.choice(kachion)
        print('vui lòng chờ kết quả sau 4 giây')
        time.sleep(4)
        print('kết quả là:',"'"+com+"'")
        i=kachion.index(player)
        if kachion[i-1]==com:
            print('bạn thua và mất',"-", money)
        else:
            print('bạn thắng và được',"+",money)
    except:
        print('bạn đã nhập sai vui lòng nhập lại')
# TRÒ CHƠI MANG TÍNH CHẤT GIẢI TRÍ KO ÁP DỤNG VÀO CỜ BẠC