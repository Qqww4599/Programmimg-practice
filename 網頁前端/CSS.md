<center><h1>
    <u>CSS</u>
    </h1></center>



##CSS基礎

- 背景
  - 傳統用html實現頁面有很多不方便的地方
    - 樣式和內容程式碼都放在一起，**雜亂、不易閱讀**
    - 無法實現更好的效果
  - HTML和CSS之間的關係
    - HTML只負責頁面的**內容**部分
    - CSS負責**美化頁面**

- 概念
  - 層疊樣式表-(cascading style sheet)
    - 層疊：CSS的一個特性
    - 樣式：標籤的外觀部分。例如尺寸、顏色、形狀、字體等等
    - 表：CSS的程式碼書寫的表現形式類似於一張表
  - 作用：書寫CSS程式碼用於**美化頁面**
- 使用
  - CSS程式碼還是寫在HTML裡面
  - 3種使用方式
    - `嵌入`：利用每個標籤自帶的`style`屬性來設置樣式
    - `內聯`：在**`<head></head>`**中添加`<style></style>`來寫程式，**推薦**
    - `外聯`：創建一個`.css`為後綴的文件，在文件中書寫CSS程式碼，在HTML頁面中的`<head></head>`中通過`<link href="css文件路徑">`引入CSS文件，**推薦**

```html
<img src="" sytle="css程式碼">

<style>
    css代碼
</style>

<link href="css文件路徑">
```

- css代碼書寫格式

  - 由**選擇器**和**屬性代碼**構成

  ```css
  標籤選擇器{
  	css屬性名1:屬性值1;
  	css屬性名2:屬性值2;
      css屬性名n:屬性值n;
  }
  ```

  - css會通過標籤選擇器來找到設置樣式的標籤，設置對應的樣式(css屬性)

- 註釋內容

  - `/*註釋內容*/`

- css基礎屬性

  - 文字類

    - `color`:設置標籤的**文本顏色**

    - `font-size`：設置字體大小。默認與瀏覽器有關，一般為16px

    - `font-family`：設置標籤文字字體類型，默認字體跟系統有關。可以設置多種字體，若沒有該字體則使用默認字體

    - `text-decoration`：設置文本的樣式，默認超連結有下畫線
      
      - `underline`：下畫線，默認超連結
      - `none`：刪除樣式
      - `line-through`：類似於刪除線
      
    - `text-align`：設置標籤內部內容的對齊方式，center、left、right

    - `font-weight`：設置標籤文字的粗細程度，可以取數字100到900，間格為100，也可以使用`bold`、`bolder`

      ```css
      font-weight:300 |bold |bolder
      ```

    - `line-height`：設置標籤一行內容的高度，簡稱**行高**，標籤裡的一行內容會顯示在行高的中間
      - 文字垂直居中：設置行高與標籤高度一致

  - 尺寸類

    - `width`：設置標籤的寬度，以像素或百分比為單位

    - `height`：設置標籤的高度，以像素或百分比為單位

    - `border`：設置標籤的邊框，需要設置邊框的寬度，邊框的樣式，邊框的顏色

      - `border:1px solid red`：1px的紅色實現邊框
      - `border-left`：單獨設置左邊框
      - `border-right`：單獨設置右邊框
      - `border-top`：單獨設置上邊框
      - `border-bottom`：單獨設置下邊框

      ```css
      body{
          width:
      }
      ```

    - `padding`：

  - 背景

    - `background-color`：設置背景顏色

    - `background-image`：設置某個標籤的背景圖片

      ```css
      選擇器{
          background-image:url("圖片路徑")
      }
      
      ```

    - `background-size:cover`：設置背景圖片拉伸

    - `background-position`：背景圖片的顯示位置，分為x軸y軸(網頁設計中x軸向右，y軸向下)

    - `background-repeat`：設置背景圖片是否平鋪，默認平鋪(repeat)，不平鋪(no-repeat)

  - 其他

    - `margin:0 auto;`：特殊用法，用於將某個標籤相對**頁面**水平居中，不適用於內容

    - `outline:none`：取消瀏覽器默認邊框，針對表單元素

    - `display`：設置標籤的顯示模式，塊級元素(block)、行內塊級元素(inline-block)、行內元素(inline)、隱藏(none)

      ```css
      display:block;
      display:inline;
      ```

      

  - `color`屬性及`font-size`對**標籤**及其**子標籤**都有效果

  ```css
  body{
      color:white
  }
  ```

  

