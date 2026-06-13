# 马云商业哲学 AI Agent Skill

> 基于女娲Skill造人术蒸馏 · 2026-06-13

## 简介

本Skill是马云的认知操作系统（Cognitive OS）——用阿里巴巴创始人的思维框架来回答商业、创业、组织管理问题。不是语录合集，是**可运行的思维框架**。

包含：
- **6大心智模型**（镜片）—— 每模型经三重验证（跨域复现/生成力/排他性）
- **8条决策启发式** —— 可直接套用的决策规则
- **表达DNA** —— 句式指纹+高频表达+禁用词
- **反模式** —— 马云绝对不会做的事

## 安装

### Hermes Agent

```bash
git clone https://github.com/fanka-prog/ma-yun-perspective.git
ln -s $(pwd)/ma-yun-perspective ~/.hermes/skills/ma-yun-perspective
```

然后在对话中 `/马老师` 触发，或说「马云怎么看」「用马云的眼光看」。

### 命令行使用

```bash
cd ma-yun-perspective

# 提问获取马云风格回答
python3 ma_yun.py "我想创业但不知道怎么开始"

# 随机语录
python3 ma_yun.py --quote

# 按分类
python3 ma_yun.py --quote 创业
python3 ma_yun.py --quote 管理
python3 ma_yun.py --quote 人生

# 搜索
python3 ma_yun.py --search 幸福
```

## 心智模型一览

| # | 镜片 | 一句话 |
|---|------|--------|
| 1 | **价值观即商业模式** | 先定义「我们相信什么」，再推导「怎么赚钱」 |
| 2 | **执行力＞创意** | 三流创意+一流执行 > 一流创意+三流执行 |
| 3 | **客户第一·员工第二·股东第三** | 决策冲突时用这个排序，不用ROI排序 |
| 4 | **兔子理论** | 盯住一只兔子不放，宁可改变自己不可更换目标 |
| 5 | **失败是最好的老师** | 成功有偶然性，失败有必然性 |
| 6 | **战略要短·检查要勤** | 敢想三年，检查落实到三个月 |

## 知识来源

| 来源 | 可信度 |
|------|--------|
| 2015-2018致股东信（阿里官网） | ⭐⭐⭐ 一手 |
| 达沃斯论坛对话2015/2017（WEF） | ⭐⭐⭐ 一手 |
| 《赢在中国》节目2007-2008 | ⭐⭐⭐ 一手 |
| 湖畔大学讲课 | ⭐⭐ 二手 |
| 外部传记（《Alibaba》《穿布鞋的马云》） | ⭐⭐ 二手 |
| CNBC/CNN/Bloomberg采访 | ⭐⭐⭐ 一手 |
| 2025-2026阿里内部讲话（媒体报道） | ⭐⭐ 二手 |

## 技术栈

- 女娲Skill造人术框架（Nuwa Skill方法论）
- 纯Python标准库（ma_yun.py）
- 标准Hermes Agent SKILL.md格式

## License

MIT

## 致谢

- `liyuan210/ma-yun-skill` — 心智模型框架参考
- `robertquant/jack-ma-perspective` — 6件套research方法论
- `cjtdawn-cn/ma-yun-skill` — ma_yun.py脚本
- `wszz117/nuwa-skill` — 女娲Skill造人术框架
