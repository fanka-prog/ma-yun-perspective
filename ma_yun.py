"""
马云导师 — Jack Ma Mentor Skill
用法:
  python ma_yun.py "我想创业但不知道怎么开始"
  python ma_yun.py --quote        # 随机一条经典语录
  python ma_yun.py --list          # 列出所有语录分类
"""
import random

# ═══════════════════════════════════════
#  马云知识库
# ═══════════════════════════════════════

JACK_MA_PROFILE = {
    "name": "马云 (Jack Ma)",
    "birth": "1964年9月10日，杭州",
    "education": "杭州师范学院英语学士",
    "title": "阿里巴巴集团创始人、蚂蚁集团创始人",
    "net_worth": "约300-400亿美元",
    "key_achievements": [
        "1999年创办阿里巴巴（18人，6万美元起步）",
        "2003年创建淘宝，打败eBay中国",
        "2004年创建支付宝（现蚂蚁集团）",
        "2014年纽交所上市，创美股史上最大IPO（250亿美元）",
        "2025-2026年推动阿里3800亿AI战略",
    ],
    "nickname": "风清扬（阿里内部花名）",
}

QUOTES = {
    "创业": [
        "创业是为未来而战，不是为今天而活。",
        "100个人创业，95个人会死掉，你连声音都没听见。",
        "创业要永远去想，你是为五年后、十年后创业。",
        "既要有兔子一样的速度，也要有乌龟一样的耐力。",
        "我创业十多年来，最大的心得是：永远思考别人是怎么失败的。",
        "成功的案例看了会让人想入非非，失败的教训才值钱。",
        "如果有来世我还会从商，最好的经验是你经历了多少。",
        "任何一棵大树下面一定有巨大的营养，来自这个时代很多人犯的错误。",
    ],
    "战略": [
        "眼光看到一个省，做一省生意；看到全世界，做全世界生意。",
        "生意越来越难做，越难做越是机会，关键是你的眼光。",
        "战略就是你知道这样下去，将来一定在这儿，所以先挖个坑。",
        "比聪明你已经没机会了，比勤奋估计更没机会，你只能比未来。",
        "上世纪拼智商，这世纪拼情商——让别人舒服，没有比这更重要的。",
        "AI不是工具，AI是生产力本身的重构。",
        "阿里最大的风险不是做错了什么，而是什么都不做。",
    ],
    "商业": [
        "做任何生意，必须想到3W——客户赢、伙伴赢、你赢。少一赢，生意没法做。",
        "客户要的不是服务，客户要的是体验。",
        "互联网最了不起的东西：利他主义——只有别人成功，你才能成功。",
        "阿里考核成功的标准，不是我们有没有成功，而是客户有没有成功。",
        "钱和权不能碰在一起。做了生意就别想当官，当了官就别想赚钱。",
        "追着钱没有意义，钱是追人的。人要是追钱，一点出息都没有。",
        "一个人怎么可能有20亿那么多钱，不管你多努力，都不该有那么多钱。",
    ],
    "管理": [
        "选择平凡的人。没把自己当精英，有平凡的梦想——买房买车娶老婆。",
        "平凡人在一起做不平凡的事。伟大的事就是重复、单调、枯燥地做同一件事。",
        "公司里最大的资源就是信任。",
        "我从没留过任何人。他们不是为马云工作，而是为共同目标工作。",
        "培就是多关注他，养就是给他失败的机会、成功的机会。",
        "企业是野生动物园，要学会发现他们，用欣赏的眼光看他们。",
        "阿里可以失去一切，但不能失去理想主义。",
        "我最难过的是有人说阿里人骄横了，变得无所不能。我们必须谦卑。",
    ],
    "人生": [
        "这一辈子，你到底有什么？你要什么？你放弃什么？",
        "幸福是自己去找的。创业带来快感，但快感背后是很多痛苦。",
        "我们到这个世界不是来创业的，是来体验生活的。",
        "世界本来就是不公平的。但你跟比尔·盖茨一样都是24小时。",
        "永不放弃的是使命和价值观，宁可关了公司也不为钱放弃。",
        "当你学会放弃的时候，才真正开始进步。撞不过去就往后退一步，绕着走。",
        "信是感恩，仰是敬畏。有感恩之心运气就来；有敬畏之心鬼神避开。",
    ],
    "阶段": [
        "20-30岁：加入好公司，跟好老板学做事。",
        "30-40岁：想做就去做，失败了也无所谓。",
        "40-50岁：做自己擅长的事，不要盲目尝试新事物。",
        "50-60岁：关注培训年轻人。",
        "60岁以上：最好跟外孙在一起共享天伦。",
    ],
}


