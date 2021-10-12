<template>
  <div class="about">
    <p>{{ message }}</p>
    <h1>アカウント</h1>
    <v-form ref="form">
      <v-simple-table>
        <thead></thead>
        <tbody>
          <tr>
            <th>アカウント名称</th>
            <td>
              <v-text-field
                v-model="account_name"
                :counter="64"
                :rules="nameRules"
                :value="account_name"
                label="アカウント名称"
                required
              ></v-text-field>
            </td>
          </tr>
          <tr>
            <th>有効開始日</th>
            <td>
              <v-menu v-model="menu" max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="start_on"
                    :value="start_on"
                    label="有効開始日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="start_on"></v-date-picker>
              </v-menu>
            </td>
          </tr>
          <tr>
            <th>有効終了日</th>
            <td>
              <v-menu v-model="menu" max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="end_on"
                    :value="end_on"
                    label="有効終了日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="end_on"></v-date-picker>
              </v-menu>
            </td>
          </tr>
          <tr>
            <th>作成者</th>
            <td>
              <v-text-field
                v-model="created_by"
                :value="created_by"
                :counter="10"
                :rules="nameRules"
                label="作成者"
                required
              ></v-text-field>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
      <v-btn class="mr-4" @click="submit">保存</v-btn>
      <v-btn @click="reset">リセット</v-btn>
    </v-form>
  </div>
</template>
<script>
</script>
