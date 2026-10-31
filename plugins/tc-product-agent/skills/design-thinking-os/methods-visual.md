# UI 界面视觉方法库

本文件属于 Figma UI 设计，处理界面中的视觉系统与资产应用，不是 UI 后必须追加的独立阶段。视觉方法不改变已确认的路径、职责和主行动含义。实现设计参考时必须以正式主稿和真实资产为准，不得近似降级。

界面中的插画、图片、图标和品牌图形属于 Figma UI。只有最终产物是非界面视觉成品，或用户明确把某项资产拆成独立视觉委托时，才按 [methods-tool-routing.md](methods-tool-routing.md) `TR4` 调用视觉工具；确认后的独立资产可再导入 Figma。不得用占位或近似资产代替正式生产。

所有视觉方法同时遵守以下记录规则：

- 把正式来源、设计推导、待确认候选和人的决定分开记录；候选不能写成品牌事实或已确认规范。
- 每个实现值必须给出准确来源与版本、正式系统引用，或标为 `CANDIDATE_PENDING_CONFIRMATION`；不能凭常识补品牌值。
- 来源缺失且不同答案会改变成品时暂停受影响部分：可由本轮设计探索解决且已有授权时标 `MISSING/RESOLVE_NOW`；必须等待正式来源、资产或授权时标 `BLOCKED/WAIT_EXTERNAL`。只有明确委托或可追溯依据时才形成候选。
- 实现或还原设计参考时，布局、字体、间距、颜色、真实内容、真实资产和交互均须忠实应用；资产、权限或正式值缺失时停止，不用近似值、占位符或简化替代品冒充完成。
- 所有产出都写适用页面、组件、平台、主题、表面、状态和版本，使新会话能够直接实现并逐项验收。

## V0 0→1 视觉风格库与 6 维决策漏斗

**触发问题**：在页面职责、信息层级（U1–U3）与所用组件（U4）已确认、且经 `U0` 判定属于 **C 端或强品牌差异化产品从 0 到 1 新建** 时，如何系统地帮用户选定风格并敲定具体视觉构件？  
**最低输入**：已确认的页面结构与组件选型、市场生态（国际化 / 国内）、行业与任务严肃度、目标人群。  
**跳过**：
- 有现成相关页面或既有设计系统（走 `U0` 路线 1：存量延展模式，直接提取现有 5 个视觉常量复用）；
- 纯 B 端/企业中后台从 0 到 1（走 `U0` 路线 2：直接绑定 `Ant Design` / `Arco Design` / `TDesign` / `shadcn/ui` / `MUI` / `Fluent UI` 等公开组件库快搭）。

### Step 1：语境自动剪枝（先过滤，不把违和选项抛给用户）

根据前面已确认的 4 个条件自动排除不匹配的风格与视觉构件：

1. **市场生态与品类池**：
   - 出海 / 国际化产品优先从「A. 国际化产品风格池（`INT-01`～`INT-08`）」选；
   - 国内主流 App / 小程序优先从「B. 国内产品风格池（`CN-01`～`CN-08`）」选；
   - 游戏界面、游戏官网或强游戏化互动活动页，直接进入「D. 游戏与互动娱乐 UI 风格池（`GAME-01`～`GAME-10`）」按世界观与题材匹配；
   - 以上均可叠加「C. 通用视觉质感手法（`TEX-01`～`TEX-06`）」。
2. **行业与风险底线**：高严肃、高风险行业（金融、银行、医疗诊断、法律、政务、核心交易台）**强制剔除**糖果游戏化（`INT-07`）、先锋粗野撞色（`INT-08`）、高能量大促红海（`CN-05`）、Z 世代暗黑霓虹（`CN-07`）以及卡通手绘插画、花哨多色渐变。
3. **任务形态**：高频重操作、高密度数据比对任务，优先克制背景、强层级对比与清晰容器；低频浏览、内容消费、品牌展示任务，可引入强氛围感、大留白或大图视觉。
4. **目标人群**：银发族、大众民生或下沉市场，强制高可见度、大字号与明确文字标签，剔除极简小字留白和暗黑微光风。

### Step 2：从共同维护的风格库 List 中提供 2–3 个方向供用户选择

不固定死 3 个选项：严肃度极高时只给 2–3 个稳重克制方向；探索空间大时给 3 个反差明显的方向。

#### A. 国际化产品常见设计风格池（8 类）

| 编号 | 风格名称 | 典型代表 / 视觉印象 | 核心视觉特征 | 适用产品 | 强制排除条件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `INT-01` | **Apple 原生通透风**<br>*(Apple HIG / iOS 现代风)* | Apple 原生应用、Flighty、Things | 大留白、字体粗细强对比、毛玻璃半透明导航/浮层、细腻圆角、克制单主色 | iOS 出海应用、个人效率工具、品质生活与健康硬件配套 | 重度多列后台表格、低端安卓机为主的下沉市场 |
| `INT-02` | **硅谷现代极简风**<br>*(Swiss / Clean SaaS)* | Notion、Raycast、Vercel、Readwise | 黑白灰高纯度主导、1px 细描边分割、极少装饰色、排版秩序感极强、内容即界面 | AI 工具、知识库、生产力 SaaS、B2B 工作台、文档社区 | 强促销氛围电商、重娱乐游戏化产品 |
| `INT-03` | **暗色微光科技风**<br>*(Dark Bento & Glow)* | Linear、Cursor、Arc 局部 | 深炭黑底（非纯黑）、Bento 便当盒网格、1px 渐变发光边框、低饱和蓝紫/青绿微光、毛玻璃叠层 | 开发者工具、AI 前沿产品、高阶科技官网、专业创作者工具 | 银发族/大众民生工具、强日光户外场景、传统母婴/医疗 |
| `INT-04` | **流体渐变专业风**<br>*(Refined Fintech / Fluid)* | Stripe、Wise、Mercury | 主体干净理性的白/浅冷灰底 + 局部高质量流体/网格渐变或清晰高对比品牌色、数字字体精良 | 出海金融科技（Fintech）、跨境支付、企业服务官网、高客单价 SaaS | 追求极致朴素零装饰的内部后台 |
| `INT-05` | **暖色人文出版风**<br>*(Warm Editorial)* | Claude、Medium、Substack | 暖米白/纸张底色、低饱和赤陶橙/墨绿/深棕点缀、衬线体标题 + 无衬线正文混排、阅读感强 | AI 对话/阅读产品、深度内容平台、文化/教育/心理健康、品质品牌站 | 高频秒级盯盘交易、强促销导购 |
| `INT-06` | **Google 现代动态风**<br>*(Material You / Expressive)* | Google 系列应用、现代 Android 原生 | 柔和动态色彩提取（粉彩容器底色）、大圆角胶囊容器、清晰表面色阶代替生硬阴影 | Android 主力出海应用、大众日常工具、跨设备通用消费应用 | 要求极度冷峻威严的机构或重奢品牌 |
| `INT-07` | **亲和游戏化糖果风**<br>*(Friendly Gamified)* | Duolingo、Headspace | 高明度高饱和友好色块、超圆角卡片、有厚度的立体按压按钮（底部硬阴影）、轻量几何/卡通图形 | 语言/技能学习、习惯打卡、儿童/青少年产品、轻心理陪伴 | 严肃金融、医疗诊断、法律政务、B 端严肃审批 |
| `INT-08` | **先锋粗野撞色风**<br>*(Neo-Brutalism / Bold)* | Gumroad、Figma 活动页、The Verge | 2–3px 纯黑粗描边、无模糊硬阴影偏移、高饱和撞色块、超大粗体字、反传统网格 | 潮流电商、创作者经济、设计/音乐先锋活动、Web3/潮玩 | 传统金融、医疗、政务、大众中老年产品 |

#### B. 国内产品常见设计风格池（8 类）

| 编号 | 风格名称 | 典型代表 / 视觉印象 | 核心视觉特征 | 适用产品 | 强制排除条件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CN-01` | **大厂标准蓝白效率风**<br>*(企业级理性工作台)* | 飞书、钉钉、企业微信、Ant 体系 | 冷白+浅蓝灰底（如 `#F7F8FA`）、科技蓝主色、4–8px 标准圆角、高信息密度且对齐工整 | 国内 B 端 SaaS、协同办公、中后台系统、政务/医疗专业端 | 追求强情绪感染力的潮流消费/娱乐产品 |
| `CN-02` | **新中产生活杂志风**<br>*(清爽卡片内容流)* | 小红书、蔚来 App、得物局部 | 纯白底、弱化分割线、大比例高质量配图+精炼标题、克制品牌点缀色、圆润卡片与精致标签 | 生活方式社区、品质消费/文旅、新消费品牌商城、图文种草 | 纯文字/纯表单重度录入工具 |
| `CN-03` | **克制专业金融风**<br>*(稳重财富/银行风)* | 招商银行掌上生活、蚂蚁财富、雪球 | 深海蓝/墨黑/香槟金辅助、数字使用高辨识度等宽字体（如 DIN）、风险提示与收益层级分明 | 银行、保险、理财、证券、征信、企业财务、高信任交易 | 泛娱乐、儿童教育、随意涂鸦社区 |
| `CN-04` | **国民级轻快小程序风**<br>*(WeChat 生态原生感)* | 微信原生服务、瑞幸/喜茶点单小程序、滴滴 | 操作路径极短、浅灰底配白卡片、单屏主按钮极其醒目、功能胶囊/宫格清晰、零学习成本 | 微信/支付宝小程序、到店点单、出行/快递/生活缴费、轻量工具 | 需要深度复杂配置的专业桌面软件 |
| `CN-05` | **高能量大促导购风**<br>*(高密度电商转化风)* | 淘宝、美团、拼多多、京东 | 暖红/亮橙高饱和主色、价格与优惠标签强对比（红/橙/香槟金）、宫格入口密集、促行动感强 | 综合电商、本地生活团购、外卖生鲜、领券促销活动页 | 高冷奢侈品、严肃医疗/法律、极简效率工具 |
| `CN-06` | **东方新中式雅致风**<br>*(国风/人文留白)* | 观夏、茶颜悦色、故宫文创 | 中国传统低饱和色（黛蓝、竹青、宣纸白、赭石、米砂）、适度留白、细线边框、人文衬线/宋体标题 | 茶饮/香氛/东方消费品牌、文旅景区、博物馆/文化内容、养生 | 现代硬核代码工具、西式高频金融交易台 |
| `CN-07` | **Z 世代机能潮酷风**<br>*(暗黑霓虹/酸性潮流)* | 得物潮品区、B 站活动页、电竞产品 | 深黑底色 + 荧光绿/电光紫/高亮渐变、微 3D 或金属玻璃质感、斜切/徽章/强动感排版 | 潮玩、电竞游戏、音乐/演出票务、Z 世代社交、数码硬件营销 | 中老年产品、严肃 B 端、传统金融政务 |
| `CN-08` | **适老/大众普惠大字风**<br>*(高可见度直白风)* | 各大 App 长辈模式、下沉民生工具 | 字号整体放大 1–2 档、超高对比度、正色主按钮、全部图标带明确中文标签、无隐藏手势 | 银发群体产品、县域/下沉市场大众工具、社区团购、基层政务 | 追求极简小字留白的先锋设计师品牌 |

