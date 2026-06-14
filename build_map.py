import json

HOTEL = {
    "name": "灯市口/东四附近",
    "lat": 39.9225,
    "lng": 116.4178,
    "desc": "灯市口—金鱼胡同—东四南大街，地铁5号线+6号线交汇"
}

DAYS = [
    {
        "id": 1,
        "label": "Day 1",
        "title": "🧱 八达岭长城",
        "date": "6/17 周三",
        "locations": [
            {
                "name": "北京北站",
                "lat": 39.9436,
                "lng": 116.3477,
                "type": "transport",
                "time": "08:00",
                "desc": "高铁出发站，20分钟直达八达岭",
                "budget": "🚄 约25元",
                "pay": 1,
                "xhs": "北京北站坐高铁去八达岭攻略"
            },
            {
                "name": "八达岭长城",
                "lat": 40.3584,
                "lng": 116.0155,
                "type": "spot",
                "time": "09:30-13:00",
                "desc": "北线风景更好，带够水，提前预约门票",
                "budget": "🎫 40元+缆车100元",
                "pay": 1,
                "reserve": "https://wx.littleprogram.com/长城内外旅游",
                "xhs": "八达岭长城北线攻略",
                "detail": "建议北线登城，风景更好。带足水，山上补给点少。高铁站出来走几分钟就到入口。"
            },
            {
                "name": "前门大街",
                "lat": 39.8945,
                "lng": 116.3975,
                "type": "food",
                "time": "18:30-20:30",
                "desc": "逛吃+为Day2升旗踩点认路",
                "budget": "🍜 约50-80元",
                "pay": 0.5,
                "xhs": "前门大栅栏必吃小吃"
            }
        ]
    },
    {
        "id": 2,
        "label": "Day 2",
        "title": "⭐ 升旗·故宫·景山·夜景",
        "date": "6/18 周四",
        "locations": [
            {
                "name": "天安门广场（升旗）",
                "lat": 39.9042,
                "lng": 116.3974,
                "type": "spot",
                "time": "03:40-06:30",
                "desc": "看升旗→晨景拍照，一气呵成不回酒店",
                "budget": "🎫 免费（需预约）",
                "pay": 1,
                "reserve": "小程序「天安门广场预约参观」",
                "xhs": "天安门升旗攻略最佳位置",
                "detail": "日出约04:45，提前1小时到安检口。别带包走得快。看完升旗待到06:30，人少光线好拍大片。"
            },
            {
                "name": "前门早餐",
                "lat": 39.8965,
                "lng": 116.3960,
                "type": "food",
                "time": "06:30-07:30",
                "desc": "锦芳小吃/炒肝赵/庆丰包子",
                "budget": "🍜 约20-30元",
                "pay": 1,
                "xhs": "前门地道早餐推荐"
            },
            {
                "name": "故宫博物院",
                "lat": 39.9163,
                "lng": 116.3972,
                "type": "spot",
                "time": "08:00-12:30",
                "desc": "午门进，中轴线+东西六宫+珍宝馆",
                "budget": "🎫 60元+珍宝馆10元",
                "pay": 1,
                "reserve": "小程序「故宫博物院」今晚20:00抢票！",
                "xhs": "故宫半日游路线推荐",
                "detail": "⚠️ 故宫票今晚(6/14)20:00放票！提前实名认证+填好身份证。推荐：午门→太和殿→中和殿→保和殿→乾清宫→御花园→东六宫→珍宝馆。"
            },
            {
                "name": "景山公园（白天）",
                "lat": 39.9222,
                "lng": 116.3966,
                "type": "spot",
                "time": "14:00-15:00",
                "desc": "俯瞰故宫全景，拍中轴线",
                "budget": "🎫 2元",
                "pay": 1,
                "xhs": "景山公园俯瞰故宫最佳角度"
            },
            {
                "name": "景山晚霞（夜景）",
                "lat": 39.9222,
                "lng": 116.3966,
                "type": "spot",
                "time": "~19:30",
                "desc": "🌟 傍晚再上景山，故宫中轴线亮灯，体验完全不同",
                "budget": "🎫 2元",
                "pay": 1,
                "xhs": "景山公园日落晚霞"
            },
            {
                "name": "国家大剧院（夜景拍）",
                "lat": 39.9037,
                "lng": 116.3833,
                "type": "spot",
                "time": "路过",
                "desc": "晚上灯光+水面倒影，随手拍大片",
                "pay": 1
            }
        ]
    },
    {
        "id": 3,
        "label": "Day 3",
        "title": "🏛️ 天坛·牛街·前门",
        "date": "6/19 周五·端午",
        "locations": [
            {
                "name": "天坛公园",
                "lat": 39.8822,
                "lng": 116.4066,
                "type": "spot",
                "time": "08:00-10:30",
                "desc": "祈年殿、回音壁，建议买联票",
                "budget": "🎫 联票34元",
                "pay": 1,
                "reserve": "小程序「畅游公园」",
                "xhs": "天坛公园游览攻略",
                "detail": "推荐买联票（含祈年殿+回音壁+圜丘）。祈年殿是最出片的地方。"
            },
            {
                "name": "牛街（美食主线）",
                "lat": 39.8885,
                "lng": 116.3589,
                "type": "food",
                "time": "11:00-13:00",
                "desc": "聚宝源涮肉🔥/白记年糕/洪记小吃",
                "budget": "🍜 约80-120元",
                "pay": 1,
                "xhs": "北京牛街必吃美食",
                "detail": "聚宝源北京涮肉天花板，建议11点前到。白记年糕的驴打滚可以买了带走。洪记牛肉饼也很赞。"
            },
            {
                "name": "前门大街",
                "lat": 39.8945,
                "lng": 116.3975,
                "type": "spot",
                "time": "14:00-16:00",
                "desc": "老字号溜达，买伴手礼",
                "budget": "自由消费",
                "pay": 0.5
            }
        ]
    },
    {
        "id": 4,
        "label": "Day 4",
        "title": "🌿 颐和园·圆明园",
        "date": "6/20 周六·端午",
        "locations": [
            {
                "name": "颐和园",
                "lat": 39.9998,
                "lng": 116.2755,
                "type": "spot",
                "time": "08:00-12:00",
                "desc": "昆明湖、长廊、佛香阁，买联票",
                "budget": "🎫 联票60元",
                "pay": 1,
                "reserve": "小程序「畅游公园」",
                "xhs": "颐和园半日游路线"
            },
            {
                "name": "圆明园",
                "lat": 39.9991,
                "lng": 116.3033,
                "type": "spot",
                "time": "13:30-16:00",
                "desc": "西洋楼遗址、大水法",
                "budget": "🎫 联票25元",
                "pay": 1,
                "reserve": "小程序「圆明园门票」"
            }
        ]
    },
    {
        "id": 5,
        "label": "Day 5",
        "title": "🚲 胡同骑行·恭王府·什刹海",
        "date": "6/21 周日·端午",
        "locations": [
            {
                "name": "雍和宫",
                "lat": 39.9475,
                "lng": 116.4174,
                "type": "spot",
                "time": "08:30-10:00",
                "desc": "北京香火最旺的寺庙，烧香祈福",
                "budget": "🎫 25元",
                "pay": 1,
                "xhs": "雍和宫祈福攻略"
            },
            {
                "name": "地坛公园",
                "lat": 39.9537,
                "lng": 116.4102,
                "type": "spot",
                "time": "10:00-10:40",
                "desc": "雍和宫对面，小而美的皇家祭坛",
                "budget": "🎫 2元",
                "pay": 1
            },
            {
                "name": "鼓楼",
                "lat": 39.9405,
                "lng": 116.4042,
                "type": "spot",
                "time": "11:00-12:00",
                "desc": "北京中轴线北端点，打卡拍照",
                "budget": "🎫 20元（可不登楼）",
                "pay": 0.5,
                "xhs": "北京鼓楼打卡拍照"
            },
            {
                "name": "姚记炒肝（午餐）",
                "lat": 39.9417,
                "lng": 116.4058,
                "type": "food",
                "time": "12:00-13:00",
                "desc": "地道北京小吃，炒肝+包子",
                "budget": "🍜 约30-50元",
                "pay": 1,
                "xhs": "姚记炒肝鼓楼店"
            },
            {
                "name": "什刹海（后海）",
                "lat": 39.9372,
                "lng": 116.3879,
                "type": "spot",
                "time": "13:00-14:30",
                "desc": "沿湖散步吹风，可划船",
                "budget": "🛶 划船约80元/h",
                "pay": 0.5,
                "xhs": "什刹海后海散步"
            },
            {
                "name": "恭王府",
                "lat": 39.9379,
                "lng": 116.3833,
                "type": "spot",
                "time": "14:30-16:00",
                "desc": "一座恭王府半部清朝史，和珅府邸",
                "budget": "🎫 40元",
                "pay": 1,
                "reserve": "小程序「恭王府博物馆」"
            },
            {
                "name": "🌟 胡同骑行（全天高光）",
                "lat": 39.9361,
                "lng": 116.3908,
                "type": "spot",
                "time": "16:00-17:30",
                "desc": "🚲 恭王府→后海→银锭桥→烟袋斜街→鼓楼→五道营，傍晚路灯亮起最美",
                "budget": "🚲 共享单车约3元",
                "pay": 1,
                "xhs": "北京胡同骑行路线推荐",
                "detail": "路线：恭王府→柳荫街→后海西沿→银锭桥→烟袋斜街→鼓楼东大街→南锣鼓巷→帽儿胡同→雨儿胡同→五道营。全程5km/1-1.5h，傍晚最美。"
            },
            {
                "name": "簋街（晚饭）",
                "lat": 39.9350,
                "lng": 116.4250,
                "type": "food",
                "time": "19:00-21:00",
                "desc": "胡大饭馆（麻小）、花家怡园（北京菜）",
                "budget": "🍜 约100-150元",
                "pay": 1,
                "xhs": "簋街必吃胡大麻小"
            }
        ]
    },
    {
        "id": 6,
        "label": "Day 6",
        "title": "🎢 环球影城",
        "date": "6/22 周一",
        "locations": [
            {
                "name": "北京环球度假区",
                "lat": 39.8454,
                "lng": 116.6722,
                "type": "spot",
                "time": "09:00-21:00",
                "desc": "哈利波特、变形金刚、侏罗纪。周一人相对少",
                "budget": "🎫 约400元+优速通400-600元",
                "pay": 1,
                "reserve": "官方小程序购票",
                "xhs": "北京环球影城攻略",
                "detail": "建议至少买单项优速通给哈利波特禁忌之旅。地铁7号线/八通线直达。"
            }
        ]
    }
]