def get_random_quote(category=None):
    """随机获取一条马云语录"""
    if category and category in QUOTES:
        return random.choice(QUOTES[category])
    cat = random.choice(list(QUOTES.keys()))
    return f"【{cat}】{random.choice(QUOTES[cat])}"


def get_all_categories():
    """列出所有分类及语录数量"""
    return {k: len(v) for k, v in QUOTES.items()}


def search_quotes(keyword):
    """按关键词搜索语录"""
    results = []
    for cat, lines in QUOTES.items():
        for line in lines:
            if keyword in line:
                results.append(f"【{cat}】{line}")
    return results


def mentor_response(question):
    """根据用户问题，返回马云风格的导师回答"""
    question_lower = question.lower()

    # 关键词匹配 → 给出对应领域的语录
    if any(w in question_lower for w in ["创业", "辞职", "开始", "项目", "startup"]):
        theme = "创业"
    elif any(w in question_lower for w in ["钱", "融资", "投资人", "投资", "funding", "money"]):
        theme = "商业"
    elif any(w in question_lower for w in ["管理", "团队", "员工", "用人", "招聘", "team"]):
        theme = "管理"
    elif any(w in question_lower for w in ["战略", "方向", "未来", "趋势", "竞争", "strategy"]):
        theme = "战略"
    elif any(w in question_lower for w in ["人生", "迷茫", "意义", "幸福", "选择", "life"]):
        theme = "人生"
    elif any(w in question_lower for w in ["年纪", "年龄", "阶段", "20", "30", "40", "50"]):
        theme = "阶段"
    else:
        theme = random.choice(list(QUOTES.keys()))

    quotes = random.sample(QUOTES[theme], min(3, len(QUOTES[theme])))
    return {
        "theme": theme,
        "quotes": quotes,
        "response": f"马云说过：\n" + "\n".join(f"  > {q}" for q in quotes),
    }


# ═══════════════════════════════════════
#  CLI
# ═══════════════════════════════════════

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("马云导师 Skill")
        print("用法: python ma_yun.py <问题>")
        print("     python ma_yun.py --quote    随机语录")
        print("     python ma_yun.py --list     所有分类")
        print("     python ma_yun.py --search <关键词>")
        print()
        print(get_random_quote())
    elif sys.argv[1] == "--quote":
        cat = sys.argv[2] if len(sys.argv) > 2 else None
        print(get_random_quote(cat))
    elif sys.argv[1] == "--list":
        for cat, count in get_all_categories().items():
            print(f"  {cat}: {count}条")
    elif sys.argv[1] == "--search" and len(sys.argv) > 2:
        results = search_quotes(sys.argv[2])
        if results:
            print(f"搜索 '{sys.argv[2]}' 结果:\n" + "\n".join(results))
        else:
            print(f"未找到与 '{sys.argv[2]}' 相关的语录")
    elif sys.argv[1] == "--profile":
        import json
        print(json.dumps(JACK_MA_PROFILE, ensure_ascii=False, indent=2))
    else:
        result = mentor_response(" ".join(sys.argv[1:]))
        print(result["response"])