#### C. 通用视觉质感手法标签（6 种，可单选或与 A/B/D 组合）

1. `TEX-01 极简扁平（Clean Flat）`：纯色块 + 留白 + 细线，无复杂光影，开发还原最稳。
2. `TEX-02 毛玻璃通透（Glassmorphism / 液态玻璃）`：半透明背景模糊 + 1px 高光细边，适合悬浮导航、卡片叠层、深浅过渡。
3. `TEX-03 Bento 便当盒分块（Bento Grid）`：规整圆角矩形模块化拼图，适合首页总览、功能聚合、数据看板。
4. `TEX-04 轻质感微立体（Soft UI）`：极柔和多层投影与微渐变表面，按钮和卡片有细腻触感（禁用老式厚重拟物）。
5. `TEX-05 弥散光氛围（Aurora / Mesh Gradient）`：底层柔和多色高斯模糊光晕，上层承载干净界面，适合首屏 Hero、AI 状态、情绪类应用。
6. `TEX-06 杂志感大字报（Editorial Typography）`：弱化框线，靠超大标题字重反差与严密网格撑起气场。

#### D. 游戏与互动娱乐 UI 风格池（10 类，面向游戏界面 / 游戏官网 / 强游戏化活动页）

| 编号 | 风格名称 | 典型代表作 / 视觉印象 | 核心视觉与材质特征 | 适用游戏题材与场景 | 强制排除条件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `GAME-01` | **暴雪史诗暗黑重拟物风**<br>*(Blizzard Dark Fantasy & Heavy Skeuomorphism)* | 《魔兽世界》《暗黑破坏神4》《炉石传说》 | 深炭黑/石材肌理底、锻造黄铜/做旧古金金属包边与铆钉角、宝石/羊皮纸/木纹高光材质、古典罗马衬线大写标题、强烈内发光与厚重浮雕阴影 | 西幻 MMORPG、暗黑刷宝 ARPG、策略卡牌、史诗级游戏官网与资料库 | 现代极简效率工具、清新日常小程序 |
| `GAME-02` | **Supercell 高饱和立体卡通风**<br>*(Clash / Casual Tactile Cartoon)* | 《皇室战争》《荒野乱斗》《部落冲突》 | 高饱和明快色块（宝石蓝/亮黄/草绿/紫）、粗黑外描边（2–3px）+ 顶部白色高光条 + 底部厚实深色硬阴影（强 Q 弹按压感）、微倾斜粗体大字带黑色描边与投影 | 休闲竞技、卡牌对战、塔防、潮玩盲盒、高转化游戏化大转盘/闯关活动页 | 硬核写实军事/恐怖题材、严肃金融政务 |
| `GAME-03` | **腾讯大众竞技鎏金流光风**<br>*(Honor of Kings / Competitive Gold-Tech)* | 《王者荣耀》《和平精英》大厅与赛事 UI | 深海蓝/暗金渐变半透明底、45° 斜切几何金属边框、灿金/青蓝流光高光边、锐利斜体粗黑大字、强段位徽章与电竞赛事仪式感 | MOBA、战术竞技、国民手游大厅/战绩/商城、电竞赛事专题与战报页 | 低龄儿童绘本、极简无装饰文档工具 |
| `GAME-04` | **网易哥特悬疑手绘拼贴风**<br>*(Identity V / Gothic Vintage Sketch)* | 《第五人格》《哈利波特：魔法觉醒》 | 做旧羊皮纸/复古暗褐底、钢笔手绘交叉排线阴影、纽扣/缝线/火漆印章/撕纸边缘材质、怪诞高反差哥特衬线/手写字体、暗红与复古铜金点缀 | 非对称竞技、剧本杀/推理解谜、克苏鲁/哥特暗黑题材、万圣节/悬疑主题活动 | 阳光运动健康、大众民生政务、标准企业后台 |
| `GAME-05` | **叠纸浪漫轻奢乙游/换装风**<br>*(Papergames Otome & Dreamy Couture)* | 《恋与深空》《闪耀暖暖》《无限暖暖》 | 极度通透的浅色毛玻璃/珍珠母贝流光底、香槟金/玫瑰金/星光银极细描边（0.5–1px）+ 四角星芒点缀、纤细高雅衬线体（宋刻/Didot 感）配呼吸感小字、柔和弥散光晕 | 女性向恋爱乙游、换装养成、浪漫互动叙事、美妆/香氛/轻奢跨界联名活动页 | 硬核重工业/暗黑血腥题材、高密度数据后台 |
| `GAME-06` | **网易新国风仙侠水墨丹青风**<br>*(Oriental Xianxia & Ink Gold)* | 《逆水寒》《阴阳师》《永劫无间》 | 宣纸水墨晕染渐变底、鎏金云纹/回纹细框、朱砂红印章作为核心次级标识、苍劲书法标题 + 雅致宋体正文、半透明纱感图层 | 国风武侠/仙侠 MMO、和风/志怪卡牌、国潮文旅联动、古风剧情互动页 | 西式赛博朋克、现代极客代码工具 |
| `GAME-07` | **二次元轻机能扁平潮酷风**<br>*(Anime Sci-Fi UI / Arknights & Hoyoverse)* | 《原神》《崩坏：星穹铁道》《明日方舟》 | 高对比黑白/深灰几何斜切色块 + 极亮单色点缀（明黄/青蓝）、微缩英文机能编码/装饰线/十字准星、超薄半透明磨砂面板、利落无衬线粗体 | 二次元开放世界、科幻机甲/二次元抽卡养成、ACG 展会与虚拟偶像专题页 | 传统中老年应用、古典写实历史题材 |
| `GAME-08` | **复古像素 / 独立街机风**<br>*(Retro Pixel & Indie Arcade)* | 《星露谷物语》《小丑牌 Balatro》《蔚蓝》 | 严格像素网格对齐（`image-rendering: pixelated`）、木牌/CRT 扫描线或复古卡带配色、阶梯状像素边框与硬阴影、8-bit 点阵像素字体 | 独立游戏、像素模拟经营/肉鸽（Roguelike）、复古怀旧彩蛋活动页 | 追求写实高精渲染的奢品或严肃金融 |
| `GAME-09` | **棋牌桌游绿毡奢金拟物风**<br>*(Poker / Guandan / Casino Club Table)* | 《JJ斗地主》《腾讯欢乐麻将/掼蛋》《WSOP 德州扑克》 | 经典祖母绿台呢/深皇家蓝天鹅绒牌桌底、胡桃木与香槟亮金包边护栏、高对比纯白圆角扑克牌面（超大数字角标与红黑花色）、立体齿纹筹码与金豆、胶囊形操作大按钮（过牌/跟注/加注/出牌分色极清） | 德州扑克、掼蛋、斗地主、麻将、桥牌、俱乐部棋牌大厅与赛事牌桌 | 极简冷淡文档、严肃政务医疗 |
| `GAME-10` | **大富翁 / 派对棋盘 3D 糖果富豪风**<br>*(Monopoly GO! / Richman Board & Dice)* | 《Monopoly GO!》《大富翁10》《金币大师 Coin Master》《蛋仔派对》 | 2.5D/3D 等轴立体棋盘格子、钞票绿/富豪金/喜庆红高饱和 glossy 漆面、底部居中超大立体投骰子（Roll）圆弧主按钮、顶部钞票/护盾/体力胶囊资源条、漫天金币钞票飞溅与丝带横幅弹窗 | 大富翁强手棋、掷骰子闯关、社交派对桌游、电商/金融“天天大富翁/掷骰领红包”互动营销活动 | 阴郁恐怖暗黑题材、严肃B端审批 |

### Step 3：联动确认 6 个具体视觉维度（带默认推荐，用户可一键确认或微调）

选定大方向后，顺着该方向给出已过滤违和项的默认组合，与用户确认以下 6 个维度：

1. **主色与色彩表现**：
   - 是否有既定品牌主色？若无，按语境推荐色相（HSB 右上高明度高饱和区或稳重深色区）。
   - **主色表现形式**：`纯色填充（Solid）`（严肃金融/B端/极简默认） / `同色系微渐变（Subtle Gradient）` / `多色流体或弥散渐变（Fluid / Mesh）`（严肃行业禁用）。
   - **辅助色策略**：`单色系克制` / `双色冷暖平衡（如蓝主色+香槟金/暖橙点缀价格或会员）` / `多色分类标签`。
2. **背景底色与中性色冷暖**：
   - **明暗模式**：`亮色清爽底` / `暖纸人文底` / `深色沉浸底` / `上深下浅混合底（头部核心卡深色凸显品质+下方亮色保易读，金融/会员常用）`。
   - **中性灰冷暖倾向**：禁用死板纯黑纯灰（`S=0`），按主色混入 1%–3% 冷暖色相（明度越高饱和度越低，明度越深饱和度略高），选 `微冷蓝灰` / `微暖米灰` / `高对比纯黑白`。
3. **容器分隔与表面材质**：
   - `无框留白 + 1px 细分割线` / `浅灰底配纯白无阴影卡片` / `微阴影悬浮卡片` / `毛玻璃半透明叠层`。
4. **圆角与几何性格**（全套圆润与尖锐必须统一，不得混用）：
   - `0–4px 利落直角/微圆角` / `6–10px 理性标准圆角` / `12–16px 现代亲和圆角 + 胶囊按钮` / `20px+ 超圆角软萌`。
5. **字体气质与排版密度**：
   - **字体组合**：`系统标准黑体（苹方/思源/SF/Inter）` / `标准黑体 + 强化等宽数字字体（如 DIN 风格，金融/电商/看板必推）` / `人文衬线标题 + 无衬线正文`。
   - **信息密度**：`紧凑高效型` / `均衡标准型` / `舒展留白型`。
6. **图标风格与配图边界**：
   - **工具图标**（粗细、圆角、透视三统一，4px 倍数画布与像素对齐）：`精致细线性（1.5–2px）` / `醒目面性填充` / `双色线面结合` / `微质感图标（轻渐变/毛玻璃/轻3D，用于核心宫格入口）`。
   - **配图与空状态图形**（按行业严肃度过滤）：高严肃行业只推 `纯文字与数据图形 / 克制几何抽象图形 / 真实专业摄影`（屏蔽卡通手绘）；消费/社区可选 `高清真实场景摄影 / 扁平现代矢量插画 / 3D 质感元素 / 温暖手绘风`。

### Step 4：单页先行与模块化提炼

只挑选权重最高的 **1 个核心代表页**（如首页或核心操作页）落地上述选择；用户确认后，将配色、文字层级、控件和组件提炼到同一组件/资源画板，再模块化拼装其余页面。

### Step 5：Agent 怎样调用选定的视觉风格（弹窗选择 → 写入任务包 → 自动拼进 Figma/生图指令）

用户进入 C 端 0→1 视觉决策后，**Agent 严禁只拿一个风格名字去凭感觉画图或写代码**，必须严格执行以下 3 步闭环：

