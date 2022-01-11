sudo apt update -y
sudo curl -sL https://deb.nodesource.com/setup_15.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo node -v && npm -v
v16.13.1
8.1.2

sudo npm install -g @vue/cli
vue create hello-world



nginx
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name walters.topyl666.com;

	#location / {
    #    include proxy_params;
    #    proxy_pass http://localhost:8080;
	#}
    location / {
        include proxy_params;
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

respond
Invalid Host header 


add vue.config.js in root doc
module.exports = {
  devServer: {
    disableHostCheck: true
  }
}


assets: 放需要 webpack 編譯的靜態資源
static: 不需要編譯的靜態資源
pages: 各頁對應的頁面元件 (相當於你寫 SPA 時，VueRouter路由指定的元件)
components: 跨頁面的元件，不具狀態
nuxt.config.js: Nuxt 全域設定檔
nuxt: Nuxt 暫存資料夾
middleware 能指定這頁採用哪種權限驗證
validate 能指定這頁得具備哪些資訊才看得到
asyncData 和 fetch 能設置頁面狀態(data & store)，收納 API 呼叫邏輯
