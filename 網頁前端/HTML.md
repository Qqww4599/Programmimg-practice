##HTML概念

- 直接玩HTML5就好，舊的不需要用。

- 網頁是甚麼：網路頁面，展示網路上的各種資源，用於顯示**網路資源**的載體，網頁資源可以是圖片、各種框(輸入框等等)、超連結。

- HTML：Hyper-Text Markup Language(超文本標記語言)

  - 超文本：指網路上展示的內容，Hyper表示不僅僅是文本。

  - 標記：用於描述超文本的程式碼格式。

    ```html
    一般：<標記名></標記名>
    特殊：<標記名>
    ```
    - 頁面上的每一個超文本都會有**對應的標籤**負責

- 標籤中的屬性

  - 指的是標籤中的某個特徵，EX：超連結中有href屬性，表示用戶要跳轉的地址； `<img>`有src屬性，表示圖片標籤展示的圖片地址。

##HTML基礎標籤

- #### **a標籤：負責超連結**

  - ```html
    <a href="跳轉的頁面網址">文本內容</a>
    ```
    
    - href="網址"，href是標籤中的屬性，指定當前用戶跳轉到哪個頁面。

- #### **img標籤：負責圖片**

  - ```html
    <img src="圖片地址" />
    ```
    
  - 屬於特殊格式，不需要結束標籤。

  - src屬性：要展示的圖片地址。

  - 標題標籤：<h1>到<h6>

  - ```html
    <h1>h1文本內容</h1>
    <h2>h2文本內容</h2>
    <h3>h3文本內容</h3>
    <h4>h4文本內容</h4>
    <h5>h5文本內容</h5>
    <h6>h5文本內容</h6>
    ```
    
  - width：設置圖片的寬度
  
  - height：設置圖片的高度
  
  - 建議設置width和height只設置其中一個，另一個按照圖片比例自動調整(可能會導致圖片失真)。
  
- #### **p標籤：段落標籤**

  - ```html
    <p>
    段落內容
    </p>
    
  - 每個p標籤都是獨占一行
    
  - 不帶首行縮進

- #### **br換行標籤**

  - ```html
    <br>
    ```

  - 一個br換一行

- **特殊符號-空格**：`&nbsp;`
  
  - 一個`&nbsp;`表示一個空格
  
- 註釋

  - 是一種特殊的說明，用於對自己城市碼進行說明。在打開頁面時，瀏覽器會自動忽略掉註釋，不影響代碼執行
  - vscode可以利用`ctrl+/`快速生成或刪除註釋

```html
<!-- 註釋內容 -->
<a></a>
<!-- 註釋內容 -->
```





##HTML表格

- #### 基礎標籤

  - `<table></table>`:表示一個表格，行跟列需要用`tr`和`td`表示，`tr`和`td`寫在`table`裡面

    - `border`:表示表格邊框，默認0，以數字為單位

    - `width`:設置整個表格的寬度，以數字為單位

    - `hwight`:設置整格表格的高度，以數字為單位

    - `align`:設置整個表格對於整格頁面的水平對齊方式

    - ```html
      <table border="1" width="200" height="300">
          
      </table>
      ```

    - 

  - `<tr></tr>`:一個`tr`代表一行，本身不包含單元格，單元格需要用`td`表示

    - `align`:設置一行內容的對齊方式，可以去`left`、`right`、`center`，默認是`left`

  - `<td></td>`:一個`td`代表一個單元格，`td`需要寫在`tr`裡面

    - `width`:設置某個單元格的寬度

    - `height`:設置單元格的寬度

    - `align`:設置該單元格內容對齊方式

    - ```html
      <td align="left" width="100" height="100">
      </td>
      ```

    - 

  - `<th></th>`:表示**表格標題行**中的一個單元格

    - td和th的區別：th字體自動加粗

  - `<hr>`:顯示一條貫穿頁面的橫線

- #### 表格拓展

  - 合併單元格

    - `colspan`針對同一行單元格的合併：跨列合併，是`<td>`、`<th>`專屬屬性

    - ```html
      <td colspan"3"></td>
      ```

      - 合併三個單元格

    - `rowspan`:針對同一列不同行單元格合併：跨行合併，是`<td>`和`<th>`專屬屬性

      - ```html
        <td rowspan"3"></td>

  - 控制單元格的間距(現在比較不會用)

    - `cellspacing`:table標籤專屬，用於控制單元格之間的距離

    - `cellpadding`:table標籤專屬，單元格內容和單元格的間距

    - ```html
      <table cellspacing="2" cellpadding="2">
      </table>
      ```

    - **後期被css功能替代。**

##路徑(使用本地圖片以及超連結到本地HTML目標)

- ###概念
  - 路徑是指某個文件在電腦中或網路中的訪問位置

