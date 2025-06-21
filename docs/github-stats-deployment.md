# GitHub Statistics 部署指南

本文档介绍如何在个人主页中集成GitHub统计功能。

## 方案一：直接使用公共API（推荐）

### 优点
- 无需部署，直接使用
- 维护成本低
- 即时生效

### 使用方法

在您的Markdown文件中添加以下代码：

```markdown
<!-- GitHub Stats Card -->
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=huashanjian&show_icons=true&theme=tokyonight)

<!-- Top Languages -->
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=huashanjian&layout=compact&theme=tokyonight)

<!-- GitHub Streak -->
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=huashanjian&theme=tokyonight)
```

### 可用参数

- `username`: 您的GitHub用户名
- `theme`: 主题（dark, radical, merko, gruvbox, tokyonight等）
- `show_icons`: 显示图标（true/false）
- `hide`: 隐藏特定统计（stars,commits,prs,issues,contribs）
- `include_all_commits`: 包含所有提交（true/false）
- `count_private`: 计算私有仓库（true/false）

## 方案二：部署自己的API服务

### 优点
- 更高的速率限制
- 完全自定义
- 私有统计支持

### 部署步骤

1. **Fork项目到您的GitHub账户**
   ```bash
   git clone https://github.com/huashanjian/github-readme-stats.git
   cd github-readme-stats
   ```

2. **在Vercel上部署**
   - 访问 [vercel.com](https://vercel.com)
   - 连接您的GitHub账户
   - 导入github-readme-stats项目
   - 设置环境变量：
     ```
     PAT_1=您的GitHub Personal Access Token
     ```

3. **获取GitHub Token**
   - 访问GitHub Settings > Developer settings > Personal access tokens
   - 创建新token，权限选择：
     - `public_repo`
     - `read:user`
     - `read:org`（可选）

4. **使用自己的API**
   ```markdown
   ![GitHub Stats](https://your-app-name.vercel.app/api?username=huashanjian)
   ```

## 样式自定义

### 主题选择
- `dark`: 深色主题
- `radical`: 彩虹主题
- `merko`: 绿色主题
- `gruvbox`: 复古主题
- `tokyonight`: 东京夜晚主题
- `onedark`: 暗黑主题
- `cobalt`: 钴蓝主题
- `synthwave`: 合成波主题
- `dracula`: 德古拉主题

### 布局选项
- `compact`: 紧凑布局
- `donut`: 甜甜圈图表
- `donut-vertical`: 垂直甜甜圈图表
- `pie`: 饼图

## 故障排除

### 常见问题

1. **图片不显示**
   - 检查用户名是否正确
   - 确认网络连接
   - 检查API服务状态

2. **私有仓库数据不显示**
   - 需要使用自己部署的服务
   - 设置正确的GitHub Token权限

3. **速率限制**
   - 公共API有速率限制
   - 建议使用自己部署的服务

## 进阶配置

### 响应式设计
```html
<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=huashanjian&show_icons=true&theme=tokyonight#gh-dark-mode-only" alt="GitHub Stats (Dark)" />
  <img src="https://github-readme-stats.vercel.app/api?username=huashanjian&show_icons=true&theme=default#gh-light-mode-only" alt="GitHub Stats (Light)" />
</div>
```

### 多卡片组合
```html
<div align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=huashanjian&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=huashanjian&layout=compact&langs_count=8&theme=tokyonight"/>
</div>
```

## 维护建议

1. 定期检查API服务状态
2. 更新GitHub Token（如使用自部署服务）
3. 根据需要调整显示参数
4. 监控加载速度和用户体验

---

更多详细信息请参考：
- [GitHub Readme Stats官方文档](https://github.com/anuraghazra/github-readme-stats)
- [Vercel部署文档](https://vercel.com/docs) 