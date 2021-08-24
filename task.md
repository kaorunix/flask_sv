# タスク

## データベース設計

|Field|Type|Null|Key|Default|Extra|
|:--|:--|:--|:--|:--|:--|
|task_id（タスクID）|int|NO|PRI|NULL||
|heading（タスク見出し）|text|NO||NULL|| 
|contents（タスク内容）|text|NO||NULL||
|deadline（期日）|datetime|NO||NULL||
|man_hours（工数）|int|NO||NULL||
|start_on（開始日）|datetime|YES||NULL||
|end_on（終了日）|datetime|YES||NULL||
|status（進行状況）|int|YES||NULL|0=未着手 1=進行中 2=完了|
|account_id（担当者）|varchar(64)|NO||NULL||
|project_id（プロジェクト）|int|NO||NULL||
|sprint_id（スプリント）|int|NO||NULL||
|story_id（ストーリー）|int|NO||NULL||

```
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task` (
  `task_id` int NOT NULL,
  `heading` text NOT NULL ,
  `contents` text NOT NULL ,
  `deadline` datetime NOT NULL,
  `man_hours` int NOT NULL,
  `start_on` datetime DEFAULT NULL,
  `end_on` datetime DEFAULT NULL,
  `status` int DEFAULT NULL,
  `account_id` varchar(64) NOT NULL,
  `progect_id` int NOT NULL,
  `sprint_id` int NOT NULL,
  `story_id` int NOT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## API設計

### taskからの検索

#### URL

**/task/get/**

#### HTTP METHOD

GET

#### request

GETのためなし

#### response

```request
{
  "body": {
     "task_id": <task_id>,
     "heading": <heading>,
     "contents": <contents>,
     "deadline": <deadline>,
     "account_id": <account_id>,
     "man_hours": <man_hours>,
     "start_on": <start_on>,
     "status": <status>,
     "account_id": <account_id>,
  }
}
```




## task作成

#### URL

/task/create

#### HTTP METHOD

POST

#### request


```
{   
    "task_id":
    "heading":
    "contents":
    "deadline":
    "start_on"
    "account_id":
}
```

#### response

```
{
  "body" : "",
  "status": {
    "code" : "I0001",
    "message" : "account {} was created.",
    "detail" : ""
  }
}

```
