
<template>
  <div class="about">
   <p>{{ message }}</p>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>S.S.</h1>
    <h2>経歴</h2>
    <p>過去の案件</p>
    <p>現在の案件</p>
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
