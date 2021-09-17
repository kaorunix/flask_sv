# タスクステータス2テーブル API定義

## 新規タスクステータスの作成

### URL

/task_status2/create

### Method

POST

### Request

```
{
    "status_name":
    "background_color":
    "operation_account_id":
}
```

### Response

```
{
  "body" : "",
  "status": "I0001",
  "message": "task status {} was created.",
  "detail": ""
}
```


## タスクステータス一覧の取得

### URL

/task_status2/list

### Method

GET

### Request

GETなのでなし

### Response

```request
{
  "body": [
        {
        "name": "task_status2",
        "id": <task_status2_id>,
        "task_status_name": <task_status2_name>,
        "background_color": <background_color>
    }
  ],
  "status": {
    "code" : "I0001",
    "message" : "",
    "detail" : ""
  }
}
```

## タスクステータスIDを指定した検索

### URL

/task_status2/get/<task_status2_id>

### Method

GET

### Request

なし

### Response

```request
{
  "body": {
     "name": "task_status2",
     "id": <task_status2_id>,
     "task_status_name": <task_status2_name>,
     "background_color": <background_color>
  },
  "status": {
    "code" : "I0001",
    "message" : "",
    "detail" : ""
  }
}
```


### タスクステータスの更新


### URL

/task_status2/update/<task_status2_id>

### Method

POST

### Request

```
{
    "status_name":
    "background_color":
    "operation_account_id":
}
```

### Response

```
{
  "body" : "",
  "status": "I0001",
  "message": "task status {} was updated.",
  "detail": ""
}
```


### タスクステータスの更新


### URL

/task_status2/update/<task_status2_id>

### Method

POST

### Request

なし

### Response

```
{
  "body" : "",
  "status": "I0001",
  "message": "task status {} was deleted.",
  "detail": ""
}
```


