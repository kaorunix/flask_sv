
<template>
    <!-- <v-app id="inspire">
    <div class="text-center"> -->
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
        @click="getAccount(); dialog = true; "
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
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
var header = 'application/json'

var urllock = 'http://localhost:5000/api/account/lock'
var urlupdate = 'http://localhost:5000/api/account/update_for_lock'
const configget = {
	 headers: {
	 	'Content-Type': 'application/json',
	 },
}
const configupdate = {
	 headers: {
	 	'Content-Type': 'application/json',
	 },
}
  var account_name = '';
  var start_on = '';
  var end_on = '';
  var operation_account_id = 0;
  var account_id = 1448;
export default {
  name: 'Update',
  props: {
    accountId: {
       type: Number,
       required: true
     }
  },
  data () {
    return {
      dialog: false,
      account: {
        id: '',
        account_name: '',
        start_on: '',
        end_on: ''
      },
      operation_account_id: 50
    }
  },
  mounted () {
  	// this.axios
	  // .get(url + account_id.toString(10), config)
		// .then(function(response) {
    //     console.log("Update axios response");
    //     console.log(response);
    //     console.log(response.headers);
    //     self.account=response.json.body;
    //     console.log(self.account);
    //     self.meesage=response.status.message; 
    //     console.log(self.accounts);
    //     account = response.json;
    //   })
		// .catch(err => {
		// 	console.log("Update axios error")
		// 	console.log(err)
		// })
  },
  created: function () {
    //getAccount()
  },
  computed: {
    form () {
      return {
        id: this.account.id,
        account_name: this.account.account_name,
        start_on: this.account.start_on.concat(" 00:00:00"),
        end_on: this.account.end_on.concat(" 00:00:00"),
        operation_account_id: parseInt(this.operation_account_id)
      }
    },
    req () {
      return {
        id: this.account.id,
        operation_account_id: parseInt(this.operation_account_id)
      }
    }
  },
  watch: {
    name () {
      this.errorMessages = ''
    },
  },
  methods: {
    getAccount () {
      var request = {
        id: this.accountId,
        operation_account_id: parseInt(this.operation_account_id)
      }
      console.log("getAccount was called");
      this.axios
      .post(urllock, request, configget)
      .then(function(response) {
          console.log("Get axios response");
          console.log(response);
          console.log(response.headers);
          self.account=response.data.body;
          //this.$set(this.account,"account_name", response.data.body.account_name)
          console.log("self.account");
          console.log(self.account);
          self.account.account_name = "ABC";
          self.meesage=response.status.message; 
          //account = response.json.get("body");
        })
      .catch(err => {
        console.log("Get axios error")
        console.log(err)
      })
    },
    validate () {
      this.$refs.form.validate()
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
    submit () {
      // this.$v.$touch()

      var self = this;
      console.log(this.form)
      this.axios
        .post(urlupdate, this.form, configupdate)
        .then(function (response) {
        console.log('Update axios response')
        console.log(response)
        document.location = "http://localhost:8080/account";
      })
       .catch(err => {
	console.log('Update axios error')
        console.log(err)
      })
    },
  }
}
</script>