1. **Step 5.1｜原生弹窗让用户选（`AskQuestion` / 宿主原生提问工具）**：
   - **第一轮或同轮问题 1（选大风格）**：从经 Step 1 剪枝后的池子中列出 2–3 个候选风格（展示风格编号、名称、代表产品印象与核心视觉特征，首项标 `(Recommended)`）。
   - **同轮问题 2–7（确认 6 个具体维度，带默认推荐）**：顺着首选风格给出「①主色表现（纯色/微渐变/流体渐变）、②底色明暗与中性灰冷暖、③容器材质、④圆角阶梯、⑤字体与等宽数字及密度、⑥图标与配图风格」的默认推荐项，让用户一键确认或单独改某一项。
2. **Step 5.2｜查表加载参数包并写入任务包（唯一视觉数据源）**：
   - 从下方「可执行参数字典」读取所选风格编号对应的精确数值配方（底色/卡片 Hex、主辅色与中性字色阶梯、圆角 px、边框/阴影/毛玻璃 `blur`、字号/字重/行高/间距、专用 Prompt 片段），并用用户的 6 维微调值覆盖对应字段。
   - 立即写入当前任务的 `V0 视觉方向与 6 维决策卡`（或 `DESIGN-<模块>-任务包.md`），锁死为本轮唯一视觉数据源。
3. **Step 5.3｜自动拼进 Figma / 组件库 / 生图执行指令**：
   - **操作 Figma（`use_figma` / Figma Agent / Make）**：使用下方模板将锁定的 Token 数值绑定为 Figma Variables / Styles，并把组装好的指令发送给 Figma 执行层：
     ```text
     [Figma 视觉执行指令组装模板]
     - 绑定风格：{style_id} {style_name}
     - 画布与表面色：Page Canvas = {bg_hex}；Card Surface = {card_hex}；Text Hierarchy = {text_primary} / {text_secondary} / {text_muted}
     - 品牌主色与表现：Primary = {primary_hex}（表现方式：{solid_or_gradient}）；Accent = {accent_hex}
     - 容器与材质：Border = {border_spec}；Shadow = {shadow_spec}；Blur = {blur_spec}
     - 圆角阶梯：Card Radius = {card_radius}；Button/Input Radius = {control_radius}
     - 字体与字阶：Font Family = {font_family}（数字规则：{numeric_font_rule}）；Scale = {type_scale_and_spacing}
     - 图标与配图规范：Icon = {icon_spec}；Imagery = {imagery_rule}
     - 风格 Prompt 注入：{style_prompt_snippet}
     ```
   - **调用公开组件库（纯 B 端 `U0` 路线 2）**：直接连接对应组件库（如 `user-shadcn-ui` MCP 或 Ant Design / Arco / TDesign 规范 token），将 `colorPrimary`、`borderRadius`、`fontSize` 与 `compact/default` 密度一键写入主题配置。
   - **调用 UI 内原位生图（`V7 路径 A`）或独立海报生图（`V7 路径 B`）**：自动把该风格的 `{style_prompt_snippet}`、主色 `{primary_hex}` 与底色冷暖追加进生图模型的 `prompt` 参数。

#### 国际化风格可执行参数字典（`INT-01`～`INT-08`）

| 编号 | 底色 / 卡片 / 字色阶梯（主·次·弱） | 默认主色参考（可被品牌色覆盖） | 边框 / 阴影 / 模糊参数 | 圆角阶梯（卡片 / 按钮控件） | 字族 / 字阶（H1·H2·正文·辅助） / 间距 | Figma / 代码 / 生图专用 Prompt 片段 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `INT-01`<br>Apple 原生通透风 | 底：`#F2F2F7`<br>卡：`#FFFFFF` 或 `rgba(255,255,255,0.78)`<br>字：`#000000` / `#3C3C43` / `#8E8E93` | `#007AFF`（纯色或极轻同色微渐变） | 边框：`0.5px solid rgba(0,0,0,0.06)`<br>浮层：`backdrop-filter: blur(20px)`<br>阴影：`0 4px 20px rgba(0,0,0,0.05)` | 卡片 `16px`<br>按钮 `12px` 或胶囊 `999px` | `SF Pro` / `PingFang SC`<br>字阶：`28/20/16/13px`（标题 `700`，正文 `400` 行高 `1.45`）<br>内边距：`16–20px`，间距 `12/16px` | `Apple HIG modern iOS aesthetic, frosted glass translucent bar (blur 20px), #F2F2F7 canvas, 16px card radius, generous whitespace, crisp SF typography, subtle elevation` |
| `INT-02`<br>硅谷现代极简风 | 底：`#FFFFFF` / `#FAFAFA`<br>卡：`#FFFFFF`<br>字：`#09090B` / `#52525B` / `#A1A1AA` | `#111827`（近黑主按钮）+ 点缀 `#2563EB` | 边框：`1px solid #E4E4E7`<br>阴影：无或极轻 `0 1px 2px rgba(0,0,0,0.04)`<br>模糊：无 | 卡片 `8px`<br>按钮/输入 `6px` | `Inter` / `Geist` + `PingFang SC`<br>字阶：`24/18/14/12px`（标题 `600` 字距 `-0.02em`，行高 `1.5`）<br>内边距：`16–24px`，间距 `8/16px` | `Swiss minimal SaaS UI, crisp 1px #E4E4E7 hairline borders, high-contrast monochrome with single accent, 8px radius, zero clutter, Notion/Vercel inspired` |
| `INT-03`<br>暗色微光科技风 | 底：`#08090A`<br>卡：`rgba(255,255,255,0.03)`<br>字：`#F7F8F8` / `#8A8F98` / `#575BC7` | `#5E6AD2` 或微光渐变 `#4EA7FC -> #B59AFF` | 边框：`1px solid rgba(255,255,255,0.08)`<br>微光：`0 0 24px rgba(94,106,210,0.22)`<br>模糊：`blur(16px)` | 卡片 `12px`<br>按钮 `8px` | `Inter` / `Geist` + `JetBrains Mono`<br>字阶：`28/20/14/12px`（标题 `600`，数字/标签等宽）<br>内边距：`20–24px`，网格间距 `12/16px` | `Dark mode Bento grid UI, deep charcoal #08090A surface, 1px rgba(255,255,255,0.08) luminous border, subtle ambient glow, blur 16px, Linear/Cursor aesthetic` |
| `INT-04`<br>流体渐变专业风 | 底：`#F6F9FC`<br>卡：`#FFFFFF`<br>字：`#0A2540` / `#425466` / `#8898AA` | `#635BFF`（主按钮纯色，局部 Hero 流体渐变） | 边框：`1px solid #E3E8EE`<br>阴影：`0 6px 24px rgba(15,23,42,0.06)`<br>模糊：局部 `blur(12px)` | 卡片 `10px`<br>按钮 `6px` | `Inter` + 强制等宽数字 `tabular-nums`<br>字阶：`28/20/15/13px`（数字 `700`）<br>内边距：`20–24px`，间距 `12/16px` | `Refined fintech UI, clean cool-grey #F6F9FC canvas, structured white 10px cards, #635BFF primary, controlled fluid mesh gradient accent, precise tabular numbers` |
| `INT-05`<br>暖色人文出版风 | 底：`#F5F0E8`（暖纸色）<br>卡：`#FAF7F2`<br>字：`#191918` / `#5C5852` / `#8C857B` | `#CC785C`（赤陶橙）或 `#1F4E3D`（深墨绿），纯色 | 边框：`1px solid #E6DEC8`<br>阴影：无，靠暖色阶与细线分层<br>模糊：无 | 卡片 `8px`<br>按钮 `6px` | 标题衬线 `Fraunces`/`Newsreader`/`宋体` `600`<br>正文无衬线：`30/22/16/13px`（正文行高 `1.65`）<br>内边距：`24–32px` | `Warm editorial UI, cream paper #F5F0E8 background, #CC785C terracotta accent, high-contrast serif headlines with clean sans body, bookish calm` |
| `INT-06`<br>Google 现代动态风 | 底：`#FEF7FF`<br>卡：`#F3EDF7`（Tonal 色阶）<br>字：`#1D1B20` / `#49454F` / `#79747E` | `#6750A4`（配粉彩容器 `#EADDFF`） | 边框：无（纯靠 Tonal Surface 色阶区分）<br>阴影：极轻或无<br>模糊：无 | 卡片 `20px`–`24px`<br>按钮胶囊 `999px` | `Roboto` / `Google Sans` / `思源黑体`<br>字阶：`28/22/16/12px`（标题 `500/600`）<br>内边距：`16–24px`，间距 `12/16px` | `Material You expressive UI, tonal surface color hierarchy (#FEF7FF / #F3EDF7) without heavy shadows, pill-shaped buttons, 20px rounded containers` |
| `INT-07`<br>亲和游戏化糖果风 | 底：`#FFFFFF`<br>卡：`#F7F9FA`<br>字：`#3C3C3C` / `#777777` / `#AFAFAF` | `#58CC02`（活力绿）+ `#FFC800`（明黄）+ `#1CB0F6`（亮蓝） | 边框：`2px solid #E5E5E5`<br>按钮立体底阴影：`0 4px 0 #46A302`（零模糊） | 卡片 `16px`<br>按钮 `14px` | `Nunito` / `Baloo 2` / 圆体 `700/800`<br>字阶：`26/20/16/14px`<br>内边距：`16–20px`，间距 `12/16px` | `Friendly gamified UI, vibrant candy colors (#58CC02 / #FFC800), tactile 3D pressable buttons with 4px solid bottom shadow, 16px chunky rounded corners` |
| `INT-08`<br>先锋粗野撞色风 | 底：`#FFFDF7` 或 `#F8E000`<br>卡：`#FFFFFF`<br>字：`#000000` / `#222222` / `#555555` | `#FF433D` / `#5200FF` 高饱和撞色块 | 边框：`2.5px solid #000000`<br>硬偏移阴影：`4px 4px 0 #000000`（零模糊） | 卡片 `0px`–`4px`<br>按钮 `4px` | `Space Grotesk` / `Archivo Black` `800`<br>字阶：`36/22/15/12px`<br>内边距：`16–24px`，间距 `12/16px` | `Neo-brutalist UI, thick 2.5px solid #000 borders, hard 4px offset drop shadows without blur, high-saturation color blocks, bold display type` |

#### 国内风格可执行参数字典（`CN-01`～`CN-08`）

