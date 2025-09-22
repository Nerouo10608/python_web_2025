# Lesson2 - Python Functions 函數

## 課程簡介
本課程將深入學習Python中最重要的概念之一：函數(Functions)。函數是組織程式碼、提高程式碼重用性和可讀性的關鍵工具。透過實際範例學習如何定義、呼叫函數，以及掌握各種參數傳遞方式。

## 學習目標
完成本課程後，學員將能夠：
- 理解函數的基本概念和重要性(程式碼重用、模組化、易維護、提高可讀性)
- 學會使用`def`關鍵字定義Python函數
- 掌握位置參數(Positional Arguments)和關鍵字參數(Keyword Arguments)的使用
- 了解預設參數值(Default Values)的設定與應用
- 掌握函數的回傳值機制，包含回傳單個值和多個值
- 實際應用函數解決程式設計問題(溫度轉換、成績處理等)

## 主要課程重點
- 如何定義python的function
- function的參數(paramater)和預設的參數值(default value)  
- 如何呼叫function
- 如何使用引數值呼叫(position arguments)、引數名稱呼叫(argument labels)
- 函數回傳值的使用與處理
- 常見錯誤與注意事項

## 課程大綱
1. **函數基礎概念**
   - 什麼是函數？(具有特定功能的程式碼區塊)
   - 為什麼要使用函數？(程式碼重用、模組化、易於維護、提高可讀性)
   
2. **函數的定義與呼叫**
   - `def` 關鍵字的使用
   - 函數命名規則(英文snake_case)
   - 基本函數結構與docstring

3. **函數參數詳解**
   - 位置參數 (Positional Arguments) - 依順序傳遞
   - 關鍵字參數 (Keyword Arguments) - 指定參數名稱
   - 預設參數值 (Default Values) - 提供預設值
   - 參數傳遞的混合使用方式

4. **函數回傳值**
   - `return` 語句的使用
   - 回傳多個值的技巧
   - 沒有回傳值的函數(回傳None)

5. **實際應用範例**
   - 溫度轉換器(攝氏華氏互轉)
   - 學生成績處理(平均、最高、最低分計算)
   - 數學計算函數(面積、周長計算)

6. **常見錯誤與注意事項**
   - 忘記return語句的問題
   - 預設參數使用可變物件的危險
   - 最佳實作建議

## 實用小範例預覽

### 範例1：簡單問候函數
```python
def greet_person(name, greeting="哈囉"):
    """問候特定的人"""
    return f"{greeting}，{name}！很高興認識你！"

# 呼叫函數
print(greet_person("小明"))              # 哈囉，小明！很高興認識你！
print(greet_person("小華", "你好"))       # 你好，小華！很高興認識你！
```

### 範例2：BMI計算機
```python
def calculate_bmi(weight, height):
    """計算BMI值和健康狀態"""
    bmi = weight / ((height/100) ** 2)
    
    if bmi < 18.5:
        status = "體重過輕"
    elif bmi < 24:
        status = "正常範圍"
    elif bmi < 27:
        status = "過重"
    else:
        status = "肥胖"
    
    return bmi, status

# 使用範例
bmi_value, health_status = calculate_bmi(65, 170)
print(f"BMI: {bmi_value:.1f}, 健康狀態: {health_status}")
```

### 範例3：溫度轉換器
```python
def celsius_to_fahrenheit(celsius):
    """攝氏溫度轉華氏溫度"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """華氏溫度轉攝氏溫度"""
    return (fahrenheit - 32) * 5/9

# 使用範例
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # 25°C = 77.0°F
```

### 範例4：密碼驗證器
```python
def check_password_strength(password):
    """檢查密碼強度"""
    if len(password) < 8:
        return "密碼太短，至少需要8個字元"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password) 
    has_digit = any(c.isdigit() for c in password)
    
    if has_upper and has_lower and has_digit:
        return "密碼強度：強"
    else:
        return "密碼強度：中等或弱"

# 使用範例
print(check_password_strength("Password123"))  # 密碼強度：強
```

## 實作檔案
- `lesson2_1.py` - 函數基礎定義與呼叫
- `lesson2_2.py` - 參數與引數的使用  
- `lesson2_3.py` - 綜合練習與應用

## 練習題目
1. **基礎練習**：寫一個函數計算兩個數字的最大公約數
2. **進階練習**：寫一個函數判斷一個數字是否為質數  
3. **應用練習**：寫一個函數處理購物車，計算總金額和折扣

## 前置知識
- Python基礎語法 (lesson1內容)
- 變數與資料型態
- 基本控制結構(if/else, for/while)
- 串列(list)和字典(dict)的基本操作