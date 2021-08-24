## スプリントAPI設計

---

<br>

### スプリントの検索

### URL
/sprint/get

### HTTP METHOD
GET

### request
なし

### response
```
{
  "body" : {
      "id": 1,
      "project_id": 1,
      "sprint_name": "sprint_1",
      "sprint_remarks": "スプリント特記事項",
      "sprint_start_date": "2021-08-01",
      "sprint_end_date": "2021-08-14",
      "sprint_status": 2,
      "objectives_velocity": 10,
      "result_velocity": 8,
      "create_by": "11111",
      "create_name": "yamada",
      "create_at":"2021-08-01 10:00:00",
      "update_by": "11111",
      "update_name": "yamada",
      "update_at":"2021-08-14 17:00:00"
  },
  "status": {
    "code" : "I0001",
    "message" : "",
    "detail" : ""
  }
}
```
<br>

### スプリントの登録

---

<br>

### URL
/sprint/create

### HTTP METHOD
POST

### request
```
{
    "project_id":
    "sprint_name":
    "sprint_remarks":
    "sprint_start_date":
    "sprint_end_date":
    "sprint_status":
    "objectives_velocity":
    "result_velocity":
    "create_by":
}
```
response
```
{
  "body" : "",
  "status": {
    "code" : "I0001",
    "message" : "",
    "detail" : ""
  }
}
```
