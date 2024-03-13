# autolol
autolol python3.8

#### 创建环境

`python -m venv env`

#### 使用环境

`env\Scripts\activate`

#### 安装依赖

`pip install -r requirements.txt`

#### 运行

`python main.py`

#### 退出环境

`deactivate`

### UI设计

```
pyside6-designer.exe main.ui
pyside6-designer.exe card_library.ui
```

#### 编译

```
pyside6-uic.exe main.ui -o main_ui.py
pyside6-uic.exe card_library.ui -o card_library_ui.py
```