| 编号 | 底色 / 卡片 / 字色阶梯（主·次·弱） | 默认主色参考（可被品牌色覆盖） | 边框 / 阴影 / 模糊参数 | 圆角阶梯（卡片 / 按钮控件） | 字族 / 字阶（H1·H2·正文·辅助） / 间距 | Figma / 代码 / 生图专用 Prompt 片段 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CN-01`<br>大厂标准蓝白效率风 | 底：`#F7F8FA`（微冷蓝灰）<br>卡：`#FFFFFF`<br>字：`#1D2129` / `#4E5969` / `#86909C` | `#1677FF` / `#3370FF`（科技蓝纯色） | 边框：`1px solid #E5E6EB`<br>阴影：`0 2px 8px rgba(0,0,0,0.04)`<br>模糊：无 | 卡片 `8px`<br>按钮/输入 `6px` | `PingFang SC` / `HarmonyOS Sans`<br>字阶：`20/16/14/12px`（表头/标题 `500/600`）<br>内边距：`16–20px`，间距 `8/12/16px` | `Enterprise clean blue-and-white workbench UI, #F7F8FA cool-grey canvas, #1677FF primary, structured 8px white cards, high information clarity` |
| `CN-02`<br>新中产生活杂志风 | 底：`#F8F8F8` 或 `#FFFFFF`<br>卡：`#FFFFFF`<br>字：`#111111` / `#666666` / `#999999` | `#FF2442` 或克制黑金/青灰点缀 | 弱化分割线，无框或极淡底色差 `0 2px 12px rgba(0,0,0,0.03)` | 卡片 `12px`<br>按钮胶囊 `999px` | `PingFang SC`<br>字阶：`22/17/15/12px`（标题 `600` 精炼，行高 `1.5`）<br>内边距：`12–16px`，间距 `8/12px` | `Modern Chinese lifestyle magazine feed UI, clean 12px white cards, high-ratio photography, refined pill tags, airy spacing` |
| `CN-03`<br>克制专业金融风 | 底：上深 `#0F2942` + 下浅 `#F5F7FA`<br>卡：`#FFFFFF` / 黑金卡 `#1A2233`<br>字：`#141E28` / `#5A6675` / `#8C97A6` | `#0F2942`（深海藏青）或 `#165DFF` + 香槟金 `#D4AF37` | 边框：`1px solid #E8EDF3`<br>阴影：`0 4px 16px rgba(15,41,66,0.06)`<br>模糊：无 | 卡片 `8px`–`10px`<br>按钮 `8px` | `PingFang SC` + 金额/收益率强制 `DIN Alternate` / `tabular-nums` `700`<br>字阶：`26(金额)/18/14/12px`<br>内边距：`16–20px`，间距 `10/12px` | `Trustworthy wealth management & banking UI, deep navy #0F2942 and champagne gold #D4AF37 header card, crisp white data cards, bold DIN tabular numbers` |
| `CN-04`<br>国民级轻快小程序风 | 底：`#F5F5F5`<br>卡：`#FFFFFF`<br>字：`#191919` / `#576B95`(链接) / `#888888` | `#07C160`（微信绿）或品牌高明度主色 | 无多余描边，浅灰底托纯白模块，底部固定操作栏 `0 -2px 10px rgba(0,0,0,0.04)` | 卡片 `10px`–`12px`<br>按钮 `8px` 或胶囊 `999px` | `PingFang SC`<br>字阶：`20/17/15/12px`（主按钮 `16px` `600`）<br>内边距：`12–16px`，间距 `8/12px` | `Lightweight WeChat Mini-Program native style, #F5F5F5 background with clean 12px white rounded cards, prominent single bottom CTA, zero friction` |
| `CN-05`<br>高能量大促导购风 | 底：`#F4F4F4`（局部深暖红头）<br>卡：`#FFFFFF`<br>字：`#111111` / `#666666` / `#FF5000`(价格) | `#FF5000` / `#E1251B`（暖橙红渐变 `#FF7A00 -> #FF2A00`） | 价格/券标签高对比描边 `1px solid #FFD6CC`，宫格紧凑无阴影 | 卡片 `12px`<br>按钮胶囊 `999px` | `PingFang SC` + 价格超大 `DIN` `700`<br>字阶：`28(到手价)/16/13/11px`<br>内边距：`10–12px`，间距 `6/8px`（紧凑） | `High-conversion e-commerce promotional UI, warm orange-red gradient (#FF7A00 to #FF2A00) CTA, bold DIN price callouts, compact grid entry, clear coupon badges` |
| `CN-06`<br>东方新中式雅致风 | 底：`#F7F4ED`（宣纸米白）<br>卡：`#FCFBF7`<br>字：`#2B2B28` / `#6E6A63` / `#9E988E` | `#2F4F4F`（黛青）/ `#5B7A57`（竹青）/ `#9E2A2B`（朱砂点缀） | 边框：`1px solid #DED6C6` 细线框，留白充足，禁用刺眼荧光色 | 卡片 `4px`–`6px`（内敛微圆角）<br>按钮 `4px` | 标题人文宋体/衬线 `600`，正文清秀黑体<br>字阶：`24/18/15/12px`（行高 `1.6`）<br>内边距：`20–24px`，间距 `16/20px` | `Modern Oriental neo-Chinese aesthetic UI, warm Xuan-paper #F7F4ED background, muted slate-green and cinnabar accents, 1px #DED6C6 border, serif headlines, poetic whitespace` |
| `CN-07`<br>Z 世代机能潮酷风 | 底：`#0B0C10`<br>卡：`#161821`<br>字：`#FFFFFF` / `#A0A6B8` / `#CCFF00` | `#CCFF00`（酸性荧光绿）或 `#7000FF -> #00F0FF` 高亮渐变 | 金属/玻璃边框 `1px solid rgba(204,255,0,0.35)`<br>微光：`0 0 16px rgba(204,255,0,0.2)` | 卡片 `4px` 或斜切角<br>按钮 `4px` 或胶囊 | 粗黑体 / 几何宽体 `800` + 等宽机能标签<br>字阶：`28/20/14/11px`<br>内边距：`16px`，间距 `10/12px` | `Gen-Z cyber street-culture UI, pitch dark #0B0C10 background, acid neon lime #CCFF00 accent, metallic glass badges, kinetic bold typography` |
| `CN-08`<br>适老/大众普惠大字风 | 底：`#F5F5F5`<br>卡：`#FFFFFF`<br>字：`#000000` / `#333333`（禁用浅灰字） | `#D93025` 或 `#0066CC`（高纯度正色实心主按钮） | 边框：`1.5px solid #CCCCCC`<br>对比度强制 $\ge 7:1$（AAA 级） | 卡片 `12px`<br>按钮 `10px`（高度 $\ge 52\text{px}$） | `PingFang SC` 全站放大 1–2 档<br>字阶：`26/22/18/16px`（正文 $\ge 18\text{px}$ `500`，标题 `700`）<br>内边距：`16–20px`，间距 `12/16px` | `Senior-friendly high-visibility accessible UI, extra-large 18px+ body text, 52px+ tall solid buttons, explicit Chinese text labels under every icon, ultra-high AAA contrast` |

#### 游戏与互动娱乐 UI 可执行参数字典（`GAME-01`～`GAME-10`）

