<template>
    <v-dialog
      v-model="dialog"
      width="800"
    >
      <template v-slot:activator="{ on }">
      <v-btn
        fab
        x-small
        class="mx-2"
        slot="activator"
        color="cyan"
        dark
        @click="dialog = true; "
      >
        <v-icon dark>
          mdi-pencil
        </v-icon>
      </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          アカウント更新
        </v-card-title>

        <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field label="アカウントid" disabled required v-model="account.id"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field label="アカウント名称" required v-model="account.account_name"></v-text-field>
            </v-flex>
            <v-flex xs12>
            <v-menu max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="account.start_on"
                    :value="account.start_on"
                    label="有効開始日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="account.start_on"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs12>
            <v-menu max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="account.end_on"
                    :value="account.end_on"
                    label="有効終了日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="account.end_on"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs12>
              <v-text-field label="作成者" required v-model="operation_account_id"></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="submit();dialog = false"
          >
            更新
          </v-btn>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            キャンセル
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  <!-- </div>
  </v-app> -->
</template>
<script>
export default {
  name: 'Update',
  data () {
    return {
      dialog: false,
      account: {
        id: 1234,
        account_name: '',
        start_on: '',
        end_on: ''
      },
      operation_account_id: 4321
    }
  }
}
</script>
