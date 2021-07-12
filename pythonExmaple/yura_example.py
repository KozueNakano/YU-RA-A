#移動に使用しているjogコマンドに関して
#https://github.com/gnea/grbl/wiki/Grbl-v1.1-Jogging
#その他のコマンドに関して
#https://github.com/gnea/grbl/wiki
#ボードに関して
#https://github.com/bdring/Grbl_Esp32/wiki
import serial
import time
#初期化処理----------------------------------------------
#デバイス名とボーレートを設定しポートをオープン 
ser = serial.Serial('/dev/cu.usbserial-14130', 115200)  
#起動メッセージ読み飛ばし
time.sleep(3)
ser.reset_input_buffer()
#アラート解除
ser.write(str.encode('$X\n'))
line = ser.readline()#改行までブロッキングで読み込み　タイムアウトが設定できるが設定してない。必要なら設定してerrorをthrowする。
print(line)
#X軸ホーミング
ser.write(str.encode('$HX\n'))
line = ser.readline()#ホーミングに関しては完了してからok\r\nが送信されるので、それを待ってコマンドの実行をはじめる。
print(line)

#----------------------------------------------初期化処理



#移動コマンドexample----------------------------------------------
jogCancelCode=[0x85,0x0D,0x0A]#ジョグキャンセルコマンド
jogCancel =bytes(jogCancelCode)
#通常のGコードはブロッキングで実行されるので、同期して操作したい場合は、ジョグコマンドを使用する。
#$J=Xnnn Fnnnの形で動作する。Fは送り速度。tooltrayの場合は10000に固定でいいと思う。あまり速いと脱調する。
#0x85 ジョグキャンセルコマンドで、現在のコマンドを中断し、それまでに送ったジョグコマンドのバッファをクリアできる。
#新規のコマンドの発行前に常にジョグキャンセルを送信することで、リアルタイムの操作を簡単に作れる。
#おそらく上記の方法はGRBLのモーションスムージングをだいなしにしている


ser.write(jogCancel)      #ジョグキャンセルコマンド
line = ser.readline()
print(line)
#ser.write(str.encode('$J=X500 F10000\n'))      #X軸400mmへ移動
#line = ser.readline()#ジョグコマンドは、実行の完了ではなくバッファへの到達をもってok\r\n or error\r\nを返す。
#print(line)

#中断が見やすいようにX500mmへ到達する前にabort
#time.sleep(1)


#ser.write(jogCancel)      #ジョグキャンセルコマンド
#line = ser.readline()
#print(line)
#ser.write(str.encode('$J=X600 F10000\n'))      #X軸10mmへ移動
#line = ser.readline()
#print(line)

#中断が見やすいようにX500mmへ到達する前にabort
#time.sleep(1)

ser.write(str.encode('$J=X10 F10000\n'))      #X軸10mmへ移動
line = ser.readline()
print(line)


for num in range(10,500,10):
    #中断が見やすいようにX500mmへ到達する前にabort
    time.sleep(0.1)
    ser.write(jogCancel)      #ジョグキャンセルコマンド
    line = ser.readline()
    print(line)
    ser.write(str.encode('$J=X'+str(num)+' F10000\n'))      #X軸10mmへ移動
    line = ser.readline()
    print(line)

for num in range(500,10,-10):
    #中断が見やすいようにX500mmへ到達する前にabort
    time.sleep(0.1)
    ser.write(str.encode('$J=X'+str(num)+' F10000\n'))      #X軸10mmへ移動
    line = ser.readline()
    print(line)


ser.close()             # ポートのクローズ

#----------------------------------------------移動コマンドexample