| 编号 | 底色 / 面板表面色 / 字色阶梯 | 默认主色与能量色参考 | 边框 / 材质高光 / 阴影参数 | 圆角与异形切角阶梯 | 字族 / 字阶 / 排版特征 | Figma / 代码 / 生图专用 Prompt 片段 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GAME-01`<br>暴雪史诗暗黑重拟物风 | 底：`#0D0A08`（暗黑岩石）<br>面：`#1C1613`（黑铁/羊皮卷 `#D8C39E`）<br>字：`#F3E5AB`（古金白） / `#B8A68E` / `#7A6A58` | 传奇橙 `#FF8000` / 奥术紫 `#A335EE` / 血红 `#9E1B1B`（内发光宝石按钮） | 边框：`2px solid #8C6D3F`（锻造黄铜渐变框）<br>内发光：`inset 0 1px 0 rgba(255,230,160,0.45)`<br>重浮雕阴影：`0 8px 24px rgba(0,0,0,0.85)` | 卡片 `2px`–`4px`（带金属包角装饰）<br>按钮 `4px` 斜面浮雕 | `Cinzel` / `Friz Quadrata` / 力量感衬线粗体 `700`<br>字阶：`32/22/15/12px`（标题带 `0 2px 4px #000` 文字投影） | `Blizzard dark fantasy RPG UI, forged aged brass & stone frame, glowing gemstone CTA button, deep bevel embossing, Cinzel serif gold-leaf typography, Diablo/Warcraft HUD aesthetic` |
| `GAME-02`<br>Supercell 高饱和立体卡通风 | 底：`#1E5799`（皇室蓝底）或 `#2C3E50`<br>面：`#F4F6F9` 或木板/石砖色<br>字：`#FFFFFF`（必带 2px 纯黑外描边） / `#FFE600` | 对战亮黄 `#FFCC00 -> #FF9900` / 宝石绿 `#38E54D` / 史诗紫 `#B537F2` | 边框：`2.5px solid #000000`（纯黑粗描边）<br>顶高光：`inset 0 3px 0 rgba(255,255,255,0.65)`<br>厚底硬阴影：`0 6px 0 #995500, 0 8px 12px rgba(0,0,0,0.45)` | 卡片 `16px`–`20px`<br>按钮 `14px`（按下时 `translateY(4px)` 压缩底阴影） | `Supercell-Magic` / `Lilita One` / `Luckiest Guy` / 超粗圆体 `900`<br>字阶：`30/22/16/13px`（微倾斜 `-3deg` + 黑描边） | `Supercell Clash Royale tactile cartoon game UI, vibrant glossy 3D button with top white highlight bar, thick black outline, 6px solid bottom press shadow, chunky tilted outlined typography` |
| `GAME-03`<br>腾讯大众竞技鎏金流光风 | 底：`#0A1324`（深海夜空蓝）<br>面：`rgba(16,28,52,0.82)` 半透明磨砂<br>字：`#F7E6C4`（香槟亮金） / `#D0DDF0` / `#6C84A6` | 荣耀灿金渐变 `#F5D08A -> #C49346` + 竞技青蓝 `#00E5FF` | 边框：`1.5px solid #C89D54`（45° 斜切双层金属线）<br>流光：`0 0 18px rgba(245,208,138,0.35)`<br>模糊：`blur(12px)` | `clip-path` 45° 斜切角（Chamfer `8px–12px`）或 `2px` 锐角 | 锐利斜体粗黑 / `剑体` + `DINPro-Bold` 战绩数字<br>字阶：`28/20/14/12px`（字重 `700/800`） | `Honor of Kings competitive MOBA game lobby UI, deep navy translucent HUD with 45-degree chamfered metallic gold borders, cyan energy glow, sharp italic bold Chinese typography, esports crest` |
| `GAME-04`<br>网易哥特悬疑手绘拼贴风 | 底：`#1A1615`（暗夜煤黑）<br>面：`#D8CBB8`（做旧羊皮档案纸）<br>字：`#241C18`（墨迹黑） / `#5E4B3E` / `#8C1D1D`（暗血红） | 火漆暗红 `#8C1D1D` / 古董铜 `#9C7A44` | 边框：手绘不规则双墨线 `2px dashed/solid #2B221E` + 撕纸锯齿边缘<br>阴影：`4px 6px 14px rgba(0,0,0,0.65)`（交叉排线暗影感） | 不规则手绘微折角 `2px` + 纽扣/回形针/火漆印章角标 | 哥特衬线 / 打字机字体 `Special Elite` / `Playfair Display` + 手写批注字<br>字阶：`28/20/15/12px` | `Identity V gothic vintage detective game UI, distressed parchment paper dossier, hand-drawn crosshatch ink lines, wax seal & button fasteners, eerie serif & typewriter typography` |
| `GAME-05`<br>叠纸浪漫轻奢乙游/换装风 | 底：`#F8F4F9` 或星夜紫蓝 `#161426`<br>面：`rgba(255,255,255,0.68)`（珠光毛玻璃）<br>字：`#2E2532` / `#7A6B82` / `#B5A3BE` | 玫瑰香槟金 `#E5C1BD -> #C99E9A` / 星光银白 `#F0EBF8` | 边框：`0.8px solid rgba(229,193,189,0.75)`（细金线 + 四角十字星芒 `✦`）<br>模糊：`backdrop-filter: blur(24px)`<br>柔光：`0 8px 32px rgba(180,140,190,0.18)` | 卡片 `12px` 或优雅菱形/拱形切角<br>按钮胶囊 `999px` | 纤细高反差衬线 `Cormorant Garamond` / `Didot` / `方正清刻本悦宋` `500` + 细黑体<br>字阶：`26/18/14/11px`（宽字距 `+0.08em`） | `Papergames Love and Deepspace / Shining Nikki otome luxury game UI, pearlescent frosted glass panel, ultra-thin rose-gold hairline frame with 4-point star sparkles, dreamy aurora bokeh, elegant serif` |
| `GAME-06`<br>网易新国风仙侠水墨丹青风 | 底：`#ECE6DA`（宣纸水墨底）或玄黑 `#141619`<br>面：`rgba(247,244,237,0.85)` 纱感面板<br>字：`#1F1E1B`（徽墨） / `#5C574F` / `#9E2A2B` | 鎏金 `#C89B57` + 朱砂印章红 `#B82923` + 青绿山水 `#3B6E6C` | 边框：`1px solid #C89B57`（内嵌中式回纹/云雷纹细角花）<br>阴影：水墨晕染淡影 `0 6px 20px rgba(31,30,27,0.12)` | 卡片 `4px` 中式折角 / 海棠角<br>按钮卷轴或玉佩胶囊形 | 苍劲毛笔书法标题 + `思源宋体` / `方正宋刻` 正文<br>字阶：`30/20/15/12px`（支持局部竖排点缀与朱文印章） | `Oriental Xianxia ink-and-gold game UI (Justice Online / Onmyoji style), Xuan paper & mist wash surface, delicate gold cloud-fretwork corners, cinnabar red seal stamp, calligraphy title` |
| `GAME-07`<br>二次元轻机能扁平潮酷风 | 底：`#121316` 或冷灰白 `#ECEFF4`<br>面：`rgba(24,26,32,0.88)` 极薄战术面板<br>字：`#FFFFFF` / `#9AA4B2` / `#FFE600` | 机能明黄 `#FFE600` 或星铁青蓝 `#00D2FF` / 活力橙 `#FF6B00` | 边框：`1px solid rgba(255,255,255,0.15)` + 局部 `3px` 高亮色块条与十字准星 `+` 装饰 | 卡片 `2px` 结合单侧 45° 斜切角<br>按钮硬朗斜切矩形 | 几何无衬线粗体 `HarmonyOS Sans` / `Rajdhani` / `DIN` `700` + 微缩 `8px` 英文机能编号 | `Hoyoverse / Arknights anime sci-fi tactical flat UI, sleek dark translucent HUD, sharp geometric diagonal cut corners, bright yellow/cyan accent bar, micro-tech typography & crosshair decals` |
| `GAME-08`<br>复古像素 / 独立街机风 | 底：`#1A1C2C`（PICO-8 深紫蓝）<br>面：`#333C57` 或像素木框 `#8F563B`<br>字：`#F4F4F4` / `#94B0C2` / `#FFCD75` | 街机红 `#E43B44` / 像素金 `#FEAE34` / 能量绿 `#38B764` | 边框：`4px` 阶梯状像素边框（`box-shadow` 阶梯拼合，零模糊）<br>硬阴影：`4px 4px 0 #0F101A` | `0px` 纯直角像素阶梯切角（严禁平滑圆角与抗锯齿模糊） | 点阵像素字体 `Press Start 2P` / `Zpix (最像素)` / `VT323`<br>字阶：`24/16/12/8px`（严格按 `8px` 整数倍缩放） | `Retro 16-bit pixel art indie game UI (Stardew Valley / Balatro style), crisp pixelated stepped frame, zero anti-aliasing blur, 8-bit bitmap font, tactile arcade button with hard pixel shadow` |
| `GAME-09`<br>棋牌桌游绿毡奢金拟物风 | 底：径向渐变祖母绿台呢 `#0F5132 -> #072B1A`（或深蓝天鹅绒 `#0C2340`）<br>牌面：`#FFFFFF`（纯白高对比）<br>字：`#FFF8E7` / `#FFD700`(筹码金) / 牌面红 `#D92626`·黑 `#1A1A1A` | 出牌/加注亮橙黄 `#FFB800 -> #E67E00` + 跟注/提示翠绿 `#2ECC71` + 不要/弃牌冷蓝灰 `#4A6572` | 桌沿：`6px` 深胡桃木 `#3E2723` 配 `1.5px` 香槟金内嵌线 `#D4AF37`<br>牌阴：`0 4px 10px rgba(0,0,0,0.45)`<br>按钮高光：`inset 0 2px 0 rgba(255,255,255,0.5)` | 扑克牌 `6px`–`8px` 标准圆角<br>操作按钮胶囊 `999px`（高 $\ge 48\text{px}$ 防误触） | 扑克角标大号高辨识度粗体 `DIN` / `Roboto Condensed Bold` `800`（左上角标紧凑放大，支持单手扇形叠牌识别） | `Texas Hold'em Poker & Guandan card table UI, radial emerald green felt cloth background with mahogany & gold trim rail, crisp white playing cards with oversized corner indices, 3D casino chips, glossy pill action buttons` |
| `GAME-10`<br>大富翁 / 派对棋盘 3D 糖果富豪风 | 底：明亮天蓝/薄荷绿环绕 `#E0F7FA` + 奶油白棋盘格 `#FFFDF9`<br>面：`#FFFFFF` 配彩色地产色带顶栏<br>字：`#FFFFFF`（带深色描边） / `#2D3436` / `#00B894`(钞票绿) | 富豪金 `#FFD700 -> #FFA502` + 钞票翠绿 `#00C853` + 大亨红 `#FF3838` | 边框：`2px solid #FFFFFF` 内高光 + 饱满 3D 膨胀果冻漆面光泽<br>投骰主按钮底阴影：`0 8px 0 #C23616, 0 12px 20px rgba(0,0,0,0.3)` | 棋盘格 `10px`<br>弹窗 `24px` 大圆角（带拱形丝带横幅头）<br>投骰主按钮超大圆弧/正圆 | `Fredoka` / `Baloo 2` / 圆润胖体字 `800` + 超大立体金币数字<br>字阶：`32/22/16/13px` | `Monopoly GO! & Richman 3D board game UI, isometric colorful property tiles, glossy candy-coated 3D dice roll centerpiece button, floating cash & gold coin counters, festive ribbon banner modal` |

#### 通用质感手法叠加参数（`TEX-01`～`TEX-06`）

- `TEX-01 极简扁平`：移除投影与模糊，使用 `1px` 实线或纯底色差区分层级。
- `TEX-02 毛玻璃通透`：浮层/卡片使用 `background: rgba(255,255,255,0.72)`（暗色 `rgba(20,22,30,0.68)`）+ `backdrop-filter: blur(20px)` + `1px solid rgba(255,255,255,0.35)` 高光边。
- `TEX-03 Bento 便当盒分块`：容器统一 `12px–16px` 圆角、固定网格间距 `12px` 或 `16px`，模块按 `1x1 / 2x1 / 2x2` 严密拼合。
- `TEX-04 轻质感微立体`：卡片表面微渐变 + 双层柔光阴影 `0 8px 24px rgba(0,0,0,0.06), inset 0 1px 0 rgba(255,255,255,0.8)`。
- `TEX-05 弥散光氛围`：底层铺 `filter: blur(60px)` 低透明度双色/三色径向渐变光斑（透明度 `12%–22%`），不干扰上层文字对比度。
- `TEX-06 杂志感大字报`：主标题字号拉大至正文的 `2.5x–3.5x`，去掉多余卡片外框，用 `1px` 细横线与大留白切分章节。

**产出**：`V0 视觉方向与 6 维决策卡`（选定风格编号、预设参数包、6 维确认值、排除项及核心代表页范围），作为 V1–V6 及下游工具调用的直接输入。  
**完成证据**：候选方向经过语境与行业严肃度剪枝；主色纯色/渐变、底色、容器、圆角、字体密度、图标风格 6 项均已明确，且已映射为具体可执行数值与专用 Prompt 片段。  
**不得替代**：不能跳过 U1–U4 直接在结构未定时选风格。

## V1 视觉依据

**触发问题**：本次视觉决定依据什么？  
**最低输入**：设计系统、正式主稿、品牌材料、用户委托或允许探索的范围。  
**跳过**：任务不包含视觉。

**步骤**

1. 为每项来源记录来源 ID、类型、所有者、准确文件或节点、版本或日期、适用范围及状态；优先引用正式设计系统或主稿。
2. 写清哪些值已锁定、哪些允许探索、哪些不得改变，以及谁有权确认。
3. 无基线时记录用户委托及可追溯依据。仍有重大取舍时只生成同结构候选，并标为 `CANDIDATE_PENDING_CONFIRMATION`；连候选依据也不存在时请求输入并阻断，不任意设定品牌值。
4. 区分参考文件和可编辑目标，记录目标版本、允许修改范围和验收对象。
5. 真实资产缺失时停止相关视觉制作并请求资产，不用占位、近似或简化替代后称完成。

**产出**：视觉依据卡。  
**完成证据**：每项实现值都能回到正式来源、系统引用或待确认候选；允许范围、确认人和阻断项明确。  
**不得替代**：用“类似品牌风格”伪造规范。

## V2 语义色

**触发问题**：颜色如何表达行动和状态？  
**最低输入**：主行动、文字层级和状态列表。  
**跳过**：已有 token 且只需忠实应用。

**步骤**

1. 先列出主行动、主/次文字、链接、边框、焦点、选择、成功、警告、错误、禁用和各层背景表面的语义角色，再考虑氛围色。氛围不得降低主行动、状态或关键文本的辨识度。
2. 每个 token 必须形成以下实现记录；不适用的状态也要写 `N/A` 及理由：

```text
Token ID：
语义角色：
用途及对应对象：
来源：来源 ID / 版本 / 变量、样式或节点路径
值状态：CONFIRMED / CANDIDATE_PENDING_CONFIRMATION / MISSING / BLOCKED
实际值或正式系统引用：
前景对象及 token：
背景或表面及 token：
状态映射：
- default：
- hover：
- pressed：
- focus：含焦点指示器、粗细和偏移所用 token
- disabled：
对比验证：
- 采用标准、级别、阈值及来源：
- 各状态 × 主题 × 表面的前景/背景实际值、实测比值、工具或方法：
- 结果：PASS / FAIL / NOT_TESTED / NOT_APPLICABLE
非颜色辅助：文字、图标、形状、边框、位置、纹理或其他线索
亮色 / 暗色 / 其他表面映射：
适用范围：页面 / 组件 / 平台 / 主题 / 表面 / 状态 / 版本
责任人及确认人：
```