- ### 分類

  - **絕對路徑**:無論在哪個地方使用，永遠都指向的同一個文件，以`http://`開頭的或`C:/`以硬碟開頭的路徑都是絕對路徑。

    ```html
    <a href="http://www.google.com"></a>
    <img src="C://asda/cxas/XXX.png">
    ```

  - **相對路徑**:從參考的位置出發，另一個文件所在位置是相對路徑，參考位置不同，即使是同一個相對路徑，得到的最終文件是不一樣的。

    - 如果要在頁面中使用相對路徑，正在編輯文件目錄即為參考位置。

## 列表

- 分類

  - 無序列表

    - `ul`:定義一個無序列表

    - `li`:一個li指的是一個列表的一個列表項，一個列表可以有多個列表項

    - ```html
      <ul>
          <li>第一個列表項</li>
          <li>第二個列表項</li>
          <li>第三個列表項</li>
      </ul>
      ```

  - 有序列表

    - `ol`:定義一個有序列表，列表以數字進行編號

    - `li`:一個li指的是一個列表的一個列表項，一個列表可以有多個列表項

    - ```html
      <ol>
          <li>第一個列表項</li>
          <li>第二個列表項</li>
          <li>第三個列表項</li>
      </ol>
      ```

  - 定義列表-`<dl>`

    - 每個列表項由一個標題`<dt>`和正文`<dd>`表示
    - `dl`:定義一個定義列表
    - `dt`:定義每個列表項的標題
    - `dd`:每個列表項的正文

- 嵌套列表

  ```html
  <ul>
        <li>第一個列表項
              <ul>
                   <li>二級目錄第一個列表項</li>
                   <li>二級目錄第二個列表項</li>
                   <li>二級目錄第三個列表項</li>
              </ul>
        </li>
        <li>第二個列表項</li>
        <li>第三個列表項</li>
  </ul>
  ```

  

## 表單

- form

  - 一個`<form></form>`標籤，表示一個表單，form標籤可以嵌入表單元素，形成頁面上的表單

  - 作用:配置用戶表單提交的路徑和方式

  - 標籤屬性

    - `method`:指定提交方式，模認是get，還可以取post等等

    - `action`:指定表單數據提交的路徑，需要**手動指定**，一般指定是服務器的ip地址，也可以指定為另一個頁面用於查看效果。

      ```html
      <form action="index.html">
          
      </form>
      當點擊表單裡面的按鈕的時候，會把數據提交到index.html
      ```

      

- 表單元素

  - `input`:實現各種框，會根據自身的type屬性來確定具體表現的是什麼類型的框

    - `type`

      - 輸入框:`type="text"`，input標籤type屬性的默認值

        - 如果需要帶有默認值，可以指定`value`屬性

      - 密碼框:`type="password"`

      - 單選框:`type="radio"`

        - 如果需要多個單選框只選其中一個，需所有的單選框有**一樣的`name`屬性**
        - 可以給默認選項添加`checked`屬性設置為**默認選項**

      - 多選框:`type="checkbox"`

        - 可以給默認選項添加`checked`屬性設置為**默認選項**

      - 按鈕(html5有單獨標籤):`type="button"`

        - 給input設置`value`屬性來給按鈕添加文本，`type="button"`不帶提交功能
        - 如果type為`submit`，可以進行表單提交
        - 如果`type="reset"`，可以重製表單

        ```html
        <input type="text">
        <input type="radio" name="demo" checked> <input type="radio" name="demo">
        <input type="checkbox">
        <input type="button" value="確認">
        <input type="submit" value="確認">
        ```

    - 多個input可以同行顯示

  - `select`:實現下拉選單，搭配`option`標籤

    - 下拉選單

    - ```html
      <select>
          <option>選項1</option>
          <option selected>選項2</option>
          <option>選項3</option>
      </select>
      ```

    - 每個`option`就是一個選項

    - 給`option`添加`selected`設置為默認選項

  - `textarea`:實現文本域

    - ```html
      <textarea cols="" rows="" value=""></textarea>
      ```

    - `cols`:一行的列數，間接用於設置**寬度**(但是不太嚴謹)

    - `rows`:有多少行，間接用於設置**高度**(但是不太嚴謹)

    - `value`:設置默認文本域的內容

  - `button`:實現按鈕(html5)

    - 在`form`標籤裡按鈕會**自帶提交功能**

    ```html
    <button>確認</button>
    ```

- 表單補充(html5新增)

  1. 針對`<input>`的類型進行擴展
     1. 郵件：`type="email"`
     2. 顏色：`type="color"`
     3. 日期：`type="date"`
     4. 範圍：`type="range"`
     5. 數字：`type="number"`
  2. 提供`required`屬性，可以設置某個表單元素為必填
  3. 提供`disable`屬性，可以設置某個表單元素不可更改

  ```html
  <input type="submit" value="提交" disable>
  <input type="text" value="123" disable>
  ```

  









