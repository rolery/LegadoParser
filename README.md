# LegadoParser

阅读3.0书源规则解析库

支持大多数 `Default` `Jsonpath` `Xpath` `Regex` 规则

支持部分 `Js` 规则

支持部分特殊规则，如 `{{ }}`、`{$. }`、正则替换

支持 `webView` ，使用Selenium驱动，需要安装[`Chrome`](https://www.google.cn/chrome/)浏览器

Windows下需要Python 3.9版本，其他Python版本的部分依赖安装需要自行编译

## 安装

### Windows （Python 3.9）

```bash
git clone https://github.com/821938089/LegadoParser
cd LegadoParser
pip install -r requirements_win.txt
```

### Linux/WSL （Python 3.8+）

```bash
git clone https://github.com/821938089/LegadoParser
cd LegadoParser
sudo apt-get install libxml2 libxml2-dev
pip install -r requirements_linux.txt
```

## 基础用法

详见 [`usage.py`](https://github.com/821938089/LegadoParser/blob/main/usage.py)

## 高级API

```python
from LegadoParser2.Search import search

def search(bS, key, page=1):
"""
搜索函数

参数 - 描述 - 类型

bS - 书源 - dict
key - 搜索 - str
page - 页数 - int

返回值 list[dict]

注意：如果搜索后直接跳转到了详情页，将调用parseBookInfo获取信息，字典key注意差异。
书籍Url的key将从bookUrl变为tocUrl。
"""
```

```python
from LegadoParser2.BookInfo import getBookInfo

def getBookInfo(bS, url):
"""
获取详情信息

参数 - 描述 - 类型

bS - 书源 - dict
url - search函数中返回的 bookUrl 或 tocUrl - str

"""
```

```python
from LegadoParser2.ChapterList import getChapterList

def getChapterList(bS, url):
"""
获取章节列表

参数 - 描述 - 类型

bS - 书源 - dict
url - getBookInfo函数中返回的tocUrl - str

"""
```

```python
from LegadoParser2.Chapter import getChapterContent

def getChapterContent(bS, url, nextChapterUrl=''):
"""
获取章节内容

参数 - 描述 - 类型

bS - 书源 - dict
url - getChapterList函数中返回的url - str
nextChapterUrl - 下一章的url - str
"""
```

```python
from LegadoParser2.RuleEval import getElements, getString, getStrings
from LegadoParser2.RulePacket import getRuleObj

# 基础API
```

## 示例结果

```python
--------------------开始搜索--------------------
{'author': '遥的海王琴',
 'bookUrl': 'https://www.zhaishuyuan.org/book/9/9256/',
 'coverUrl': 'https://img.zhaishuyuan.org/9/9256/9256s.jpg',
 'intro': '方瑾凌刚醒过来的时候，正好听到云阳侯将外室接了回来，据说私生子分外出息，欢欢喜喜地准备认祖归宗。府里上下都觉得云阳侯要舍弃活不长久的嫡子，培养庶子，等着看云阳侯夫人和方瑾
凌的笑话。然而云阳侯夫人却守在方瑾凌身边，放下一句：“凌儿，娘想和离。”云阳侯只道他的夫人只是一句狠话，温柔贤惠的性子哪儿敢真走。可没想到，春节未过，西陵侯府来人敲开了大门，一字排开 
的尚家小姐们恭请小姑姑和小表弟回家。看着这一二三',
 'kind': '连载,其他,55分钟前',
 'lastChapter': '第194章 谋逆蛊惑太子悖逆人伦55分钟前',
 'name': '我的江山，你随便捏',
 'wordCount': '98字'}
--------------------开始获取详情--------------------
{'author': '遥的海王琴',
 'coverUrl': 'https://img.zhaishuyuan.org/9/9256/9256s.jpg',
 'intro': '\u3000\u3000'
          '方瑾凌刚醒过来的时候，正好听到云阳侯将外室接了回来，据说私生子分外出息，欢欢喜喜地准备认祖归宗。府里上下都觉得云阳侯要舍弃活不长久的嫡子，培养庶子，等着看云阳侯夫人和方瑾
凌的笑话。然而云阳侯夫人却守在方瑾凌身边，放下一句：“凌儿，娘想和离。”云阳侯只道他的夫人只是一句狠话，温柔贤惠的性子哪儿敢真走。可没想到，春节未过，西陵侯府来人敲开了大门，一字排开 
的尚家小姐们恭请小姑姑和小表弟回家。看着这一二三',
 'kind': '其他,连载,2022-02-02',
 'lastChapter': '',
 'name': '我的江山，你随便捏',
 'tocUrl': 'https://www.zhaishuyuan.org/book/9/9256/',
 'wordCount': '98 万字'}
--------------------开始获取章节列表--------------------
列表大小193
[{'name': '第1章 寒冬 ',
  'url': 'https://www.zhaishuyuan.org/book/9256/7423287.html'},
 {'name': '第2章 苏醒 ',
  'url': 'https://www.zhaishuyuan.org/book/9256/7423288.html'},
 {'name': '第3章 做戏 ',
  'url': 'https://www.zhaishuyuan.org/book/9256/7423289.html'}]
--------------------开始获取内容--------------------
{'content': '京城已经入冬了，临着春节，最是寒冷的时候。\n'
            '\u3000\u3000'
            '第一场鹅毛雪刚尽，降下一片银装素裹，而闹腾的云阳侯府，也迎来了短暂的寂静，仿佛所有的喧嚣被这莹白大雪所掩盖。\n'
            '\u3000\u3000可这无暇的纯洁实在太难留住了，只需踩上几脚，立刻便染上了污浊和令人厌恶的肮脏。\n'
            '\u3000\u3000'
            '云阳侯夫人尚轻容透过浮云雕花的窗格，看到她院里的丫环素云连曲折的环廊都来不及走，一路踩着雪小跑过庭院，留下了那一串刺目泥泞的脚印。\n'
            '\u3000\u3000“夫人，不好了，侯爷真的，真的将人接回来了！”\n'
            '\u3000\u3000明明是寒冷的冬日，素云的额头却跑出了一层细细的汗，她顾不得擦拭，只是红着眼睛看着侯夫人，六神无主。\n'
            '\u3000\u3000'
            '一股冷风随着她的闯入一并吹进了这个暖阁中，云阳侯夫人坐在床榻边，下意识地起身挡了挡，不让这风吹着床上之人。\n'
            '\u3000\u3000'
            '床上躺着的是一位少年，眉眼安静恬然，容貌与尚轻容极为相似，只是似乎病魔缠身，脸色看起来苍白近透，犹如精致易碎的瓷器娃娃。\n'
            '\u3000\u3000'
            '林嬷嬷端着药走出来，一见到素云的模样就皱了眉，低声呵斥道：“慌张什么，也不在门口站站去去寒气，小心吹着少爷！”\n'
            '\u3000\u3000'
            '“是，可是……”素云年纪小，被林嬷嬷一训斥眼里便带了委屈，只是看着侯夫人，小声辩解道，“奴婢着急，怕禀告迟了，夫人来不及阻止……”\n'
            '\u3000\u3000云阳侯夫人纤眉微微一蹙，那颗心又仿佛被针扎了一下，泛起细细的疼。\n'
            '\u3000\u3000林嬷嬷看得心酸，将碗递给侯夫人提醒道：“夫人，小心烫。”\n'
            '\u3000\u3000侯夫人回过神，未曾言语，只是接过了碗，捏着汤匙一边轻轻搅动，一边小口吹着药汁。\n'
            '\u3000\u3000'
            '她垂下的眼睫如蝉翼，精致的耳坠随着她的动作轻轻摆动，冬日雪后短暂的阳光透过窗子斜射进来，谁见了不得赞叹一句：美人如画。只是如今蛾眉轻皱，久不散开，叫人心疼不已。\n'     
            '\u3000\u3000素云被带下去更衣休息，大丫鬟清叶和拂香走进来，与林嬷嬷对视了一眼，纷纷露出担忧。\n'
            '\u3000\u3000林嬷嬷最终道：“夫人，您打算怎么办，就由着侯爷将那对母子领进门？”\n'
            '\u3000\u3000'
            '“自是叫她们打哪儿来就回哪儿去！不经过夫人同意就想进来，痴心妄想！”拂香竖着眼睛，一脸怒容，她性子泼辣护主，什么话都敢说，“侯爷简直鬼迷心窍了，如今少爷还昏迷着呢，他竟然 
想迎新人，这将夫人和少爷置于何地！”\n'
            '\u3000\u3000别说是拂香，就是稳重的清叶也低骂了一声。\n'
            '\u3000\u3000然而云阳侯夫人却垂下眼睛，轻声道：“他不糊涂，他早就等不了了。”\n'
            '\u3000\u3000“夫人……”林嬷嬷听着哑下的声音，瞧着侯夫人心如死灰的神情，不由地眼睛一酸。\n'
            '\u3000\u3000'
            '放眼大顺京城，哪家女子不曾赞叹云阳侯对其夫人的情深意重？嫉妒同为女子，在她们与小妾斗法争宠的时候，尚轻容却得丈夫全心全意的疼爱和敬重。\n'
            '\u3000\u3000尚轻容不远千里从边关嫁到京城，也以为终得良人，夫妻恩爱，憧憬着将来白头偕老。\n'
            '\u3000\u3000可事实上呢？却是云阳侯偷偷养了十来年的外室，居然还有个跟原配嫡子一般大的私生子！\n'
            '\u3000\u3000看着将人拿捏的死死，却像傻子一样被蒙在鼓里，她瞬间成了整个京城的笑话。\n'
            '\u3000\u3000“都是假的，假的……”尚轻容眼里的泪水终于噙不住，一滴一滴地落下来，进了药碗。\n'
            '\u3000\u3000一朝佳梦破，从此无良人，只剩薄情寡义。\n'
            '\u3000\u3000'
            '拂香见此眼睛跟着湿红，咬着牙道：“奴婢现在就去拦住她们，我就不信若是夫人您坚持不同意，侯爷难道非得让那卑贱的犯官女进门吗？”\n'
            '\u3000\u3000“她已经不是犯官之女了，杨大人月前已官复原职，重新受到皇上器重，朝堂位列靠前。”清叶轻声纠正道。\n'
            '\u3000\u3000'
            '拂香顿时梗起脖子，强硬道：“哈，那又如何？外室就是外室，依旧是个下贱胚子，她生的儿子永远是个贱种，要被人一辈子戳脊梁骨，抬不起头来！想要名分，做梦！”\n'
            '\u3000\u3000'
            '清叶虽也是这样想，只是她更为冷静，看向尚轻容道：“夫人，其实那杨氏进不进门还是其次，奴婢听静思堂的文福说，侯爷的意思还要趁着这个年节开祠堂，让那私生子认祖归宗！”\n'     
            '\u3000\u3000“什么？”拂香瞪大了眼睛。\n'
            '\u3000\u3000而林嬷嬷忙问道：“夫人可知道？”\n'
            '\u3000\u3000云阳侯夫人闭上眼睛，然后缓缓地点头。\n'
            '\u3000\u3000'
            '被她知晓的当日，云阳侯便捧着小心，带着歉疚，以一副悔不当初却又无可奈何的语气，跪在她的面前，哄了又哄，请她高抬贵手，全他脸面，让流落在外的方家子嗣回宗，别让人看笑话。\n'
            '\u3000\u3000可是这笑话的始作俑者又究竟是谁？\n'
            '\u3000\u3000侯夫人一想起来那副画面，心口的痛就更加煎熬难忍，也让她犯起一阵又一阵的恶心。\n'
            '\u3000\u3000只是这两日，儿子病情又因为这个消息突然恶化，让她无暇顾及这些。\n'
            '\u3000\u3000然而没想到云阳侯竟然不顾夫妻情谊，不顾嫡子生死，竟执意将人迎进门。\n'
            '\u3000\u3000她觉得这一切都是如此的匪夷所思，这短短不到一月的时间恍如做梦一样，身边的那个男人是那么陌生又可怕。\n'
            '\u3000\u3000'
            '“实在太过分了，太欺负人了！”拂香越想越气，胸口大伏大起，最终一转身便朝门口奔去，不管不顾地踩进雪地中，就要去拦人。\n'
            '\u3000\u3000“拂香……”清叶唤了一声，没将人喊住，愁眉转过头看着侯夫人道，“这……奴婢也去看看吧。”\n'
            '\u3000\u3000尚轻容没有回答，林嬷嬷给清叶使了一个眼色，后者便欠了欠身，也追了出去。\n'
            '\u3000\u3000直到两个丫鬟的身影离开，林嬷嬷才担忧道：“夫人，您说这能拦住吗？”\n'
            '\u3000\u3000'
            '尚轻容缓缓地摇头：“如今腊月，进门正好在春节里姻亲走动。听说那孩子学问好，杨家悉心栽培，明年正可以下场一试，他岂会放开？”\n'
            '\u3000\u3000林嬷嬷一怔：“这……”\n'
            '\u3000\u3000“如今想来，他早已经对凌儿放弃。”\n'
            '\u3000\u3000'
            '方瑾凌自小体弱，三天两头缠绵病榻，这从娘胎里带出来的毛病，让他汤药不离手，又如何读书考取功名？就是官位放在面前，也没那个心力。\n'
            '\u3000\u3000'
            '尚轻容想到这里，眼里浮起湿意：“这次他是铁了心要给杨家做脸，拂香他们越拦着，他越一意孤行，让我更难堪罢了。”\n'
            '\u3000\u3000尚轻容的一番话让林嬷嬷简直心疼不已，不禁急道：“那您怎么还让那俩丫头去啊？”\n'
            '\u3000\u3000'
            '尚轻容惨然一笑，目光落在床上的少年脸上，带着一丝怨，一丝愤：“我只是想看看，我和凌儿在他心里究竟还剩多少分量，或者，让我知道托付终生之人是怎样的薄情寡义。”\n'
            '\u3000\u3000'
            '汤药已经放凉了，她拭了拭脸颊上的湿意，示意林嬷嬷扶起少年的上身，让其靠在自己的怀里。她调整着姿势，让儿子靠得更舒适些，虽然昏迷的人根本无知无觉，她却极尽小心。\n'       
            '\u3000\u3000'
            '林嬷嬷端起药碗凑到少年的嘴边，尚轻容舀着汤匙小心地送进他的嘴里，一点一点地喂进去，只是无法吞咽的人，这药自然又大半地沿着唇角流下来。\n'
            '\u3000\u3000'
            '林嬷嬷急急拿帕子垫着，然而看着药汁浸染的程度，就知道几乎没喂进去，不禁慌了：“夫人，这……少爷不见好，看着似乎越来越严重了！”\n'
            '\u3000\u3000侯夫人心中一颤，强自镇定道：“再去请大夫，另外拿名帖，请太医一趟，快！”\n'
            '\u3000\u3000“是。”\n'
            '\u3000\u3000'
            '林嬷嬷去唤人，侯夫人接过药碗继续喂着方瑾凌：“凌儿，你快醒来呀，喝药，病就能好了，你答应娘要活到长命百岁，求你张嘴喝呀，快喝药……”\n'
            '\u3000\u3000'
            '侯夫人低低的乞求声中，那固执的汤匙强行撬开少年的唇，却又无可奈何地阻挡不了药汁溢出，如此来回，便洒了衣襟和床铺，一片狼藉。\n'
            '\u3000\u3000'
            '林嬷嬷回来的时候就听到哐当一声，汤匙落在碗中发出了声响，却是尚轻容再也喂不下去，崩溃地直接抱着儿子压抑地哭泣起来。\n'
            '\u3000\u3000“凌儿，娘只有你了……你无论如何不能弃娘而去……”\n'
            '\u3000\u3000'
            '云阳侯再如何背叛当初的誓言，辜负她的情谊，她都不在乎，只有唯一的儿子，病情恶化才让她痛彻心扉，再也坚强不下去，无法抑制住那股浓浓的怨恨。\n'
            '\u3000\u3000'
            '然而谁能想到云阳侯府的公子根本熬不过这个冬天，已经一命呜呼了。至今气若游丝，未曾断绝生机，却是因为后世的一抹孤魂阴差阳错地进了这具身体。\n'
            '\u3000\u3000庞大又繁杂的记忆碎片不断充斥着他的脑海，让他浑浑噩噩，方瑾凌对外界毫无任何反应，自然也醒不过来。\n'
            '\u3000\u3000'
            '可是侯夫人这声声在耳边的哀求仿佛一下子突破了他的迷障，揪住了心，让他从凌乱的记忆中终于找回了思绪，能够接纳外界的声音。\n'
            '\u3000\u3000鼻尖闻着淡淡的清香，却是记忆中属于母亲的味道。\n'
            '\u3000\u3000'
            '方瑾凌想抬起手，抱一抱这位可怜的母亲，然而此刻他全身无力，难以动弹，甚至连掀个眼皮看一看人都办不到，更无从安慰。\n'
            '\u3000\u3000这具天生羸弱的身体实在太虚了！\n'
            '\u3000\u3000好在强大的新魂似乎注入了新的力量，他的身体正慢慢融合恢复着，再过不久他就能睁开眼睛。\n'
            '\u3000\u3000只是不知为何，听着女子的恳求让他心口不由地发酸，却是身体与他发起了共鸣。\n'
            '\u3000\u3000恍惚之间，原本的方瑾凌好似与他重合在一起。\n'
            '\u3000\u3000而这时，一个急切的声音传来。\n'
            '\u3000\u3000'
            '“夫人，拂香姐姐和清叶姐姐没有拦住，如今侯爷带着那……那对母子往这边来了……”前去门口查看的小丫鬟，急切地回来报信，“说是要拜见您。”\n'
            '\u3000\u3000林嬷嬷一怔，脱口而出道：“这么快？”\n'
            '\u3000\u3000就是抱着方瑾凌的尚轻容闻言也止了泣声。\n'
            '\u3000\u3000接着那小丫鬟带着哭腔道：“夫人，两位姐姐不过刚到门口，就叫人堵住了嘴，连开口的机会都没有！”\n'
            '\u3000\u3000'
            '闻言林嬷嬷手里的帕子掉了，不禁往后倒了一步，颤着声音道：“侯爷竟心狠如此？这是生生打夫人的脸啊……怎么会这样？”\n'
            '\u3000\u3000'
            '舒云院上下纷纷望向了尚轻容，后者抱着儿子，定定地看着门口的方向，那哭红的眼睛终于迸发出浓烈的恨意，咬牙切齿道：“好，真是好，方文成，比我想象中的还要无情无义……林嬷嬷！”\n'
            '\u3000\u3000“夫人。”\n'
            '\u3000\u3000侯夫人小心地将儿子放下，接着缓缓地起身，毫无焦距的目光在四周围一扫，问道：“我的剑呢？”\n'
            '\u3000\u3000林嬷嬷闻言一惊，“您要剑做什么？”\n'
            '\u3000\u3000侯夫人没有回答，只是再一次吩咐：“把我的剑取来。”\n'
            '\u3000\u3000林嬷嬷手脚冰凉，终于发现尚轻容的不对劲，连忙劝道：“夫人，这是少爷的屋子，没有您的剑，您冷静一些。”\n'
            '\u3000\u3000'
            '“凌儿的，对，这里是舒云院……”侯夫人踉跄着站起来，却绕过床头，到了屏风之后，见到架上那根方瑾凌从未用过的红缨长.枪，她素手一抬，直接握在手里，眼中含泪，透着绝望，咬着牙说 
，“是我识人不轻，天真痴傻，才叫人蒙蔽了那么多年。眼瞎如我，落得这样的下场，活该。可是……”\n'
            '\u3000\u3000'
            '看似柔弱娇美的云阳侯夫人在握住长.枪的一瞬间气势就变了，眉目凌厉，似有红炎烈火在她身上灼烧，烧尽了那股温柔慧娟，却烧出隐藏多年的锐气锋芒。\n'
            '\u3000\u3000'
            '“可是却不该连累到我的凌儿，让他遭受这样的苦难……”她的眼底迸发出强烈的恨，似有癫狂之意，豁出去了，“那就谁也别想好过！”\n'
            '\u3000\u3000'
            '林嬷嬷看着尚轻容提枪走向门口，大有当初西陵侯一斩敌方首级的架势，顿时心中大恸，不禁对着床上的少年噗通一声跪下，嚎啕大哭起来：“少爷啊，奴婢求求您醒来吧——”\n'
            '\u3000\u3000'
            '舒云院立刻混乱起来，看着侯夫人好似玉石俱焚地远去，林嬷嬷除了哭，只剩六神无主，可在这个时候，床上却突然传来一个虚弱至极的咳嗽声。\n'
            '\u3000\u3000'
            '仿佛是错觉，却好像按下了休止符一下子让周围安静下来，接着那咳嗽一声比一声重，直到最后少年沙哑的嗓子唤着：“娘……”\n'
            '\u3000\u3000这声音明明那么轻微，却好似一道明亮的光，瞬间驱散了众人心头的乌云。'}
--------------------结束--------------------
```
