import os
import pyautogui
import pandas as pd

excelFilename = "profile/action.xlsx"
actionMap = {}
clickMap = {"左键单击":"left,1", "左键双击":"left,2", "右键单击":"right,1", "右键双击":"right,2"}

def readSetting():
    data = pd.read_excel(excelFilename)
    for i in range(len(data)):
        # 将excel中文件名和对应的操作存储在字典中
        actionMap[data.loc[i].values[0]] = data.loc[i].values[1]
    print(actionMap)

def action():
    for filename in actionMap.keys():
        imageFilename = os.path.join("images", filename)
        click = clickMap[actionMap[filename]]
        buttonType = click.split(",")[0]
        clickNum = int(click.split(",")[1])
        print(imageFilename)
        location = pyautogui.locateCenterOnScreen(imageFilename, confidence = 0.6)
        pyautogui.click(x = location[0], y = location[1], button = buttonType, clicks = clickNum, duration = 2)

def main():
    readSetting()
    action()

if __name__ == '__main__':
    main()