3. 有正式系统时引用准确 token 路径和版本，不把当前渲染值抄成新的品牌规范；正式系统未覆盖的状态标缺口。
4. 无基线时，先回到 V1 取得明确委托、批准参考或可验证约束，再产出同语义结构的候选 token 组。所有候选实际值均标 `CANDIDATE_PENDING_CONFIRMATION`；没有任何依据时不得凭空选色。
5. 对每个实际使用的前景/背景组合，覆盖 default、hover、pressed、focus、disabled 以及亮暗主题和多层表面，记录实测对比结果。只目测或只测一个背景不能写通过。
6. 成功、警告、错误、选择、焦点和禁用等关键含义必须同时定义非颜色辅助；只换颜色不算完整状态。
7. 若同一 token 在不同主题或表面映射到不同值，逐项记录映射、继承关系和作用域，不允许实现者自行推断。

**产出**：实现级语义色 token 记录、状态映射和对比验证记录。  
**完成证据**：每个已使用 token 有来源或候选状态、实际值或系统引用、完整状态、前景/背景、主题与表面映射、适用范围和实测结果；关键状态不只靠颜色。  
**不得替代**：品牌色规范和无障碍实测。

## V3 字体与密度

**触发问题**：字体和密度是否匹配任务并保持信息层级？  
**最低输入**：UI 层级、内容长度、使用场景。  
**跳过**：字体和密度由正式系统锁定。

**步骤**

1. 沿用正式字族、fallback、字体文件和版本；记录授权或系统可用性。无正式系统时，只有在明确委托或可追溯依据下才能提出候选，不能把默认选择写成品牌字体。
2. 每个排版角色形成以下实现记录：

```text
Typography Token ID：
角色及用途：
字族与 fallback：
字族来源、文件或系统引用、版本及授权状态：
字号：
行高：
字重：
字距：
最大行宽或文本容器限制：
各实际值的来源或系统引用：
值状态：CONFIRMED / CANDIDATE_PENDING_CONFIRMATION / MISSING / BLOCKED
适用范围：页面 / 组件 / 平台 / 语言 / 宽度 / 状态 / 版本
```

3. 每种密度模式形成 spacing token 记录，写明 token ID、实际值或系统引用、来源、组件内边距、组内间距、组间间距、布局沟槽、触控或点击区域及适用范围。操作密集任务可减少装饰并保持组内紧凑，浏览任务可增加留白和图像，但两者都不能改变已确认的信息和行动层级。
4. 所有字号、行高、字重、字距、行宽和 spacing 实际值都必须来自正式系统或准确来源；探索值必须逐项标为候选并等待确认，不能凭经验补成既定规范。
5. 建立内容压力测试记录：使用目标范围内可取得的真实最长标题、正文、标签、按钮、数字、日期和错误信息，记录内容 ID、来源、语言、字符或词数、页面、组件和状态。真实最长内容缺失时标 `MISSING`，不能用短假文案宣称已通过。
6. 在最窄受支持视口或容器宽度检查换行、截断、溢出、层级、点击区域和相邻组件，记录准确宽度、页面、状态、截图或检查结果及修复去向。
7. 对所有目标语言逐项检查字形覆盖、fallback、字重可用性、断行、标点、数字格式、文本扩张、从右到左方向及混排中实际适用的项目；没有覆盖的语言标 `NOT_TESTED`，不能泛称“多语言通过”。

**产出**：实现级排版 token、密度与 spacing token、真实内容压力测试记录。  
**完成证据**：字族、角色、字号、行高、字重、字距、行宽和间距均有来源、系统引用或候选状态；真实最长内容、窄宽和全部目标语言有可追溯检查结果，次要信息不压过主任务。  
**不得替代**：UI 信息层级。

## V4 气质句

**触发问题**：视觉气质如何变成可执行约束？  
**最低输入**：品牌目标、使用情境或明确委托。  
**跳过**：只做严格还原。

写：`气质 = 两个可观察特征；不做 = 三条具体禁令；来源 = 准确材料或委托；范围 = 页面 / 组件 / 平台 / 版本。`  
禁用“高级、国际化、有灵魂”等无法验收的词。
无正式品牌依据时只能写待确认候选，不把气质推导成未经确认的颜色、字体或资产值。

**产出**：气质与禁令。  
**完成证据**：第三人可以据此判断符合/不符合。  
**不得替代**：完整品牌战略。

## V5 图标与图片

**触发问题**：图像资产是否帮助识别、内容或信任？  
**最低输入**：内容职责、真实资产或资产要求。  
**跳过**：无图任务。

**步骤**

1. 按代表页面和状态枚举所有图标、标志、照片、插画及其他必需视觉资产；图标不承担唯一信息，一套内的网格、尺寸、描边、端点和填充规则保持来源一致。
2. 每项资产建立以下 manifest，禁止用笼统“后补图片”代替：

```text
资产 ID：
资产类型：
用途及出现位置：
来源及授权：创建者 / 提供方 / 链接或库 / 许可范围 / 到期或限制
文件及版本：准确文件名或路径 / 格式 / 版本或日期 / 变体
尺寸与比例：源尺寸 / 目标尺寸或密度 / 宽高比
裁切规则：焦点 / 安全区 / 各断点裁切或禁止裁切
真实内容要求：必须呈现的对象、地点、产品、语言、数据或状态；不得出现什么
当前状态：APPROVED / AVAILABLE_UNVERIFIED / NEEDS_EXPORT / NEEDS_LICENSE / MISSING / BLOCKED
责任人：
缺失阻断：受影响页面或组件 / 被阻断产物 / 所需输入 / 恢复条件
```

3. 图片必须与任务相关，并满足 manifest 中的真实内容要求；真实内容、授权、文件版本或裁切信息不足时，受影响成品保持阻断。
4. 将实际装载文件与 manifest 的文件、版本、尺寸比例和裁切逐项对照；错版本、低清导出、错误比例或未经授权的替代均不得通过。
5. 缺资产时请求准确导出或授权，不随机寻找相似素材，不使用占位、表情、假内容或简化图形冒充成品。
6. **IconScout 双通道真实资产调取（优先官方 MCP `https://mcp.iconscout.com/mcp` + 内置 v3 API 脚本自动兜底，用于 `icon` 图标、`3d` 图标、`lottie` 动画、`illustration` 插画）**：
   - 当项目中需要工具图标、金刚区 3D 图标、空状态/引导页插画或 Lottie 微动效且无现成内部资产时，按 **「通道 A（MCP 优先）→ 通道 B（内置 API 脚本零配置兜底）」** 执行：
   - **通道 A｜优先检测并调用 IconScout 官方 MCP Server（支持自然语言搜同系列 Pack、改色与直下 `.svg / .json` 源文件）**：
     1. 先通过 `GetDynamicTools` 检索当前宿主环境是否已连接 `iconscout` MCP。
     2. **已连接**：直接调用 IconScout MCP 工具，支持用自然语言描述风格与色板、拉取同一视觉系列的配套资产（Consistent Pack），并直接按用户账号权限下载 `SVG`、`PNG`、`Lottie JSON`、`GIF` 或 `MP4`。
     3. **未连接**：向用户提示可一键接入官方 MCP（地址：`https://mcp.iconscout.com/mcp`，参考 `https://iconscout.com/mcp`，无需填 API Key，首次浏览器 OAuth 登录即可解锁全库 `SVG / Lottie JSON` 直下）：
        - **Cursor / Claude Desktop / Windsurf (`mcp.json`)**：
          ```json
          {
            "mcpServers": {
              "iconscout": {
                "url": "https://mcp.iconscout.com/mcp"
              }
            }
          }
          ```
        - **Claude Code CLI**：`claude mcp add --transport http iconscout https://mcp.iconscout.com/mcp`
        - **Codex / ChatGPT**：`Settings -> Connectors -> Add custom connector`，填入 `https://mcp.iconscout.com/mcp` 并完成浏览器登录授权。
   - **通道 B｜内置 IconScout v3 REST API 脚本自动兜底（免安装、开箱即用）**：
     - 若用户当前未安装 MCP 或选择本次先不配置，**严禁卡死流程或退回手画劣质 SVG**，立即自动调用本 Skill 预置的 v3 API 脚本（已内置 `Client-ID: 232598791050530`，文档：`https://api-docs.iconscout.com/#description/credits-and-limits`，OpenAPI：`https://cdn.iconscout.com/openapi.json`）：
     - **直接调用命令**：`python3 scripts/iconscout.py search -q "<英文关键词>" -a <icon|3d|lottie|illustration> -s <风格> --icon-grid 24 -d <本地保存目录>`（在 `design-thinking-os` Skill 目录下执行）
   - **与 `V0` 第 6 维图标/配图风格的精确参数映射（MCP 与 API 通用）**：

| `V0` 选定的图标/配图类型 | IconScout `asset` 参数 | IconScout `styles[]` 过滤参数 | 附加参数与一致性要求 |
| :--- | :--- | :--- | :--- |
| **人物头像 / 用户形象（Avatar）** | **禁用 `3d` 搜通用 `avatar`！**<br>仅限 `illustration` 同 Pack 或走 AI 同母体生图 / 矢量纹章 | 若用插画头像仅限 `flat / dualtone` 同系列 Pack | **严禁从 IconScout `3d` 拉取欧美豆豆眼橡皮泥人头（带黑底、呆滞丑陋）**！游戏/C端头像必须走统一风格高颜值生图（潮玩手办/国风厚涂/真实写真）或精致矢量纹章，且入稿前必过 `Read` 读图审美筛查 |
| 精致细线性图标（1.5–2px） | `icon` | `line` 或 `rounded` | `--icon-grid 24`，全套保持同一 `styles[]` 或同一 Pack |
| 醒目面性 / 填充图标 | `icon` | `glyph` 或 `flat` | `--icon-grid 24`，用于选中态或高权重入口 |
| 双色 / 线面结合图标 | `icon` | `dualtone` 或 `colored-outline` | `--icon-grid 24`，金融/生活服务金刚区常用 |
| 微质感 / 渐变图标 | `icon` | `gradient` | 适合核心宫格入口提亮品质 |
| 3D 质感图标 / 海报主视觉立体物 | `3d` | —（可加 `isometric`） | 获取高清透明底 `PNG`，可直接用于金刚区或**快速拼装海报/主视觉 KV** |
| 扁平现代矢量 / 等轴插画 | `illustration` | `flat` / `dualtone` / `isometric` / `colored-outline` | 用于空状态、引导页、卡片配图或**快速拼装运营海报** |
| 温暖手绘风插画 | `illustration` | `doodle` | 仅限轻松消费/社区场景，严肃行业禁用 |
| 轻量矢量动画 / 微动效 | `lottie` | — | MCP 直接下 `Lottie JSON / GIF / MP4`；API 脚本免密直取预览 `MP4/PNG`（可直接嵌入动态海报或 UI） |

   - **API 通道鉴权与额度边界**：
     - 仅靠预置 `Client-ID: 232598791050530` 即可免费调用 `GET /v3/search` 与 `GET /v3/items/{uuid}`，直接拿回可用的高清 CDN 预览文件（图标 `png_64/128/256`、3D 与插画透明底 `thumb` PNG、Lottie `thumb` MP4 与 `preview_image`）；
     - 若走 API 通道下载源文件（`svg` / `json` / `lottie` / `glb`）、调用格式转换 `POST /v3/convert/{operation}`（如 `svg-to-lottie`、`lottie-to-gif`、`lottie-to-webp`、`lottie-to-mp4`）或 `POST /v3/ai/{operation}`，需同时传入 `Client-Secret`（或直接使用已登录的通道 A 官方 MCP）。
