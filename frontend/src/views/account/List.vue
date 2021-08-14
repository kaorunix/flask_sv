
<template>
  <div class="about">
    <p>{{ message }}</p>
    <h3>アカウント一覧</h3>
    <v-simple-table>
      <template v-slot;default>
		<thead>
	  	<tr>
	    <th>アカウントID</th>
	    <th>アカウント名称</th>
	    <th>有効開始日</th>
	    <th>有効終了日</th>
	    <th>作成者</th>
	    <th>作成日時</th>
	    <th>更新者</th>
	    <th>更新日時</th>
	    <th>ステータス</th>
	  	</tr>
		</thead>
	<tbody>
	  <tr>
	    <td>アカウントID(id)</td>
	    <td>アカウント名称(account_name)</td>
	    <td>有効開始日</td>
	    <td>有効終了日</td>
	    <td>作成者</td>
	    <td>作成日時</td>
	    <td>更新者</td>
	    <td>更新日時</td>
	    <td>ステータス</td>
	  </tr>
	</tbody>
      </template>
    </v-simple-table>
  </div>
</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'SS',
  data () {
    return {
      message: '出力メッセージ'
    }
  }
}
</script>
