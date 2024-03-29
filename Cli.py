﻿# -*-* coding:UTF-8
import gc
import os
import re
import sys
import time
import toml
import click
import inspect
import warnings
from IPy import IP
from core.app import Application

warnings.filterwarnings("ignore")


def cost_time(func):
    """ 计算使用时间 """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        all_time = round(stop_time - start_time, 2)
        print(f'\r\033[0;34m[⇣]\033[0m Finished use time {all_time}s{50 * " "}')
        sys.exit()

    return wrapper


def show_banner(func):
    """ 打印banner """

    def wrapper(options, processors):
        os.system('')
        print(f"""
    \033[0;31mPolaris - 渗透测试框架 1.0.1\033[0m

 =# Author: 浮鱼
 =# Github: https://github.com/doimet/Polaris
 
 Output File: {options['output']}
                """)
        return func(options, processors)

    return wrapper


def check_environment():
    """ 检测解释器版本 """

    version = sys.version.split()[0]
    if version < '3.6':
        raise Exception('Require python 3.6 or higher')
    """ 检测字符编码 """
    if sys.getdefaultencoding() != 'utf-8':
        raise Exception('Character encoding must be UTF-8')


def merge_options(kwargs):
    keyword = inspect.stack()[1][3]
    return dict(**{'command': keyword, **kwargs})


def parse_input_param(ctx, param, value):
    """ 解析输入参数 """
    if not value:
        return
    match = re.match(rf"^([a-zA-Z]+)[=|: ]([\w\S]+)$", value)
    if match:
        task_list, key, value = [], match.group(1), match.group(2)
        if os.path.isfile(value):
            with open(value, encoding='utf-8') as f:
                value_list = filter(lambda x: x != '', list(set(map(lambda x: x.strip(), f.readlines()))))
        else:
            value_list = [value]
        for value in value_list:
            # match = re.match(rf"^([a-zA-Z]+)[=|: ]([\w\S:]+)$", value)
            # if match:
            #     print(match.group(1), match.group(2))
            #     key, value = match.group(1), match.group(2)
            if key == 'ip':
                ip_list = IP(value, make_net=True)
                for ip in ip_list:
                    task_list.append(('ip', str(ip)))
            else:
                task_list.append((key, value))
        return task_list
    else:
        click.echo('\033[0;31m[-]\033[0m Incorrect input syntax. PS: domain:example.com\n')
        ctx.exit()


def parse_output_param(ctx, param, value):
    """ 解析输出参数 """
    filename = time.strftime("%Y-%m-%d-%H-%M-%S-report.json", time.localtime())
    if not value:
        return os.path.join('output', filename)
    elif os.path.isdir(value):
        return os.path.join(value, filename)
    else:
        return value


def parse_verbose_param(ctx, param, value):
    """ 解析详细参数 """

    if not value:
        return 20
    else:
        return (7 - (value if value <= 6 else 6)) * 10


@click.group(chain=True, invoke_without_command=True)
@click.option('--input', '-i', help='设置目标.', callback=parse_input_param)
@click.option('--output', '-o', help='输出结果到指定路径.', callback=parse_output_param)
@click.option('--verbose', '-V', help='设置程序日志的等级.', callback=parse_verbose_param, count=True)
@click.help_option('--help', '-H', help='显示帮助信息并退出.')
def cli(**kwargs):
    """ Easy to use red team attack tool """


@cli.resultcallback()
def process_pipeline(processors, **kwargs):
    main(kwargs, processors)


@cost_time
@show_banner
def main(options, processors):
    check_environment()

    config = toml.load(os.path.join('conf', 'setting.toml'))
    app = Application(config=config, options=options)
    for processor in processors:
        gc.collect()
        app.options.update(processor)
        if processor['list']:
            app.shows()
        else:
            app.setup()
    app.save()


@cli.command(name='collect')
@click.option('--plugin', '-p', help='指定信息搜集的插件.', multiple=True)
@click.option('--list', '-L', help='列出插件的详细信息.', is_flag=True)
@click.help_option('--help', '-H', help='显示帮助信息并退出.')
def collect(**kwargs):
    """ 网络信息收集模块 """
    return merge_options(kwargs)


@cli.command(name='exploit')
@click.option('--plugin', '-p', help='指定漏洞利用的插件.', multiple=True)
@click.option('--attack', '-A', help='指定漏洞利用的模式.', is_flag=True)
@click.option('--shell', '-S', help='开启插件的终端模式.', is_flag=True)
@click.option('--list', '-L', help='列出插件的详细信息.', is_flag=True)
@click.help_option('--help', '-H', help='显示帮助信息并退出.')
def exploit(**kwargs):
    """ 漏洞验证利用模块 """
    return merge_options(kwargs)


@cli.command(name='login')
@click.option('--plugin', '-p', help='指定漏洞利用的插件.', multiple=True)
@click.option('--method', '-m', help='指定口令爆破的模式.', type=click.Choice(['0', '1', '2']), default='1')
@click.option('--username', '-un', help='登录账户序列或文件.')
@click.option('--password', '-pw', help='登录密码序列或文件.')
@click.option('--timeout', '-t', help='指定服务超时的时间.', default=5)
@click.option('--list', '-L', help='列出插件的详细信息.', is_flag=True)
@click.help_option('--help', '-H', help='显示帮助信息并退出.')
def login(**kwargs):
    """ 服务登录爆破模块 """
    return merge_options(kwargs)


@cli.command(name='auxiliary')
@click.option('--plugin', '-p', help='指定漏洞利用的插件.', multiple=True)
@click.option('--list', '-L', help='列出插件的详细信息.', is_flag=True)
@click.help_option('--help', '-H', help='显示帮助信息并退出.')
def auxiliary(**kwargs):
    """ 渗透测试辅助模块 """
    return merge_options(kwargs)


if __name__ == '__main__':
    cli()