7. **人物头像与角色形象的 4 条审美硬约束（防丑、防欧美塑料泥人、防手搓 SVG 假人、防跨画风乱拼）**：
   - **硬约束 1｜双禁令：严禁 IconScout 通用 3D 泥人头像 + 严禁代码手搓 SVG 简笔人脸**：
     - IconScout 的 `asset=3d` 非常适合拉取 **金币、皇冠、礼盒、奖杯、盾牌、徽章等 3D 道具物件**；但其中的通用 `avatar` 大多是欧美 B 端 SaaS 风格的“豆豆眼、僵硬橡皮泥小人、带纯黑底块”，**严禁不加筛选直接塞进国内 C 端产品或游戏界面**！
     - **同时严禁用 `<svg>` 几何路径手画人物五官头像**（代码手画的 SVG 人脸必然像简陋火柴人/占位符）。
   - **硬约束 2｜按产品品类锁定「头像美学矩阵（Avatar Aesthetic Matrix）」**：
     - 无现成官方头像资产时，**必须调用 AI 生图工具（如宿主 `GenerateImage` 或 Figma `generate_image`）** 按统一风格词生成高颜值真实图像：
     - **游戏 / 棋牌 / 泛娱乐（`GAME-01..10`）**：必须使用 **泡泡玛特（Pop Mart）盲盒潮玩手办风**（灵动大眼、精致高光材质、国潮/赛博/西幻服饰、柔光干净底）或 **高颜值二次元/新国风厚涂半身立绘**；严禁使用欧美办公秃头/大胡子塑料泥人。
     - **国内 C 端社交 / 消费 / 生活方式（`CN-02/04/05/06`）**：使用自然光高颜值生活写真人像或年轻潮流扁平/噪点插画头像。
     - **B 端工作台 / 国际化 SaaS（`INT-01..06` / `CN-01/03`）**：使用专业商务人像或高定首字母几何徽章（Monogram Badge）。
   - **硬约束 3｜同屏多头像「同母体 / 同 Pack 一致性」铁律**：
     - 同一页面出现 $\ge 2$ 个头像（如 4 人牌桌、排行榜、评论流）时，**必须出自同一个视觉系列（走生图时必须使用完全相同的画风前缀词、头肩比例、打光方向与底色体系；走 IconScout MCP 时必须用 `Find related assets` 锁定同一套系 Pack）**，严禁把 4 个不同作者、不同画风、不同头身比的头像拼在同一屏。
   - **硬约束 4｜入稿前强制「先读图审美筛查（Look-Before-Use Gate）」**：
     - Agent 下载或生成任何头像后，**必须先调 `Read` 工具肉眼检查图像**；凡出现以下任一丑点，**立即淘汰重换，严禁入稿**：① 豆豆眼、五官呆滞、比例畸形或手画 SVG 简笔人脸；② 带死板纯黑背景块或抠图黑边；③ 肤色材质发脏暗沉；④ 多人同屏画风割裂。
8. 界面资产在 Figma UI 范围内完成：若需生成界面内配图、背景或插画，可先用 IconScout API 检索真实图标/3D/插画导入 Figma，或按 `V7 路径 A` 由 Codex / Agent 调用 Figma 内置生图在目标图层原位生成；若所需真实资产无法取得且无法在已授权 UI 范围内生成，标 `BLOCKED/WAIT_EXTERNAL` 并请求正式输入，不自动扩成独立视觉工具任务。只有用户明确建立独立视觉成品或资产委托（如海报、运营图、KV）时，才将 manifest 作为 TR4 与 `V7 路径 B` 输入；外部产物验收后记录准确文件与版本，再按需回到 Figma 完成界面内应用。

**产出**：可交付实现的资产 manifest、缺失阻断和恢复清单；若存在明确独立视觉资产委托，附视觉工具动作 ID、已确认文件版本和 Figma 导入位置。  
**完成证据**：每项已用资产都有 ID、用途、来源与授权、准确文件版本、尺寸比例、裁切、真实内容要求、状态和责任人；所有缺失项明确阻断范围，无无关图片、假内容或占位符冒充成品。  
**不得替代**：版权和品牌授权。

## V6 同结构候选

**触发问题**：没有既定基线且确实需要人做视觉方向选择。  
**最低输入**：已确认的同一内容、结构、状态和代表页面。  
**跳过**：已有设计系统、存量迭代沿用基线、或用户已明确委托方向。

**步骤**

1. 每轮先冻结内容、信息层级、结构、行为、资产、数据、平台、视口、页面状态及不在本轮比较的 token，并记录准确版本。
2. 每条比较记录只能有一个唯一变化变量；为该变量提供 2–3 个有依据且标为待确认的候选值。若需比较另一个变量，另开一轮并重新冻结基线。
3. 使用关键任务的代表页面及实际相关状态，至少覆盖正常状态和会暴露差异的 hover、pressed、focus、disabled、空、错误或长内容状态；不用闪屏或纯情绪板代替。
4. 在同一设备、视口、内容、状态和资产条件下，比较主行动可见性、关键判断、状态辨识、对比、内容承载和品牌边界，并保留结果证据。
5. 每轮填写：

```text
比较 ID 及待回答问题：
固定变量及准确版本：
唯一变化变量：
候选 ID、值、依据和状态：
代表页面、视口及状态：
比较标准：
逐候选比较结果及证据：
结论：推荐 / 不推荐 / 无结论
确认人及其权限：
当前状态：DRAFT / READY_FOR_REVIEW / PENDING_CONFIRMATION / CONFIRMED / REJECTED / NO_CONCLUSION / BLOCKED
选择来源、适用范围及可吸收部分：
```

6. 未经有权的人确认，结果保持 `PENDING_CONFIRMATION`。如果一轮同时改变了多个变量，该轮不能把结果归因到任何一个变量，也不能据此确认 token；必须拆分并重做单变量比较。

**产出**：每轮 2–3 个同结构、单变量真实候选及完整比较记录。  
**完成证据**：固定变量、唯一变化变量、代表页面与状态、比较结果、确认人和当前状态完整；候选差异可解释，未确认前不称确认。  
**不得替代**：用三套结构不同的方案假装视觉比较。

## V7 视觉素材拼装与图片生成双路径协议（优先 IconScout 素材快拼 vs Figma 原位生图 / 海报双垫生图）

**触发问题**：当任务需要人物头像、图标、3D 元素、插画、UI 配图，或需要制作独立运营图/海报/主视觉（KV）时，何时直接从 IconScout 拉素材快速拼装，何时才调 AI 生图模型？  
**最低输入**：视觉用途（UI 内部元素 vs 独立海报/主视觉交付）、核心传达信息与尺寸比例。  
**跳过**：纯文字/纯组件界面且无任何图标、头像、图片或海报需求。

> **核心选型铁律（能用现成透明底高品质素材快拼，就不盲目跑整图 AI 生图）**：
> 1. **人物头像（User Avatar）、工具/装饰图标（Icon）、3D 立体图标（3D）、标准场景插画（Illustration）、轻量动画（Lottie）**：**第一优先级一律从 IconScout（官方 MCP 或 `scripts/iconscout.py`）检索拉取**，严禁手画 SVG 人脸或动辄跑大模型整图生成。
> 2. **快捷生成海报 / 主视觉（KV） / 运营 Banner**：先评估能否用 **「清晰版式底板（渐变/网格/色块）+ 真实矢量文字 + IconScout 透明底 3D/插画/头像素材拼装」** 直接完成。能拼装的优先走快捷拼装（文字 100% 清晰、元素可独立微调、零 AI 乱码假字）；只有需要全画幅写实摄影或复杂光影一体融合时，才走整图 AI 生图。

### 路径 A：UI 界面内头像 / 图标 / 配图 / 背景（优先 IconScout 拉取 + Figma 原位生图补充）

适用：元素是 UI 页面的一部分，服务于用户资料、金刚区入口、卡片、Banner 位、头部背景或空状态。

1. **优先按品类正确获取高颜值头像与 IconScout 透明底道具/图标**：
   - **人物头像（严禁拉取 IconScout 欧美 3D 橡皮泥人头）**：游戏/C端人物头像优先使用统一风格模板生成高颜值同套系头像（泡泡玛特盲盒潮玩风 / 国风二次元厚涂立绘 / 自然光写真），或采用与牌桌/界面同频的精致高定矢量徽章；严禁调用 IconScout `3d` 搜 `avatar` 拿豆豆眼黑底塑料人充数！
   - **图标 / 金刚区 3D 道具（金币/皇冠/礼盒/奖杯） / 空状态插画**：按 `V5` 映射表从 IconScout 拉取同系列素材导入 Figma。
2. **Figma 原位调用 AI 生图（仅当需要特定写实摄影或定制氛围背景，且 IconScout 无匹配现成素材时）**：
   - 直接读取当前 Figma 目标图层的宽高比、已确认的 `V0` UI 风格、主色与冷暖色调；
   - 优先通过 Figma MCP 原生生图接口（如 `generate_image` 直接传入目标 `fileKey` 与 `nodeId` 替换图层填充，或调用 Figma Weave 生图模型），或由 Codex / Agent 通过 GUI 操作调用 Figma 内置生图插件，在目标 Frame 图层内原位生成。

### 路径 B：独立海报 / 运营图 / 主视觉 KV（先定结构草图 → 优先 IconScout 素材快拼，或走双垫 AI 生图）

适用：最终交付物本身是一张运营图、活动海报、宣发主视觉（KV）或社媒配图。**严禁跳过版面结构分析直接写一段提示词盲目生图。**

#### Step 1：先判断图文角色与占比（谁是主角？）

根据这张运营图要传达的核心信息，先定 3 种角色模式之一：

- **模式 A｜画面主导型（图占 70%–90%）**：靠视觉冲击、产品特写或氛围吸引点击（如新品首发、穿搭/美食/旅行大图）。图片占绝对主体，文字浓缩为极简标题嵌入留白区。
- **模式 B｜标题/信息主导型（字占 50%–70%，图只做装饰或局部点缀）**：大促折扣、核心利益点喊话、规则通知、战报。主标题和利益点必须极大极醒目（并同步确定标题造型：超大强对比色块字 / 3D 立体膨胀字 / 金属质感字 / 手写书法字）；图片只做角落装饰、底纹或小主体，严禁抢夺标题注意力。
- **模式 C｜图文均衡型（图 50% + 字 50% 分区）**：活动宣发、课程/沙龙海报、功能介绍卡。采用上下分割、左右分割或中心构图，图文各守一区、互不遮挡。

#### Step 2：画出「海报版面结构草图（Layout Sketch）」并选择制作方式（快拼 vs 整图 AI 生图）

先根据 Step 1 产出一张可视化的 **结构草图**（可用 HTML/SVG/Figma 快速排出并导出为 `layout_sketch.png`），明确标出 `L1 主标题 / L2 副标题利益点 / L3 时间地点规则 / L4 品牌 Logo 与行动区` 的字号比例、位置和配图区域，然后**二选一决定制作方式**：