# ============================================================
# Generate the HTML
# ============================================================

with open('/Users/zyyu/.codex/skills/trip-map-builder/assets/template.html', 'r') as f:
    template = f.read()

# Replace title/description
template = template.replace('<!-- REPLACE: Trip Title -->', '北京6日游攻略 6/17-6/22 端午避高峰版')
template = template.replace('<!-- REPLACE: Trip Description -->', '北京6日自由行攻略-端午假期避开人流-故宫长城工作日-胡同骑行-牛街美食-互动地图')

# Build the HOTEL JS object
hotel_js = f"""{{
  name: '{HOTEL["name"]}',
  lat: {HOTEL["lat"]},
  lng: {HOTEL["lng"]},
  desc: '{HOTEL["desc"]}'
}}"""

# Build the DAYS JS array
days_js_lines = []
days_js_lines.append("const DAYS = [\n")

# Overview day (id=0)
overview = """{
    id: 0,
    label: '总览',
    title: '',
    date: '',
    locations: []
  },"""
days_js_lines.append(overview)

for d in DAYS:
    day_js = f"""  {{
    id: {d['id']},
    label: '{d['label']}',
    title: '{d['title']}',
    date: '{d['date']}',
    locations: [
"""
    for loc in d['locations']:
        lat = loc['lat']
        lng = loc['lng']
        name = loc['name'].replace("'", "\\'")
        desc = loc.get('desc', '').replace("'", "\\'")
        time = loc.get('time', '—')
        loc_type = loc['type']
        budget = loc.get('budget', '')
        detail = loc.get('detail', '')
        xhs = loc.get('xhs', '')
        reserve = loc.get('reserve', '')
        
        day_js += f"""      {{
        name: '{name}',
        lat: {lat},
        lng: {lng},
        type: '{loc_type}',
        time: '{time}',
        desc: '{desc}',
"""
        if budget:
            day_js += f"        budget: '{budget}',\n"
        if 'pay' in loc:
            day_js += f"        pay: {loc['pay']},\n"
        if detail:
            detail_esc = detail.replace("'", "\\'").replace('\n', '\\n')
            day_js += f"        detail: '{detail_esc}',\n"
        if xhs:
            day_js += f"        xhs: '{xhs}',\n"
        if reserve:
            day_js += f"        reserve: '{reserve}',\n"
        day_js += "      },\n"
    
    day_js += """    ]
  },"""
    days_js_lines.append(day_js)

