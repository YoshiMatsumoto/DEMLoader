# DEMLoader
## こちらは国土地理院の5m標高メッシュの点群化プラグインです。  

20190131追記
ポイントを出力する際にx座標が反転してしまうバグを修正しました。

### 1. 国土地理院からDEMをダウンロードしてください。
[国土地理院5mメッシュ](https://fgd.gsi.go.jp/download/menu.php)  

こちらから数値標高モデル/該当範囲のDEMデータをダウンロードし適当なところへ解凍してください。  

ここから該当する番号のxmlファイルを選択してください。
https://maps.gsi.go.jp/#14/34.620989/136.441441/&base=std&ls=std%7Cchiikimesh%7Cfgd_dem5a_area_dtil&disp=111&lcd=fgd_dem5a_area_dtil&vs=c1j0h0k0l0u0t0z0r0s0m0f0&d=m

### 2. DEMLoader.pyの読み込み

clone or downloadタブからzip形式でダウンロードし、適当なところへ解凍してください。

### 3. DEMLoaderを走らせる  

- Rhinocerosを起動し、コマンドラインへ"RunPythonScript"を書いてください。  
- Explorer/Finderが表示され先程のDEMLoader.pyを選択してください。
- 1で解凍した.xmlファイルを選択てください。  

- おわり
