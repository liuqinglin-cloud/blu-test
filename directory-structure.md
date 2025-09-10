# Project Directory Structure



```
python版本：pyhton3.9


blu-test/
├── api_test---------------------------------接口测试
│   ├── api_request.py-----------------------封装接口请求方法，测试时直接使用
│   ├── assert_methods.py--------------------断言方法，当前支持返回结果任意字段断言、数据库数据断言
│   ├── case.xlsx----------------------------用例&测试结果，设计是以sheet区分不同场景或者不同服务
│   ├── precondition_methods.py--------------前置条件处理，包含依赖前面的接口返回数据、数据库查询、数据库写入
│   ├── run.py-------------------------------执行用例，现阶段用不着
│   └── test_case.py-------------------------用例方法，测试时更改获取的接口数据来测试指定内容
├── common_android---------------------------安卓的公共方法
│   ├── log----------------------------------日志，airtest会使用此日志生成测试报告
│   ├── app_operation.py---------------------App通用操作，比如登录、返回主页、切换语言
│   ├── assert_methods.py--------------------断言方法
│   ├── basic_operations.py------------------基本操作，比如定位、点击、滑动、输入文本
│   ├── system_operation.py------------------系统操作，比如切换WiFi，给App授权
├── common_ios-------------------------------Apple设备公共方法
│   ├── log----------------------------------日志，airtest会使用此日志生成测试报告
│   ├── app_operation.py---------------------App通用操作，比如返回主页、切换语言
│   ├── assert_methods.py--------------------断言方法
│   ├── basic_operations.py------------------基本操作，比如定位、点击、滑动、输入文本
│   ├── system_operation.py------------------系统操作，比如切换WiFi，给App授权
├── config-----------------------------------配置，全是测试用到的相对固定的数据
│   ├── device.ini---------------------------设备，测试设备时使用
│   ├── environment.ini----------------------环境信息，测试接口、操作mysql、操作redis使用
│   ├── header.json--------------------------header，测试接口使用
│   ├── local_element_android.ini------------Android元素信息，测试翻译、UI功能使用
│   ├── local_element_ios.ini----------------iOS元素信息，测试翻译、UI功能使用
│   ├── test_user.ini------------------------测试账号信息
│   ├── translation.ini----------------------翻译文案，测试翻译使用
├── report-----------------------------------报告
│   ├── airtest_report-----------------------airtest报告，有截图，方便测试翻译时检查UI效果，每次会覆盖上一次的报告
│   │   ├── translation_android--------------Android翻译测试报告
│   │   ├── translation_h5-------------------H5翻译测试报告
│   │   ├── ui_android-----------------------Android UI测试报告
│   │   ├── translation_ios------------------iOS翻译测试报告
│   │   └── ui_ios---------------------------iOS UI测试报告
│   └── unittest_report----------------------unittest报告，无截图，可以添加截图，按时间命名，不会覆盖
│       ├── translation_android--------------Android翻译测试报告
│       ├── ui_android-----------------------Android UI测试报告
│       ├── translation_ios------------------iOS翻译测试报告
│       └── ui_ios---------------------------iOS UI测试报告
├── translation_android----------------------Android翻译测试，仅用于pixel6测试翻译，暂时不维护，新增功能时维护
│   ├── run.py-------------------------------执行用例
│   ├── translation_english.py---------------英语翻译测试
│   ├── translation_french.py----------------法语翻译测试
│   ├── translation_german.py----------------德语翻译测试
│   ├── translation_italian.py---------------意大利语翻译测试
│   ├── translation_japanese.py--------------日语翻译测试
│   ├── translation_korean.py----------------韩语翻译测试
│   ├── translation_portuguese.py------------葡萄牙语翻译测试
│   ├── translation_simplified_chinese.py----简体中文翻译测试，维护了一部分，用于了解具体测试时的坑
│   ├── translation_spanish.py---------------西班牙语翻译测试
│   ├── translation_traditional_chinese.py---繁体中文翻译测试
│   └── translation_ukrainian.py-------------乌克兰语翻译测试
├── translation_ios--------------------------iOS翻译测试，仅用于ipad pro12.9测试翻译，暂时不维护，新增功能时维护
│   ├── run.py-------------------------------执行用例
│   ├── translation_english.py---------------英语翻译测试
│   ├── translation_french.py----------------法语翻译测试
│   ├── translation_german.py----------------德语翻译测试
│   ├── translation_italian.py---------------意大利语翻译测试
│   ├── translation_japanese.py--------------日语翻译测试
│   ├── translation_korean.py----------------韩语翻译测试
│   ├── translation_portuguese.py------------葡萄牙语翻译测试
│   ├── translation_simplified_chinese.py----简体中文翻译测试
│   ├── translation_spanish.py---------------西班牙语翻译测试
│   ├── translation_traditional_chinese.py---繁体中文翻译测试
│   └── translation_ukrainian.py-------------乌克兰语翻译测试
├── ui_android-------------------------------Android UI功能测试，此处计划以4个一级页面区分用例，也可以按照功能、场景来区分
│   ├── run.py-------------------------------执行用例
│   ├── test_comunity.py---------------------“社区”页面所有功能测试用例，用于pixel6，测试可能出现的异常，覆盖较全
│   ├── test_me.py---------------------------“我的”页面所有功能测试用例，用于pixel6，测试可能出现的异常，覆盖较全
│   ├── test_home.py-------------------------“首页”页面所有功能测试用例，用于pixel6，测试可能出现的异常，覆盖较全
│   ├── test_service.py----------------------“服务”页面所有功能测试用例，用于pixel6，测试可能出现的异常，覆盖较全
│   └── universal_test_for_all_device.py-----专用于测试所有机型的基本页面(UI兼容性)，要兼容所有机型，限于定位原因，覆盖不全
├── ui_ios-----------------------------------iOS UI功能测试，待维护，此处计划以4个一级页面区分用例，也可以按照功能、场景来区分
│   ├── run.py-------------------------------执行用例
│   ├── test_comunity.py---------------------“社区”页面所有功能测试用例
│   ├── test_me.py---------------------------“我的”页面所有功能测试用例
│   ├── test_home.py-------------------------“首页”页面所有功能测试用例
│   └── test_service.py----------------------“服务”页面所有功能测试用例
└── utils------------------------------------实用方法
    ├── adb_command.py-----------------------执行ADB命令，如抓取日志
    ├── handle_api_res_data.py---------------主要是获取指定的接口返回数据，用于获取依赖数据、断言、处理header
    ├── handle_cookie.py---------------------cookie处理，如果做web自动化，也会用到，故放于此
    ├── handle_excel.py----------------------读写excel
    ├── handle_header.py---------------------cookie处理，如果做web自动化，可能也会用到，故放于此
    ├── handle_ini.py------------------------ini文件处理
    ├── handle_json.py-----------------------json文件处理
    ├── handle_mysql.py----------------------mysql操作
    └── handle_redis.py----------------------redis操作
```