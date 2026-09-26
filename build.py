#!/usr/bin/env python3
"""Generate a static six-page site. Set SITE_URL to the deployed origin."""
import html
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIGIN = os.environ.get('SITE_URL', 'https://daejeon-eyebrow.tambleofficial.workers.dev').rstrip('/')
BRAND = '결담 브로우'
ITEMS = [
    ('natural', '자연결 눈썹', '기존 눈썹결을 살펴 빈 부분을 정리하는 방향', 'brow.webp', '눈썹의 시작과 끝을 무리하게 채우지 않고, 기존 모의 흐름을 기준으로 디자인을 살펴봅니다.'),
    ('soft-arch', '소프트 아치', '눈매와 표정에 맞춘 부드러운 곡선', 'studio.webp', '높은 산과 긴 꼬리보다 얼굴에 자연스럽게 이어지는 곡선을 상담합니다.'),
    ('color', '색상 상담', '피부톤과 기존 눈썹색을 함께 확인', 'color.webp', '갈색 한 가지로 정하지 않고 피부톤, 모발색, 기존 눈썹색을 함께 살펴봅니다.'),
    ('process', '상담 과정', '모양을 결정하기 전 확인할 것들', 'consult.webp', '원하는 인상과 기존 눈썹 상태를 먼저 확인하고 디자인 방향을 함께 조정합니다.'),
    ('aftercare', '관리 안내', '시술 후 일상 관리에서 살필 점', 'care.webp', '관리 방식은 실제 진행 방식과 피부 상태에 따라 달라질 수 있어 현장 안내를 우선합니다.'),
]

def url(slug=''):
    return ORIGIN + ('/' + slug + '/' if slug else '/')

def esc(s): return html.escape(s, quote=True)

