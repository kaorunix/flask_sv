
<template>
    <!-- <v-app id="inspire">
    <div class="text-center"> -->
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
      <v-btn
        fab
        x-small
        class="mx-2"
        slot="activator"
        color="red lighten-2"
        dark
        @click="dialog = true"
      >

        <v-icon dark>
          mdi-delete
        </v-icon>
      </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          削除ダイアログ
        </v-card-title>

        <v-card-text>
          ここに確認ボタンを表示する予定
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="dialog = false"
          >
            キャンセル
          </v-btn>
          <v-btn
            color="primary"
            flat
            @click="dialog = false"
          >
            削除
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

export default {
  name: 'Delete',
  data () {
    return {
      dialog: false
    }
  }
}
</script>