days_js_lines.append("];")
days_js = '\n'.join(days_js_lines)

# Build overview content
overview_content = """<div class="hero"><h1>🏯 北京 6 日游</h1><p class="subtitle">6/17 周三 → 6/22 周一 · 端午避高峰版</p></div>
<div class="info-grid">
  <div class="info-card"><div class="label">🏨 住宿</div><div class="value">灯市口—东四南大街<br><span style="font-size:13px;font-weight:400;color:var(--text-secondary)">地铁5/6号线，去哪都方便</span></div></div>
  <div class="info-card"><div class="label">🎯 策略</div><div class="value">故宫/长城放工作日<br><span style="font-size:13px;font-weight:400;color:var(--text-secondary)">端午安排园林+胡同</span></div></div>
  <div class="info-card"><div class="label">🚇 交通</div><div class="value">亿通行APP刷码乘车</div></div>
  <div class="info-card"><div class="label">💰 预估预算</div><div class="value">~3000-5000元<br><span style="font-size:13px;font-weight:400;color:var(--text-secondary)">不含住宿，含环球影城</span></div></div>
</div>

<div class="section-head">⚠️ 最重要的提醒</div>
<div class="info-grid">
  <div class="info-card" style="grid-column:1/-1;background:#ff3b30;color:#fff;border:none">
    <div style="font-size:15px;font-weight:600;margin-bottom:4px">🔴 故宫今晚(6/14) 20:00 放 6/18 的票！</div>
    <div style="font-size:14px;opacity:.9">提前登录微信实名认证+填好身份证，准点抢！</div>
  </div>
  <div class="info-card" style="grid-column:1/-1;background:#ff9500;color:#fff;border:none">
    <div style="font-size:15px;font-weight:600;margin-bottom:4px">🟡 天安门广场/升旗需预约</div>
    <div style="font-size:14px;opacity:.9">小程序「天安门广场预约参观」，提前1-9天，选"升旗"时段</div>
  </div>
  <div class="info-card" style="grid-column:1/-1;background:#0071e3;color:#fff;border:none">
    <div style="font-size:15px;font-weight:600;margin-bottom:4px">🌟 Day 5 胡同骑行为全天高光</div>
    <div style="font-size:14px;opacity:.9">傍晚租共享单车骑穿胡同，恭王府→后海→银锭桥→鼓楼→五道营</div>
  </div>
</div>"""

