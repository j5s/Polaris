<h1 align="center">Polaris</h1>
<h1 align="center">

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-GPLv3-fe5f55.svg)](https://raw.githubusercontent.com/doimet/Fish/master/docs/LICENSE)
[![Author](https://img.shields.io/badge/author-浮鱼-28b78d)](https://github.com/doimet)
</h1>

# 项目简介
这是一款集信息收集、漏洞利用、漏洞爆破等功能的一体化渗透测试框架

# 使用帮助

+ 修改配置文件
    ```
    conf/setting.toml
    ```
    配置文件里配置了程序运行的必要参数以及插件的参数, 按需修改即可
+ 安装支持类库
    ```shell script
    pip3 install -r requirements.txt -i https://pypi.douban.com/simple/
    ```
+ 查看帮助信息
    ```shell script
    python Cli.py --help
    ```
    ![avatar](docs/images/screenshort_01.png)
    ```shell script
    python Cli.py {命令} --help
    ```
    ![avatar](docs/images/screenshort_02.png)
    可选命令: `collect`、`exploit`、`login`、`auxiliary`
+ 查看插件信息
    ```shell script
    python Cli.py {命令} --list
    ```
    ![avatar](docs/images/screenshort_03.png)
    ```shell script
    python Cli.py {命令} --plugin '{插件}' --list
    ```
    ![avatar](docs/images/screenshort_04.png)
    ```shell script
    python Cli.py {命令} --plugin '@{类型}' --list
    ```
    ![avatar](docs/images/screenshort_05.png)
    ```shell script
    python Cli.py {命令} --plugin '!{插件}' --list
    ```
    ![avatar](docs/images/screenshort_06.png)
    可选类型: `ip`、`domain`、`subdomain`、`url`、`company`、`email`、`md5`等
+ 运行命令格式
    ```shell script
    python Cli.py --input {类型}:{目标/文件} {调用命令} {调用参数}
    ```
    ![avatar](docs/images/screenshort_07.png)
    可选输出文件类型: `json`
## 使用示例

### 收集信息

+ 收集子域名
    ```shell script
    python Cli.py --input domain:360.com collect
    python Cli.py --input domain:360.com collect --plugin china
    python Cli.py --input domain:360.com collect --plugin china --pugin ip138
    python Cli.py --input domain:360.com collect --plugin !ksubdomain
    ```
+ 收集ip信息
    ```shell script
    python Cli.py --input ip:x.x.x.x collect
    ```
+ 收集邮箱
    ```shell script
    python Cli.py --input email:xxx@gmail.com collect
    ```

### 漏洞利用
```shell script
python Cli.py --input url:http://example.com exploit
python Cli.py --input url:http://example.com exploit --plugin CVE-2021-22205
python Cli.py --input url:http://example.com exploit --plugin CVE-2021-22205 --shell
```
### 口令爆破

```shell script
python Cli.py --input ip:x.x.x.x login
python Cli.py --input ip:x.x.x.x login --plugin ssh
python Cli.py --input ip:x.x.x.x login --plugin ssh --username root --password root --method 1
python Cli.py --input ip:x.x.x.x login --plugin ssh --username username.txt --password password.txt --method 2
```
`method`可选参数:   
1. 单点模式: 一个账号对应一个密码   
2. 交叉模式: 多个账号对应多个密码

### 渗透辅助
+ MD5解密
```shell script
python Cli.py --input md5:1a79a4d60de6718e8e5b326e338ae533 auxiliary --plugin md5
```

### 命令联动
```shell script
python Cli.py --input domain:example.com collect --plugin ip138 exploit --plugin CVE-2021-xxx 
```

## 插件开发
[插件开发手册](docs/DEVELOPMENT.md)

## 版本日志
[版本修改日志](docs/CHANGELOG.md)

## 使用声明
本工具仅用于安全测试目的   
用于非法用途与开发者无关   
