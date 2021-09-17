# タスクステータス2テーブル テーブル定義

| 項目    | Field            | Type         | Null | Key | Default | Option         | Description |
|---------|------------------|--------------|------|-----|---------|----------------|-------------|
| ID      | id               | int          | YES  | PRI |         | AUTO_INCREMENT |             |
| ステータス名 | status_name      | varchar(64)  | YES  |     |         |                |             |
| 背景色  | background_color | varchar(512) | NO   |     | NULL    |                |             |
| 作成者  | created_by       | int          | NO   |     |         |                |             |
| 作成日  | created_at       | datetime     | NO   |     |         |                |             |
| 更新者  | updated_by       | int          | NO   |     |         |                |             |
| 更新日  | updated_at       | datetime     | NO   |     |         |                |             |
