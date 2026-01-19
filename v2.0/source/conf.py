project = 'RCP 2.0'
copyright = '2026, 484012'
author = '484012'
release = 'v2.0'

# 1. 启用 RTD 主题（确保已安装：pip install sphinx-rtd-theme）
html_theme = 'sphinx_rtd_theme'
html_baseurl = 'https://1934044624.github.io/v2.0/' 
# 2. 移除"查看页面源码"链接（核心配置）
html_show_sourcelink = False

# 3. 配置自定义模板和静态文件路径
templates_path = ['_templates']  # 自定义模板目录
html_static_path = ['_static']   # 自定义静态文件目录

# 4. RTD 主题自定义配置（可选，适配aimrt.org风格）
html_theme_options = {
    'navigation_depth': 4,        # 导航菜单深度
    'collapse_navigation': False, # 展开所有导航
    'sticky_navigation': True,    # 导航栏固定
    'style_external_links': True, # 外部链接样式
    'logo_only': False,           # 仅显示logo（如有需要）
    'canonical_url': 'https://1934044624.github.io/v2.0/'
}

# 5. 版本跳转的全局变量（方便模板调用）
html_context = {
    'version_options': [
        {'name': 'v1.0', 'url': '../v1.0/index.html'},
        {'name': 'v2.0', 'url': '../v2.0/index.html'},
        # 可添加更多版本：{'name': 'v3.0', 'url': '../v3.0/index.html'}
    ],
    'current_version': 'v2.0'  # 当前版本（v1.0目录需改为'v1.0'）
}

html_css_files = [
    'css/custom.css',
]
