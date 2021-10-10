
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
          <tr v-for="account in accounts" v-bind:key="account">
            <td>{{ account.id }}</td>
            <td>{{ account.account_name }}</td>
            <td>{{ account.start_on }}</td>
            <td>{{ account.end_on }}</td>
            <td>{{ account.created_by }}</td>
            <td>{{ account.created_at}} </td>
            <td>{{ account.updated_by }}</td>
            <td>{{ account.updated_at }}</td>
            <td>{{ account.status }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>
<script>

var accounts = [
  {
    id: 123,
    account_name: 'macbeth',
    start_on: '2021/02/01 10:00:00',
    end_in: '2021/11/30 18:00:00',
    created_by: 10,
    created_at: '2021/08/25 12:00:00',
    updated_by: 10,
    updated_at: '2021/08/25 12:00:00',
    status: 0
  },
  {
    id: 124,
    account_name: 'duncan',
    start_on: '2021/05/01 10:00:00',
    end_in: '2021/10/30 18:00:00',
    created_by: 12,
    created_at: '2021/08/25 12:00:00',
    updated_by: 10,
    updated_at: '2021/08/25 12:00:00',
    status: 1
  }
]
var header = 'application/json'
var request = {
  operation_account_id: 100
}
var url = 'http://localhost:5000/api/account/search'
const config = {
  headers: {
    'Content-Type': header
  }
}

export default {
  name: 'List',
  data () {
    return {
      accounts: accounts
    }
  },
  mounted () {
    var self = this
    this.axios
      .post(url, request, config)
      .then(function (response) {
        console.log('List axios response %o', response.data.body)
        self.accounts = response.data.body
        self.message = response.data.status.message
      })
      .catch(err => {
        console.log('List axios error')
        console.log(err)
      })
  }
}

</script>
