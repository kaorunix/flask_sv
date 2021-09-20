
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
        color="cyan"
        dark
        @click="dialog = true"
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
          更新モーダル
        </v-card-title>

        <v-card-text>
          ここにフォームを埋める予定
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="dialog = false"
          >
            I accept
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
  name: 'Create',
  data () {
    return {
      dialog: false
    }
  }
}
</script>
