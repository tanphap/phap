# PHAP
### *Programing Helpful Algorithm Package*
#### *一个对编程有帮助的算法包*
### 本项目由Python3.11环境下编写，资源在该环境下编译
[![Apache License 2.0](https://img.shields.io/badge/license-Apache2.0-green.svg?style=flat)](https://choosealicense.com/licenses/apache-2.0/)
### [English](README.md)  | 简体中文

# 项目链接
[Github](https://github.com/DashStudio/phap/ "Github") | [Pypi](https://pypi.org/project/phap/ "Pypi") | [Pypi (stralgo)](https://pypi.org/project/stralgo/ "Pypi (stralgo)")
<br><br>
[Kgithub](https://kgithub.com/DashStudio/phap/)：国内Github镜像站，可能会有延迟，推送请使用Github链接推送

# 版本
## 稳定版本
+ v0.1.0 (stralgo)
+ v1.1.1 (stralgo)
+ v2.1.2
+ v2.2.1

## 最新正式版本
+ v3.1.0

## 最新版本
+ v4.0.0-alpha1

# 使用
## 阅读开发文档
### *(尽量打开项目链接中的[Github](https://github.com/DashStudio/phap "Github")链接打开，使用Pypi或其他链接可能会发生打不开的情况)*
+ [开发文档链接](doc/README_zh-CN.md)

# 从源码构建
## 准备工作
+ 安装git和make (方法自行百度)
+ 安装Python(3.9版本或者3.11版本皆可)
+ 从源码仓库克隆源代码
```
git clone git@github.com:DashStudio/phap.git
```
#### 或者
```
git clone https://github.com/DashStudio/phap.git
```
### 国内网比较差可以尝试：
```
git clone https://kgithub.com/DashStudio/phap.git
```

## 初始化打包环境
```
make init
```
#### 或者
#### 尝试手动安装以下包:
+ build
+ twine
#### 以下是在Windows环境下的示例命令行:
```
python -m pip install build
python -m pip install twine
```

## 构建包
```
make build
```

# 关于版权
## 版本历史
本项目最初名为Stralgo，后期更名为PHAP。
因为一些原因，本项目的老旧版本仍名为Stralgo。
即使这样，版权仍然归属在PHAP项目下。

## 目前情况
因为一些原因，本项目决定更改许可证，从原本的MIT许可证，迁移至Apache许可证。
这为我们的版权问题添加了不少麻烦。

为了减少问题冲突，决定简单粗暴地将v0.\*、v1.\*、v2.\*归属于MIT许可证，
v3.\*以及更高版本归属于Apache许可证。

对于迁移至Apache许可证下的新代码中存在的归属于MIT许可证的老版本代码，
仍归属于MIT许可证管辖范围。

对于本项目商业化后的命名和版权声明问题，v0.\*、v1.\*按照MIT许可证处理，
v2.\*、v3.\*以及更高版本中按照Apache许可证处理，不考虑代码内容。

本解释无法对版权进行规定，实际情况以[许可证文件](LICENSE)为准。