# Replace in template
template = template.replace(
    "// ║  REPLACE THIS SECTION — Hotel and Days data                 ║",
    f"const HOTEL = {hotel_js};\n\n{days_js}"
)

template = template.replace(
    "// ║  REPLACE THIS SECTION — Overview tab content                ║",
    f"function overviewContent() {{ return `{overview_content}`; }}"
)

# Also replace the info-grid REPLACE placeholders
template = template.replace('<div class="info-card"><div class="label">酒店</div><div class="value"><!-- REPLACE --></div></div>', '')
template = template.replace('<div class="info-card"><div class="label">航班</div><div class="value"><!-- REPLACE --></div></div>', '')
template = template.replace('<div class="info-card"><div class="label">交通卡</div><div class="value"><!-- REPLACE --></div></div>', '')
template = template.replace('<div class="info-card"><div class="label">预估费用</div><div class="value"><!-- REPLACE --></div></div>', '')
template = template.replace('<!-- REPLACE: Add pay-summary cards as needed -->', '')

# Fix the showDay function
# The template uses showDay(idx) which needs to work
old_show_day = """function showDay(idx) {
  const locs = idx===0 ? DAYS.flatMap(d=>d.locations) : (DAYS.find(d=>d.id===idx)?.locations||[]);
  const markers = [];
  markers.clearLayers?.();
  locs.forEach(l => {
    const m = L.marker([l.lat, l.lng], {icon: iconMap[l.type]||icons.default}).addTo(map);
    m.bindPopup(`<b>${l.name}</b><br>${l.desc}`);
    markers.push(m);
  });
  if(locs.length) { const g = L.featureGroup(markers); map.fitBounds(g.getBounds().pad(.15)); }
}"""

# The template might have a slightly different version, let's find and replace
# Actually, let me look at the showDay function
import re

# Replace the showDay function to properly use iconMap
new_show_day = """function showDay(idx) {
  map.eachLayer(l => { if(l._isPopup) {} else if(typeof l._latlng !== 'undefined' && l !== locateMarker && l._map) { map.removeLayer(l); }});
  document.querySelectorAll('.leaflet-marker-icon').forEach(el => el.remove());
  const locs = idx===0 ? DAYS.flatMap(d=>d.locations) : (DAYS.find(d=>d.id===idx)?.locations||[]);
  const markers = [];
  locs.forEach(l => {
    const icon = iconMap[l.type] || icons.default;
    const m = L.marker([l.lat, l.lng], {icon}).addTo(map);
    m.bindPopup('<b>'+l.name+'</b><br>'+l.desc);
    markers.push(m);
  });
  if(markers.length) { 
    const g = L.featureGroup(markers); 
    map.fitBounds(g.getBounds().pad(0.15));
  } else {
    map.setView([39.9042, 116.4074], 5);
  }
}"""

# Find showDay function - it might be slightly different
# Let me just find and replace the function body
template = re.sub(
    r'function showDay\(idx\) \{[\s\S]*?\n\}',
    new_show_day,
    template
)

# Write output
output_path = '/Users/zyyu/Documents/Codex/2026-06-14/trip-map-builder-users-zyyu-codex/outputs/index.html'
with open(output_path, 'w') as f:
    f.write(template)

print(f"Written to {output_path}")
print(f"File size: {len(template)} bytes")
