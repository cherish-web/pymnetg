# pymnetg
python封装三菱光纤板卡读写库

demo_write
-----
```python
worker = MnetgWorker(255, 0, ChanEnum.CC_Link_IE_Controller_1)
worker.connect()
if worker.is_connected():
    print("MNETG Connect Success!")

while True:
    input_str = input('请输入寄存器地址(W0000,10|B0000,10):')
    if len(input_str.split(',')) == 2:
        datas = input_str.split(',')[1]
        input_str = input_str.split(',')[0]
        try:
            print(worker.write(input_str, for data in datas.split(':')))
        except Exception as e:
            # print("输入错误, 程序终止",e)
            # mc.close_connect()
            # break
            print(e)
```

demo_read
-----
```python
worker = MnetgWorker(255, 0, ChanEnum.CC_Link_IE_Controller_1)
worker.connect()
if worker.is_connected():
    print("MNETG Connect Success!")

while True:
    input_str = input('请输入寄存器地址(W0000,1:2:3|B0000,1:0:1:0):')
    length = 1
    if len(input_str.split(',')) == 2:
        length = input_str.split(',')[1]
        input_str = input_str.split(',')[0]
    try:
        print(worker.read(input_str, int(length)))
    except Exception as e:
        # print("输入错误, 程序终止",e)
        # mc.close_connect()
        # break
        print(e)
```
