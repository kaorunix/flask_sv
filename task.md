# タスク

## データベース設計

|Field|Type|Null|Key|Default|Extra|
|:--|:--|:--|:--|:--|:--|
|heading（タスク見出し）|text|NO|PRI|NULL|| 
|contents（タスク内容）|text|NO||NULL||
|deadline（期日）|datetime|NO||NULL||
|man_hours（工数）|int|NO||NULL||
|start_on（開始日）|datetime|YES||NULL||
|end_on（終了日）|datetime|YES||NULL||
|account_name（担当者）|varchar(64)|NO||NULL||
|status（進行状況）|datetime|YES||NULL||
|deliverable（成果物）|text|NO||NULL||

```
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task` (
  `heading` text NOT NULL ,
  `contents` text NOT NULL ,
  `deadline` datetime NOT NULL,
  `man_hours` int NOT NULL,
  `start_on` datetime DEFAULT NULL,
  `end_on` datetime DEFAULT NULL,
  `account_name` varchar(64) NOT NULL,
  `status` datetime DEFAULT NULL,
  `deliverable` text NOT NULL,
  PRIMARY KEY (`heading`)
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
     "heading": <heading>,
     "contents": <contents>,
     "deadline": <deadline>,
     "account_name": <account_name>
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
    "heading":
    "contents":
    "deadline":
    "account_name":
}
```

#### response

```
{
  "message": "Completed successfully"
}
```