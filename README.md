# robosys2018-homework1
2018年ロボットシステム学の提出課題1

## 概要
* USBデバイスが接続されたことを認識し、LEDが点灯するプログラム
* main.pyを実行中にUSBデバイス(キーボード、マウスなど)を接続することにより、/dev/usb/hiddev0を検出
* 動画URL: https://youtu.be/fc5arNBySLQ


## 使用環境
* Raspberry Pi 3B
* OS: Ubuntu Mate
* 接続しているUSBデバイス: 有線キーボード

## 参考
* ロボットシステム学第８回講義で扱ったLEDをGPIOピンで制御するデバイスドライバを参考にしました。
https://github.com/ryuichiueda/robosys_device_drivers.git

## 実行方法
* 実行
  ターミナル1
```
$ make
$ sudo insmod myled.ko
$ sudo chmod 666 /dev/myled0
```
  ターミナル2
```
$ python main.py
//なにも接続されていない場合、(ls: cannot access '/dev/usb': No such file or directory)と表示される
```

* 削除する場合
```
$ sudo rmmod myled
$ make clean
```

## 課題
* main.py の実行中にUSBデバイスが2つ以上接続された場合、hiddev が複数表示されるため現段階ではLEDが点灯しなくなる。
--LEDの数を増やし、接続している数がわかるよう変更する必要がある。