- css基礎選擇器

  - 標籤選擇器

  ```css
  標籤名{
      css屬性名1:屬性值1;
  }
  例如:
  body{
      background-color: black;
  }
  效果：對頁面上所有的body設置背景顏色為黑色
  ```

  - 對頁面上所有同類型的標籤設置樣式
  - 應用：給同類型標籤設置通用樣式

- id選擇器

  - 能夠對`單獨的某個標籤`設置樣式
  - 步驟：
    1. 給需要單獨設置樣式的標籤添加`id`屬性
    2. 利用css的id選擇器來設置樣式
  - 同一個頁面**不允許有一樣的id屬性**

```css
html
<td id="logo"></td>
css
#id屬性值{
	css屬性名1:屬性值1;
}

例子：
#logo{
    text-align:left;
}
效果：會對id屬性是logo的標籤設置齊內容左對齊
```

- class選擇器

  - 對具有**`相同class屬性`**的**`多個標籤`**同時設置樣式

  - 步驟：

    1. 給需要設置樣式的標籤一樣的class屬性，class屬性每個標籤都可以設置
    2. 利用class選擇器來進行設置

    ```css
    .class屬性值{
     css屬性名1:屬性值1;
    }
    
    例子
    .demo{
    	color:white;
    }
    效果：對class屬性為demo的文字顏色設置為白色
    ```

    - 特別適合頁面上多個標籤有**同樣的樣式**

- 組合選擇器

  - 概念：同時使用**id、class、標籤選擇器**中的一種或多種，來達到給多個標籤設置樣式的目的，具有條件的選擇器

  - 作用：減少不必要的class代碼

  - 思路：利用標籤的**嵌套**關係來精確尋找需要設置樣式的標籤

  - 例子

    ```css
    找到所有table標籤裡的a標籤，字體顏色為白色
    table a{
        color: white;
    }
    
    找到所有body標籤下的class為item標籤，字體顏色為紅色
    body .item{
        color:red;
    }
    ```

    

- 偽類選擇器

  - 根據用戶游標行為來改變標籤的樣式

  - 分類

    - `a:link`：超連結專屬，頁面一打開超連接就有的樣式，**舊屬性**
    - `a:visit`：超連結專屬，超連結被訪問後的樣式
    - `:hover`：游標璇停到標籤上時標籤使用的樣式
    - `:active`：游標點擊標籤不釋放時使用的樣式
    - `:focus`：當標籤獲取游標焦點時使用的樣式，比如點擊輸入框

  - 使用語法

    ```css
    a:link{
        css屬性名1:屬性值1;
    }
    a:visit{
        css屬性名1:屬性值1;
    }
    非偽類選擇器:hover{
        css屬性名1:屬性值1;
    }
    非偽類選擇器:active{
        css屬性名1:屬性值1;
    }
    非偽類選擇器:focus{
        css屬性名1:屬性值1;
    }
    ```

    

## 選擇器命令規範

- id屬性、class屬性

  - 盡量體現標籤的作用

  - 不能以數字開頭

    ```html
    <a id="head-logo"></a>
    ```



## CSS技巧

- 用極小的圖片配合`background-repeat`實現整張背景圖



## HTML標籤的顯示模式

- 塊級元素：block
  - 指的是獨占一行的標籤：`p` 、`h1~h6`、`table`、`tr`、`oi`、`li`、`hr`
- 行內塊級元素：inline-block
  - 指的是同行顯示，但可以設置寬高的屬性：`input`、`textarea`、`select`、`button`、`img`
- 行內元素：inline
  - 指的是可以同行顯示的標籤：`a`、`span`
  - 行內元素中`a`和`span`是**不能**設置寬高的
- 顯示模式可以通過`display`來進行轉換

