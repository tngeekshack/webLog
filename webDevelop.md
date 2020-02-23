> Django
### django開発手順

1. djangoプロジェクトの作成
~~~
django-admin startproject config .
~~~
2. setting.pyの変更
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'

3. staticurlを追加
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

4. アプリケーションの作成
~~~
python manage.py startapp 名前
~~~

~~~
### アプリケーションを作成したらsettingpyのISNSTALL_APPに記載する
~~~
weblog.apps
~~~
### モデルを作成したら打つコマンド
~~~
python manage.py makemigrations
~~~

### 【Django】サーバー起動 ※ターミナルから起動しないと仮想環境が入った状態でできない
~~~
python manage.py runserver
~~~



> Vue.js
cssフレームワークを利用する際は最初の時点で挿入することができる
### 【Vue.js】サーバー立ち上げコマンド
~~~
npm run serve
~~~

### Routerのダウンロード
~~~
npm install vue-router
~~~
外部ファイルの読み込み
~~~
<style>
/* ファイルパスに従って@importntの後にファイルパスを書き込む */
@import "./css/styles.css";

</style>
~~~
Appという部品をHTMLにおけるid="app"となっている要素に表示する
参考<br>
https://note.com/tis_engineer/n/ne6ff2e82196b
~~~
new Vue({
  render: h => h(App),
}).$mount('#app')
~~~
<style lang="less" scoped></style>
※scopedを使用することで他のファイルへの影響をなくすことができる。