- **制作方式 1｜IconScout 素材快捷拼装模式（默认优先推荐：适合模式 B / 模式 C、功能发布 KV、嘉宾/人物海报、常规运营 Banner）**
  - **为什么优先**：不需要整张图跑 AI 生图！文字 100% 矢量锐利无乱码，每个元素位置大小随时可改，出图极快。
  - **怎么拼装**：
    1. 在 Figma 或 HTML/CSS 画布中，按 `V0` 风格参数搭好背景底板（纯色、弥散光晕渐变、Bento 色块或几何网格线）并排好 L1–L4 真实文字层级；
    2. 调用 IconScout（MCP 或 `scripts/iconscout.py`）检索拉取高清透明底的 **主视觉 3D 模型（`--asset 3d`，如礼盒、奖杯、火箭、金币、地球）、主题插画（`--asset illustration`）、嘉宾/人物头像（`user avatar`）或装饰角标（`--asset icon`）**；
    3. 将透明底素材按结构草图摆放到主视觉区或标题四周做层次穿插，直接合成导出高清海报！
    4. **若需动效版海报**：可直接从 IconScout 拉取同主题 **`--asset lottie` 动态元素** 嵌入版面并导出为 `MP4 / GIF / 动态 WebP`，连生视频模型都无需调用即可获得丝滑动态海报。
- **制作方式 2｜AI 双垫整图生图模式（仅当需要全画幅写实摄影、特殊场景合成或单素材拼不出整体光影时调用）**
  - 继续执行下方 Step 3–Step 4。

#### Step 3：从运营图风格表选 2–3 个方向，并「搜索直观风格参考图」给用户选定垫图

1. 不搜竞品业务截图，而是按下方「运营图 / KV 专用风格表」挑选 2–3 个契合主题的美学/材质/光影方向，**搜索或调取对应的直观风格参考图直接展示给用户看**。
2. 用户看图选定 1 张作为 **风格参考垫图（`style_ref.png`）**（或采用用户自己提供的参考图），并确认：
   - **怎么垫**：只垫材质光影与色调 / 垫构图+画风 / 垫真实产品白底原图生成周边场景；
   - **主色调与标题质感**：确认活动主色及标题字体的视觉表现。

| 编号 | 运营图风格名称 | 直观画面与材质特征 | 搜索参考图关键词（中 / 英） | 适用运营场景 |
| :--- | :--- | :--- | :--- | :--- |
| `KV-01` | **C4D / 3D 礼盒微距渲染风** | 圆润精致 3D 模型、柔和全局光照、磨砂塑料与金属混合材质、悬浮几何元素 | `3D Blender C4D podium product render pastel studio lighting` / `C4D 电商微距渲染 运营海报` | 大促活动 Banner、会员权益图、互联网功能发布 |
| `KV-02` | **清透亚克力与液态玻璃风** | 半透明折射玻璃、柔和弥散彩色光斑、极简几何空间、通透科技质感 | `abstract frosted glass acrylic refraction dispersion 3d art` / `液态玻璃 亚克力折射 海报背景` | AI/科技新品发布、金融高端权益、美妆/数码质感海报 |
| `KV-03` | **杂志级商业静物摄影风** | 真实自然阳光树影或影棚布光、极高材质真实感（水滴、织物、木纹、石材） | `editorial still life product photography natural shadow sunlight` / `静物商业摄影 光影质感` | 品质消费品、咖啡茶饮、家居生活、实体商品宣发 |
| `KV-04` | **软萌粘土 / 膨化玩具风** | 彩色软陶或充气膨胀材质、圆润饱满、温暖治愈、高亲和力 | `3d claymorphism inflatable puffy cute illustration` / `3D 粘土风 膨胀材质 插画` | 节日打卡活动、教育/亲子、宠物、年轻化社媒互动图 |
| `KV-05` | **新中式东方美学 / 国潮风** | 宣纸肌理、留白意境、工笔/水墨晕染结合现代几何、黛青/朱砂/鎏金传统色 | `modern oriental aesthetics minimal ink wash gold foil poster` / `新中式 东方美学 节气海报` | 传统节气/节日营销、茶饮/东方品牌、文旅文创活动 |
| `KV-06` | **现代扁平噪点插画风** | 明快几何色块构图 + 细腻复古颗粒噪点肌理、人物或生活场景故事感强 | `modern flat vector illustration grain texture editorial` / `扁平肌理感插画 运营配图` | 品牌故事、生活服务长图、社区话题头图、引导页大图 |
| `KV-07` | **暗黑赛博 / 酸性金属流体风** | 深色背景、液态铬金属反射、霓虹流光或高对比荧光色、未来先锋感 | `dark futuristic liquid chrome iridescent 3d abstract` / `液态金属 酸性设计 潮流海报` | 音乐节/演出、潮玩首发、电竞游戏活动、夜经济营销 |
| `KV-08` | **温暖胶片生活纪实风** | 真实人物或生活一角、微颗粒胶片色调、温暖自然光、松弛不摆拍 | `warm film photography lifestyle candid natural light` / `胶片感 生活方式 摄影` | 旅行/民宿、心理健康、社区氛围、人文故事型 Banner |

#### Step 4：「结构草图 + 风格垫图 + 结构化提示词」双图同垫喂给生图模型

调用生图工具（如宿主生图工具 `GenerateImage`、Nano Banana / GPT-Image / Gemini Image 等）时，将 **两张垫图 + 结构化提示词** 一并传入：

```text
垫图输入 (reference_image_paths)：
1. 结构草图 (layout_sketch.png)：锁定版面构图、标题与信息块位置、图文面积比与留白区
2. 风格参考图 (style_ref.png)：锁定渲染材质、光影氛围、色调与艺术画风
（若有真实产品原图，作为第 3 张主体垫图传入）

结构化提示词 (Prompt)：
- 【构图与版式指令】：严格参照参考图 1 的版面结构、图文占比与留白区域排布；
- 【风格与材质指令】：严格采用参考图 2 的视觉画风、材质表现与光影色调；
- 【画面主体与文案信息】：具体主体物细节 + 标题/副标题内容及造型要求（或留出纯净留白区由设计工具精准叠字）；
- 【色彩与布光】：主色、辅助色与光线方向；
- 【纯净度约束】：禁止无关杂物、禁止错乱伪文字、保持文字区背景干净可读。
画幅比例 (aspect_ratio)：1:1 / 3:4 / 4:3 / 16:9 / 9:16
```

#### Step 5：静态海报/单图定稿后的「动效版升级判断与预期对齐」（主动增值询问）

当用户的原始需求是生成一张海报、运营图或单图时，在静态图确认（或在 Step 1 盘点投放场景）时，Agent **必须主动判断该图的使用场景是否支持动图、以及做成微动图是否效果更好**：

1. **先判使用场景是否支持并受益于动图**：
   - **不支持或不宜动（直接只交静态图，不打扰用户）**：线下印刷海报/易拉宝、纯文字规则长图、严禁闪烁的严肃公告。
   - **支持且动图明显更吸睛（触发主动询问）**：App 开屏、首页弹窗、Banner/金刚区、网页 Hero 首屏、微信朋友圈/公众号嵌入 GIF、小红书/社媒动态封面、电子邀请函、新品发布 KV。
2. **向用户发起「是否生成动效升级版」询问，并明确告知真实效果预期**：
   - 使用提问工具询问用户：*“你的使用场景支持动图（`MP4` / `GIF` / `动态 WebP`），做成微动态往往比静态单图更抓眼球。基于刚确认的静态海报，要不要顺手为你生成一个【动态升级版】？”*
   - **同时必须向用户说明能达到的真实效果预期（管理预期，不夸大）**：
     - **能做到的高质感效果（微动氛围 Loop）**：
       1. `光影与材质流转`：液态玻璃折射流光、金属边缘高光扫过、霓虹呼吸闪烁、自然阳光树影摇曳；
       2. `主体微动态`：3D 礼盒/核心产品轻微悬浮或缓速自转、热气/云雾升腾、水面涟漪、粒子/气泡/花瓣缓慢漂浮；
       3. `镜头呼吸感`：极缓慢的推进（Slow Zoom-in）或前景背景微视差（Parallax）。
     - **明确不能靠生视频模型硬做的（防翻车说明）**：
       画面上的小字、优惠规则、二维码如果直接交给生视频模型运动，容易出现笔画扭曲或模糊。因此最佳实现方案是：**拿无字/少字的主体底图作为【首帧垫图】送入生视频模型做背景与主体微动，保持文字层清晰稳定（或后期叠字），最后导出为高清 `GIF` / `动态 WebP` / 循环 `MP4`**。
3. **用户选择“需要动效版”后的无缝衔接执行**：
   - 直接复用 Step 4 已确认的静态图（或去字版底图）作为 **【首帧静帧垫图】**，转入 [methods-tool-routing.md](methods-tool-routing.md) `TR5-B`；
   - 附上微动控制提示词（如 `subtle floating motion, soft caustic light sweeping across surface, camera gentle push-in, keep main subject structure stable, seamless loop`）；
   - 调用生视频模型生成 3–5 秒动态视频后，按投放渠道一键转码交付 **高清 `GIF`、`动态 WebP` 或循环 `MP4 / WebM`**。

**产出**：
- 路径 A：Figma 目标图层内已生成的真实配图及节点版本记录。
- 路径 B：图文角色判断、版面结构草图、展示给用户并经确认的风格参考垫图、双垫生图参数包、最终静态海报/运营图成品；以及（若场景支持且用户确认升级）基于静态图首帧生成的微动态版本（`MP4 / GIF / 动态 WebP`）。

**完成证据**：路径 A 配图与 UI 风格及容器尺寸一致；路径 B 具备明确的结构草图与用户选定的风格垫图，图文主次分明、标题可读、无盲目生图；支持动图的场景已向用户完成动效升级询问与真实效果预期对齐。  
**不得替代**：不能用未确认风格的随机生图冒充运营海报定稿；不能在未告知文字变形风险的情况下直接把满屏小字海报丢进生视频模型。

## 视觉规格通过门

- [ ] V0–V7 中本轮适用的方法均有触发问题、最低输入、准确产物和完成证据；跳过项有理由。
- [ ] UI 视觉已先做三路分流：存量延展直接复用、纯 B 端绑定公开组件库快搭、C 端 0→1 经过语境剪枝与风格库 + 6 维确认。
- [ ] 所有颜色、字体、间距、密度和资产实现值都有正式来源、系统引用或明确的待确认候选，没有编造品牌值。
- [ ] 语义色覆盖实际状态、前景/背景、亮暗主题、多层表面、非颜色辅助、作用域和实测对比。
- [ ] 排版与密度覆盖字族、角色、字号、行高、字重、字距、行宽、spacing token、真实最长内容、窄宽和目标语言。
- [ ] 资产 manifest 可定位到准确文件和授权；UI 内生图走 Figma 原位生图，独立运营图/海报走「结构草图 + 风格垫图 + 提示词」双垫生图；缺失资产阻断受影响成品，没有近似降级或占位替代。
- [ ] 候选比较冻结了共同变量，每轮仅改变一个变量；结果有证据、确认人和当前状态。
- [ ] 实现者无需猜测即可制作，验收者可按来源、状态、范围和检查记录逐项判定通过、失败、未测或阻断。
