<template>
  <v-app>
    <v-navigation-drawer
    v-model="drawer"
    app cliped
    >
      <v-container>
        <v-list-item>
      メニュー
        </v-list-item>
        <v-divider/>
        <v-list dense nav=false>

          <v-list-group v-for="main_menu_item in main_menu"
          :key="main_menu_item.name"
          :prepend-icon="main_menu_item.icon"
          no-action
          :append-icon="main_menu_item.lists ? undefined : ''">

            <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>
                {{ main_menu_item.name }}
              </v-list-item-title>
            </v-list-item-content>
            </template>

            <v-list-item v-for="sub_menu in main_menu_item.lists"
            :key="sub_menu.name"
            :to="sub_menu.link"
            >
              <v-list-item-content>
                <v-list-item-title>{{ sub_menu.name }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>

        </v-list>
      </v-container>
    </v-navigation-drawer>
    <v-app-bar color="#0182D1" app clipped>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>flask_sv_front</v-toolbar-title>
      <v-spacer/>
      <v-menu offset-y>
      <template v-slot:activator="{on}">
      <v-btn v-on="on" color="#9182D9">操作</v-btn>
      </template>
      <v-list>
        <v-subheader>ヘルプ</v-subheader>
        <v-list-item v-for="menu_item in company_menu"
        :key="menu_item.name"
        :to="menu_item.link">
          <v-list-item-content>
            <v-list-item-title>{{ menu_item.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-menu>
    </v-app-bar>
    <v-main app>
      <router-view />
    </v-main>
    <v-footer app>
      フッター
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: null,
      company_menu: [
        { name: '参照', link: '/' },
        { name: '編集', link: '/' },
        { name: '削除', link: '`mailto:s@a`' }
      ],
      main_menu: [
        {
          name: 'アカウント',
          icon: 'mdi-account',
          lists: [
            { name: '一覧', link: '/account' },
            { name: '作成', link: '/account/create' }
          ]
        },
        {
          name: 'プロジェクト',
          icon: 'mdi-clipboard-list',
          lists: [
            { name: '一覧', link: '/project' },
            { name: '作成', link: '/project/create' }
          ]
        },
        {
          name: 'スプリント',
          icon: 'mdi-alpha-s-box',
          lists: [
            { name: '一覧', link: '/splint' },
            { name: '作成', link: '/splint/create' }
          ]
        },
        {
          name: 'ストーリー',
          icon: 'mdi-directions-fork',
          lists: [
            { name: '一覧', link: '/story' },
            { name: '作成', link: '/story/create' }
          ]
        },
        {
          name: 'タスク',
          icon: 'mdi-clipboard-check-outline',
          lists: [
            { name: '一覧', link: '/task' },
            { name: '作成', link: '/task/create' }
          ]
        },
        {
          name: 'タスクのステータス',
          icon: 'mdi-scale-balance',
          lists: [
            { name: '一覧', link: '/task_status' },
            { name: '作成', link: '/task_status/create' }
          ]
        },
        {
          name: 'プロジェクトグループ',
          icon: 'mdi-clipboard-multiple',
          lists: [
            { name: '一覧', link: '/project_group' },
            { name: '作成', link: '/project_group/create' }
          ]
        },
        {
          name: '権限',
          icon: 'mdi-account-tie',
          lists: [
            { name: '一覧', link: '/authority' },
            { name: '作成', link: '/authority/create' }
          ]
        },
        {
          name: '業務',
          icon: 'mdi-city-variant-outline',
          lists: [
            { name: '一覧', link: '/category' },
            { name: '作成', link: '/category/create' }
          ]
        },
        {
          name: '画面',
          icon: 'mdi-desktop-mac',
          lists: [
            { name: '一覧', link: '/page' },
            { name: '作成', link: '/page/create' }
          ]
        },
        {
          name: 'プロジェクト2',
          icon: 'mdi-clipboard-list',
          lists: [
            { name: '一覧', link: '/project2' },
            { name: '作成', link: '/project2/create' }
          ]
        },
        {
          name: 'スプリント2',
          icon: 'mdi-alpha-s-box',
          lists: [
            { name: '一覧', link: '/splint2' },
            { name: '作成', link: '/splint2/create' }
          ]
        },
        {
          name: 'ストーリー2',
          icon: 'mdi-directions-fork',
          lists: [
            { name: '一覧', link: '/story2' },
            { name: '作成', link: '/story2/create' }
          ]
        },
        {
          name: 'タスク2',
          icon: 'mdi-clipboard-check-outline',
          lists: [
            { name: '一覧', link: '/task2' },
            { name: '作成', link: '/task2/create' }
          ]
        },
        {
          name: 'タスクのステータス2',
          icon: 'mdi-scale-balance',
          lists: [
            { name: '一覧', link: '/task_status2' },
            { name: '作成', link: '/task_status2/create' }
          ]
        },
        {
          name: 'プロジェクトグループ2',
          icon: 'mdi-clipboard-multiple',
          lists: [
            { name: '一覧', link: '/project_group2' },
            { name: '作成', link: '/project_group2/create' }
          ]
        },
        {
          name: '権限2',
          icon: 'mdi-account-tie',
          lists: [
            { name: '一覧', link: '/authority2' },
            { name: '作成', link: '/authority2/create' }
          ]
        },
        {
          name: '業務2',
          icon: 'mdi-city-variant-outline',
          lists: [
            { name: '一覧', link: '/category2' },
            { name: '作成', link: '/category2/create' }
          ]
        },
        {
          name: '画面2',
          icon: 'mdi-desktop-mac',
          lists: [
            { name: '一覧', link: '/page2' },
            { name: '作成', link: '/page2/create' }
          ]
        }

      ]
    }
  }
}
</script>
