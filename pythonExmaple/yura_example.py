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
ser = serial.Serial('/dev/cu.usbserial-141420', 115200)  
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
#jogコマンドによる移動関数
def jogCommand(position , rate):#mm,mm/min
    ser.write(str.encode("$J=X"+str(position)+" F"+str(rate)+"\n"))      #X軸10mmへ500mm/minで移動
    line = ser.readline()
    print(line)
    return
#移動距離と移動速度から、完了までの時間ブロッキングで待機する関数
def sleepUntilMotionComplete(travel , rate):#mm,mm/min
    sleepSec = (travel/rate)*60
    time.sleep(sleepSec)
    return
#照明コマンドexample----------------------------------------------
ser.write(str.encode('M67 E0 Q50\n'))
ser.write(str.encode('M67 E1 Q50\n'))
line = ser.readline()
print(line)
#----------------------------------------------照明コマンドexample

#移動コマンドexample----------------------------------------------
jogCancelCode=[0x85,0x0D,0x0A]#ジョグキャンセルコマンド
jogCancel =bytes(jogCancelCode)
#通常のGコードはブロッキングで実行されるので、同期して操作したい場合は、ジョグコマンドを使用する。
#$J=Xnnn Fnnnの形で動作する。Fは送り速度。あまり速いと脱調する。
#0x85 ジョグキャンセルコマンドで、現在のコマンドを中断し、それまでに送ったジョグコマンドのバッファをクリアできる。
#新規のコマンドの発行前に常にジョグキャンセルを送信することで、リアルタイムの操作を簡単に作れる。
ser.write(jogCancel)        #コマンド送信
line = ser.readline()       #GRBLからの応答ダンプ
print(line)


#ジョグコマンドは、実行の完了ではなくバッファへの到達をもってok\r\n or error\r\nを返す。
jogCommand(500 , 1000)#X軸500mmへ1000mm/minで移動
sleepUntilMotionComplete(500 , 1000)

ser.write(jogCancel)      #ジョグキャンセルコマンド
line = ser.readline()
print(line)

jogCommand(10 , 500)#X軸10mmへ500mm/minで移動
sleepUntilMotionComplete(500-10 , 500)


ser.close()             # ポートのクローズ

#----------------------------------------------移動コマンドexample