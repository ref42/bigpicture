<p align="center">
  <img src="assets/icon.svg" alt="Big Picture" width="160"/>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh.md">中文</a>
</p>

# Big Picture

> 看见森林，不止树木。

<br/>

**Big Picture** 是一个 AI Agent 技能，能把混乱、模糊的问题变成清晰的地图——真正发生了什么、为什么发生、什么最重要、下一步该怎么做。

支持 **Claude Code** 和 **Codex**，开箱即用。

---

## 安装

**macOS / Linux**

```sh
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- both
```

**Windows PowerShell**

```powershell
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target both
```

安装完成后重启 Claude Code 或 Codex。已安装过？加上 `--force` / `-Force` 覆盖更新。

---

## 使用方式

**Claude Code**

```
/bigpicture 我们的部署流水线断断续续出问题已经两周了，三个团队都试过修但没解决
```

```
/bigpicture 我在纠结要不要辞掉现在的工作，去一家早期创业公司当第5号员工
```

```
/bigpicture 用户活跃数据看起来正常，但流失率在悄悄上升，我们搞不清原因
```

**Codex**

```
Use $bigpicture 帮我看清团队执行力问题背后真正发生了什么
```

---

## 它能做什么

无论是技术问题、战略决策、人际冲突还是创意方向，Big Picture 都会：

- 重新表述真正的问题，而不只是表面症状
- 绘制系统地图：参与方、激励机制、瓶颈、反馈回路
- 区分原因、约束与选择
- 挖掘隐藏假设和二阶效应
- 诚实地呈现权衡
- 给出 2–4 条可行路径，并推荐下一个最小行动

它综合了系统思维、软件架构、分布式系统、决策理论、团队协作等领域的分析框架，并根据你的具体情况选用最合适的那些。

---

## 问题类型

| | |
|---|---|
| **诊断型** | 为什么会这样？根本原因是什么？ |
| **战略型** | 我们该往哪个方向走？ |
| **决策型** | 在几个选项之间纠结，难以抉择 |
| **系统型** | 参与方、激励机制、反馈回路、结构性原因 |
| **技术型** | 架构、失败模式、工程权衡 |
| **产品/商业型** | 市场、用户、分发渠道、定位 |
| **职业/学习型** | 目标、机会成本、技能杠杆 |
| **冲突/组织型** | 利益相关方、权力、信任、沟通 |
| **创意/传播型** | 受众、信息、叙事、框架 |

---

## 更多安装选项

只安装到单个 Agent：

```sh
# 仅 Claude Code
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- claude

# 仅 Codex
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- codex
```

```powershell
# 仅 Claude Code
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target claude

# 仅 Codex
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target codex
```

从仓库克隆安装：

```sh
git clone https://github.com/ref42/bigpicture.git
cd bigpicture
sh scripts/install.sh both
```

```powershell
git clone https://github.com/ref42/bigpicture.git
cd bigpicture
.\scripts\install.ps1 -Target both
```

**安装位置**

| Agent | 路径 |
|---|---|
| Claude Code | `~/.claude/skills/bigpicture` |
| Codex | `~/.agents/skills/bigpicture` |

如果你的 Agent 使用自定义的 skills 目录，可以用 `--install-root` / `-InstallRoot` 指定。

---

## 开发

验证 skill：

```sh
python scripts/validate_skill.py bigpicture
bash -n scripts/install.sh
```

测试本地安装：

```sh
tmp="$(mktemp -d)"
sh scripts/install.sh codex --install-root "$tmp"
test -f "$tmp/bigpicture/SKILL.md"
```

```powershell
$tmp = Join-Path ([IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString("N"))
.\scripts\install.ps1 -Target codex -InstallRoot $tmp
Test-Path (Join-Path $tmp "bigpicture\SKILL.md")
```

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。
