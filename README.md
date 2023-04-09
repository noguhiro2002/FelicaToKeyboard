# FelicaToKeyboard
A Python script to read Felica card infomation and input it as keyboard input, with a rate of once per second.

![animation](https://github.com/noguhiro2002/FelicaToKeyboard/blob/main/readme/animation.gif?raw=true)


## Summary 
This is the first of a series of Python scripts to interact with Felica cards. The current script reads the IDm from a Felica card and inputs it as keyboard input at a rate of once per second.

これは、Felicaカードとやりとりする一連のPythonスクリプトの最初のものです。現在のスクリプトは、FelicaカードからIDmを読み取り、1秒に1回の速度でキーボード入力として入力します。

## Usage

1. First, install the following Python libraries.

```
pip install pyscard 
pip install pyautogui
pip install playsound # If you want to play sound when read a card IDm.
```

2. Run the program.

```
python Felica_idm_input.py # Normal version
python Felica_idm_input_withSound.py # with sound. Please add sound file path.
```

3. When you hold the IC card over the card reader, the IDm will be entered as a keyboard input.

---

1. まず、以下のPythonライブラリをインストールしてください。

```
pip install pyscard
pip install pyautogui
pip install playsound # IDm読み込み時にサウンドを鳴らす場合はこちらをご使用ください。
```

2. プログラムを実行します。

```
python Felica_idm_input.py
python Felica_idm_input_withSound.py # サウンドを鳴らす場合はこちら. Settingに鳴らすサウンドファイルのpathを記してください。
```

3. カードリーダーにICカードをかざすと、IDmがキーボード入力されます。

## Note

- This program uses the first detected card reader. If multiple card readers are connected, you need to specify the reader to use.
- The security of Felica's IDm is low, and it can be easily forged. If reliability is required, use more secure methods such as internal authentication.

---

- このプログラムは、最初に検出されたカードリーダーを使用します。複数のカードリーダーが接続されている場合、リーダーを指定する必要があります。
- FelicaのIDmはセキュリティが低く、偽造される可能性があります。信頼性が必要な場合は、内部認証などの安全な方法を利用してください。
- 効果音は[効果音ラボ](https://soundeffect-lab.info/)さんなどから入手することができます。

## License

In Apr./08/2023, This project uses the following third-party libraries:

- [pyscard](https://github.com/LudovicRousseau/pyscard): Distributed under the LGPL-2.1 license.
- [pyautogui](https://github.com/asweigart/pyautogui): Distributed under the BSD-3-Clause license.
- [playsound](https://github.com/TaylorSMarks/playsound): Distributed under the MIT license。

Please refer to the respective licenses for more information.

---

このプロジェクトでは、次のサードパーティのライブラリを使用しています (2023/04/08 現在) :

- [pyscard](https://github.com/LudovicRousseau/pyscard) : LGPL-2.1ライセンスで配布されています。
- [pyautogui](https://github.com/asweigart/pyautogui): BSD-3-Clauseライセンスで配布されています。
- [playsound](https://github.com/TaylorSMarks/playsound): MITライセンスで配布されています。

詳細については、各ライセンスを参照してください。
