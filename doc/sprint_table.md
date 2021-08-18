#スプリントテーブル設計

---

<br>

|項目名|Field|Type|Null|Key|Default|Option|Description|
|:--|:--|:--|:--|:--|:--|:--|:--|
|ID|id|int|NO|PRI||auto_increment||
|プロジェクトID|project_id|int|NO|||||
|スプリント名|sprint_name|varchar(64)|NO|||||
|スプリント特記事項|sprint_remarks|varchar(64)|||NULL|||
|スプリントステータス|sprint_status|int|NO||||0:未着手,1:着手中,2:完了|
|スプリント開始日|sprint_start_date|date|NO|||||
|スプリント終了日|sprint_end_date|date|NO|||||
|目標ベロシティ|objectives_velocity|int|NO||0|||
|実績ベロシティ|result_velocity|int|NO||0|||
|作成者|create_by|int|NO|||||
|作成日時|create_at|datetime|NO|||||
|更新者|update_by|int|||NULL|||
|更新日時|update_at|datetime|||NULL|||

<br>


#スプリントテーブルDDL

---

<br>

```
DROP TABLE IF EXISTS `sprint`;
CREATE TABLE `sprint` (
`id` int NOT NULL AUTO_INCREMENT,
`project_id` int NOT NULL,
`sprint_name` varchar(64) NOT NULL,
`sprint_remarks` varchar(64) DEFAULT NULL,
`sprint_status` int NOT NULL,
`sprint_start_date` date NOT NULL,
`sprint_end_date` date NOT NULL,
`objectives_velocity` int DEFAULT 0,
`result_velocity` int DEFAULT 0,
`create_by` int NOT NULL,
`create_at` datetime NOT NULL,
`update_by` int DEFAULT NULL,
`update_at` datetime DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