def head(title, desc, slug='', image='studio.webp', listing=False):
    canonical = url(slug)
    tags = [
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<title>{esc(title)}</title>',
        f'<meta name="description" content="{esc(desc)}">',
        f'<link rel="canonical" href="{esc(canonical)}">',
        f'<meta property="og:type" content="website"><meta property="og:locale" content="ko_KR">',
        f'<meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{esc(canonical)}">',
        f'<meta property="og:image" content="{ORIGIN}/assets/images/{image}">',
    ]
    if listing:
        data = {'@context':'https://schema.org','@type':'ItemList','name':'결담 브로우 눈썹 디자인 안내','itemListElement':[
            {'@type':'ListItem','position':i,'name':name,'image':f'{ORIGIN}/assets/images/{img}','url':url(slug)}
            for i,(slug,name,_,img,_) in enumerate(ITEMS,1)]}
        tags.append('<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,separators=(',',':'))+'</script>')
    tags += [f'<link rel="alternate" type="application/rss+xml" title="{BRAND} RSS" href="{ORIGIN}/rss.xml">',f'<link rel="describedby" href="{ORIGIN}/llms.txt" type="text/plain">','<link rel="stylesheet" href="/assets/css/style.css">','<script src="/assets/js/site.js" defer></script>','</head>']
    return '\n'.join(tags)

def navigation(active=''):
    links = ''.join(f'<a href="/{s}/" {"aria-current=page" if active==s else ""}>{n}</a>' for s,n,*_ in ITEMS)
    return f'''<header class="site-header"><a class="brand" href="/" aria-label="{BRAND} 홈"><span class="brand-ko">결담</span><span class="brand-en">BROW ATELIER</span></a><button class="menu-button" aria-expanded="false" aria-controls="site-nav" type="button">MENU <span aria-hidden="true">☰</span></button><nav id="site-nav" class="site-nav" aria-label="주요 메뉴">{links}</nav><a class="header-contact" href="https://pf.kakao.com/_QqyKn" target="_blank" rel="noopener noreferrer">임대문의 <span aria-hidden="true">↗</span></a></header>'''

def footer():
    return '''<footer class="footer"><div class="footer-brand">결담 <span>BROW ATELIER</span></div><div class="footer-note"><p>대전 눈썹 디자인을 위한 시안 사이트</p><p>실제 업체 정보와 운영 정보는 배포 전에 입력해 주세요.</p></div><a href="/">BACK TO TOP ↑</a></footer>'''

def card(row, i):
    slug,name,kicker,img,desc=row
    return f'''<article class="card"><a href="/{slug}/"><div class="card-image"><img src="/assets/images/{img}" alt="{esc(name)} 안내 이미지" loading="lazy" width="1024" height="1024"><span class="card-image-link" aria-hidden="true">↗</span></div><div class="card-copy"><span class="number">0{i} / 05</span><h3>{name}</h3><p>{esc(kicker)}</p></div></a></article>'''

def home():
    title='대전 눈썹문신 디자인 상담 | 결담 브로우'
    desc='대전 눈썹문신을 알아보는 분을 위한 눈썹 디자인 안내. 자연결 눈썹, 소프트 아치, 색상 상담과 진행 과정을 살펴보세요.'
    body=f'''<body>{navigation()}<main><section class="hero-banner" aria-label="임대문의"><a href="https://pf.kakao.com/_QqyKn" target="_blank" rel="noopener noreferrer" aria-label="카카오 채널에서 임대문의하기 (새 창)"><img src="/assets/images/lease-inquiry.png" alt="홈페이지 임대문의. 브랜드와 잘 맞는 공간 제안을 기다립니다. 문의 남기기" width="1672" height="941" fetchpriority="high"></a><div class="hero-mobile-copy"><span class="eyebrow">LEASE INQUIRY</span><h2>홈페이지 <em>임대문의</em></h2><p>브랜드와 잘 맞는 공간 제안을 기다립니다.</p><a href="https://pf.kakao.com/_QqyKn" target="_blank" rel="noopener noreferrer">문의 남기기 <span aria-hidden="true">↗</span></a></div><div class="hero-caption"><span>01 / 03</span><span>SPACE &amp; BEAUTY · DAEJEON</span><span>SCROLL TO EXPLORE ↓</span></div></section><section class="intro" id="designs"><div class="intro-side"><span class="eyebrow">THE ART OF NATURAL BROWS</span><span class="intro-number">01 — 05</span></div><div class="intro-main"><h1>눈썹은 얼굴에<br><em>조용히 남는 선.</em></h1><p>대전 눈썹문신을 알아볼 때 가장 먼저 볼 것은 유행하는 모양보다 나에게 이미 있는 결입니다. 눈매, 피부톤, 평소의 표정을 함께 살펴 자연스러운 방향을 찾아갑니다.</p><a class="text-link" href="/process/">디자인 상담 과정 <span aria-hidden="true">↗</span></a></div></section><section class="studio-feature"><div class="studio-photo"><img src="/assets/images/studio.webp" alt="따뜻한 자연광이 드는 차분한 상담 공간" width="1024" height="1024" loading="lazy"></div><div class="studio-copy"><span class="eyebrow">A MOMENT TO PAUSE</span><h2>서두르지 않고<br>먼저 살펴보는 시간.</h2><p>앞머리의 밀도부터 눈썹산의 높이, 꼬리의 길이까지. 작은 차이가 인상을 바꾸기에 원하는 느낌을 구체적으로 확인하는 과정을 중요하게 생각합니다.</p><div class="studio-rule"><span>01</span><span>기존 결 확인</span></div><div class="studio-rule"><span>02</span><span>눈매와 인상 조율</span></div><div class="studio-rule"><span>03</span><span>색상 방향 상담</span></div></div></section><section class="carousel-section" aria-label="눈썹 디자인 안내"><div class="section-heading"><div><span class="eyebrow">THE DESIGN NOTES</span><h2>결에 맞는 다섯 가지 이야기</h2></div><div class="carousel-controls"><button type="button" class="prev" aria-label="이전 카드">←</button><button type="button" class="next" aria-label="다음 카드">→</button></div></div><div class="carousel" tabindex="0">{''.join(card(row,i) for i,row in enumerate(ITEMS,1))}</div><p class="carousel-hint">옆으로 넘겨 더 살펴보세요 <span aria-hidden="true">→</span></p></section><section class="statement"><div><span class="eyebrow">A THOUGHTFUL FINISH</span><h2>선명함보다<br><em>나답게 남는 균형.</em></h2></div><div><p>같은 눈썹도 얼굴에서는 모두 다르게 보입니다. 내 결을 이해하는 데서 디자인이 시작됩니다.</p><a class="light-link" href="/natural/">자연결 눈썹 알아보기 <span aria-hidden="true">↗</span></a></div></section></main>{footer()}</body></html>'''
    return head(title,desc,image='lease-inquiry.png',listing=True)+body

CONTENT = {
 'natural': [('기존 모의 흐름을 먼저 봅니다','비어 보이는 부분만 정리하고 싶다면 기존 눈썹이 자라는 방향과 밀도를 살펴보는 것이 출발점입니다.'),('앞머리와 꼬리를 다르게 생각합니다','앞머리는 결이 보이도록, 꼬리는 얼굴과 눈매에 맞는 길이로 조정할 수 있습니다. 원하는 선명도를 상담에서 구체적으로 이야기해 주세요.')],
 'soft-arch': [('곡선의 높이를 조율합니다','부드러운 아치는 눈썹산을 과하게 올리지 않고 눈매의 흐름과 연결하는 디자인입니다.'),('표정에 맞는 끝선을 봅니다','같은 곡선도 꼬리 길이에 따라 인상이 달라집니다. 평소 표정과 메이크업 취향을 함께 살펴봅니다.')],
 'color': [('한 가지 색으로 정하지 않습니다','피부톤과 모발색, 원래 눈썹의 색, 평소 메이크업을 함께 확인한 뒤 색상 방향을 이야기합니다.'),('시간에 따른 변화를 안내받으세요','색의 보이는 정도는 피부 상태와 관리 방식에 영향을 받을 수 있습니다. 진행 전 실제 사용 색상과 관리 안내를 확인하세요.')],
 'process': [('원하는 인상을 이야기합니다','자연스럽게 정돈하고 싶은지, 윤곽이 더 또렷했으면 하는지 원하는 방향을 먼저 이야기합니다.'),('디자인을 확인한 뒤 결정합니다','기존 결, 좌우 차이, 눈썹산과 꼬리를 살펴보고 모양과 색상에 대해 충분히 확인합니다.')],
 'aftercare': [('개별 안내를 우선합니다','시술 방식과 피부 상태에 따라 관리 지침이 다를 수 있습니다. 실제 진행을 맡은 곳에서 받은 안내를 따라주세요.'),('변화가 걱정되면 문의하세요','예상과 다른 반응이나 불편함이 있으면 시술 담당자에게 현재 상태를 설명하고 적절한 안내를 받으세요.')]
}

def detail(row):
    slug,name,kicker,img,desc=row
    title=f'{name} | 대전 눈썹문신 · {BRAND}'
    description=f'대전 눈썹문신 {name} 안내. {desc}'
    number=next(i for i,item in enumerate(ITEMS,1) if item[0]==slug)
    sections=''.join(f'<section class="detail-block"><span class="number">0{i}</span><div><h2>{heading}</h2><p>{text}</p></div></section>' for i,(heading,text) in enumerate(CONTENT[slug],1))
    others=''.join(f'<a href="/{s}/"><span>{n}</span><span aria-hidden="true">↗</span></a>' for s,n,*_ in ITEMS if s!=slug)
    body=f'''<body>{navigation(slug)}<main><section class="detail-hero"><div class="detail-heading"><div class="breadcrumb"><a href="/">HOME</a><span> / </span>{name}</div><span class="eyebrow">THE DESIGN NOTES · 0{number}</span><h1>{name}</h1><span class="heading-line"></span><p class="lead">{esc(kicker)}.<br>{esc(desc)}</p><a class="text-link" href="#read-more">자세히 살펴보기 <span aria-hidden="true">↓</span></a></div><div class="detail-image"><img src="/assets/images/{img}" alt="{esc(name)} 안내 이미지" width="1024" height="1024"></div></section><div class="detail-content" id="read-more"><div class="detail-kicker"><span class="eyebrow">A CLOSER LOOK</span><p>작은 차이를<br>차분하게 살핍니다.</p></div><div class="detail-text">{sections}</div></div><section class="related"><div><span class="eyebrow">CONTINUE EXPLORING</span><h2>다른 이야기도<br>살펴보세요.</h2></div><div class="related-links">{others}</div></section></main>{footer()}</body></html>'''
    return head(title,description,slug,img)+body

(ROOT/'index.html').write_text(home(),encoding='utf-8')
for row in ITEMS:
    folder=ROOT/row[0];folder.mkdir(exist_ok=True)
    (folder/'index.html').write_text(detail(row),encoding='utf-8')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n',encoding='utf-8')
pages=[url()]+[url(row[0]) for row in ITEMS]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{html.escape(p)}</loc></url>' for p in pages)+'</urlset>',encoding='utf-8')
rss_items=[('대전 눈썹문신 디자인 상담 | 결담 브로우',url(),'눈썹 디자인과 상담 과정을 살펴보세요.')]+[(name,url(slug),desc) for slug,name,_,_,desc in ITEMS]
(ROOT/'rss.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
    +f'<title>{BRAND}</title><link>{html.escape(url())}</link><description>대전 눈썹 디자인 안내</description><language>ko-KR</language>'
    +''.join(f'<item><title>{html.escape(name)}</title><link>{html.escape(link)}</link><guid isPermaLink="true">{html.escape(link)}</guid><description>{html.escape(description)}</description></item>' for name,link,description in rss_items)
    +'</channel></rss>',encoding='utf-8')
llms_lines = [
    f'# {BRAND}',
    '',
    '> 대전 눈썹문신 디자인을 알아보는 방문자를 위한 시안 사이트. 기존 눈썹결, 눈매, 피부톤을 고려한 디자인 상담의 방향을 소개합니다.',
    '',
    '이 사이트의 상호는 임시로 설정한 이름입니다. 주소, 가격, 후기, 자격 및 실제 영업 정보는 제공하지 않습니다. 메인 상단의 임대문의 이미지는 별도의 카카오 채널로 연결됩니다.',
    '',
    '## 주요 페이지',
    '',
    f'- [홈]({url()}): 대전 눈썹문신 디자인 안내와 다섯 개 세부페이지의 목록.',
]
llms_lines += [f'- [{name}]({url(slug)}): {desc}' for slug,name,_,_,desc in ITEMS]
llms_lines += [
    '',
    '## 기타',
    '',
    f'- [RSS]({ORIGIN}/rss.xml): 현재 홈과 세부페이지의 피드.',
    f'- [사이트맵]({ORIGIN}/sitemap.xml): 공개 페이지의 URL 목록.',
    '- [임대문의 카카오 채널](https://pf.kakao.com/_QqyKn): 메인 배너 이미지의 외부 연결.',
    '',
]
(ROOT/'llms.txt').write_text('\n'.join(llms_lines),encoding='utf-8')
print(f'Generated {len(pages)} pages for {ORIGIN}')
